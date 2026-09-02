from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class SystemController:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

    # -------------------------
    # SET VOLUME
    # -------------------------

    def set_volume(self, percentage):

        # Make sure value stays between 0 and 100
        percentage = max(0, min(100, percentage))

        # Convert 0-100 into 0.0-1.0
        volume_level = percentage / 100.0

        # Set Windows master volume
        self.volume.SetMasterVolumeLevelScalar(
            volume_level,
            None
        )

        print(f"Volume set to {percentage}%")

    # -------------------------
    # MUTE
    # -------------------------

    def mute(self):

        self.volume.SetMute(
            1,
            None
        )

        print("Volume muted.")

    # -------------------------
    # UNMUTE
    # -------------------------

    def unmute(self):

        self.volume.SetMute(
            0,
            None
        )

        print("Volume unmuted.")

    def take_screenshot(self):

        

        # Get the current timestamp for the filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Define the filename with the timestamp
        filename = f"screenshot_{timestamp}.png"

        # Capture the screenshot
        screenshot = ImageGrab.grab()

        # Save the screenshot to a file
        screenshot.save(filename)

        print(f"Screenshot saved as {filename}")