#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../../common.sh

install() {
    dnf install -qy fedora-workstation-repositories

    dnf config-manager --set-enabled google-chrome

    dnf install -qy google-chrome-stable
}

install
