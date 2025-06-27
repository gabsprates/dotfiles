import os
import subprocess
import shutil
import tempfile
import urllib.request

from pathlib import Path
from app_system import AppInstaller


class ZshInstaller(AppInstaller):
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
        user_home = Path('/', 'home', 'me')
        omz_path = user_home.joinpath('.oh-my-zsh')
        config_file = user_home.joinpath(".zshrc")
        local_config_file = user_home.joinpath(".zsh_local")

        if config_file.is_file():
            os.remove(config_file)

        if not local_config_file.is_file():
            shutil.copy(self.plugin_path.joinpath(
                '.zsh_local'), local_config_file)

        config_file.symlink_to(self.plugin_path.joinpath('.zshrc'))

        tmp_script = Path(tempfile.mkdtemp(), "install-zsh.sh")

        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh", tmp_script)

        subprocess.run(['sh', tmp_script, '--unattended', '--keep-zshrc'])
        subprocess.run(['sudo', 'usermod', '--shell', '/usr/bin/zsh', 'me'])

    def install_on_fedora(self):
        subprocess.run(['sudo', 'dnf', 'install', '-y', 'zsh'])

    def install_on_ubuntu(self):
        subprocess.run(['sudo', 'apt', 'install', '-y', 'zsh'])
