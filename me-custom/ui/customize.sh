#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

apply_settings() {
    # cat "$DOTFILES_BASE_PATH/me-custom/ui/profile"
    dconf load / <"$DOTFILES_BASE_PATH/me-custom/ui/profile"
}

apply_settings
