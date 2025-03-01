#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    apt install -qy gnome-tweaks gnome-clocks
}

install
