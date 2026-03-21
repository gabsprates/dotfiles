import subprocess
import shutil

from dotfiles_toolkit.app_installer import AppInstaller
from pathlib import Path


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
        local_config_file = user_home.joinpath(".zsh_local")

        if not local_config_file.is_file():
            shutil.copy(self.plugin_path.joinpath(
                '.zsh_local'), local_config_file)

        AppInstaller.create_symlink(
            link=user_home.joinpath(".zshrc"),
            target=self.plugin_path.joinpath('.zshrc')
        )

        tmp_script = AppInstaller.download(
            "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
            "install-zsh.sh",
        )

        subprocess.run(['sh', tmp_script, '--unattended', '--keep-zshrc'])
        subprocess.run(['sudo', 'usermod', '--shell', '/usr/bin/zsh', 'me'])

    def install_on_fedora(self):
        subprocess.run(['sudo', 'dnf', 'install', '-y', 'zsh'])

    def install_on_ubuntu(self):
        subprocess.run(['sudo', 'apt', 'install', '-y', 'zsh'])
