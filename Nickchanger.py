# Module information
__module_name__ = "nickchanger"
__module_version__ = "0.2"
__module_description__ = "Python module for HexChat to change and maintain a specific nickname"

# Import the hexchat module
import hexchat

# User configurable settings
# The desired nickname can be set via HexChat's plugin preferences
desired_nickname = hexchat.get_pluginpref("nickchanger_nickname") or "your_nickname"
retry_interval = 60  # Time in seconds to wait before retrying nickname change

def check_nickname(word, word_eol, userdata):
    """
    Responds to the 'nickname in use' server event (numeric 433).
    If the desired nickname is in use, it sets a timer to retry after the specified interval.
    """
    if word[1] == "433":
        print(f"Nickname {desired_nickname} is in use. Trying again in {retry_interval} seconds.")
        hexchat.command(f"timer {retry_interval} nick {desired_nickname}")
    return hexchat.EAT_NONE  # Continue processing other HexChat events

def set_nickname(word, word_eol, userdata):
    """
    Sets the user's nickname to the desired nickname if it's currently different.
    """
    current_nickname = hexchat.get_info("nick")
    if current_nickname != desired_nickname:
        print(f"Incorrect nickname detected. Changing nickname to {desired_nickname}.")
        hexchat.command(f"nick {desired_nickname}")
    return hexchat.EAT_NONE

def monitor_nickname(userdata):
    """
    Periodically checks and sets the nickname.
    This function is called repeatedly by a HexChat timer.
    """
    set_nickname(None, None, None)
    return 1  # Return 1 to keep the timer running

# Hook the relevant HexChat events
# 433: Nickname in use
# Your Nick: When your nickname is changed
# Connected: When you connect to a server
hexchat.hook_server("433", check_nickname)
hexchat.hook_print("Your Nick", set_nickname)
hexchat.hook_print("Connected", set_nickname)
hexchat.hook_timer(retry_interval * 1000, monitor_nickname)  # Timer to periodically check the nickname

# Print a confirmation message when the module is loaded
print(f"{__module_name__} version {__module_version__} loaded.")
