import win32com.client


class TTSController:

    def __init__(self):

        # Windows Speech API
        self.speaker = win32com.client.Dispatch(
            "SAPI.SpVoice"
        )

        # Speech speed
        self.speaker.Rate = 0

        # Volume: 0 - 100
        self.speaker.Volume = 100

    def speak(self, text):

        print("Assistant:", text)

        try:

            self.speaker.Speak(
                text
            )

        except Exception as e:

            print("TTS Error:", e)
