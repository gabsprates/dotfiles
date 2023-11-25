#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh
source /home/me/.asdf/asdf.sh

apply_settings() {
    asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git

    sed -i -e "/#nodejs_profile/r $DOTFILES_BASE_PATH/me-custom/javascript/profile" -e '/#nodejs_profile/d' /home/me/.zsh_local

    asdf install nodejs latest:20
    asdf global nodejs latest:20
}

apply_settings
