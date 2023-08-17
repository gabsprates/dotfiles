#!/bin/bash

export DOTFILES_BASE_PATH=/home/me/.dotfiles

function run_as_me {
    sudo -g me -u me "$@"
}