#
# spec file for package patterns-lxde
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_with betatest

Name:           patterns-lxde
Version:        20170319
Release:        0
Summary:        Patterns for Installation (lxde)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the lxde desktop patterns.

################################################################################

%package lxde
%pattern_graphicalenvironments
Summary:        LXDE Desktop Environment
Group:          Metapackages
Provides:       pattern() = lxde
Provides:       pattern-icon() = pattern-lxde
Provides:       pattern-order() = 1410
Provides:       pattern-visible()
Requires:       pattern() = x11
Recommends:     pattern() = lxde_office
Recommends:     pattern() = multimedia

# Move to lightdm instead of lxdm - the latter still depends on ConsoleKit
# See mail thread: https://lists.opensuse.org/opensuse-factory/2016-07/msg00417.html
Recommends:     lightdm
Recommends:     lxappearance
Recommends:     lxde-common
Recommends:     lxde-common-branding-openSUSE
Recommends:     lxinput
Recommends:     lxmenu-data
Recommends:     lxmusic
Recommends:     lxpanel
Recommends:     lxrandr
Recommends:     lxsession
Recommends:     lxtask
Recommends:     lxterminal
Recommends:     lxcc
Recommends:     menu-cache
Recommends:     nuoveXT2-icon-theme
Recommends:     openbox
Recommends:     obconf
Recommends:     pcmanfm
Recommends:     viewnior
Recommends:     leafpad
Recommends:     geany
Recommends:     xarchiver
Recommends:     galculator
Recommends:     gmixer
Recommends:     parcellite
Recommends:     xscreensaver
Recommends:     pidgin
Recommends:     hexchat
Recommends:     claws-mail
Recommends:     uget
Recommends:     xdg-user-dirs-gtk
Recommends:     xfce4-power-manager
Recommends:     xfce4-screenshooter
Recommends:     gconf2-branding-openSUSE
#xfburn, community asks for brasero
Recommends:     brasero
Recommends:     mtpaint
Recommends:     gcolor2
Recommends:     cheese
# #540627
Recommends:     xdg-utils
# #393956 + 450220 + 481468(xdm)
Recommends:     xorg-x11-essentials
Recommends:     xdm
# bnc#537362
Recommends:     gnome-packagekit
Recommends:     pk-update-icon
# #404447
Recommends:     gtk2-engine-murrine
# #440285
Recommends:     pinentry-gtk2
Recommends:     avahi
# #537365
# use gnomesu as su wrapper
Recommends:     libgnomesu
# we need a GPG GUI
Recommends:     seahorse
# We need a printer configuration util
Recommends:     system-config-printer
# And scanner one
Recommends:     simple-scan
# Video player and codecs
# do we need an LXDE_MULTIMEDIA pattern??
Recommends:     totem
Recommends:     totem-browser-plugin
# Use Qt UI for YaST
Recommends:     libyui-qt-pkg
Recommends:     yast2-control-center-qt
# Use NM by default
Recommends:     NetworkManager
Recommends:     NetworkManager-applet
Recommends:     desktop-branding
Suggests:       lxlauncher

# from data/COMMON-DESKTOP
Recommends:     google-droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
Recommends:     avahi
# bnc#508120
Recommends:     xdg-user-dirs

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip

%description lxde
LXDE is a lightweight X11 desktop environment similiar to XFCE in its nature.

%files lxde
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/lxde.txt

################################################################################

%package lxde_laptop
%pattern_lxdedesktop
Summary:        LXDE Laptop
Group:          Metapackages
Provides:       pattern() = lxde_laptop
Provides:       pattern-extends() = laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 5160
Supplements:    packageand(patterns-lxde-lxde:patterns-desktop-laptop)
Requires:       pattern() = lxde

Recommends:     gnome-bluetooth

%description lxde_laptop
LXDE Tools designed specifically for use with laptop computers.

%files lxde_laptop
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/lxde_laptop.txt

################################################################################

%package lxde_office
%pattern_graphicalenvironments
Summary:        LXDE Office
Group:          Metapackages
Provides:       pattern() = lxde_office
Provides:       pattern-extends() = office
Provides:       pattern-icon() = pattern-lxde
Provides:       pattern-order() = 1880
Supplements:    packageand(patterns-lxde-lxde:patterns-office-office)
Requires:       pattern() = lxde

Recommends:     abiword
Recommends:     atril
Recommends:     gnumeric
Recommends:     goffice

%description lxde_office
LXDE Office

%files lxde_office
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/lxde_office.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns
for i in lxde lxde_laptop lxde_office; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog
