import re


class CommandParser:

    def parse(self, command):

        if command is None:
            return None

        command = command.lower().strip()

        # -------------------------
        # BROWSER + URL
        # -------------------------

        browser_url_match = re.search(
            r"open\s+(.+?)\s+(?:and\s+go\s+to|and\s+visit|in)\s+(.+)",
            command
        )

        if browser_url_match:
            browser = browser_url_match.group(1).strip()
            target = browser_url_match.group(2).strip()

            if target.startswith("http"):
                url = target
            elif target in ["youtube", "youtube.com", "google", "google.com"]:
                url = {
                    "youtube": "https://www.youtube.com",
                    "youtube.com": "https://www.youtube.com",
                    "google": "https://www.google.com",
                    "google.com": "https://www.google.com",
                }[target]
            else:
                url = f"https://www.{target.replace(' ', '')}.com"

            return {
                "action": "open_browser_and_url",
                "browser": browser,
                "url": url
            }

        # -------------------------
        # MOUSE
        # -------------------------

        if command == "scroll down":

            return {
                "action": "scroll",
                "direction": "down"
            }

        if command == "scroll up":

            return {
                "action": "scroll",
                "direction": "up"
            }

        if command == "click":

            return {
                "action": "click"
            }

        if command == "double click":

            return {
                "action": "double_click"
            }

        if command == "right click":

            return {
                "action": "right_click"
            }

        # -------------------------
        # VANTIS
        # -------------------------

        if command == "restart vantis":

            return {
                "action": "restart_vantis"
            }

        # -------------------------
        # KEYBOARD
        # -------------------------

        if command.startswith("press "):

            key = command[6:].strip()

            return {
                "action": "press_key",
                "key": key
            }

        if command.startswith("type "):

            text = command[5:].strip()

            return {
                "action": "type_text",
                "text": text
            }

        # -------------------------
        # HOTKEYS
        # -------------------------

        if command == "copy it":

            return {
                "action": "hotkey",
                "keys": ["ctrl", "c"]
            }

        if command == "paste it":

            return {
                "action": "hotkey",
                "keys": ["ctrl", "v"]
            }

        if command == "cut it":

            return {
                "action": "hotkey",
                "keys": ["ctrl", "x"]
            }

        if command == "undo":

            return {
                "action": "hotkey",
                "keys": ["ctrl", "z"]
            }

        if command == "redo":

            return {
                "action": "hotkey",
                "keys": ["ctrl", "y"]
            }

        if command == "select all":

            return {
                "action": "hotkey",
                "keys": ["ctrl", "a"]
            }

        # -------------------------
        # APPLICATIONS
        # -------------------------

        if command.startswith("open "):

            application = command[5:].strip()

            return {
                "action": "open_application",
                "application": application
            }

        if command.startswith("close "):

            application = command[6:].strip()

            return {
                "action": "close_application",
                "application": application
            }

        # -------------------------
        # VOLUME
        # -------------------------

        if command == "mute":

            return {
                "action": "mute"
            }

        if command == "unmute":

            return {
                "action": "unmute"
            }

        if command.startswith("set volume at "):

            value = command[len("set volume at "):].strip()

            # Remove percentage words
            value = (
                value
                .replace("%", "")
                .replace("percent", "")
                .strip()
            )

            if value.isdigit():

                percentage = int(value)

                if 0 <= percentage <= 100:

                    return {
                        "action": "set_volume",
                        "amount": percentage
                    }

        # -------------------------
        # UNKNOWN
        # -------------------------
        #take ss
        if command == "take screenshot" or command == "take ss":

            return {
                "action": "take_screenshot"
            }

        return {
            "action": "unknown",
            "command": command
        }

