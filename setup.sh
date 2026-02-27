#!/bin/bash

update_os() {
    echo "# Updating SO"

    case "$1" in
    fedora)
        sudo dnf upgrade -y
        ;;

    ubuntu)
        sudo apt update -y && sudo apt upgrade -y
        ;;
    esac

    return $?
}

install_dependencies() {
    echo "# Install dependencies"

    case "$1" in
    fedora)
        sudo dnf install curl git tree vim -y
        ;;

    ubuntu)
        sudo apt install -y curl git tree vim
        ;;
    esac

    return $?
}

clone_repo() {
    if [ -d /home/me/.dotfiles ]; then
        echo
        echo "# .dotfiles [OK]"
    else
        echo
        echo "# Cloning .dotfiles"
        git clone https://github.com/gabsprates/dotfiles.git /home/me/.dotfiles
        sed -i 's/https:\/\/github.com\//git@github.com:/' /home/me/.dotfiles/.git/config
    fi
}

main() {
    os="$(. /etc/os-release && echo "$ID")"

    echo "# Setting up: $os"
    echo

    update_os $os

    if [ $? -eq 0 ]; then install_dependencies $os; fi
    if [ $? -eq 0 ]; then clone_repo $os; fi

    echo
    echo "# Setup preparation done!"
}

main
