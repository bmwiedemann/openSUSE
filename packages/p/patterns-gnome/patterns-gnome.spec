#
# spec file for package patterns-gnome
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


%bcond_with betatest
Name:           patterns-gnome
Version:        20201210
Release:        0
Summary:        Patterns for Installation (Gnome)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains all the Gnome patterns.

%if 0%{?is_opensuse}
%package devel_gnome
%pattern_development
Summary:        GNOME Development
Group:          Metapackages
Provides:       patterns-openSUSE-devel_gnome = %{version}
Provides:       pattern() = devel_gnome
Provides:       pattern-icon() = pattern-gnome-devel
Provides:       pattern-order() = 3160
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-devel_gnome < %{version}
Requires:       pattern() = devel_C_C++
Requires:       pattern() = gnome_basis
Recommends:     cairo-devel
Recommends:     clutter-devel
Recommends:     clutter-gst-devel
Recommends:     clutter-gtk-devel
Recommends:     evolution-data-server-devel
Recommends:     gdk-pixbuf-devel
Recommends:     glib2-devel
# Build tools
Recommends:     gnome-common
Recommends:     gnome-online-accounts-devel
Recommends:     gobject-introspection-devel
Recommends:     gtk-doc
Recommends:     gtk3-devel
Recommends:     gtksourceview-devel
Recommends:     intltool
Recommends:     itstool
Recommends:     json-glib-devel
Recommends:     libcanberra-devel
Recommends:     libgdata-devel
Recommends:     libgnome-desktop-3-devel
Recommends:     libgnome-keyring-devel
Recommends:     libgsf-devel
Recommends:     libgtop-devel
Recommends:     libgweather-devel
Recommends:     libnotify-devel
Recommends:     librsvg-devel
Recommends:     libsoup-devel
Recommends:     libwebkitgtk-devel
Recommends:     libwnck-devel
Recommends:     pango-devel
Recommends:     tracker-devel
Recommends:     vala
Recommends:     vte-devel
Recommends:     yelp-tools

%description devel_gnome
GNOME development packages.

%files devel_gnome
%dir %{_docdir}/patterns
%{_docdir}/patterns/devel_gnome.txt
%endif

%package gnome_x11
%pattern_graphicalenvironments
Summary:        GNOME Desktop Environment (X11)
Group:          Metapackages
Provides:       pattern() = gnome_x11
Provides:       pattern-icon() = pattern-gnome-xorg
Provides:       pattern-order() = 1020
Provides:       pattern-visible()
# bsc#1065166
Requires:       pattern() = gnome_basic
%if 0%{?is_opensuse}
Recommends:     pattern() = games
Recommends:     pattern() = gnome_internet
Recommends:     pattern() = gnome_utilities
Recommends:     pattern() = imaging
Recommends:     pattern() = multimedia
%endif
# These were not in the tumbleweed pattern
Requires:       gnome-packagekit
# #545263
Requires:       seahorse
Requires:       totem
Requires:       xdg-user-dirs-gtk
Recommends:     pattern() = gnome_imaging
Recommends:     pattern() = office
Recommends:     pattern() = x11_yast
#
# Official upstream
#
# no longer need to hard require cheese for g-c-c user panel
Recommends:     cheese
Recommends:     dconf-editor
Recommends:     evince
Recommends:     evolution
Recommends:     evolution-ews
Recommends:     gnome-bluetooth
# bsc#1069699
Recommends:     gnome-characters
Recommends:     gnome-clocks
# bsc#1069699
Recommends:     gnome-contacts
Recommends:     gnome-control-center-color
Recommends:     gnome-control-center-goa
Recommends:     gnome-desktop
# #554954
Recommends:     gnome-disk-utility
Recommends:     gnome-documents
Recommends:     gnome-menus
Recommends:     gnome-remote-desktop
Recommends:     gpgme
# #399801
Recommends:     mousetweaks
Recommends:     nautilus-sendto
Recommends:     noto-sans-cjk-fonts
Recommends:     orca
# bsc#1065191
Recommends:     pidgin
Recommends:     planner
Recommends:     python3-speechd
Recommends:     speech-dispatcher
Recommends:     speech-dispatcher-module-espeak
# #608156
Recommends:     tracker
Recommends:     tracker-miner-files
Recommends:     zenity
Suggests:       pattern() = documentation
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-gnome = %{version}
Obsoletes:      patterns-openSUSE-gnome < %{version}
%else
Provides:       patterns-sled-Default
Obsoletes:      patterns-sled-Default < %{version}
%endif
%if 0%{?is_opensuse}
Recommends:     vinagre
%else
Recommends:     remmina
%endif
%if !0%{?is_opensuse}
Recommends:     gnome-initial-setup
%endif
%if !0%{?is_opensuse}
# bsc#1075136
Recommends:     gutenprint
%endif
#
# #447627
%if !0%{?is_opensuse}
# bsc#1087222
Recommends:     gnome-user-share
%else
Requires:       gnome-user-share
%endif
%if 0%{?is_opensuse}
#
# Official upstream
#
# #544192
Recommends:     baobab
Recommends:     bijiben
Recommends:     file-roller
Recommends:     gcr-viewer
Recommends:     gedit
Recommends:     gnome-characters
Recommends:     gnome-contacts
Recommends:     gnome-dictionary
Recommends:     gnome-documents
Recommends:     gnome-logs
Recommends:     gnome-maps
Recommends:     gnome-screenshot
Recommends:     gnome-system-monitor
#
# While running a GNOME3 session, it's nice to have the GNOME3 related pinentry
# for proper gpg2 integration
#
Recommends:     pinentry-gnome3
Recommends:     sushi
#
# Packages that really make sense
#
# Tool for advanced configuration of printers
Recommends:     system-config-printer
Recommends:     totem-browser-plugin
Recommends:     tracker-miner-evolution
# #302492
Suggests:       brasero
# bnc#698250
Suggests:       gnome-color-manager
%else
Recommends:     NetworkManager-openconnect-gnome
# bsc#1065148
Recommends:     NetworkManager-openvpn-gnome
Recommends:     NetworkManager-pptp-gnome
Recommends:     desktop-data-SLE-extra
%endif
Recommends:     malcontent-control

