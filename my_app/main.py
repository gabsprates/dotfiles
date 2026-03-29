#!/bin/env python3

import distro
import argparse

from dotfiles_toolkit.install_manager import InstallManager
from pathlib import Path


def get_default_apps():
    return [
        'git',
        'docker',
        'asdf',
        'zsh',
        'terminator',

        'javascript',
        'java',
        'vscode',

        'brave',
        'google-chrome',
        'gimp',
        'gnome',
        'ui',
        'inkscape',
        'flameshot',
    ]


if __name__ == "__main__":
    default_apps = get_default_apps()
    base_path = Path(__file__).parent.resolve()

    parser = argparse.ArgumentParser()
    parser.add_argument('apps', nargs='+',
                        choices=default_apps, help='apps to install')

    args = parser.parse_args()

    install_manager = InstallManager(
        apps_path=base_path.joinpath("plugins").resolve(),
        distro=distro.id(),
    )

    for app in args.apps:
        install_manager.register(app)

    install_manager.install_apps()
