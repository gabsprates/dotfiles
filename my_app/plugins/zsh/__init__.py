import os
import subprocess
import shutil
from pathlib import Path
import tempfile
import stat

import urllib.request
from app_system import AppInstaller, run_as_me


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
            shutil.chown(local_config_file, 'me', 'me')

        run_as_me([
            'ln', '-s', self.plugin_path.joinpath('.zshrc'), config_file
        ])

        tmp_dir = tempfile.mkdtemp()
        tmp_script = Path(tmp_dir, "install-zsh.sh")

        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh", tmp_script)

        env = os.environ.copy()
        env["USER"] = "me"
        env["HOME"] = user_home
        env["CHSH"] = "no"
        env["RUNZSH"] = "no"
        env["KEEP_ZSHRC"] = "yes"

        os.chmod(tmp_script, stat.S_IXOTH)
        subprocess.run([tmp_script], env=env, shell=True)
        subprocess.run(['chown', '-R', "me:me", str(omz_path)])
        subprocess.run(['usermod', '--shell', '/usr/bin/zsh', 'me'])

    def install_on_fedora(self):
        subprocess.run(['dnf', 'install', '-y', 'zsh'])

    def install_on_ubuntu(self):
        subprocess.run(['apt', 'install', '-y', 'zsh'])