%description gnome_x11
The GNOME desktop environment is an intuitive and attractive desktop for users.
This pattern installs a full featured GNOME desktop environment, including
Office suite, E-Mail client, Web Browser, File Manager, running with X11
technology.

%files gnome_x11
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_x11.txt

################################################################################

%package gnome
%pattern_graphicalenvironments
Summary:        GNOME Desktop Environment (Wayland)
Group:          Metapackages
Provides:       pattern() = gnome
Provides:       pattern-icon() = pattern-gnome-wayland
Provides:       pattern-order() = 1010
Provides:       pattern-visible()
Requires:       pattern() = gnome_x11
Recommends:     gnome-session-wayland

%description gnome
The GNOME desktop environment is an intuitive and attractive desktop for users.
This pattern installs components for GNOME to run with Wayland and X11 technologies.

%files gnome
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome.txt

################################################################################

%package gnome_basis
%pattern_graphicalenvironments
Summary:        GNOME Base System
Group:          Metapackages
Provides:       pattern() = gnome_basis
Provides:       pattern-icon() = pattern-gnome
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-gnome_basis = %{version}
Obsoletes:      patterns-openSUSE-gnome_basis < %{version}
Recommends:     pattern() = gnome_basis_opt
%endif
Requires:       gdm
Requires:       gnome-session
Requires:       pattern() = x11
# from data/COMMON-DESKTOP
Recommends:     desktop-data
Recommends:     desktop-file-utils
#
# Now the real packages
#
# #332596
Recommends:     gnome-keyring-pam
# implied by gnome-keyring-pam
#Recommends:     gnome-keyring
Recommends:     gnome-power-manager
# implied by gdm
#Requires: gnome-shell
#Requires: gnome-settings-daemon
# implied by gnome-shell
#Requires:       gnome-control-center
#
# Default sessions
# - Put in Recommends for now, to make sure the livecd will always build; but
#   ideally, should be in Requires
# - We also we explicitly put the packages required by those sessions, in case
#   gnome-session-*-session is not installable, to make sure the livecd is
#   somehow a bit usable
#
Recommends:     gnome-session-default-session
# boo#1090117
Recommends:     gnome-shell-classic
Recommends:     gnome-extensions
Recommends:     gnome-terminal
# bnc#879466
Recommends:     gnome-user-docs
Recommends:     gpgme
# we need something for xdg-su
Recommends:     libgnomesu
Recommends:     nautilus
Recommends:     polkit-default-privs
# Pulseaudio is the default sound server
Recommends:     pulseaudio-module-gsettings
Recommends:     pulseaudio-module-x11
Recommends:     samba
# #509829
Recommends:     xdg-user-dirs-gtk
Recommends:     yelp
#
# Low-level parts that we need
#
%if 0%{is_opensuse}
# bnc#430161
Recommends:     NetworkManager
%endif
%if 0%{is_opensuse}
Recommends:     canberra-gtk-play
%endif
%if 0%{is_opensuse}
Recommends:     MozillaFirefox
Recommends:     avahi
#
# Branding
#
# #591535
Recommends:     gdm-branding-openSUSE
Recommends:     gio-branding-openSUSE
Recommends:     gnome-control-center-branding-openSUSE
Recommends:     gnome-panel-branding-openSUSE
Recommends:     gtk2-branding-openSUSE
Recommends:     gtk3-branding-openSUSE
Recommends:     hicolor-icon-theme-branding-openSUSE
Recommends:     libsocialweb-branding-openSUSE
%endif

