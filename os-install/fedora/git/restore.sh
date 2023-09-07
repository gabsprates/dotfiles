#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh
source ../../../common.sh

install() {
    is_lazygit_repo_enabled=$(dnf copr list | grep "atim/lazygit")

    if [ ! "$is_lazygit_repo_enabled" ]; then
        dnf copr enable atim/lazygit -y
    fi

    dnf -qy install git lazygit
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/git/customize.sh
}

install
apply_user_settings
