#!/bin/env python3

import os
import sys
import distro
from app_system import AppManager


def get_default_apps():
    return [
        'git',
        'docker',

        'asdf',
        'javascript',
        'java',
        'vscode',

        'zsh',
        'terminator',

        'brave',
        'google-chrome',
        'gimp',
        'gnome'
        'inkscape',
        'flameshot',
    ]


if __name__ == "__main__":
    apps = sys.argv[1:]
    base_path = os.path.dirname(__file__)

    app_manager = AppManager(
        plugin_dir=os.path.join(base_path, "plugins"),
        os_id=distro.id(),
        apps=apps
    )

    app_manager.install_apps()

# 'zsh',              # general
# 'asdf',             # general
# 'docker',           # general
# 'htop',             # general
# 'openvpn3',         # general
# 'telnet',           # general
# 'terminator',       # general

# 'vscode',           # general
# 'javascript',       # general
# 'java',             # general
# 'maven, ant',       # general (depends on java)

# 'brave',            # general
# 'google-chrome',    # general
# 'gimp',             # general
# 'gnome'             # general
# 'inkscape',         # general
# 'flameshot',        # general
