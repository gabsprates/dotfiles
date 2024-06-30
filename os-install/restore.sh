#!/bin/sh

cd "$(dirname "$0")" || exit

. ../global-vars.sh

setup_packages() {
    os="$(. /etc/os-release && echo "$ID")"

    packages_to_restore='
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
        terminator
        vscode

        gnome
        ui
    '

    if [ $# -gt 0 ]; then
        packages_to_restore=$(printf '%s\n' "$@")
    fi

    echo "> Current OS: ${os}"
    echo "${packages_to_restore}"

    printf '%s\n' "$packages_to_restore" |
        while IFS='' read -r ppackage; do
            package=$(echo "$ppackage" | sed -e 's/^[[:space:]]*//')

            if [ "$package" = '' ]; then
                continue
            fi

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
