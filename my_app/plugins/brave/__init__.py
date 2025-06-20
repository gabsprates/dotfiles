import os
import subprocess
import sys

import urllib.request
from app_system import AppInstaller


class BraveInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        sys.path.append(os.path.dirname(__file__))

    def install(self):
        tmp_install = '/tmp/brave.sh'

        urllib.request.urlretrieve(
            'https://dl.brave.com/install.sh', tmp_install)

        subprocess.run(['sh', tmp_install])

    def customize(self):
        pass