%description gnome_basis
Base packages for the GNOME desktop environment.

%files gnome_basis
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_basis.txt

################################################################################
%package gnome_basic
%pattern_graphicalenvironments
Summary:        GNOME Desktop Environment (Basic)
Group:          Metapackages
Provides:       pattern() = gnome_basic
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 1000
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Requires:       pattern() = x11
%else
Requires:       pattern() = x11_enhanced
%endif
Requires:       gsettings-backend-dconf
Requires:       pattern() = basesystem
Requires:       pattern() = gnome_basis
# bsc#1065945
Recommends:     brasero
Recommends:     evince
# bsc#1069699
Recommends:     file-roller
# bsc#1065146
Recommends:     gedit
# implified by gnome-keyring-pam
# Recommends:     gnome-keyring
# bsc#1063156
Recommends:     gnome-calculator
Recommends:     gnome-software
Recommends:     gnome-system-monitor
# bnc#859494 bsc#1065790
Recommends:     gnome-tweak-tool
Recommends:     nautilus-extension-terminal
Recommends:     nautilus-share
Recommends:     pinentry-gnome3
# bsc#1164858 bsc#1081584
# - only in Leap and SLE as we don't want to install gnome-packagekit by
#   default on TW
%if 0%{?sle_version}
Recommends:     gnome-packagekit
%endif
%if !0%{?is_opensuse}
Obsoletes:      patterns-sles-gnome-basic
%endif

%description gnome_basic
The GNOME desktop environment is an intuitive and attractive desktop for users.
This pattern installs GNOME desktop environment with only essential graphical
applications installed (File Manager, Web Browser).

%files gnome_basic
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_basic.txt

################################################################################

%if 0%{?is_opensuse}
%package gnome_basis_opt
%pattern_graphicalenvironments
Summary:        GNOME Base System
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_basis_opt = %{version}
Provides:       pattern() = gnome_basis_opt
Provides:       pattern-extends() = gnome_basis
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 1420
Obsoletes:      patterns-openSUSE-gnome_basis_opt < %{version}
Requires:       pattern() = x11
# #394406
Recommends:     dynamic-wallpaper-branding-openSUSE
# MAYBE later lsb-graphics
# give net shares
Recommends:     samba

%description gnome_basis_opt
Base packages for the GNOME desktop environment.

%files gnome_basis_opt
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_basis_opt.txt
%endif

################################################################################

%if 0%{?is_opensuse}
%package gnome_games
%pattern_gnomedesktop
Summary:        GNOME Games
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_games = %{version}
Provides:       pattern() = gnome_games
Provides:       pattern-extends() = games
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2100
Obsoletes:      patterns-openSUSE-gnome_games < %{version}
Recommends:     gnome-chess
Recommends:     gnome-mahjongg
Recommends:     gnome-mines
Recommends:     gnome-sudoku
Recommends:     gnuchess
# from data/GNOME-Games
Recommends:     iagno
Recommends:     lightsoff
Recommends:     quadrapassel
Recommends:     swell-foop
Suggests:       gnome-games-extra-data
Suggests:       phalanx
Supplements:    packageand(patterns-gnome-gnome:patterns-games-games)

