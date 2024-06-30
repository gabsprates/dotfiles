#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../global-vars.sh
. ../../../common.sh

install_lazygit() {
    LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
    curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
    tar xf lazygit.tar.gz lazygit
    sh -c 'install lazygit /usr/local/bin'
    rm lazygit.tar.gz lazygit
}

install_git_lfs() {
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
    apt-get install git-lfs
}

install_github_cli() {
    mkdir -p -m 755 /etc/apt/keyrings &&
        wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null &&
        chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg &&
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list >/dev/null &&
        apt update &&
        apt install gh -y
}

install() {
    install_lazygit
    install_git_lfs
    install_github_cli
}

apply_user_settings() {
    run_as_me sh "$DOTFILES_BASE_PATH"/me-custom/git/customize.sh
}

install
apply_user_settings
