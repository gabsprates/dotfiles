#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    apt install -qy flameshot
}

install
