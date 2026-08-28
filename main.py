#import keyboard and mouse controllers
from controllers.keyboard_controller import KeyboardController
from controllers.mouse_controller import MouseController
from controllers.screen_controller import ScreenController
from controllers.application_controller import ApplicationController
from controllers.system_controller import SystemController
#Phase 2
from controllers.voice_controller import VoiceController
from command_parser import CommandParser
from executor import CommandExecutor





################

# restart jarvis in executor.py

################


#Phase 1
keyboard = KeyboardController()

# keyboard.type_text("Hello from my AI computer agent!")
# keyboard.press("enter")


mouse = MouseController()

# mouse.move(600, 310)
# mouse.click()
# mouse.scroll(-50)


screen = ScreenController()

# screen.screenshot("test.png")
# print("Screen size:", screen.get_screen_size())
# print("Mouse position:", screen.get_mouse_position())



app = ApplicationController()

# app.open_application("chrome")
# app.open_url("https://www.youtube.com")

# app.open_folder(r"C:\Users\fun2b\OneDrive\Desktop\CSE\DSA+JAVA")


# system = SystemController()

# system.increase_volume(5)
# system.decrease_volume(3)
# system.mute()



##PHASE 2

voice = VoiceController()
parser = CommandParser()
executor = CommandExecutor()

# audio = voice.listen()
# text = voice.recognize(audio)
# print("You said:", text)

# while True:

#     audio = voice.listen()

#     text = voice.recognize(audio)

#     if text:
#         print("You said:", text)

#     if text and text.lower().strip() in ["exit", "stop jarvis", "jarvis stop", "quit", "shutdown jarvis"]:
#         print("Assistant stopped.")
#         break


while True:

    audio = voice.listen()

    text = voice.recognize(audio)

    if text is None:
        continue

    text = text.lower().strip()

    print("You said:", text)

    if text and text.lower().strip() in ["exit", "stop jarvis", "jarvis stop", "quit", "shutdown jarvis"]:
        print("Assistant stopped.")
        break

    action = parser.parse(text)

    print("Action:", action)

    executor.execute(action)


