#
# spec file for package patterns-cinnamon
#
# Copyright (c) 2021 SUSE LLC
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


Name:           patterns-cinnamon
Version:        202021205
Release:        0
Summary:        Patterns for Installation (Cinnamon)
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Cinnamon patterns.

################################################################################

%package cinnamon
%pattern_graphicalenvironments
Summary:        Cinnamon Desktop Environment
Group:          Metapackages
Provides:       pattern() = cinnamon
Provides:       pattern-icon() = pattern-cinnamon
Provides:       pattern-order() = 1350
Provides:       pattern-visible()

Requires:       pattern() = cinnamon_basis

Requires:       pattern() = x11
Recommends:     pattern() = x11_yast
Recommends:     pattern() = office

Provides:       patterns-openSUSE-cinnamon = %{version}
Obsoletes:      patterns-openSUSE-cinnamon < %{version}

#
# cinnamon Recommanded applications
#
# doc viewer, img viewer, video player, music player
Recommends:     xviewer
Recommends:     pix
Recommends:     celluloid
Recommends:     rhythmbox

# other utilities
Recommends:     gnome-screenshot
Recommends:     simple-scan
Recommends:     gnote
Recommends:     baobab
Recommends:     hexchat
Recommends:     seahorse
Recommends:     blueberry
Recommends:     colord
Recommends:     gucharmap
Recommends:     gnome-calendar
Recommends:     gnome-calculator
Recommends:     gnome-disk-utility
Recommends:     gnome-font-viewer
Recommends:     hypnotix

# Replaced by blueberry
# Recommends:     gnome-bluetooth

# Missing on openSUSE
# Recommends:     drawing

%description cinnamon
Cinnamon is a modern Linux desktop which provides advanced innovative
features and a traditional user experience. It's easy to use,
powerful and flexible.

%files cinnamon
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/cinnamon.txt

################################################################################

%package cinnamon_basis
%pattern_graphicalenvironments
Summary:        Cinnamon Base System
Group:          Metapackages
Provides:       pattern() = cinnamon_basis
Provides:       pattern-extends() = cinnamon
Provides:       pattern-icon() = pattern-cinnamon
Provides:       pattern-order() = 1350
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Provides:       patterns-openSUSE-cinnamon_basis = %{version}
Obsoletes:      patterns-openSUSE-cinnamon_basis < %{version}

#
# Core functionality packages 
#
Requires:       cinnamon
Requires:       cinnamon-control-center
Requires:       cinnamon-screensaver
Requires:       cinnamon-session
Requires:       cinnamon-settings-daemon
Requires:       cjs

#
# Display manager with cinnamon customization
#
Recommends:     lightdm
Recommends:     lightdm-slick-greeter

#
# Themes
#
Recommends:     mint-x-icon-theme
Recommends:     mint-y-icon-theme

#
# Bare minimum cinnamon applications, like terminal, text editor, file managers, doc reader....
#
Recommends:     gnome-terminal
Recommends:     xed
Recommends:     nemo
Recommends:     xreader

Recommends:     file-roller
Recommends:     gnome-system-monitor
Recommends:     MozillaFirefox

# Default Nemo Extensions on Linux Mint
Recommends:     nemo-preview
Recommends:     nemo-fileroller

#
# Some low level functionalities
#
Recommends:     xdg-user-dirs-gtk
Recommends:     polkit-default-privs
Recommends:     avahi
Recommends:     yelp
Recommends:     desktop-data-openSUSE
Recommends:     gnome-online-accounts
Recommends:     gnome-keyring
Recommends:     gnome-keyring-pam
Recommends:     shared-mime-info

# yast
Recommends:     libyui-qt-pkg
Recommends:     yast2-control-center-qt

# cinnamon have special support for qt applications
Recommends:     qt5ct

#
# Brandings
#
Suggests:       wallpaper-branding-openSUSE
Suggests:       lightdm-slick-greeter-branding-openSUSE
Suggests:       gio-branding-openSUSE

# `desktop-branding` will Suggest: cinnamon-branding-openSUSE
# also openSUSE's branding may need some rework (which is back to the days of openSUSE 4x.x)
Suggests:       desktop-branding

%description cinnamon_basis
Base packages for the cinnamon Desktop Environment

%files cinnamon_basis
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/cinnamon_basis.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/

for i in cinnamon cinnamon_basis; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog
