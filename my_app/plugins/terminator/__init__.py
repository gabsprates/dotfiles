import os
import subprocess

from pathlib import Path
from app_system import AppInstaller


class TerminatorInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()

    def install(self):
        match self.os_id:
            case 'fedora':
                self.install_on_fedora()

            case 'ubuntu':
                self.install_on_ubuntu()

            case _:
                raise ValueError("OS not supported")

    def customize(self):
        config_file_link = Path('/home/me/.config/terminator/config')
        config_file_target = self.plugin_path.joinpath('profile')

        if config_file_link.is_file():
            os.remove(config_file_link)

        config_file_link.symlink_to(config_file_target)

        pass

    def install_on_fedora(self):
        subprocess.run(['sudo', 'dnf', 'install', '-y', 'terminator'])

    def install_on_ubuntu(self):
        subprocess.run(['sudo', 'add-apt-repository',
                       'ppa:mattrose/terminator'])
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt', 'install', '-y', 'terminator'])
