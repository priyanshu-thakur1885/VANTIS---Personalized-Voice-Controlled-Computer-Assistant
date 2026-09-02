from controllers.keyboard_controller import KeyboardController


keyboard = KeyboardController()


def type_text(text):
    """
    Type text using the computer keyboard.
    """

    keyboard.type_text(text)

    return {
        "success": True,
        "message": "Text typed successfully."
    }


def press_key(key):
    """
    Press a keyboard key.
    """

    keyboard.press(key)

    return {
        "success": True,
        "message": f"Pressed {key}."
    }


def hotkey(keys):
    """
    Press a keyboard shortcut.
    """

    keyboard.hotkey(*keys)

    return {
        "success": True,
        "message": "Keyboard shortcut executed."
    }