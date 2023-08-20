#!/bin/bash

run_as_me() {
    sudo -g me -u me "$@"
}

add_flathub_remote_if_needed() {
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
}
