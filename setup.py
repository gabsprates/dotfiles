import os
import subprocess
import distro


def is_valid_os(os_id: str):
    if not os_id in [
        'fedora', 'ubuntu'
    ]:
        raise ValueError()


def update_os(os_id: str):
    print('## Updating SO')

    os_update = {
        'fedora': [
            ['sudo', 'dnf', 'upgrade', '-y'],
        ],

        'ubuntu': [
            ['sudo', 'apt', 'update', '-y'],
            ['sudo', 'apt', 'upgrade', '-y']
        ],
    }

    update_commands = os_update[os_id]

    for command in update_commands:
        update_result = subprocess.run(command)

        if update_result.returncode != 0:
            raise RuntimeError()


def install_dependencies(os_id: str):
    print("## Install dependencies")

    os_install_dependencies = {
        'fedora': [
            'sudo', 'dnf', 'install', '-y', 'curl', 'git', 'vim'
        ],

        'ubuntu': [
            'sudo', 'apt', 'install', '-y', 'curl', 'git', 'vim'
        ]
    }

    install_dependencies_command = os_install_dependencies[os_id]
    install_dependencies_result = subprocess.run(install_dependencies_command)

    if install_dependencies_result.returncode != 0:
        raise RuntimeError()


def clone_repo(dotfiles_path: str):
    if os.path.isdir(dotfiles_path):
        print('## .dotfiles [OK]')

    else:
        print('## Cloning .dotfiles')
        subprocess.run([
            'git', 'clone', 'https://github.com/gabsprates/dotfiles.git', dotfiles_path
        ])

        gitconfig_path = dotfiles_path + '/.git/config'

        file_content = ''

        with open(gitconfig_path, 'r') as gitconfig:
            file_content = gitconfig.read()

        file_content = file_content.replace(
            "https://github.com/", "git@github.com:")

        with open(gitconfig_path, 'w') as gitconfig:
            gitconfig.write(file_content)


def main():
    os_id = distro.id()

    is_valid_os(os_id)

    print('# Setting up:', os_id, '\n')

    update_os(os_id)

    install_dependencies(os_id)

    clone_repo('/home/me/.dotfiles-asdf')

    print('\n', '# Setup preparation done!')


try:
    main()

except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
