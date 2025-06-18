from pathlib import Path
from app_system import AppInstaller, run_as_me


class TerminatorInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()

    def install(self):
        print("Not possible to install as `me` user. Run the following commands to install it:")
        print('asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git')
        print('asdf install nodejs latest:22')
        print('asdf set -u nodejs latest:22')
        print('\n')
        print("For more info about corepack, check https://github.com/asdf-vm/asdf-nodejs?tab=readme-ov-file#corepack")

    def customize(self):
        pass
