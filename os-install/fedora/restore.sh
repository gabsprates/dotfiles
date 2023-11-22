#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

setup_packages() {
    all_packages=(
        1password
        # anydesk
        brave
        docker
        edge
        gimp
        git
        google-chrome
        htop
        inkscape
        java
        javascript
        slack
        # ssh
        vscode
        zsh

        # Additional packages
    )

    packages_to_restore=("${@:-${all_packages[@]}}")

    echo "${packages_to_restore[@]}"

    for package in "${packages_to_restore[@]}"; do
        status=""
        extra_info=""

        echo ""
        echo "Restoring: [ ${package} ]"

        if [ -e ./"$package"/restore.sh ]; then
            sh ./"$package"/restore.sh
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
