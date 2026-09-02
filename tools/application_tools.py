from controllers.application_controller import ApplicationController


application = ApplicationController()


def open_application(name):
    """
    Open an application installed on the computer.
    """

    application.open_application(name)

    return {
        "success": True,
        "message": f"Opened {name}."
    }

def close_application(name):
    """
    Close an application installed on the computer.
    """

    application.close_application(name)

    return {
        "success": True,
        "message": f"Closed {name}."
    }

def open_url(url):
    """
    Open a URL in the default browser.
    """

    application.open_url(url)

    return {
        "success": True,
        "message": f"Opened {url}."
    }


def open_folder(path):
    """
    Open a folder in Windows File Explorer.
    Accepts either an absolute path or a folder name to search for on the system.
    """

    result = application.open_folder(path)

    if result:
        return {
            "success": True,
            "message": f"Folder opened: {path}"
        }

    return {
        "success": False,
        "message": f"Folder not found: {path}"
    }