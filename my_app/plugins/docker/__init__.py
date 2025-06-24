import os
import subprocess
import sys
import urllib.request
import tempfile

from app_system import AppInstaller


class DockerInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        tmp_script = Path(tempfile.mkdtemp()).joinpath("install-docker.sh")

        urllib.request.urlretrieve("https://get.docker.com", tmp_script)

        subprocess.run(["sudo", "sh", tmp_script])
        subprocess.run(["sudo", "systemctl", "start", "docker"])
        subprocess.run(["sudo", "systemctl", "enable", "docker"])
        subprocess.run(["sudo", "gpasswd", "-a", "me", "docker"])
        subprocess.run(["sudo", "systemctl", "restart", "docker"])

    def customize(self):
        pass
