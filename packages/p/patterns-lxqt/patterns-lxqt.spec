#
# spec file for package patterns-lxqt
#
# Copyright (c) 2024 SUSE LLC
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

Name:           patterns-lxqt
Version:        20240611
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

Requires:       breeze5-icons
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
# boo#1218288 -- mvetter@suse.com
Requires:       liblxqt
Requires:       oxygen5-icon-theme
# boo#1226151 -- sfalken@opensuse.org
Requires:       libfm-qt5
Requires:       lxqt-qt5plugin
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
Recommends:     openbox
Recommends:     firefox
Recommends:     sddm
Recommends:     xdg-user-dirs
Recommends:     xdg-utils
Recommends:     xorg-x11-essentials
Recommends:     xscreensaver
# misc
Recommends:     ark
Recommends:     claws-mail

Recommends:     apper
Recommends:     pk-update-icon

Recommends:     NetworkManager
Recommends:     avahi
Recommends:     kdesu
Recommends:     libyui-qt-pkg
Recommends:     simple-scan
Recommends:     system-config-printer
Recommends:     yast2-control-center-qt
# at some point nm-tray might be better
Recommends:     NetworkManager-applet
Recommends:     desktop-data-openSUSE
Recommends:     google-droid-fonts
Recommends:     samba
Suggests:       hplip

%description lxqt
LXQt is a lightweight desktop environment based on Qt.

%files lxqt
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/lxqt.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern lxqt to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/lxqt.txt

%changelog
