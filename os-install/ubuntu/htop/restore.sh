#!/bin/bash

cd "$(dirname "$0")" || exit

. ../../../global-vars.sh
. ../../../common.sh

install() {
    apt install -qy htop
}

install
