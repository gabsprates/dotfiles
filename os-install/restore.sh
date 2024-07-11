#!/bin/bash

cd "$(dirname "$0")" || exit

source ../global-vars.sh

setup_packages() {
    os="$(. /etc/os-release && echo "$ID")"

    all_packages=(
        1password
        git
        zsh
        asdf

        brave
        docker
        flameshot
        edge
        gimp
        google-chrome
        htop
        inkscape
        java
        javascript
        slack
        # ssh
        terminator
        vscode

        gnome
        ui

        # Additional packages
    )

    packages_to_restore=("${@:-${all_packages[@]}}")

    echo "${os}"
    echo "${packages_to_restore[@]}"

    for package in "${packages_to_restore[@]}"; do
        status=""
        extra_info=""

        echo ""
        echo "Restoring: [ ${package} ]"

        if [ -e ./"$os"/"$package"/restore.sh ]; then
            sh ./"$os"/"$package"/restore.sh
            status="DONE"
        else
            status="SKIPED"
            extra_info="Package not found"
        fi

        echo "Restored status: ${status}"

        if [ "$extra_info" ]; then
            echo "      @> $extra_info"
        fi

        echo ""
    done
}

setup_packages "$@"
