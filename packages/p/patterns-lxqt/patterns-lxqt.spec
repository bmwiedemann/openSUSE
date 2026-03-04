#
# spec file for package patterns-lxqt
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


%bcond_with betatest
%bcond_without wayland

Name:           patterns-lxqt
Version:        20260223
Release:        0
Summary:        Patterns for Installation (LXQt)
License:        MIT
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the LXQt patterns.






################################################################################

%package lxqt
%pattern_graphicalenvironments
Summary:        LXQt Desktop Environment
Group:          Metapackages
Provides:       pattern() = lxqt
Provides:       pattern-icon() = pattern-lxqt
Provides:       pattern-order() = 1460
Provides:       pattern-visible()

Requires:       kf6-breeze-icons
Requires:       lxqt-about
Requires:       lxqt-config
Requires:       lxqt-globalkeys
Requires:       lxqt-notificationd
Requires:       lxqt-openssh-askpass
Requires:       lxqt-panel
Requires:       lxqt-policykit
Requires:       lxqt-powermanagement
Requires:       lxqt-qtplugin
Requires:       lxqt-runner
Requires:       lxqt-session
Requires:       lxqt-sudo
Requires:       lxqt-themes
%if %{with_wayland}
Requires:       lxqt-wayland-session
Requires:       (lxqt-labwc-session or lxqt-wayfire-session or (lxqt-hyprland-session and hyprlock) or (lxqt-sway-session and swaylock) or (lxqt-river-session and waylock) or lxqt-niri-session)
Suggests:       kanshi
%endif
# boo#1218288 -- mvetter@suse.com
Requires:       liblxqt
Requires:       oxygen-icon-theme
# boo#1226151 -- sfalken@opensuse.org
Requires:       libfm-qt6
Requires:       lxqt-qtplugin
Requires:       pattern() = x11
Recommends:     xdg-desktop-portal-lxqt
Recommends:     pattern() = multimedia
# non core packages belonging to LXQt organization
Recommends:     picom-conf
Recommends:     featherpad
Recommends:     lximage-qt
Recommends:     lxqt-archiver
Recommends:     obconf-qt
Recommends:     pavucontrol-qt
Recommends:     pcmanfm-qt
Recommends:     picom
Recommends:     qterminal
Recommends:     screengrab

Suggests:       qps
Suggests:       qlipper

%if 0%{suse_version} > 1500
# Pipewire is the default sound server.
Recommends:     pipewire-pulseaudio
%else
# Pulseaudio is the default sound server
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-gconf
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
%endif
Recommends:     pulseaudio-utils

#
# Only needed on X11 session
Recommends:     openbox
Recommends:     xorg-x11-essentials
Recommends:     xscreensaver

Recommends:     firefox
Recommends:     sddm-conf
Recommends:     sddm-qt6
Recommends:     xdg-user-dirs
Recommends:     xdg-utils
# misc
Recommends:     ark
Recommends:     claws-mail

Recommends:     apper
Recommends:     pk-update-icon

Recommends:     NetworkManager
Recommends:     avahi
Recommends:     desktop-data-openSUSE
Recommends:     google-droid-fonts
Recommends:     kdesu
Recommends:     libyui-qt-pkg
Recommends:     nm-tray
Recommends:     samba
Recommends:     simple-scan
Recommends:     system-config-printer
Recommends:     yast2-control-center-qt
Suggests:       hplip

%description lxqt
LXQt is a lightweight desktop environment based on Qt.

%files lxqt
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/lxqt.txt

################################################################################
%package lxqt_wayland
%pattern_graphicalenvironments
Summary:        LXQt Desktop Environment
Group:          Metapackages
Provides:       pattern() = lxqt
Provides:       pattern() = lxqt_wayland
Provides:       pattern-icon() = pattern-lxqt
Provides:       pattern-order() = 1460
Provides:       pattern-visible()

Requires:       kf6-breeze-icons
Requires:       lxqt-about
Requires:       lxqt-config
Requires:       lxqt-globalkeys
Requires:       lxqt-notificationd
Requires:       lxqt-openssh-askpass
Requires:       lxqt-panel
Requires:       lxqt-policykit
Requires:       lxqt-powermanagement
Requires:       lxqt-qtplugin
Requires:       lxqt-runner
Requires:       lxqt-session
Requires:       lxqt-sudo
Requires:       lxqt-themes
Requires:       lxqt-wayland-session
Requires:       (lxqt-labwc-session or lxqt-wayfire-session or (lxqt-hyprland-session and hyprlock) or (lxqt-sway-session and swaylock) or (lxqt-river-session and waylock) or lxqt-niri-session)
Suggests:       kanshi
# boo#1218288 -- mvetter@suse.com
Requires:       liblxqt
Requires:       oxygen-icon-theme
# boo#1226151 -- sfalken@opensuse.org
Requires:       libfm-qt6
Requires:       lxqt-qtplugin
Recommends:     xdg-desktop-portal-lxqt
Recommends:     pattern() = multimedia
# non core packages belonging to LXQt organization
Recommends:     featherpad
Recommends:     lximage-qt
Recommends:     lxqt-archiver
Recommends:     pavucontrol-qt
Recommends:     pcmanfm-qt
Recommends:     qterminal
Recommends:     screengrab

Suggests:       qps
Suggests:       qlipper

%if 0%{suse_version} > 1500
# Pipewire is the default sound server.
Recommends:     pipewire-pulseaudio
%else
# Pulseaudio is the default sound server
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-gconf
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-zeroconf
%endif
Recommends:     pulseaudio-utils

Recommends:     firefox
Recommends:     sddm-conf
Recommends:     sddm-qt6
Recommends:     xdg-user-dirs
Recommends:     xdg-utils
# misc
Recommends:     ark
Recommends:     claws-mail

Recommends:     apper
Recommends:     pk-update-icon

Recommends:     NetworkManager
Recommends:     avahi
Recommends:     desktop-data-openSUSE
Recommends:     google-droid-fonts
Recommends:     kdesu
Recommends:     libyui-qt-pkg
Recommends:     nm-tray
Recommends:     samba
Recommends:     simple-scan
Recommends:     system-config-printer
Suggests:       hplip

Recommends:     opensuse-welcome-launcher
# Myrlyn replaces YaST2 Software / Y2PKG
Recommends:     myrlyn
# TODO: add plasma-tour or our current fallback opensuse-welcome (gtk4/rust)
# we will also need to define what to execute for lxqt in opensuse-welcome-launcher bash script

%description lxqt_wayland
A complete LXQt desktop environment for Wayland

%files lxqt_wayland
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/lxqt_wayland.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern lxqt to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/lxqt.txt
echo 'This file marks the pattern lxqt to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/lxqt_wayland.txt

%changelog
