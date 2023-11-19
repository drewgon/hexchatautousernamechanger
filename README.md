# NickChanger for HexChat

NickChanger is a Python plugin for HexChat, an IRC client, designed to automatically change and maintain a specific nickname. If your desired nickname is in use, the plugin will periodically attempt to set it until it becomes available.

## Features

- **Automatic Nickname Management**: Automatically sets your desired nickname when it's not in use.
- **Retry Interval**: If the nickname is in use, the script will retry after a specified time interval.
- **Configurable Nickname**: Set your desired nickname easily through HexChat's plugin preferences.

## Installation

1. **Download the Script**: Download the `nickchanger.py` script.
2. **Place the Script**: Place the script in your HexChat addons folder. Typically, this is located at:
   - Windows: `C:\Users\YourUserName\AppData\Roaming\HexChat\addons`
   - Linux: `~/.config/hexchat/addons/`
3. **Load the Script**: Open HexChat and load the script through the Window menu: `Window` > `Plugins and Scripts` > `Load...` and select `nickchanger.py`.

## Configuration

After installing the script, set your desired nickname using the following HexChat command:

/setpluginpref nickchanger_nickname your_desired_nickname

Replace `your_desired_nickname` with the nickname you want to use.

## Usage

Once configured, the script will automatically work in the background. It will change your nickname to the desired one if it's not already set and will retry every 60 seconds if the nickname is currently in use.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](your-github-repository-issues-link). If you want to contribute, please open a pull request.


