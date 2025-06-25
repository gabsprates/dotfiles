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
        pass

    def install_on_fedora(self):
        subprocess.run(['sudo', 'dnf', 'install', '-y', 'terminator'])

    def install_on_ubuntu(self):
        subprocess.run(['sudo', 'add-apt-repository', 'ppa:mattrose/terminator'])
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt', 'install', '-y', 'terminator'])
