#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

apply_settings() {
    PROFILE=/dev/null bash -c 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash'

    sed -i -e "/#nvm/r $DOTFILES_BASE_PATH/me-custom/javascript/nvm" -e '/#nvm/d' /home/me/.zsh_local
}

apply_settings
