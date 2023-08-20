#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../common.sh

install() {
    add_flathub_remote_if_needed

    flatpak install -y flathub org.inkscape.Inkscape
}

install
