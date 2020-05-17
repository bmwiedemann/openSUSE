#
# spec file for package patterns-lxqt
#
# Copyright (c) 2020 SUSE LLC
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
Version:        20170319
Release:        0
Summary:        Patterns for Installation (LXQt)
License:        MIT
Group:          Metapackages
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
Requires:       oxygen5-icon-theme
Requires:       pattern() = x11
Recommends:     pattern() = multimedia
# non core packages belonging to LXQt organization
Recommends:     pcmanfm-qt
Recommends:     lxqt-archiver
Recommends:     pavucontrol-qt
Recommends:     qterminal
Recommends:     obconf-qt
Recommends:     lximage-qt
Recommends:     featherpad

Suggests:       qps
Suggests:       qlipper

# Pulseaudio is the default sound server
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-gconf
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils

# 
Recommends:     openbox
Recommends:     obconf
Recommends:     qupzilla
Recommends:     xdg-utils
Recommends:     xdg-user-dirs
Recommends:     xscreensaver
Recommends:     xorg-x11-essentials
Recommends:     lightdm
# misc
Recommends:     ark
Recommends:     claws-mail

Recommends:     pk-update-icon
Recommends:     apper

Recommends:     avahi
Recommends:     kdesu
Recommends:     system-config-printer
Recommends:     simple-scan
Recommends:     libyui-qt-pkg
Recommends:     yast2-control-center-qt
Recommends:     NetworkManager
# at some point nm-tray might be better
Recommends:     NetworkManager-applet
Recommends:     google-droid-fonts
Recommends:     desktop-data-openSUSE
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
