import subprocess
import tempfile
import urllib.request

from pathlib import Path
from app_system import AppInstaller

download_urls = {
    "fedora": "https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm",
    "ubuntu": "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
}

package_types = {
    "fedora": "rpm",
    "ubuntu": "deb",
}


class GoogleChromeInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.download_url = download_urls[os_id]
        self.package_type = package_types[os_id]

    def install(self):
        tmp_package = Path(
            tempfile.mkdtemp(), "install-google-chrome." + self.package_type)

        urllib.request.urlretrieve(self.download_url, tmp_package)

        match self.os_id:
            case 'fedora':
                self.install_on_fedora(tmp_package)

            case 'ubuntu':
                self.install_on_ubuntu(tmp_package)

            case _:
                raise ValueError("OS not supported")

    def install_on_fedora(self, package):
        subprocess.run(['sudo', 'rpm', '-i', package])

    def install_on_ubuntu(self, package):
        subprocess.run(['sudo', 'apt', 'install', package])

    def customize(self):
        pass
