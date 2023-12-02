#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../common.sh

install() {
    dnf install -qy gnome-tweaks
}

install
