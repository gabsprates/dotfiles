#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../common.sh

install() {
    which docker &>/dev/null
    has_docker=$?

    if [ $has_docker -eq 0 ]; then
        return 0
    fi

    dnf -qy install dnf-plugins-core

    dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

    dnf -qy install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    systemctl start docker
    systemctl enable docker

    gpasswd -a me docker

    systemctl restart docker

    run_as_me newgrp docker
}

install
