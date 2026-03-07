import subprocess
import urllib.request
import tempfile

from dotfiles_toolkit.app_installer import AppInstaller
from pathlib import Path


class BraveInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        tmp_install = Path(tempfile.mkdtemp()).joinpath("install-brave.sh")

        urllib.request.urlretrieve(
            'https://dl.brave.com/install.sh', tmp_install)

        subprocess.run(['sh', tmp_install])

    def customize(self):
        pass
