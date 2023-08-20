#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh
source ../../../common.sh

install() {
    dnf -qy install zsh
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/zsh/customize.sh

    usermod --shell /usr/bin/zsh me
}

install
apply_user_settings
