#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../global-vars.sh

install() {
    which anydesk &>/dev/null
    has_anydesk=$?

    if [ $has_anydesk -eq 0 ]; then
        return 0
    fi

    temp_dir=$(mktemp -d)
    anydesk_version=anydesk_6.3.0-1_x86_64.rpm

    wget -O "$temp_dir"/"$anydesk_version" https://download.anydesk.com/linux/"$anydesk_version"

    dnf -y --skip-broken install "$temp_dir"/"$anydesk_version"
}

install
