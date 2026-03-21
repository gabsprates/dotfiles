import tarfile
import subprocess

from dotfiles_toolkit.app_installer import AppInstaller
from pathlib import Path


class AsdfInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        asdf_package_url = AppInstaller.get_asset_url_from_github(
            owner="asdf-vm",
            repo="asdf",
            filter=lambda url: url.lower().endswith("-linux-386.tar.gz"),
        )

        asdf_tmp = AppInstaller.download(asdf_package_url, "asdf.tar.gz")

        self.install_asdf(asdf_tmp)

    def customize(self):
        pass

    def install_asdf(self, tar_file: Path):
        dest = tar_file.parent

        with tarfile.open(tar_file, 'r') as file:
            file.extract(member='asdf', path=dest)

        subprocess.run(
            ['sudo', 'cp', str(dest.joinpath('asdf')), '/usr/local/bin/'])
