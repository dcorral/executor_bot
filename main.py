from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import subprocess
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Load environment variables from .env file
load_dotenv()

# Now, TOKEN and THE_SCRIPTS_FOLDER are read from the .env file
TOKEN = str(os.getenv('TOKEN'))
THE_SCRIPTS_FOLDER = str(os.getenv('THE_SCRIPTS_FOLDER'))
ALLOWED_CHAT_ID = int(os.getenv('ALLOWED_CHAT_ID'))


def start(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        logging.info(
            f"Unauthorized access attempt by {update.effective_chat.id}.")
        return
    scripts = [f for f in os.listdir(THE_SCRIPTS_FOLDER) if f.endswith('.sh')]
    keyboard = []

    if scripts:
        for script in scripts:
            button = [InlineKeyboardButton(
                script, callback_data=f"select_{script}")]
            keyboard.append(button)
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            'Please choose a script to execute:', reply_markup=reply_markup)
    else:
        update.message.reply_text('There are no scripts available.')


def button(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        logging.info(
            f"Unauthorized access attempt by {update.effective_chat.id}.")
        return
    query = update.callback_query
    query.answer()

    script_name = query.data
    keyboard = [
        [InlineKeyboardButton(
            "Execute", callback_data=f"execute_{script_name}")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    script_name_display = script_name.split("_")[1]
    query.edit_message_text(
        text=f"Are you sure you want to execute {script_name_display}?", reply_markup=reply_markup)


def execute_script(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        logging.info(
            f"Unauthorized access attempt by {update.effective_chat.id}.")
        return
    query = update.callback_query
    query.answer()

    if query.data.startswith("execute_"):
        script_name = query.data.split("_")[2]
        script_path = os.path.join(THE_SCRIPTS_FOLDER, script_name)

        try:
            result = subprocess.run(
                [script_path], capture_output=True, text=True, check=True)
            output = result.stdout
            query.edit_message_text(f'Execution success:\n{output}')
        except subprocess.CalledProcessError as e:
            query.edit_message_text(f'Error during execution:\n{e.output}')
    elif query.data == "cancel":
        query.edit_message_text('Script execution canceled.')


def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button, pattern='^select_.*'))
    dispatcher.add_handler(CallbackQueryHandler(
        execute_script, pattern='^execute_.*'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
