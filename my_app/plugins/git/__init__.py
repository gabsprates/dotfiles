import importlib
import os
import sys

from pathlib import Path
from app_system import AppInstaller


class GitInstaller(AppInstaller):
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
        config_file_link = Path('/home/me/.gitconfig')
        config_file_target = self.plugin_path.joinpath('.gitconfig')

        if config_file_link.is_file():
            os.remove(config_file)

        config_file_link.symlink_to(config_file_target)


    def install_on_fedora(self):
        subprocess.run(["sudo", "dnf", "copr", "enable", "atim/lazygit", "-y"])
        subprocess.run(["sudo", "dnf", "-qy", "install", "git", "lazygit"])
        subprocess.run(["sudo", "dnf", "-qy", "install", "git-lfs"])


    def install_on_ubuntu(self):
        pass