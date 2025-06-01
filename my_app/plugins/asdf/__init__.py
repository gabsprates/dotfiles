import json
import os
import sys
import urllib.request
import tarfile

from app_system import AppInstaller


class AsdfInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        sys.path.append(os.path.dirname(__file__))

    def install(self):
        asdf_tmp = os.path.join("/tmp", "asdf.tar.gz")
        asdf_package_url = ""
        asdf_releases_url = "https://api.github.com/repos/asdf-vm/asdf/releases/latest"

        with urllib.request.urlopen(asdf_releases_url) as response:
            json_data = json.loads(response.read().decode())
            asdf_package_url = self.get_asdf_linux_package_url(json_data)

        self.download_asdf_linux_package(asdf_package_url, asdf_tmp)
        self.install_asdf(asdf_tmp)

    def customize(self):
        print("asdfasdfasfasdfasdfa")
        pass

    def get_asdf_linux_package_url(self, data):
        for asset in data['assets']:
            if asset['browser_download_url'].endswith("-linux-arm64.tar.gz"):
                return asset['browser_download_url']

    def download_asdf_linux_package(self, url: str, dest: str):
        urllib.request.urlretrieve(url, dest)

    def install_asdf(self, tar_file: str):
        dest = '/usr/local/bin/'
        with tarfile.open(tar_file, 'r') as file:
            file.extract(member='asdf', path=dest)
