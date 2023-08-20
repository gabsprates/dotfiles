#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

apply_settings() {
    config_file=/home/me/.gitconfig

    if [ -e $config_file ]; then
        rm $config_file
    fi

    ln -s "$DOTFILES_BASE_PATH"/me-custom/git/.gitconfig $config_file
}

apply_settings
