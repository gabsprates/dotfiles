#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../global-vars.sh
. ../../../common.sh

install() {
    echo ""
    echo "asdf should will be installed by user"
    echo ""
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/asdf/customize.sh
}

install
apply_user_settings
