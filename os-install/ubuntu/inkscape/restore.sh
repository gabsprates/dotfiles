#!/bin/sh

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    snap install inkscape
}

install
