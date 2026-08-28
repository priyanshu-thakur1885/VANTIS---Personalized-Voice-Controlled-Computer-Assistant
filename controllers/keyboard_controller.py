import pyautogui


class KeyboardController:

    def type_text(self, text):
        pyautogui.write(text, interval=0.03)

    def press(self, key):
        pyautogui.press(key)

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)

    def key_down(self, key):
        pyautogui.keyDown(key)

    def key_up(self, key):
        pyautogui.keyUp(key)