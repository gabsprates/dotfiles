import subprocess

from pathlib import Path
from app_system import AppInstaller


class UIInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()

    def install(self):
        pass

    def customize(self):
        profile_path = self.plugin_path.joinpath('profile')

        subprocess.run(f"dconf load / <{str(profile_path)}",
                       shell=True, text=True)
