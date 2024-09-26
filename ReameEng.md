
## Description
**TeleSwap** is a Telegram bot that replaces sent messages with messages from public Telegram channels. For example, you can set up a replacement for voice messages.

> [!NOTE]
> The channel must be public

## Installation

### Requirements
1. Install [Python](https://www.python.org/downloads/)
2. Get the API for the Telegram user on [my.telegram.org ](https://my.telegram.org/auth)

### Installation options

####1. Automatic installation
1. Download and run [CLONE.bat](https://github.com/Rerowros/TeleSwap/releases/download/Main/CLONE.bat) or an archive from [Release](https://github.com/Rerowros/TeleSwap/releases/tag/Main).
2. Configure the `config.json` file and run the project via `start.bat`.

    
#### 2. Using `install.bat`
1. Run `install.bat` to install Telethon and create a virtual environment.
2. Configure the `config.json` file and run the project via `start.bat`.

#### 3. Manual installation
1. Clone the repository or download the files directly.
2. Install the Telethon library:
   ```bash
   pip install telethon
   ```
   
3. Configure the `config.json` file and run the project via `start.bat`.

## Setting up
1. Edit the `config.json` according to your requirements
    ```json
    "api_id": "YOUR API ID",
    "api_hash": "YOUR HASH ID",
    "device_model": "TeleSwap",
    "system_version": "14.8.1",
    "app_version": "8.4",
    "lang_code": "en",
    "system_lang_code": "en-US",
    "channel_id": "YOUR LINK TO TELEGRAM CHANNEL", 
    "message_map": {  
        "Message": ID MESSAGE,
        "б2": 5
    }
    ```
2. 2. To get the channel ID, copy the link to any message in the channel. Link format:
   ```
   t.me/ID_Channel/ID_Messages
   ```

   Example:
   ```
   t.me/Respect_Voice_Rerowros_Bot/5
   ```

### Launch
Launch the bot in one of the following ways:
- Via the console:
  ```bash
  python TeleSwap.py
  ```
- Via `start.bat`
