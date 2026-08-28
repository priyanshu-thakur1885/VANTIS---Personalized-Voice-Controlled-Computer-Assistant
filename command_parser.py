class CommandParser:

    def parse(self, command):

        if command is None:
            return None

        command = command.lower().strip()

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
        # JARVIS
        # -------------------------

        if command == "restart jarvis":

            return {
                "action": "restart_jarvis"
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

        return {
            "action": "unknown",
            "command": command
        }

