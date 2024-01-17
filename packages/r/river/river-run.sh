#!/bin/sh

export MOZ_ENABLE_WAYLAND=1
# Let the windows decide to use Wayland
# export QT_QPA_PLATFORM=wayland
export CLUTTER_BACKEND=wayland
export ECORE_EVAS_ENGINE=wayland
export ELM_ENGINE=wayland
export SDL_VIDEODRIVER=wayland
export _JAVA_AWT_WM_NONREPARENTING=1
export NO_AT_BRIDGE=1
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=river
export XDG_CURRENT_DESKTOP=river

systemd-cat --identifier=river /usr/bin/river -log-level debug $@
