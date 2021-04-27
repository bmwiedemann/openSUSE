#
# spec file for package patterns-deepin
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           patterns-deepin
Version:        15.2.20210440
Release:        0
Summary:        Patterns for Installation (Deepin)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

This particular package contains the Deepin Desktop patterns.

%package deepin
%pattern_graphicalenvironments
Summary:        Deepin Desktop Environment
Group:          Metapackages
Provides:       pattern() = deepin
Provides:       pattern-icon() = pattern-deepin
Provides:       pattern-order() = 1625
Provides:       pattern-visible()
Requires:       pattern() = deepin_basis
Recommends:     pattern() = games
Recommends:     pattern() = imaging
Recommends:     pattern() = deepin_admin
Recommends:     pattern() = deepin_internet
Recommends:     pattern() = deepin_multimedia
Recommends:     pattern() = office
Recommends:     pattern() = deepin_office
Suggests:       pattern() = deepin_utilities
# The third part application
Recommends:     blueberry
Recommends:     brasero
# Deepin application
Recommends:     deepin-system-monitor
Recommends:     deepin-turbo
Recommends:     deepin-wallpapers
Recommends:     deepin-terminal
Recommends:     deepin-compressor
Recommends:     deepin-editor
# Tool for advanced configuration of printers, instead of deepin-printer
Recommends:     system-config-printer-applet
Recommends:     system-config-printer
Suggests:       deepin-wallpapers-community
Suggests:       deepin-feature-enable

%description deepin
The Deepin desktop environment is a desktop environment using traditional metaphors.

%files deepin
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin.txt

%package deepin_admin
%pattern_deepindesktop
Summary:        Deepin Administration Tools
Group:          Metapackages
Provides:       pattern() = deepin_admin
Provides:       pattern-extends() = deepin
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2060
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     gnome-packagekit
Recommends:     deepin-system-monitor
Recommends:     deepin-clone
Recommends:     remmina

%description deepin_admin
Administration Tools e.g. for desktop lockdown.

%files deepin_admin
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_admin.txt

%package deepin_basis
%pattern_graphicalenvironments
Summary:        Deepin Base System
Group:          Metapackages
Provides:       pattern() = deepin_basis
Provides:       pattern-icon() = pattern-deepin
Provides:       pattern-order() = 1620
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-control-center
Requires:       deepin-control-center-data
Requires:       deepin-daemon
Requires:       deepin-desktop
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       deepin-dock
Requires:       deepin-file-manager
Requires:       deepin-gtk-theme
Requires:       deepin-icon-theme
Requires:       deepin-kwin
Requires:       deepin-launcher
Requires:       deepin-network-utils
Requires:       deepin-polkit-agent
Requires:       deepin-pw-check
Requires:       deepin-session-shell
Requires:       deepin-session-ui
Requires:       deepin-start
Requires:       libqt5-dwaylandplugin
Requires:       libqt5-dxcbplugin
Requires:       libqt5-kwayland-shellplugin
Requires:       qt5integration
Recommends:     sddm
Recommends:     deepin-api-dbus
Recommends:     deepin-api-polkit
Recommends:     deepin-daemon-dbus 
Recommends:     deepin-daemon-polkit
Recommends:     deepin-sound-theme
Recommends:     NetworkManager
Recommends:     dbus-1-x11
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
Recommends:     deepin-desktop-schemas-branding-openSUSE
Recommends:     deepin-launcher-branding-openSUSE
Recommends:     wallpaper-branding-openSUSE
Recommends:     libsocialweb-branding-openSUSE
Recommends:     desktop-branding
#
# Now the real packages
#
Recommends:     gnome-keyring-pam
Recommends:     at-spi2-core
Recommends:     canberra-gtk-play
Recommends:     gnome-keyring
Recommends:     shared-mime-info
Recommends:     xkeyboard-config
Recommends:     yelp
# PulseAudio is the default sound server.
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils
# We need something for xdg-su.
Recommends:     libgnomesu
Recommends:     google-droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
Recommends:     avahi
Recommends:     xdg-user-dirs
# metalink downloader
Suggests:       aria2
Suggests:       deepin-feature-enable

