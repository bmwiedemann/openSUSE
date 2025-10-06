#!/bin/bash

# Mimic behavior of old openSUSE-welcome with "Show on next boot" unchecked

LAUNCHER_XDG_FILE=org.opensuse.opensuse_welcome_launcher.desktop
LEGACY_XDG_FILE=org.opensuse.opensuse_welcome.desktop
OSWL_VERSION_TAG=1

# The legacy autostart was dropped let's remove it from homedir
if [[ -e "$HOME/.config/autostart/${LEGACY_XDG_FILE}" && \
      ! -e "/etc/xdg/autostart/${LEGACY_XDG_FILE}" ]]; then
    rm -f "$HOME/.config/autostart/${LEGACY_XDG_FILE}"
fi

# Show only once per version
if [ -f ${HOME}/.local/share/opensuse-welcome/launched ]; then
  if [ "$(cat ${HOME}/.local/share/opensuse-welcome/launched)" = "${OSWL_VERSION_TAG}" ]; then
    # We have already shown the laucher at this version - skipping
    exit 0
  fi
fi

test -d ${HOME}/.local/share/opensuse-welcome || mkdir -p ${HOME}/.local/share/opensuse-welcome
echo "${OSWL_VERSION_TAG}" > ${HOME}/.local/share/opensuse-welcome/launched

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
    welcome_binary=$(command -v opensuse-welcome)
elif [[ "$de" == *gnome* ]]; then
    welcome_binary=$(command -v gnome-tour)
fi

# Fallback to opensuse-welcome if nothing else is found
if [ -z "$welcome_binary" ]; then
    welcome_binary=$(command -v opensuse-welcome)
fi

if [ ! -z "$welcome_binary" ]; then
    $welcome_binary
fi
