#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh
source ../../../common.sh

install() {
    which code &>/dev/null
    has_code=$?

    if [ $has_code -eq 0 ]; then
        return 0
    fi

    ln -s "$DOTFILES_BASE_PATH"/fedora/vscode/vscode.repo /etc/yum.repos.d/vscode.repo

    rpm --import https://packages.microsoft.com/keys/microsoft.asc

    dnf -qy install code
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/vscode/customize.sh
}

install
apply_user_settings
