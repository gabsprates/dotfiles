#!/bin/bash

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    add-apt-repository ppa:mattrose/terminator
    apt-get update
    apt install -qy terminator
}

install
