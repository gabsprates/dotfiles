#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

    dpkg -i google-chrome-stable_current_amd64.deb

    rm google-chrome-stable_current_amd64.deb
}

install
