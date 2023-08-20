#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

apply_settings() {
    config_file=/home/me/.zshrc

    if [ -e $config_file ]; then
        rm $config_file
    fi

    if [ ! -e /home/me/.zsh_local ]; then
        cp "$DOTFILES_BASE_PATH"/me-custom/zsh/.zsh_local /home/me/.zsh_local
    fi

    ln -s "$DOTFILES_BASE_PATH"/me-custom/zsh/.zshrc $config_file

    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended --keep-zshrc
}

apply_settings
