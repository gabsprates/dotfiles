#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh
source ../../../common.sh

install() {
    dnf -qy install git
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/git/customize.sh
}

install
apply_user_settings
