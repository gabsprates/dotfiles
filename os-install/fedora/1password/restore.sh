#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh

install() {
    which 1password &>/dev/null
    has_1password=$?

    if [ $has_1password -eq 0 ]; then
        return 0
    fi

    ln -s "$DOTFILES_BASE_PATH"/fedora/1password/1password.repo /etc/yum.repos.d/1password.repo

    rpm --import https://downloads.1password.com/linux/keys/1password.asc

    dnf -qy install 1password 1password-cli
}

install
