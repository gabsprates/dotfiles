#!/bin/env python3

import distro
import argparse

from pathlib import Path
from app_system import InstallerManager


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

    installer_manager = InstallerManager(
        plugin_dir=base_path.joinpath("plugins").resolve(),
        os_id=distro.id(),
        apps=args.apps
    )

    installer_manager.install_apps()
