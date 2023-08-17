#!/bin/bash

cd $(dirname "${0}")

source ../../common.sh

function install_vscode {
    which code &> /dev/null
    has_code=$?

    if [ $has_code -eq 0 ]
    then
        return 0
    fi
    
    ln -s ${DOTFILES_BASE_PATH}/fedora/vscode/vscode.repo /etc/yum.repos.d/vscode.repo

    rpm --import https://packages.microsoft.com/keys/microsoft.asc

    dnf -qy install code
}

function install_extensions {
    extensions=(
        dbaeumer.vscode-eslint
        esbenp.prettier-vscode
        EditorConfig.EditorConfig
        eamodio.gitlens
    )
    
	for extension in ${extensions[@]}
	do
        run_as_me code --install-extension ${extension}
	done
}

function apply_settings {
    run_as_me ln -s ${DOTFILES_BASE_PATH}/fedora/vscode/settings.json /home/me/.config/Code/User/settings.json
}

install_vscode
install_extensions
apply_settings