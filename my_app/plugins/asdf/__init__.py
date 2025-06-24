import json
import os
import urllib.request
import tarfile
import tempfile

from pathlib import Path
from app_system import AppInstaller


class AsdfInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        asdf_tmp = Path(tempfile.mkdtemp()).joinpath("asdf.tar.gz")
        asdf_package_url = self.get_asdf_linux_package_url()

        self.download_asdf_linux_package(asdf_package_url, asdf_tmp)
        self.install_asdf(asdf_tmp)

    def customize(self):
        pass

    def get_asdf_linux_package_url(self):
        asdf_releases_url = "https://api.github.com/repos/asdf-vm/asdf/releases/latest"

        with urllib.request.urlopen(asdf_releases_url) as response:
            json_data = json.loads(response.read().decode())

            for asset in json_data['assets']:
                if asset['browser_download_url'].endswith("-linux-386.tar.gz"):
                    return asset['browser_download_url']

    def download_asdf_linux_package(self, url: str, dest: Path):
        urllib.request.urlretrieve(url, dest)

    def install_asdf(self, tar_file: Path):
        dest = Path('/usr/local/bin/')
        with tarfile.open(tar_file, 'r') as file:
            file.extract(member='asdf', path=dest)
