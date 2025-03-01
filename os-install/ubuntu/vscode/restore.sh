#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../global-vars.sh
. ../../../common.sh

install() {
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >packages.microsoft.gpg

    install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

    echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list >/dev/null

    rm -f packages.microsoft.gpg

    apt install -y apt-transport-https
    apt update
    apt install -y code
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/vscode/customize.sh
}

install
apply_user_settings
