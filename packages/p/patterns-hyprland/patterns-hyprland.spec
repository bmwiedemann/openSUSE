#
# spec file for package patterns-hyprland
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        20261031
Release:        0
Summary:        Patterns for Installation (Hyprland)
License:        MIT
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
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
Provides:       pattern() = hyprland
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1815
Provides:       pattern-visible()
# SECTION base system
Requires:       pattern() = base
# /SECTION
# SECTION compositor and portals
Requires:       hyprland
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-hyprland
# /SECTION
# SECTION login
Recommends:     greetd-gtkgreet-hyprland
# /SECTION
# SECTION lock and idle
Recommends:     hypridle
Recommends:     hyprlock
# /SECTION
# SECTION authentication agent
Recommends:     hyprpolkitagent
# /SECTION
# SECTION bar
Recommends:     waybar
# /SECTION
# SECTION notifications
Recommends:     mako
# /SECTION
# SECTION launcher
Recommends:     rofi-wayland
# /SECTION
# SECTION screenshots
Recommends:     grim
Recommends:     slurp
# /SECTION
# SECTION color picker
Recommends:     hyprpicker
# /SECTION
# SECTION Hyprland-native wallpaper
Recommends:     hyprpaper
# /SECTION
# SECTION terminal
Recommends:     kitty
# /SECTION
# SECTION file manager
Recommends:     thunar
# /SECTION
# SECTION small helper utilities
Recommends:     hyprland-qtutils
Recommends:     wl-clipboard
# /SECTION
# openSUSE welcome
%if 0%{?is_opensuse}
# SECTION openSUSE welcome
Recommends:     opensuse-welcome-launcher
# /SECTION
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
Summary:        Hyprland Extra Components (plugins and extras)
Provides:       pattern() = hyprland_extra
Provides:       pattern-extends() = hyprland
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1816
Provides:       pattern-visible()
Requires:       pattern() = hyprland
# SECTION minimal dock
Recommends:     nwg-dock-hyprland
# /SECTION
# SECTION workflow tools
Recommends:     yazi
# /SECTION
# SECTION plugins
Recommends:     hyprland-plugin-borders-plus-plus
Recommends:     hyprland-plugin-csgo-vulkan-fix
Recommends:     hyprland-plugin-hyprbars
Recommends:     hyprland-plugin-hyprfocus
# /SECTION
# SECTION browser
Recommends:     MozillaFirefox
# /SECTION

%description hyprland_extra
Optional extras for the Hyprland Wayland compositor, including commonly used
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
