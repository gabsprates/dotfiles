import os
import json
import subprocess
import urllib.request
import tarfile
import tempfile

from pathlib import Path
from app_system import AppInstaller


class GitInstaller(AppInstaller):
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
        config_file_link = Path('/home/me/.gitconfig')
        config_file_target = self.plugin_path.joinpath('.gitconfig')

        if config_file_link.is_file():
            os.remove(config_file_link)

        config_file_link.symlink_to(config_file_target)

    def install_on_fedora(self):
        subprocess.run(["sudo", "dnf", "copr", "enable", "atim/lazygit", "-y"])
        subprocess.run(["sudo", "dnf", "-qy", "install", "git", "lazygit"])
        subprocess.run(["sudo", "dnf", "-qy", "install", "git-lfs"])

    def install_on_ubuntu(self):
        subprocess.run(["sudo", "apt", "-qy", "install", "build-essential", "git"])
        subprocess.run(["curl", "-s", "https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh", "|", "sudo", "bash"])
        subprocess.run(["sudo", "apt-get", "install", "-qy", "git-lfs"])

        self.install_lazygit()

    def install_lazygit(self):
        lazygit_tmp = Path(tempfile.mkdtemp())
        lazygit_package_file = lazygit_tmp.joinpath("lazygit.tar.gz")
        lazygit_package_url = ""
        lazygit_releases_url = "https://api.github.com/repos/jesseduffield/lazygit/releases/latest"

        with urllib.request.urlopen(lazygit_releases_url) as response:
            json_data = json.loads(response.read().decode())
            lazygit_package_url = self.get_lazygit_linux_package_url(json_data)

        self.download_lazygit_linux_package(lazygit_package_url, lazygit_package_file)

        with tarfile.open(lazygit_package_file, 'r') as file:
            file.extract(member='lazygit', path=lazygit_tmp)

        subprocess.run(['sudo', 'cp', str(lazygit_tmp.joinpath("lazygit")), '/usr/local/bin/'])

    def download_lazygit_linux_package(self, url: str, lazygit_dest: Path):
        urllib.request.urlretrieve(url, lazygit_dest)

    def get_lazygit_linux_package_url(self, data):
        for asset in data['assets']:
            if asset['browser_download_url'].lower().endswith("_linux_x86_64.tar.gz"):
                return asset['browser_download_url']

