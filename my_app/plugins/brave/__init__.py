import subprocess

from dotfiles_toolkit.app_installer import AppInstaller


class BraveInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        tmp_install = AppInstaller.create_temp_path("install-brave.sh")

        tmp_install = AppInstaller.download(
            "https://dl.brave.com/install.sh", "install-brave.sh")

        subprocess.run(['sh', tmp_install])

    def customize(self):
        pass
