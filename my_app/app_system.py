import importlib
import subprocess
import sys
import os

from pathlib import Path


def run_as_me(cmd: list[str]):
    command = ["sudo", "-g", "me", "-u", "me"]
    command.extend(cmd)
    subprocess.run(cmd, user='me', group='me')


class AppInstaller:
    def install(self):
        raise NotImplementedError(
            "Plugins must implement the 'install' method.")

    def customize(self):
        raise NotImplementedError(
            "Plugins must implement the 'customize' method.")


class InstallerManager:
    def __init__(self, plugin_dir: Path, os_id: str, apps: list[str]):
        self.plugin_dir = str(plugin_dir)
        self.os_id = os_id
        self.apps = []
        self.desired_apps = apps

        sys.path.append(self.plugin_dir)

        for filename in os.listdir(self.plugin_dir):
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
