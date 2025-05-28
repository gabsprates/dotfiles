import importlib
import os
import sys
from app_system import AppInstaller


class GitInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        sys.path.append(os.path.dirname(__file__))

    def install(self):
        os_installer = importlib.import_module(f'{self.os_id}.install')
        os_installer.install()

    def customize(self):
        config_file = '/home/me/.gitconfig'

        if os.path.isfile(config_file):
            os.remove(config_file)

        base_dir = os.path.dirname(os.path.abspath(__file__))

        os.symlink(os.path.join(base_dir, '.gitconfig'), config_file)
