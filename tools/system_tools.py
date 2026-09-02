from controllers.system_controller import SystemController


system = SystemController()


def increase_volume(amount=1):
    """
    Increase system volume.
    """

    system.increase_volume(amount)

    return {
        "success": True,
        "message": f"Volume increased by {amount}."
    }


def decrease_volume(amount=1):
    """
    Decrease system volume.
    """

    system.decrease_volume(amount)

    return {
        "success": True,
        "message": f"Volume decreased by {amount}."
    }


def mute():
    """
    Mute system audio.
    """

    system.mute()

    return {
        "success": True,
        "message": "System muted."
    }