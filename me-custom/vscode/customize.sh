#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

install_extensions() {
    extensions=(
        dbaeumer.vscode-eslint
        esbenp.prettier-vscode
        EditorConfig.EditorConfig
        eamodio.gitlens
        timonwong.shellcheck
        foxundermoon.shell-format
        vscjava.vscode-java-pack
        pnp.polacode
    )

    for extension in "${extensions[@]}"; do
        code --install-extension "${extension}"
    done
}

apply_settings() {
    # settings
    config_file=/home/me/.config/Code/User/settings.json

    if [ -e $config_file ]; then
        rm $config_file
    fi

    ln -s "$DOTFILES_BASE_PATH"/me-custom/vscode/settings.json $config_file

    # shortcuts
    shortcuts_file=/home/me/.config/Code/User/keybindings.json

    if [ -e $shortcuts_file ]; then
        rm $shortcuts_file
    fi

    ln -s "$DOTFILES_BASE_PATH"/me-custom/vscode/shortcuts.json $shortcuts_file
}

install_extensions
apply_settings
