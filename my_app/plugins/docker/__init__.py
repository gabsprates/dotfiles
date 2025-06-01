import os
import subprocess
import sys
import urllib.request
import tempfile

from app_system import AppInstaller


class DockerInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        sys.path.append(os.path.dirname(__file__))

    def install(self):
        tmp_script = os.path.join(
            tempfile.mkdtemp(), "install-docker.sh")

        urllib.request.urlretrieve("https://get.docker.com", tmp_script)

        subprocess.run(["sh", tmp_script])
        subprocess.run(["systemctl", "start", "docker"])
        subprocess.run(["systemctl", "enable", "docker"])
        subprocess.run(["gpasswd", "-a", "me", "docker"])
        subprocess.run(["systemctl", "restart", "docker"])

    def customize(self):
        pass
