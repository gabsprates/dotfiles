#!/bin/bash

cd "$(dirname "$0")" || exit

source ../../global-vars.sh

apply_settings() {
    curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | bash -s -- --skip-rc && . /home/me/.jabba/jabba.sh

    sed -i -e "/#java_profile/r $DOTFILES_BASE_PATH/me-custom/java/profile" -e '/#java_profile/d' /home/me/.zsh_local

    jabba install 6=tgz+https://cdn.azul.com/zulu/bin/zulu6.22.0.3-jdk6.0.119-linux_x64.tar.gz
    jabba install 7=tgz+https://cdn.azul.com/zulu/bin/zulu7.56.0.11-ca-jdk7.0.352-linux_x64.tar.gz
    jabba install 8=tgz+https://cdn.azul.com/zulu/bin/zulu8.72.0.17-ca-jdk8.0.382-linux_x64.tar.gz
    jabba install 11=tgz+https://cdn.azul.com/zulu/bin/zulu11.66.15-ca-jdk11.0.20-linux_x64.tar.gz
    jabba install 17=tgz+https://cdn.azul.com/zulu/bin/zulu17.44.17-ca-crac-jdk17.0.8-linux_x64.tar.gz

    jabba alias default 8
}

install_maven() {
    maven_version=3.9.4
    maven_path=/home/me/.maven
    zip_file=apache-maven-${maven_version}-bin.zip

    rm -fr $maven_path
    mkdir $maven_path

    wget -O "$maven_path"/"$zip_file" https://archive.apache.org/dist/maven/maven-3/${maven_version}/binaries/${zip_file}

    unzip -q "$maven_path"/"$zip_file" -d $maven_path

    ln -s "$maven_path"/apache-maven-${maven_version} "$maven_path"/maven
}

apply_settings
install_maven
