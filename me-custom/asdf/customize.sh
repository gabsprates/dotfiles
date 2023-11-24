#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

apply_settings() {
    if [ -d /home/me/.asdf ]; then
        return 0
    fi

    git clone https://github.com/asdf-vm/asdf.git /home/me/.asdf --branch v0.13.1
}

apply_settings