%description deepin_basis
Base packages for the Deepin desktop environment.

%files deepin_basis
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_basis.txt

%package deepin_internet
%pattern_deepindesktop
Summary:        Deepin Internet
Group:          Metapackages
Provides:       pattern() = deepin_internet
Provides:       pattern-extends() = deepin
Provides:       pattern-icon() = package_deepin
Provides:       pattern-order() = 2431
Recommends:     pidgin
Recommends:     MozillaThunderbird
Recommends:     NetworkManager-openvpn
Recommends:     NetworkManager-pptp
Recommends:     NetworkManager-vpnc
Recommends:     NetworkManager-openconnect
Recommends:     uget
Suggests:       linphone


%description deepin_internet
Deepin Internet Applications.

%files deepin_internet
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_internet.txt

%package deepin_multimedia
%pattern_deepindesktop
Summary:        Deepin Multimedia
Group:          Metapackages
Provides:       pattern() = deepin_multimedia
Provides:       pattern-extends() = multimedia
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2270
Supplements:    packageand(patterns-deepin:patterns-multimedia)
Requires:       pattern() = deepin
Requires:       vlc
Recommends:     deepin-image-viewer
Recommends:     deepin-screen-recorder
Recommends:     deepin-music-player
Recommends:     deepin-movie
Recommends:     osdlyrics
Recommends:     gimp
Recommends:     patterns-desktop-multimedia
Suggests:       deepin-draw

%description deepin_multimedia
Deepin multimedia applications.

%files deepin_multimedia
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_multimedia.txt

%package deepin_office
%pattern_graphicalenvironments
Summary:        Deepin Office
Group:          Metapackages
Provides:       pattern() = deepin_office
Provides:       pattern-extends() = office
Provides:       pattern-icon() = pattern-deepin
Provides:       pattern-order() = 2270
Supplements:    packageand(patterns-deepin:patterns-office)
Requires:       pattern() = deepin_basis
Recommends:     pattern() = deepin_office_opt
Recommends:     libreoffice-qt5
# deepin-reader is not already, use evince instead
# Recommends:     deepin-reader
Recommends:     evince

%description deepin_office
Deepin Office

%files deepin_office
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_office.txt

%package deepin_office_opt
%pattern_deepindesktop
Summary:        Deepin Office
Group:          Metapackages
Provides:       pattern() = deepin_office_opt
Provides:       pattern-extends() = office
Provides:       pattern-icon() = pattern-deepin
Provides:       pattern-order() = 2271
Supplements:    packageand(patterns-deepin:patterns-office)
Requires:       pattern() = deepin_basis
Recommends:     deepin-voice-note
Recommends:     simple-scan
Recommends:     deepin-calculator
Recommends:     deepin-calendar

%description deepin_office_opt
Deepin Office

%files deepin_office_opt
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_office_opt.txt

%package deepin_utilities
%pattern_deepindesktop
Summary:        Deepin Utilities
Group:          Metapackages
Provides:       pattern() = deepin_utilities
Provides:       pattern-extends() = deepin
Provides:       pattern-icon() = pattern-deepin
Provides:       pattern-order() = 2310
Requires:       pattern() = deepin_basis
Recommends:     deepin-screen-recorder
Recommends:     deepin-draw
Recommends:     cheese

%description deepin_utilities
Deepin Utilities

%files deepin_utilities
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/deepin_utilities.txt

%prep
# Nothing to prep.

%build
# Nothing to build.

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
for i in deepin deepin_admin deepin_basis deepin_multimedia deepin_internet \
  deepin_office deepin_office_opt deepin_utilities; do
    echo "This file marks the pattern $i to be installed." \
      >"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog

