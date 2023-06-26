# This file is sourced by Xsession(5), not executed.

# to be sourced

# Copyright (C) 2014-2015, Martin Wimpress <code@flexion.org>
# Copyright (C) 2015, Mike Gabriel <mike.gabriel@das-netzwerkteam.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# .
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# .
# On Debian systems, the complete text of the GNU General Public
# License version 2 can be found in "/usr/share/common-licenses/GPL-2".

if [ "x$DESKTOP_SESSION" = "xmate" ] || [ "x$XDG_SESSION_DESKTOP" = "xmate" ]; then
    if [ -z "$GTK_MODULES" ] ; then
        GTK_MODULES="canberra-gtk-module"
    else
        GTK_MODULES="$GTK_MODULES:canberra-gtk-module"
    fi
    export GTK_MODULES

    # Disable GTK3 overlay scrollbars
    export GTK_OVERLAY_SCROLLING=0

    # Sadly this environment variable can cause applications to segfault.
    # For example:
    #  - Telegram doesn't work with QT_STYLE_OVERRIDE=gtk
    # export QT_STYLE_OVERRIDE=gtk

    # Workaround clutter issue (LP: #1462445, Debian #954783)
    export CLUTTER_BACKEND="x11,*"
fi

