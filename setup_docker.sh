#!/bin/bash

echo "# Module: docker"

which docker > /dev/null

if [ $? -gt 0 ]
then
    echo "# Installing..."
    wget -q -O- https://get.docker.com | sh

    install_return=$?
    if [ $install_return -gt 0 ]
    then
        echo "# error"
        return $install_return
    fi


    echo
    echo "# Setup user..."
    # do I need this? [sudo groupadd docker]
    sudo usermod -aG docker $USER
    newgrp docker
    docker run hello-world
else
    echo "# Installed [OK]"
fi
