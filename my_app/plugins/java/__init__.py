from pathlib import Path
from app_system import AppInstaller


class JavaInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id
        self.plugin_path = Path(__file__).parent.resolve()

    def install(self):
        print("Not possible to install as `me` user. Run the following commands to install it:\n")
        print('asdf plugin add java https://github.com/halcyon/asdf-java.git')
        print('asdf install java latest:zulu-21')
        print('asdf set -u java latest:zulu-21')

        print('\nAdd the following on your ~/.zsh_local file:\n')
        print('''
## Java
[ -s "$HOME/.asdf/plugins/java/set-java-home.zsh" ] && source "$HOME/.asdf/plugins/java/set-java-home.zsh"
'''
              )

    def customize(self):
        pass
