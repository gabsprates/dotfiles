#!/bin/bash

cd "$(dirname "$0")" || exit

. ../../../common.sh

install() {
    snap install gimp
}

install
