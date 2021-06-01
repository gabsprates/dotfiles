#!/bin/bash

echo "# Module: zsh / oh-my-zsh"

which zsh > /dev/null

if [ $? -gt 0 ]
then
    echo "# Installing..."
    sudo apt-get install zsh -y

    install_return=$?
    if [ $install_return -gt 0 ]
    then
        echo "# error"
        return $install_return
    fi
    
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    rm ~/.zshrc
    ln -s ~/.dotfiles/.zshrc ~/.zsh.rc
else
    echo "# Installed [OK]"
fi
