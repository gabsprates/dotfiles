import subprocess

from dotfiles_toolkit.app_installer import AppInstaller


class DockerInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        tmp_script = AppInstaller.download(
            "https://get.docker.com", "install-docker.sh")

        subprocess.run(["sudo", "sh", tmp_script])
        subprocess.run(["sudo", "systemctl", "start", "docker"])
        subprocess.run(["sudo", "systemctl", "enable", "docker"])
        subprocess.run(["sudo", "gpasswd", "-a", "me", "docker"])
        subprocess.run(["sudo", "systemctl", "restart", "docker"])

    def customize(self):
        pass
