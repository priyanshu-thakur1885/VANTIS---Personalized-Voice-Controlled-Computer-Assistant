import subprocess
import os
import psutil


class ApplicationController:

    # -------------------------
    # OPEN APPLICATION
    # -------------------------

    def open_application(self, application):

        application = application.lower().strip()

        applications = {

            # Browsers
            "chrome": "chrome",
            "google chrome": "chrome",

            "edge": "msedge",
            "microsoft edge": "msedge",

            # Development
            "vs code": "code",
            "vscode": "code",
            "visual studio code": "code",

            # Windows apps
            "notepad": "notepad",
            "calculator": "calc",
            "calc": "calc",

            "settings": "ms-settings:",

            "file explorer": "explorer",
            "explorer": "explorer",

            # Other applications
            "whatsapp": "whatsapp:",
        }

        if application in applications:

            command = applications[application]

            try:

                subprocess.Popen(
                    ["cmd", "/c", "start", "", command],
                    shell=True
                )

                print(f"Opening {application}...")

                return True

            except Exception as e:

                print(f"Could not open {application}.")
                print(e)

                return False

        else:

            try:

                subprocess.Popen(
                    ["cmd", "/c", "start", "", application],
                    shell=True
                )

                print(f"Trying to open {application}...")

                return True

            except Exception as e:

                print(f"Could not open {application}.")
                print(e)

                return False

    # -------------------------
    # OPEN URL
    # -------------------------

    def open_url(self, url):

        try:

            subprocess.Popen(
                ["cmd", "/c", "start", "", url],
                shell=True
            )

            return True

        except Exception as e:

            print(f"Could not open URL: {url}")
            print(e)

            return False

    # -------------------------
    # OPEN FOLDER
    # -------------------------

    def open_folder(self, path):

        if os.path.exists(path):

            try:

                subprocess.Popen(
                    ["explorer", path]
                )

                return True

            except Exception as e:

                print(f"Could not open folder.")
                print(e)

                return False

        else:

            print(f"Folder '{path}' does not exist.")

            return False

    # -------------------------
    # CLOSE APPLICATION
    # -------------------------

    def close_application(self, application):

        application = application.lower().strip()

        for process in psutil.process_iter(["name"]):

            try:

                process_name = process.info["name"]

                if not process_name:
                    continue

                process_name = process_name.lower()

                if application in process_name:

                    process.terminate()

                    print(
                        f"{application} closed successfully."
                    )

                    return True

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):

                continue

        print(f"Could not find {application}.")

        return False