%description gnome_games
GNOME Games

%files gnome_games
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_games.txt
%endif

################################################################################

%if 0%{?is_opensuse}
%package gnome_ide
%pattern_gnomedesktop
Summary:        GNOME Integrated Development Environment
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_ide = %{version}
Provides:       pattern() = gnome_ide
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2060
Obsoletes:      patterns-openSUSE-gnome_ide < %{version}
# from data/GNOME-IDE
Recommends:     devhelp
Recommends:     gitg
Recommends:     glade
Recommends:     gnome-builder
# from devel_ide
Suggests:       accerciser
Suggests:       anjuta
Suggests:       anjuta-extras
Suggests:       gedit
Suggests:       gedit-plugins
Suggests:       ghex
Suggests:       giggle
Suggests:       gnome-devel-docs
Suggests:       jhbuild
Suggests:       meld
Suggests:       nemiver

%description gnome_ide
Development under GNOME

%files gnome_ide
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_ide.txt
%endif

################################################################################

%package gnome_imaging
%pattern_gnomedesktop
Summary:        GNOME Graphics
Group:          Metapackages
Provides:       pattern() = gnome_imaging
Provides:       pattern-extends() = imaging
Provides:       pattern-icon() = package_graphics
Provides:       pattern-order() = 2140
Requires:       pattern() = gnome_basis
# from data/GNOME-IMAGE
#
# Official upstream
#
Recommends:     eog
#
# Packages that really make sense
#
Recommends:     gnome-photos
Recommends:     simple-scan
Suggests:       gthumb
Supplements:    packageand(patterns-gnome-gnome:patterns-desktop-imaging)
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-gnome_imaging = %{version}
Obsoletes:      patterns-openSUSE-gnome_imaging < %{version}
%endif

%description gnome_imaging
Handling of digital photos and graphics

%files gnome_imaging
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_imaging.txt

################################################################################

%if 0%{?is_opensuse}
%package gnome_internet
%pattern_gnomedesktop
Summary:        GNOME Internet
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_internet = %{version}
Provides:       pattern() = gnome_internet
Provides:       pattern-extends() = gnome
Provides:       pattern-icon() = package_network
Provides:       pattern-order() = 2420
Obsoletes:      patterns-openSUSE-gnome_internet < %{version}
Recommends:     NetworkManager-openconnect-gnome
#
# Packages that really make sense
#
# bnc#533580
Recommends:     NetworkManager-openvpn-gnome
Recommends:     NetworkManager-pptp-gnome
Recommends:     NetworkManager-vpnc-gnome
Recommends:     evolution
# from data/GNOME-Internet
#
# Official upstream
#
Recommends:     pidgin
Recommends:     polari
# bnc#530416
Recommends:     transmission-gtk
#
# Official upstream
#
# bnc#366894
Suggests:       ekiga
Suggests:       epiphany
Suggests:       evolution-plugin-rss
#
# Packages that can make sense
#
Suggests:       frogr

%description gnome_internet
GNOME Internet Applications

%files gnome_internet
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_internet.txt
%endif

################################################################################

%package gnome_multimedia
%pattern_gnomedesktop
Summary:        GNOME Multimedia
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_multimedia = %{version}
Provides:       pattern() = gnome_multimedia
Provides:       pattern-extends() = multimedia
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2200
Obsoletes:      patterns-openSUSE-gnome_multimedia < %{version}
#
# Packages that really make sense
#
Recommends:     gnome-music
Recommends:     gstreamer-plugins-bad
#
# GStreamer magic
#
# software.openSUSE.org/codecs
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-libav
Recommends:     gstreamer-plugins-ugly
# bnc#445314
Recommends:     gstreamer-utils
#
# Official upstream
#
Recommends:     totem
#
# Packages that really make sense
#
Suggests:       paprefs
Suggests:       pavucontrol
Suggests:       pitivi
Supplements:    packageand(patterns-gnome-gnome:patterns-desktop-multimedia)

%description gnome_multimedia
GNOME Multimedia

%files gnome_multimedia
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_multimedia.txt

################################################################################

