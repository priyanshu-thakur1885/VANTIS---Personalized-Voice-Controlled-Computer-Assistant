
import speech_recognition as sr


class VoiceController:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # Realme Buds T310 microphone
        self.microphone = sr.Microphone(
            device_index=2
        )

        # Speech settings
        self.recognizer.pause_threshold = 0.8
        self.recognizer.non_speaking_duration = 0.5

        # -------------------------
        # CALIBRATE ONCE
        # -------------------------

        with self.microphone as source:

            print("Adjusting for background noise...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        print("Microphone ready.")

    def listen(self):

        try:

            with self.microphone as source:

                print("Listening...")

                audio = self.recognizer.listen(
                    source
                )

            # microphone is released here

            return audio

        except Exception as e:

            print("Microphone error:", e)

            return None

    def recognize(self, audio):

        if audio is None:
            return None

        try:

            print("Recognizing...")

            text = self.recognizer.recognize_google(
                audio
            )

            return text

        except sr.UnknownValueError:

            print(
                "Sorry, I couldn't understand that."
            )

            return None

        except sr.RequestError as e:

            print(
                "Speech recognition service error:",
                e
            )

            return None

