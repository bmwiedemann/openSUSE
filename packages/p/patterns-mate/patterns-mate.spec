#
# spec file for package patterns-mate
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           patterns-mate
Version:        20170319
Release:        0
Summary:        Patterns for Installation (MATE)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

This particular package contains the MATE Desktop patterns.

%package mate
%pattern_graphicalenvironments
Summary:        MATE Desktop Environment
Group:          Metapackages
Provides:       pattern() = mate
Provides:       pattern-icon() = pattern-mate
Provides:       pattern-order() = 1610
Provides:       pattern-visible()
Requires:       pattern() = mate_basis
Recommends:     pattern() = games
Recommends:     pattern() = imaging
Recommends:     pattern() = mate_admin
Recommends:     pattern() = mate_internet
Recommends:     pattern() = mate_utilities
Recommends:     pattern() = multimedia
Recommends:     pattern() = office
#
# Official upstream.
# As MATE is the continuation of GNOME 2.x, patterns are based on GNOME ones
# and some GNOME's are required.
#
Recommends:     atril
Recommends:     blueman
Recommends:     caja-sendto
Recommends:     caribou
Recommends:     cheese
Recommends:     engrampa
Recommends:     eom
Recommends:     galculator
Recommends:     gcr-viewer
# Support of gnome-contacts will be added in MATE 1.12
#Recommends:     gnome-contacts
Recommends:     gnome-font-viewer
Recommends:     MozillaThunderbird
Recommends:     gnome-nettool
Recommends:     gparted
Recommends:     gucharmap
Recommends:     mate-dictionary
Recommends:     mate-disk-usage-analyzer
Recommends:     mate-screenshot
Recommends:     mate-system-log
Recommends:     mate-system-monitor
Recommends:     mate-tweak
Recommends:     mate-user-share
Recommends:     mousetweaks
Recommends:     mozo
Recommends:     orca
Recommends:     pidgin
Recommends:     pluma
Recommends:     seahorse
Recommends:     totem
Recommends:     totem-browser-plugin
Recommends:     zenity
#
# Packages that in fact make sense.
#
Recommends:     deja-dup
# Tool for advanced configuration of printers
Recommends:     system-config-printer-applet
Recommends:     system-config-printer
# Tracker is not well integrated for instance with Mate apps
Recommends:     mate-search-tool
#Recommends:     tracker
#Recommends:     tracker-gui
#Recommends:     tracker-miner-evolution
Suggests:       dasher
Suggests:       dconf-editor
Suggests:       mate-backgrounds

%description mate
The MATE desktop environment is a desktop environment using traditional metaphors.

%files mate
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate.txt

%package mate_admin
%pattern_matedesktop
Summary:        MATE Administration Tools
Group:          Metapackages
Provides:       pattern() = mate_admin
Provides:       pattern-extends() = mate
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2050
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     mozo
Recommends:     vinagre

%description mate_admin
Administration Tools e.g. for desktop lockdown.

%files mate_admin
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_admin.txt

%package mate_basis
%pattern_graphicalenvironments
Summary:        MATE Base System
Group:          Metapackages
Provides:       pattern() = mate_basis
Provides:       pattern-icon() = pattern-mate
Provides:       pattern-order() = 1600
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = gnome_basis_opt
Requires:       caja
Requires:       lightdm
Requires:       marco
Requires:       mate-control-center
Requires:       mate-desktop
Requires:       mate-panel
Requires:       mate-session-manager
Requires:       mate-settings-daemon
Requires:       xdg-desktop-portal-gtk
Requires:       dbus(org.freedesktop.Notifications)
#
# Low-level parts that we need
#
Recommends:     NetworkManager
Recommends:     desktop-file-utils
# We want useful bug reports.
Recommends:     gdb
Recommends:     gpg2
Recommends:     gpgme
Recommends:     polkit-default-privs
Recommends:     samba
Recommends:     susehelp
#
# Branding
#
Recommends:     mate-control-center-branding-openSUSE
Recommends:     desktop-branding
Recommends:     hicolor-icon-theme-branding-openSUSE
Recommends:     libsocialweb-branding-openSUSE
Recommends:     mate-menus-branding-openSUSE
Recommends:     mate-panel-branding-openSUSE
Recommends:     mate-session-manager-branding-openSUSE
#
# Now the real packages
#
Recommends:     gnome-keyring-pam
Recommends:     at-spi2-core
Recommends:     canberra-gtk-play
Recommends:     gnome-keyring
Recommends:     mate-applets
Recommends:     mate-icon-theme
Recommends:     mate-icon-theme-faenza
Recommends:     mate-media
Recommends:     mate-menu
Recommends:     mate-menus
Recommends:     mate-notification-daemon
Recommends:     mate-themes
# boo#905679
Recommends:     mate-polkit
Recommends:     NetworkManager-applet
Recommends:     mate-power-manager
Recommends:     mate-screensaver
Recommends:     mate-terminal
Recommends:     shared-mime-info
Recommends:     tango-icon-theme
Recommends:     xkeyboard-config
Recommends:     yelp

