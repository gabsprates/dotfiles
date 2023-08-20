#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh
source ../../../common.sh

install() {
    echo ""
    echo "Java should will be installed by Jabba Version Manager"
    echo ""
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/java/customize.sh
}

install
apply_user_settings
