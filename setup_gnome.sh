#!/bin/bash

setup_appearance() {
  gsettings set org.gnome.desktop.interface gtk-theme 'Yaru-dark'
  gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 16
  gsettings set org.gnome.shell.extensions.desktop-icons show-home false
  gsettings set org.gnome.shell.extensions.desktop-icons show-trash false
}

setup_top_bar() {
  gsettings set org.gnome.desktop.interface clock-show-seconds true
}

setup_nautilus() {
  gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'
  gsettings set org.gnome.nautilus.list-view use-tree-view true
  gsettings set org.gnome.nautilus.list-view default-zoom-level 'small'
}

setup_bg() {
    file_name='20150326_120831_grey.jpg'

    current_path=$( dirname $( realpath $0 ) )
    current_bg=$( gsettings get org.gnome.desktop.background picture-uri )

    new_bg="file://${current_path}/${file_name}"
 
    gsettings set org.gnome.desktop.background picture-uri $new_bg || gsettings set org.gnome.desktop.background picture-uri $current_bg
}

setup_all() {
    setup_appearance
    setup_top_bar
    setup_nautilus
    setup_bg
}

case $1 in
    all) setup_all ;;
    top_bar) setup_top_bar ;;
    nautilus) setup_nautilus ;;
    interface) setup_appearance ;;
    background) setup_bg ;;
    *)
        echo "[Error] available options:"
        echo "  - all"
        echo "  - top_bar"
        echo "  - nautilus"
        echo "  - interface"
        echo "  - background"
    ;;
esac
