#!/bin/bash

# Mimic behavior of old openSUSE-welcome with "Show on next boot" unchecked

LAUNCHER_XDG_FILE=org.opensuse.opensuse_welcome_launcher.desktop
ORIG_XDG_FILE=/org.opensuse.opensuse_welcome.desktop

# Override also the original's openSUSE-welcome startup
if [[ -e "/etc/xdg/autostart/${LAUNCHER_XDG_FILE}" && \
      ! -e "$HOME/.config/autostart/${LAUNCHER_XDG_FILE}" ]]; then
    cp /etc/xdg/autostart/${LAUNCHER_XDG_FILE} ${HOME}/.config/autostart/${LAUNCHER_XDG_FILE}
    cp /etc/xdg/autostart/${LAUNCHER_XDG_FILE} ${HOME}/.config/autostart/${ORIG_XDG_FILE}
fi


detect_de() {
    if [ -n "$XDG_CURRENT_DESKTOP" ]; then
        echo "$XDG_CURRENT_DESKTOP" | tr '[:upper:]' '[:lower:]'
    elif [ -n "$DESKTOP_SESSION" ]; then
        echo "$DESKTOP_SESSION" | tr '[:upper:]' '[:lower:]'
    else
        echo ""
    fi
}

de=$(detect_de)
welcome_binary=""

# Prefer Session specific greeter
if [[ "$de" == *plasma* ]]; then
    welcome_binary=$(command -v plasma-welcome)
elif [[ "$de" == *gnome* ]]; then
    welcome_binary=$(command -v gnome-tour)
fi

# Fallback to opensuse-welcome if nothing else is found
if [ -z "$welcome_binary" ]; then
    welcome_binary=$(command -v opensuse-welcome)
fi

if [ ! -z "$welcome_binary" ]; then
    $welcome_binary
else
    echo "No matching welcome tool is available; however, we can't leave it like this!"
    echo "So let me at least say: Welcome, and have a lot of fun!"
fi
