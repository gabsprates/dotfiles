#!/bin/bash

update_upgrade() {
    echo "# Updating SO"
    sudo apt-get update && sudo apt-get upgrade -y
    return $?
}

setup_build_essentials() {
    echo "\n# Module: build-essential"
    
    which make > /dev/null
    has_make=$?

    which gcc > /dev/null
    has_gcc=$?

    if [ $has_make -eq 0 ] && [ $has_gcc -eq 0 ]
    then
        echo "# Installed [OK]"
        return 0
    fi

    echo "# Installing..."
    sudo apt-get install build-essential -y
    return $?
}

setup_git() {
    echo "\n# Module: git"
    
    which git > /dev/null

    if [ $? -eq 0 ]
    then
        echo "# Installed [OK]"
        return 0
    fi

    echo "# Installing..."
    sudo apt-get install git -y
    return $?
}

setup_curl() {
    echo "\n# Module: curl"
    
    which curl > /dev/null

    if [ $? -eq 0 ]
    then
        echo "# Installed [OK]"
        return 0
    fi

    echo "# Installing..."
    sudo apt-get install curl -y
    return $?
}

# Updating SO
update_upgrade

# Setup packages
if [ $? -eq 0 ]; then setup_build_essentials; fi
if [ $? -eq 0 ]; then setup_git; fi
if [ $? -eq 0 ]; then setup_curl; fi

if [ -d ~/.dotfiles ] && [ $? -gt 0 ]
then
    echo "\n# Cloning .dotfiles"
    git clone https://github.com/gabsprates/dotfiles.git ~/.dotfiles
fi
