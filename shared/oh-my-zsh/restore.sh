#!/bin/bash

cd $(dirname "${0}")

source ../../common.sh

function install_oh_my_zsh {
    if [ -e /home/me/.zshrc ]
    then
        rm /home/me/.zshrc
    fi

    run_as_me ln -s ${DOTFILES_BASE_PATH}/shared/oh-my-zsh/.zshrc /home/me/.zshrc

    run_as_me sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --keep-zshrc

    which chsh &> /dev/null
    has_chsh=$?

    if [ $has_chsh -gt 0 ]
    then
        echo "Changing shell for me..."
        usermod --shell /usr/bin/zsh me
        echo "Done!"
    fi
}

install_oh_my_zsh
