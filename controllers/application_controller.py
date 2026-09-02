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

        requested_path = str(path).strip()

        if not requested_path:
            print("No folder path provided.")
            return False

        if os.path.exists(requested_path):
            target_path = os.path.abspath(requested_path)
        else:
            target_path = self._find_folder(requested_path)

        if not target_path:
            print(f"Folder '{path}' does not exist.")
            return False

        try:
            subprocess.Popen(["explorer", target_path])
            print(f"Opening folder: {target_path}")
            return True
        except Exception as e:
            print(f"Could not open folder.")
            print(e)
            return False

    def _find_folder(self, folder_name):
        """Search likely user folders first, then progressively broader locations."""
        name = os.path.basename(folder_name).lower()

        if not name:
            return None

        home = os.path.expanduser("~")
        search_roots = []

        # 1. Desktop / OneDrive Desktop first
        desktop_candidates = []
        if home:
            desktop_candidates.extend([
                os.path.join(home, "Desktop"),
                os.path.join(home, "OneDrive", "Desktop"),
            ])

        for candidate in desktop_candidates:
            if candidate not in search_roots and os.path.isdir(candidate):
                search_roots.append(candidate)

        # 2. User folders
        if home:
            other_user_locations = [
                os.path.join(home, "Documents"),
                os.path.join(home, "Downloads"),
                home,
            ]
            for location in other_user_locations:
                if location not in search_roots and os.path.isdir(location):
                    search_roots.append(location)

        # 3. Project folder
        project_dir = os.getcwd()
        if project_dir not in search_roots and os.path.isdir(project_dir):
            search_roots.append(project_dir)

        # 4. Do not scan full drives by default; only consider them if the user passed an absolute path
        seen = set()
        for root in search_roots:
            if not os.path.isdir(root):
                continue

            for current, directories, _ in os.walk(root):
                for directory in directories:
                    full_path = os.path.join(current, directory)
                    if directory.lower() == name and full_path not in seen:
                        seen.add(full_path)
                        return full_path

        return None

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
