import subprocess
import urllib.request

from dotfiles_toolkit.app_installer import AppInstaller


class BraveInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        tmp_install = AppInstaller.create_temp_path("install-brave.sh")

        urllib.request.urlretrieve(
            'https://dl.brave.com/install.sh', tmp_install)

        subprocess.run(['sh', tmp_install])

    def customize(self):
        pass
