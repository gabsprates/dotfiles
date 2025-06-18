from pathlib import Path
from app_system import AppInstaller, run_as_me


class TerminatorInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()

    def install(self):
        run_as_me([
            'asdf', 'plugin', 'add', 'nodejs', 'https://github.com/asdf-vm/asdf-nodejs.git'
        ])
        run_as_me([
            'asdf', 'install', 'nodejs', 'latest:22'
        ])
        run_as_me([
            'asdf', 'set', '-u', 'nodejs', 'latest:22'
        ])

    def customize(self):
        pass
