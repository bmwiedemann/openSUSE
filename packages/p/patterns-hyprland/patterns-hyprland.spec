#
# spec file for package patterns-hyprland
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

#
# spec file for package patterns-hyprland
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           patterns-hyprland
Version:        20260129
Release:        0
Summary:        Patterns for Installation (Hyprland)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
BuildRequires:  patterns-rpm-macros
BuildArch:      noarch

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

This particular package contains the Hyprland pattern.

%package hyprland
%pattern_graphicalenvironments
Summary:        Hyprland (Wayland compositor)
Group:          Metapackages
Provides:       pattern() = hyprland
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1815
Provides:       pattern-visible()

# Base system
Requires:       pattern() = base

# Core compositor and portal stack
Requires:       hyprland
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-hyprland

# Login/session
Recommends:     greetd-gtkgreet-hyprland

# Bar
Recommends:     swaybar

# Notifications
Recommends:     mako

# Launcher
Recommends:     rofi-wayland

# Screenshots
Recommends:     grim
Recommends:     slurp

# Color picker
Recommends:     hyprpicker

# Wallpapers (Hyprland-native)
Recommends:     hyprpaper

# Terminal
Recommends:     kitty

# File manager
Recommends:     thunar

# Small helper utilities
Recommends:     hyprland-qtutils

# openSUSE welcome + branding glue
%if 0%{?is_opensuse}
Recommends:     opensuse-welcome-launcher
Recommends:     hyprland-branding-openSUSE
%endif

%description hyprland
Hyprland is a dynamic tiling Wayland compositor.

This pattern installs a minimal Hyprland session with common essentials:
a bar, notifications, launcher, screenshot tools, wallpaper daemon, and a file
manager.

%files hyprland
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/hyprland.txt

%package hyprland_extra
%pattern_graphicalenvironments
Summary:        Hyprland Extra Components (plugins and add-ons)
Group:          Metapackages
Provides:       pattern() = hyprland_extra
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1816
Provides:       pattern-visible()
Provides:       pattern-extends() = hyprland
Supplements:    (patterns-hyprland-hyprland and patterns-hyprland-hyprland_extra)

Requires:       pattern() = hyprland

# A minimal dock
Recommends:     nwg-dock-hyprland

# Optional workflow tools
Recommends:     waybar
Recommends:     yazi

# Hyprland plugins
Recommends:     hyprland-plugin-borders-plus-plus
Recommends:     hyprland-plugin-hyprbars
Recommends:     hyprland-plugin-csgo-vulkan-fix
Recommends:     hyprland-plugin-hyprexpo
Recommends:     hyprland-plugin-hyprfocus
Recommends:     hyprland-plugin-hyprscrolling
Recommends:     hyprland-plugin-hyprtrails
Recommends:     hyprland-plugin-hyprwinwrap
Recommends:     hyprland-plugin-xtra-dispatchers

# We need a browser
Recommends: 	MozillaFirefox

%description hyprland_extra
Optional add-ons for the Hyprland Wayland compositor, including commonly used
plugins and additional workflow tools.

%files hyprland_extra
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/hyprland_extra.txt

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns

for i in hyprland hyprland_extra; do
    echo "This file marks the pattern $i to be installed." \
        >"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog

