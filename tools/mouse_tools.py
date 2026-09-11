from controllers.mouse_controller import MouseController
from controllers.screen_controller import ScreenController
from core.vision_service import VisionService
import json
import os
import re
import tempfile


mouse = MouseController()
screen = ScreenController()
vision = VisionService()


def click_at(x, y):
    """Click at the specified screen coordinates."""

    width, height = screen.get_screen_size()

    if not 0 <= x < width or not 0 <= y < height:
        return {
            "success": False,
            "message": "Coordinates are outside the screen bounds."
        }

    mouse.click_at(x, y)

    return {
        "success": True,
        "message": f"Clicked at ({x}, {y})."
    }


def click_element(description):
    """Find a visible element in a screenshot and click its center."""

    print("[1] click_element started")

    screenshot = screen.screenshot()

    print("[2] Screenshot captured")

    width, height = screenshot.size

    print(f"[3] Screenshot size: {width}x{height}")

    screenshot_path = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        ) as file:
            screenshot_path = file.name

        print(f"[4] Temporary file created: {screenshot_path}")

        screenshot.save(screenshot_path)

        print("[5] Screenshot saved")

        response = vision.analyze_image(
            screenshot_path,
            (
                f"Find the visible UI element described as: {description!r}. "
                f"The image size is {width} by {height} pixels. "
                "Return only valid JSON in this exact format: "
                '{"found": true, "x": 0, "y": 0}. '
                "Use the center of the element. If it is not visible, return "
                '{"found": false, "x": null, "y": null}.'
            )
        )

        print("[6] Vision response received")
        print("Vision response:", response)

        match = re.search(r"\{.*\}", response, re.DOTALL)

        if not match:
            return {
                "success": False,
                "message": "Vision returned invalid coordinates."
            }

        print("[7] JSON found")

        result = json.loads(match.group())

        print("[8] JSON parsed:", result)

        if not result.get("found"):
            return {
                "success": False,
                "message": f"Could not find {description}."
            }

        x = int(result["x"])
        y = int(result["y"])

        print(f"[9] Coordinates found: ({x}, {y})")

        return click_at(x, y)

    finally:
        if screenshot_path and os.path.exists(screenshot_path):
            os.unlink(screenshot_path)

            print("[10] Temporary screenshot deleted")


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