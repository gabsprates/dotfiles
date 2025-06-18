import importlib
import subprocess
import sys
import os


def run_as_me(cmd: list[str]):
    command = ["sudo", "-g", "me", "-u", "me"]
    command.extend(cmd)
    subprocess.run(cmd, user='me', group='me')


class AppInstaller:
    def install(self):
        raise NotImplementedError(
            "Plugins must implement the 'initialize' method.")

    def customize(self):
        raise NotImplementedError(
            "Plugins must implement the 'execute' method.")


class AppManager:
    def __init__(self, plugin_dir: str, os_id: str, apps: list[str]):
        self.app_dir = plugin_dir
        self.os_id = os_id
        self.apps = []
        self.desired_apps = apps

        sys.path.append(self.app_dir)

        for filename in os.listdir(self.app_dir):
            if not filename in self.desired_apps:
                continue

            module = importlib.import_module(filename)

            for attr in dir(module):
                app_class = (getattr(module, attr))

                if (isinstance(app_class, type)
                        and issubclass(app_class, AppInstaller)
                        and app_class is not AppInstaller):

                    self.apps.append({
                        "name": filename,
                        "module": app_class(self.os_id)
                    })

    def install_apps(self):
        print(f"## Installing apps for: {self.os_id.upper()}", '\n')

        for app in self.apps:
            name = app['name']
            module = app['module']

            print(f">>> Install [{name}]: start")
            module.install()
            print(f">>> Install [{name}]: done", '\n')

            print(f">>> Customize [{name}]: start")
            module.customize()
            print(f">>> Customize [{name}]: done")
