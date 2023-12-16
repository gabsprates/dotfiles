#!/bin/sh

toggle_hand() {
    is_left_handed=$(gsettings get org.gnome.desktop.peripherals.mouse left-handed)

    if [ "$is_left_handed" = 'true' ]; then
        gsettings set org.gnome.desktop.peripherals.mouse left-handed false
    else
        gsettings set org.gnome.desktop.peripherals.mouse left-handed true
    fi
}

toggle_hand
