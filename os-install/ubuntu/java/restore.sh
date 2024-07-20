#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../global-vars.sh
. ../../../common.sh

install() {
    echo ""
    echo "Java will be installed by asdf"
    echo ""
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/java/customize.sh
}

install
apply_user_settings
