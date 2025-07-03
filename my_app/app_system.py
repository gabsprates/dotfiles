import importlib
import sys
import os

from pathlib import Path


class AppInstaller:
    """
    Interface to be implemented for each app that should be installed.
    """

    def install(self):
        """
        Method that executes any sudo actions, as instaling packages.
        """
        raise NotImplementedError(
            "Plugins must implement the 'install' method.")

    def customize(self):
        """
        Method that execcutes any user level customization, like editing
        PATH, or even installing something at user's directory.
        """
        raise NotImplementedError(
            "Plugins must implement the 'customize' method.")


class InstallerManager:
    def __init__(self, plugin_dir: Path, os_id: str, apps: list[str]):
        """
        Loads plugins from the plugins directory and register them for future installation.
        """

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
        """
        Runs app .install() and .customize() methods.
        """
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
