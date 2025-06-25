import subprocess

from pathlib import Path
from app_system import AppInstaller


class JavaInstaller(AppInstaller):
    def __init__(self, os_id: str):
        self.os_id = os_id

    def install(self):
        subprocess.run(['asdf', 'plugin', 'add', 'java', 'https://github.com/halcyon/asdf-java.git'])
        subprocess.run(['asdf', 'install', 'java', 'latest:zulu-21'])
        subprocess.run(['asdf', 'set', '-u', 'java', 'latest:zulu-21'])

        zsh_local_path = Path('/home/me/.zsh_local')
        file_content = ''

        with open(zsh_local_path, 'r') as zsh_local:
            file_content = zsh_local.read()

        file_content = file_content.replace(
            "#java_profile", '''
## Java
[ -s "$HOME/.asdf/plugins/java/set-java-home.zsh" ] && source "$HOME/.asdf/plugins/java/set-java-home.zsh"
''')

        with open(zsh_local_path, 'w') as zsh_local:
            zsh_local.write(file_content)

    def customize(self):
        pass
