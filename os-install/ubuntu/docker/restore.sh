#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    # hash docker &>/dev/null
    # has_docker=$?

    # if [ $has_docker -eq 0 ]; then
    #     return 0
    # fi

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    chmod a+r /etc/apt/keyrings/docker.asc

    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        tee /etc/apt/sources.list.d/docker.list > /dev/null

    apt update
    apt install -qy docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    systemctl start docker
    systemctl enable docker

    gpasswd -a me docker

    systemctl restart docker
}

install
