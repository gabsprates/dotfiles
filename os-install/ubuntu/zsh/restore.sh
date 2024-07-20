#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../global-vars.sh
. ../../../common.sh

install() {
    apt install -y zsh
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/zsh/customize.sh

    usermod --shell /usr/bin/zsh me
}

install
apply_user_settings
