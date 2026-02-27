import subprocess
import tempfile
import urllib
import urllib.request

from pathlib import Path
from app_system import AppInstaller

download_urls = {
    "fedora": "https://code.visualstudio.com/sha/download?build=stable&os=linux-rpm-x64",
    "ubuntu": "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64",
}

package_types = {
    "fedora": "rpm",
    "ubuntu": "deb",
}


class VSCodeInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()
        self.download_url = download_urls[os_id]
        self.package_type = package_types[os_id]

    def install(self):
        tmp_package = Path(
            tempfile.mkdtemp(), "install-vscode." + self.package_type)

        urllib.request.urlretrieve(self.download_url, tmp_package)

        match self.os_id:
            case 'fedora':
                self.install_on_fedora(tmp_package)

            case 'ubuntu':
                self.install_on_ubuntu(tmp_package)

            case _:
                raise ValueError("OS not supported")

    def customize(self):
        self.install_extensions()
        self.apply_settings()
        self.apply_shortcuts()

    def install_on_fedora(self, package):
        subprocess.run(['sudo', 'rpm', '-i', package])

    def install_on_ubuntu(self, package):
        subprocess.run(['sudo', 'apt', 'install', package])

    def install_extensions(self):
        extensions = [
            "dbaeumer.vscode-eslint",
            "esbenp.prettier-vscode",
            "EditorConfig.EditorConfig",
            "eamodio.gitlens",
            "ms-python.autopep8",
        ]

        for extension in extensions:
            subprocess.run(["code", "--install-extension", extension])

    def apply_settings(self):
        config_file = Path("/home/me/.config/Code/User/settings.json")
        config_file.symlink_to(self.plugin_path.joinpath('settings.json'))

    def apply_shortcuts(self):
        shortcuts_file = Path("/home/me/.config/Code/User/keybindings.json")
        shortcuts_file.symlink_to(self.plugin_path.joinpath('shortcuts.json'))
