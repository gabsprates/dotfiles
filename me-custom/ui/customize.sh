#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../global-vars.sh

apply_settings() {
    dconf load / < "$DOTFILES_BASE_PATH/me-custom/ui/profile"
}

apply_settings