%if 0%{?is_opensuse}
%package gnome_office
%pattern_gnomedesktop
Summary:        GNOME Office
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_office = %{version}
Provides:       pattern() = gnome_office
Provides:       pattern-extends() = office
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2240
Obsoletes:      patterns-openSUSE-gnome_office < %{version}
Requires:       pattern() = gnome_basis
# from data/GNOME-Office
#
# Official upstream
#
Recommends:     evolution
#
# Packages that really make sense
#
Recommends:     libreoffice-gnome
Recommends:     libreoffice-icon-theme-tango
Suggests:       evolution-ews
Suggests:       glabels
Suggests:       planner
Supplements:    packageand(patterns-gnome-gnome:patterns-office-office)

%description gnome_office
GNOME Office

%files gnome_office
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_office.txt
%endif

################################################################################

%if 0%{?is_opensuse}
%package gnome_utilities
%pattern_gnomedesktop
Summary:        GNOME Utilities
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_utilities = %{version}
Provides:       pattern() = gnome_utilities
Provides:       pattern-extends() = gnome
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2280
Obsoletes:      patterns-openSUSE-gnome_utilities < %{version}
Requires:       pattern() = gnome_basis
#
# Official upstream
#
Recommends:     baobab
Recommends:     bijiben
Recommends:     cheese
Recommends:     file-roller
Recommends:     gdk-pixbuf-thumbnailer
Recommends:     gedit
Recommends:     gnome-calculator
Recommends:     gnome-characters
Recommends:     gnome-dictionary
Recommends:     gnome-screenshot
#
# Packages that really make sense
#
Recommends:     gnome-tweak-tool
Recommends:     gnome-weather
Recommends:     gsf-office-thumbnailer
Recommends:     nautilus-extension-seahorse
Recommends:     nautilus-sendto
Recommends:     rsvg-thumbnailer
Recommends:     seahorse
#
# Official upstream
#
Suggests:       dasher
Suggests:       eog-plugins
Suggests:       gedit-plugins
#
# Packages that can make sense
#
Suggests:       gtg
# #388570
Suggests:       nautilus-share

%description gnome_utilities
GNOME Utilities

%files gnome_utilities
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_utilities.txt
%endif

################################################################################

%if 0%{?is_opensuse}
%package gnome_yast
%pattern_basetechnologies
Summary:        YaST GNOME User Interfaces
Group:          Metapackages
Provides:       patterns-openSUSE-gnome_yast = %{version}
Provides:       pattern() = gnome_yast
Provides:       pattern-extends() = yast2_basis
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1260
Obsoletes:      patterns-openSUSE-gnome_yast < %{version}
Requires:       libyui-qt-pkg
Requires:       yast2-control-center-qt
Supplements:    packageand(patterns-gnome-gnome:patterns-yast-yast2_basis)

%description gnome_yast
Graphical YaST user interfaces for the GNOME desktop.

%files gnome_yast
%dir %{_docdir}/patterns
%{_docdir}/patterns/gnome_yast.txt
%endif

################################################################################

%if 0%{?is_opensuse}
%package sw_management_gnome
%pattern_basetechnologies
Summary:        Package Management - Graphical Tools for GNOME
Group:          Metapackages
Provides:       patterns-openSUSE-sw_management_gnome = %{version}
Provides:       pattern() = sw_management_gnome
Provides:       pattern-extends() = sw_management
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1780
Obsoletes:      patterns-openSUSE-sw_management_gnome < %{version}
Requires:       pattern() = sw_management
Requires:       pattern() = x11
Recommends:     gnome-packagekit
Recommends:     gnome-software
Supplements:    packageand(patterns-gnome-gnome_basis:patterns-base-sw_management)

%description sw_management_gnome
Package Management - Graphical Tools

%files sw_management_gnome
%dir %{_docdir}/patterns
%{_docdir}/patterns/sw_management_gnome.txt
%endif

%prep

%build

%install

mkdir -p "%{buildroot}%{_docdir}/patterns"
for i in gnome gnome_basis gnome_basic gnome_imaging gnome_x11 gnome_multimedia; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%if 0%{?is_opensuse}
for i in devel_gnome gnome_basis_opt \
    gnome_games gnome_ide gnome_internet \
    gnome_office \
    gnome_utilities gnome_yast sw_management_gnome; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}%{_docdir}/patterns/$i.txt"
done
%endif

%changelog
