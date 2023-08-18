#!/bin/bash

cd $(dirname "${0}")

source ../../common.sh

function install_jabba {
    echo "Installing Jabba"

    curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | bash -s -- --skip-rc && . /home/me/.jabba/jabba.sh

    # TODO: make it replace some tag to prevent duplication
    cat ${DOTFILES_BASE_PATH}/shared/java/jabba >> /home/me/.zsh_local

    jabba install 6=tgz+https://cdn.azul.com/zulu/bin/zulu6.22.0.3-jdk6.0.119-linux_x64.tar.gz
    jabba install 7=tgz+https://cdn.azul.com/zulu/bin/zulu7.56.0.11-ca-jdk7.0.352-linux_x64.tar.gz
    jabba install 8=tgz+https://cdn.azul.com/zulu/bin/zulu8.72.0.17-ca-jdk8.0.382-linux_x64.tar.gz
    jabba install 11=tgz+https://cdn.azul.com/zulu/bin/zulu11.66.15-ca-jdk11.0.20-linux_x64.tar.gz
    jabba install 17=tgz+https://cdn.azul.com/zulu/bin/zulu17.44.17-ca-crac-jdk17.0.8-linux_x64.tar.gz

    jabba alias default 8

    echo "Done!"
}

install_jabba


