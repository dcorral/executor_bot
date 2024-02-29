# Telegram Bot Script Executor

This project contains a Telegram bot that executes predefined shell scripts located in a specified directory. It provides an interface through Telegram where authorized users can select and execute these scripts safely.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Installing

#### 1. Clone the Repository

Start by cloning the repository to your local machine.

```bash
git clone <repository-url>
cd <repository-directory>
```

#### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment for Python projects to manage dependencies separately from your global Python installation.

To create a virtual environment, run:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On Windows:
    ```cmd
    .\venv\Scripts\activate
    ```

- On Unix or MacOS:
    ```bash
    source venv/bin/activate
    ```

#### 3. Install Dependencies

With the virtual environment activated, install the required dependencies using:

```bash
pip install -r requirements.txt
```

#### 4. Configure the Environment Variables

Copy the `env-template` file to a new `.env` file:

```bash
cp env-template .env
```

Then, open the `.env` file and update the following configuration variables:

- `TOKEN`: Your Telegram bot token. You can obtain one by registering a new bot with [BotFather](https://t.me/botfather) on Telegram.
- `THE_SCRIPTS_FOLDER`: The absolute path to the directory containing your `.sh` script files.
- `ALLOWED_CHAT_ID`: Your Telegram user ID or the ID of a group chat that is authorized to interact with the bot. You can get this ID by messaging [userinfobot](https://t.me/userinfobot) on Telegram.

Example `.env` content:

```plaintext
TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
THE_SCRIPTS_FOLDER=/path/to/THE_SCRIPTS_FOLDER
ALLOWED_CHAT_ID=123456789
```

### Running the Bot

With the environment configured, run the bot using:

```bash
python main.py
```

The bot should now be running and responding to commands sent by the authorized user or group chat.

## Usage

- Send `/start` to the bot to receive a list of available scripts.
- Select a script to execute it. The bot will ask for confirmation before execution.
- Confirm to execute the script or cancel the operation.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
EOF

