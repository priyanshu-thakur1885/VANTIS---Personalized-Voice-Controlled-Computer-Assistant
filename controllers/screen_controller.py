import pyautogui


class ScreenController:

    def screenshot(self):

        image = pyautogui.screenshot()

        return image

    def get_screen_size(self):

        width, height = pyautogui.size()

        return width, height

    def get_mouse_position(self):

        x, y = pyautogui.position()

        return x, y