from controllers.mouse_controller import MouseController


mouse = MouseController()


def click():
    """
    Click at the current mouse position.
    """

    mouse.click()

    return {
        "success": True,
        "message": "Clicked."
    }


def double_click():
    """
    Double click at the current mouse position.
    """

    mouse.double_click()

    return {
        "success": True,
        "message": "Double clicked."
    }


def right_click():
    """
    Right click at the current mouse position.
    """

    mouse.right_click()

    return {
        "success": True,
        "message": "Right clicked."
    }


def scroll(direction, amount=200):
    """
    Scroll the screen up or down.
    """

    if direction == "down":
        mouse.scroll(-amount)

    elif direction == "up":
        mouse.scroll(amount)

    else:
        return {
            "success": False,
            "message": "Invalid scroll direction."
        }

    return {
        "success": True,
        "message": f"Scrolled {direction}."
    }