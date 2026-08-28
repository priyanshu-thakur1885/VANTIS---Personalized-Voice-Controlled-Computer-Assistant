from pycaw.pycaw import AudioUtilities


class SystemController:

    def __init__(self):

        # Get the default Windows audio device
        devices = AudioUtilities.GetSpeakers()

        # Use the EndpointVolume interface
        # This was the interface that was working previously
        self.volume = devices.EndpointVolume

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
