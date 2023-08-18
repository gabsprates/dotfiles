#!/bin/bash

cd $(dirname "${0}")

source ../../common.sh

run_as_me ln -s ${DOTFILES_BASE_PATH}/shared/git/.gitconfig /home/me/.gitconfig
