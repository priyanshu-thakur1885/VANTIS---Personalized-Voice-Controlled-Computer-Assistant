from pydoc import text
from controllers.mouse_controller import MouseController
from controllers.keyboard_controller import KeyboardController
from controllers.application_controller import ApplicationController
from controllers.system_controller import SystemController
from controllers.voice_feedback import VoiceFeedback
import os
import sys
import time

class CommandExecutor:

    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.application = ApplicationController()
        self.system = SystemController()
        self.feedback = VoiceFeedback()

    def execute(self, action):

        if action is None:
            return

        action_type = action.get("action")

        if action_type == "scroll":

            direction = action.get("direction")

            if direction == "down":
                self.mouse.scroll(-20)

            elif direction == "up":
                self.mouse.scroll(20)

        elif action_type == "click":

            self.mouse.click()

        elif action_type == "double_click":

            self.mouse.double_click()

        elif action_type == "right_click":

            self.mouse.right_click()
        elif action_type == "restart_vantis":

            print("Restarting Vantis...")

            os.execv(
                sys.executable,
                [sys.executable] + sys.argv
            )

        elif action_type == "press_key":

            key = action.get("key")

            self.keyboard.press(key)

        elif action_type == "type_text":

            text = action.get("text")

            self.keyboard.type_text(text)

        elif action_type == "hotkey":

            keys = action.get("keys")

            self.keyboard.hotkey(keys)
        elif action_type == "open_application":

            application = action.get("application")

            success = self.application.open_application(application)
            if success:
                self.feedback.speak(f"Opening {application}.")
            else:
                self.feedback.speak(f"I couldn't open {application}.")

        elif action_type == "open_browser_and_url":

            browser = action.get("browser")
            url = action.get("url")

            browser_opened = self.application.open_application(browser)
            if browser_opened:
                time.sleep(1.5)
                self.application.open_url(url)
                self.feedback.speak(f"Opening {browser} and going to {url}.")
            else:
                self.feedback.speak(f"I couldn't open {browser}.")

        elif action_type == "close_application":

            application = action.get("application")

            success = self.application.close_application(application)

            if success:

                self.feedback.speak(
                    f"Closing {application}."
                )

            else:

                self.feedback.speak(
                    f"I couldn't find {application}."
                )


# -------------------------
# VOLUME
# -------------------------

        elif action_type == "set_volume":

            amount = action.get("amount")

            self.system.set_volume(amount)
            self.feedback.speak(
            f"Volume set to {amount} percent."
    )

        elif action_type == "mute":

            self.system.mute()

        elif action_type == "unmute":

            self.system.unmute()

        elif action_type == "take_screenshot":

            self.system.take_screenshot()
            self.feedback.speak(
                "Screenshot taken."
            )

        else:

            print("Unknown action:", action)