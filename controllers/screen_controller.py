import pyautogui


class ScreenController:

    def screenshot(self, filename="screenshot.png"):
        image = pyautogui.screenshot()
        image.save(filename)

    def get_screen_size(self):
        return pyautogui.size()

    def get_mouse_position(self):
        return pyautogui.position()