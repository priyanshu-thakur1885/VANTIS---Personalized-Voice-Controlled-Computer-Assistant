import pyautogui


class MouseController:

    def move(self, x, y, duration=0.2):
        pyautogui.moveTo(x, y, duration=duration)

    def click(self):
        pyautogui.click()

    def double_click(self):
        pyautogui.doubleClick()

    def right_click(self):
        pyautogui.rightClick()

    def scroll(self, amount):
        pyautogui.scroll(amount)

    def drag(self, x, y, duration=0.5):
        pyautogui.dragTo(x, y, duration=duration)