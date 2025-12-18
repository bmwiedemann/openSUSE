#!/bin/sh

#
# If the virtual keyboard of Plasma Wayland has not been configured,
# configure it for this IM.
#

im_name="ibus"
desktop_file="/usr/share/applications/org.freedesktop.IBus.Panel.Wayland.Gtk3.desktop"

# Do nothing for X11 session
if [ "$XDG_SESSION_TYPE" != "wayland" ]; then
    return 0
fi

# Do nothing if kreadconfig6 is not available
if ! command -v kreadconfig6 >/dev/null 2>&1; then
    return 0
fi

# check current virtual keyboard
current_im=$(kreadconfig6 --file kwinrc --group Wayland --key InputMethod)

#
# initialize virtual keyboard if not configured yet
#

# check if $XDG_CONFIG_HOME/plasma_wayland_input_method_configured does not exist
config_dir="${XDG_CONFIG_HOME:-$HOME/.config}"
stamp_file="$config_dir/plasma_wayland_input_method_configured"
if [ ! -e "$stamp_file" ]; then
    mkdir -p "$config_dir"
    echo "$im_name" > "$stamp_file"

    # check current virtual keyboard is None
    if [ -z "$current_im" ]; then
        # The virtual keyboard is not configured
        echo "$0 is configuring the virtual keyboard for IBus."
        current_im=$desktop_file
        kwriteconfig6 --file kwinrc --group Wayland --key InputMethod $current_im
    else
        echo "$0 detected a virtual keyboard configured."
    fi
fi

#
# export environment variables for applications running on Xwayland
#
if [ "$current_im" = "$desktop_file" ]; then
    # do not override Qt IM module settings
    if [ -z "$QT_IM_MODULE" ] && [ -z "$QT_IM_MODULES" ]; then
        echo "$0 is setting QT_IM_MODULES for $im_name."
        export QT_IM_MODULES="wayland;$im_name"
    fi
    # do not override xim settings
    if [ -z "$XMODIFIERS" ]; then
        echo "$0 is setting XMODIFIERS for $im_name."
        export XMODIFIERS="@im=$im_name"
    fi
fi
