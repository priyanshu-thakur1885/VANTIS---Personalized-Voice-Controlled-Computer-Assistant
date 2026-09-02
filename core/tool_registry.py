from tools.keyboard_tools import (
    type_text,
    press_key,
    hotkey
)

from tools.mouse_tools import (
    click,
    double_click,
    right_click,
    scroll
)

from tools.application_tools import (
    open_application,
    close_application,
    open_url,
    open_folder
)

from tools.system_tools import (
    increase_volume,
    decrease_volume,
    mute
)


TOOL_REGISTRY = {

    "type_text": type_text,

    "press_key": press_key,

    "hotkey": hotkey,

    "click": click,

    "double_click": double_click,

    "right_click": right_click,

    "scroll": scroll,

    "open_application": open_application,

    "close_application": close_application,

    "open_url": open_url,

    "open_folder": open_folder,

    "increase_volume": increase_volume,

    "decrease_volume": decrease_volume,

    "mute": mute
}