#!/bin/bash

update_upgrade() {
    echo '# Updating SO'
    sudo apt-get update && sudo apt-get upgrade -y
}

setup_build_essentials() {
    echo '# Module: build-essential'
    
    which make > /dev/null
    has_make=$?

    which gcc > /dev/null
    has_gcc=$?

    if [ $has_make -eq 0 ] && [ $has_gcc -eq 0 ]
    then
        echo '# Installed [OK]'
        return 0
    fi

    echo '# Installing...'
    return $(sudo apt-get install build-essential -y)
}

setup_git() {
    echo '# Module: git'
    
    which git > /dev/null

    if [ $? -eq 0 ] && [ $has_gcc -eq 0 ]
    then
        echo '# Installed [OK]'
        return 0
    fi

    echo '# Installing...'
    return $(sudo apt-get install git -y)
}

# Updating SO
update_upgrade

# Setup packages
setup_build_essentials
setup_git
