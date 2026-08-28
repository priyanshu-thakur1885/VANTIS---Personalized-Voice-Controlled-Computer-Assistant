
from controllers.tts_controller import TTSController


class VoiceFeedback:

    def __init__(self):

        self.tts = TTSController()

    def speak(self, message):

        self.tts.speak(message)
