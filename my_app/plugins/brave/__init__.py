import subprocess
import urllib.request
import tempfile

from pathlib import Path
from app_system import AppInstaller


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