%if 0%{suse_version} > 1500
# Pipewire is the default sound server.
Recommends:     pipewire-pulseaudio
%else
# PulseAudio is the default sound server.
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
%endif
Recommends:     pulseaudio-utils
Recommends:     xdg-user-dirs-gtk
# We need something for xdg-su.
Recommends:     libgnomesu
Recommends:     MozillaFirefox
Recommends:     avahi
Recommends:     desktop-data-openSUSE
Recommends:     google-droid-fonts
Recommends:     xdg-user-dirs
# metalink downloader
Suggests:       aria2

%description mate_basis
Base packages for the MATE desktop environment.

%files mate_basis
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_basis.txt

%package mate_internet
%pattern_matedesktop
Summary:        MATE Internet
Group:          Metapackages
Provides:       pattern() = mate_internet
Provides:       pattern-extends() = mate
Provides:       pattern-icon() = package_network
Provides:       pattern-order() = 2421
Recommends:     MozillaThunderbird
Recommends:     pidgin
#
# Packages that really make sense.
#
Recommends:     liferea
# As NetworkManager works well on MATE, we should recommend the same packages
Recommends:     NetworkManager-openvpn-gnome
Recommends:     NetworkManager-openconnect-gnome
Recommends:     NetworkManager-pptp-gnome
Recommends:     NetworkManager-vpnc-gnome
# boo#530416
Recommends:     hexchat
Recommends:     transmission-gtk
Suggests:       linphone
#
# Packages that can make sense.
#
Suggests:       gftp
Suggests:       pan
Suggests:       smuxi

%description mate_internet
MATE Internet Applications.

%files mate_internet
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_internet.txt

%package mate_laptop
%pattern_matedesktop
Summary:        MATE Laptop
Group:          Metapackages
Provides:       pattern() = mate_laptop
Provides:       pattern-extends() = laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2260
Supplements:    packageand(patterns-mate:patterns-laptop)
Requires:       pattern() = mate
Recommends:     blueman
Recommends:     xournal
Suggests:       mate-netbook

%description mate_laptop
MATE Tools designed specifically for use with laptop computers.

%files mate_laptop
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_laptop.txt

%package mate_office
%pattern_graphicalenvironments
Summary:        MATE Office
Group:          Metapackages
Provides:       pattern() = mate_office
Provides:       pattern-extends() = office
Provides:       pattern-icon() = pattern-mate
Provides:       pattern-order() = 2260
Supplements:    packageand(patterns-mate:patterns-office)
Requires:       pattern() = mate_basis
# We provide the same base environment; recommend gnome' one
Recommends:     pattern() = mate_office_opt
Recommends:     libreoffice-gnome
Recommends:     libreoffice-icon-theme-tango
Suggests:       abiword
Suggests:       mupdf
Suggests:       gnumeric
Suggests:       goffice

%description mate_office
MATE Office

%files mate_office
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_office.txt

%package mate_office_opt
%pattern_matedesktop
Summary:        MATE Office
Group:          Metapackages
Provides:       pattern() = mate_office_opt
Provides:       pattern-extends() = office
Provides:       pattern-icon() = pattern-mate
Provides:       pattern-order() = 2261
Supplements:    packageand(patterns-mate:patterns-office)
Requires:       pattern() = mate_basis
Suggests:       grisbi

%description mate_office_opt
MATE Office

%files mate_office_opt
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_office_opt.txt

%package mate_utilities
%pattern_matedesktop
Summary:        MATE Utilities
Group:          Metapackages
Provides:       pattern() = mate_utilities
Provides:       pattern-extends() = mate
Provides:       pattern-icon() = pattern-mate
Provides:       pattern-order() = 2300
Requires:       pattern() = mate_basis
#
# Official upstream
#
Recommends:     mate-disk-usage-analyzer
Recommends:     caja-extension-sendto
Recommends:     cheese
Recommends:     engrampa
Recommends:     galculator
Recommends:     gnome-font-viewer
Recommends:     gucharmap
Recommends:     mate-dictionary
Recommends:     mate-screenshot
Recommends:     pluma
Recommends:     seahorse
#
# Packages that can make sense.
#
Suggests:       conduit
Suggests:       deja-dup
Suggests:       gtg
Suggests:       kerneloops-applet
Suggests:       caja-extension-image-converter
Suggests:       caja-extension-open-terminal
Suggests:       caja-extension-share
Suggests:       pdfmod
Suggests:       synapse
Suggests:       tasque
Suggests:       the-board

%description mate_utilities
MATE Utilities

%files mate_utilities
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/mate_utilities.txt

%prep
# Nothing to prep.

%build
# Nothing to build.

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
for i in mate mate_admin mate_basis mate_laptop mate_internet \
  mate_office mate_office_opt mate_utilities; do
    echo "This file marks the pattern $i to be installed." \
      >"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog
