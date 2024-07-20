#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../global-vars.sh

ASDF_DIR="/home/me/.asdf"
. /home/me/.asdf/asdf.sh

apply_settings() {
    asdf plugin-add java https://github.com/halcyon/asdf-java.git

    sed -i -e "/#java_profile/r $DOTFILES_BASE_PATH/me-custom/java/profile" -e '/#java_profile/d' /home/me/.zsh_local

    asdf install java latest:zulu-11
    asdf global java latest:zulu-11
}

apply_settings
