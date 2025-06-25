import subprocess

from app_system import AppInstaller


class FlameshotInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

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
        subprocess.run(['sudo', 'dnf', 'install', '-y', 'flameshot'])

    def install_on_ubuntu(self):
        subprocess.run(['sudo', 'apt', 'install', '-y', 'flameshot'])
