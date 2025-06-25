import subprocess

from pathlib import Path
from app_system import AppInstaller


class JavaScriptInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()

    def install(self):
        subprocess.run(['asdf', 'plugin', 'add', 'nodejs', 'https://github.com/asdf-vm/asdf-nodejs.git'])
        subprocess.run(['asdf', 'install', 'nodejs', 'latest:22'])
        subprocess.run(['asdf', 'set', '-u', 'nodejs', 'latest:22'])
        print("\nFor more info about corepack, check https://github.com/asdf-vm/asdf-nodejs?tab=readme-ov-file#corepack")

    def customize(self):
        pass
