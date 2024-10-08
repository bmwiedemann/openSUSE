#
# spec file for package patterns-xfce
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           patterns-xfce
Version:        20230212
Release:        0
Summary:        Patterns for Installation (Xfce)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Xfce patterns.

################################################################################

%package xfce
%pattern_graphicalenvironments
Summary:        XFCE Desktop Environment
Group:          Metapackages
Provides:       pattern() = xfce
Provides:       pattern-icon() = pattern-xfce
Provides:       pattern-order() = 1310
Provides:       pattern-visible()
Requires:       pattern() = x11
Requires:       pattern() = xfce_basis
Provides:       patterns-openSUSE-xfce = %{version}
Obsoletes:      patterns-openSUSE-xfce < %{version}

# Xfce Recommended applications
Recommends:     gigolo
Recommends:     mousepad
Recommends:     parole
Recommends:     ristretto
Recommends:     thunar-plugin-archive
Recommends:     thunar-plugin-media-tags
Recommends:     thunar-volman
Recommends:     tumbler
Recommends:     xfce4-dict
Recommends:     xfce4-panel-profiles
Recommends:     xfce4-screenshooter
Recommends:     xfce4-taskmanager

# Recommended Xfce Panel plugins
Recommends:     xfce4-calculator-plugin
Recommends:     xfce4-clipman-plugin
Recommends:     xfce4-cpufreq-plugin
Recommends:     xfce4-cpugraph-plugin
Recommends:     xfce4-diskperf-plugin
Recommends:     xfce4-docklike-plugin
Recommends:     xfce4-eyes-plugin
Recommends:     xfce4-fsguard-plugin
Recommends:     xfce4-genmon-plugin
Recommends:     xfce4-kbdleds-plugin
Recommends:     xfce4-mailwatch-plugin
Recommends:     xfce4-mount-plugin
Recommends:     xfce4-mpc-plugin
Recommends:     xfce4-netload-plugin
Recommends:     xfce4-notes-plugin
Recommends:     xfce4-places-plugin
Recommends:     xfce4-screenshooter-plugin
Recommends:     xfce4-sensors-plugin
Recommends:     xfce4-smartbookmark-plugin
Recommends:     xfce4-stopwatch-plugin
Recommends:     xfce4-systemload-plugin
Recommends:     xfce4-timeout-plugin
Recommends:     xfce4-timer-plugin
Recommends:     xfce4-verve-plugin
Recommends:     xfce4-wavelan-plugin
Recommends:     xfce4-weather-plugin

# Third-party applications
Recommends:     blueman
Recommends:     evince
Recommends:     file-roller
Recommends:     galculator
Recommends:     gnome-disk-utility
Recommends:     gucharmap
Recommends:     lightdm
Recommends:     lightdm-gtk-greeter
Recommends:     lightdm-gtk-greeter-settings
Recommends:     menulibre
Recommends:     mugshot
Recommends:     pragha
Recommends:     seahorse
Recommends:     simple-scan
Recommends:     thunar-sendto-blueman

# Additional applications for easy debugging

Recommends:     gdb
Recommends:     system-config-printer
Recommends:     system-config-printer-applet
# bnc#537362

# This is needed so that openQA does not fail (poo#124364) but also in preparation for offline updates method
Recommends:     gnome-packagekit

# Currently only Leap fully supports this update method via packagekit
%if 0%{?sle_version} >= 150400 && 0%{?is_opensuse}
Recommends:     package-update-indicator
%endif

# bnc#537365
Recommends:     gnome-keyring
Recommends:     gnome-keyring-pam
# bnc#1108381
Recommends:     gcr-ssh-askpass
Recommends:     opensuse-welcome

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip

%description xfce
Xfce is a lightweight desktop environment for various *NIX systems.

%files xfce
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/xfce.txt

################################################################################

%package xfce_extra
%pattern_graphicalenvironments
Summary:        XFCE Extra Applications
Group:          Metapackages
Provides:       pattern() = xfce_extra
Provides:       pattern-extends() = xfce
Provides:       pattern-icon() = pattern-xfce
Provides:       pattern-visible()
Provides:       pattern-order() = 1315
Requires:       pattern() = xfce
Requires:       pattern() = xfce_basis
Recommends:     pattern() = office
Recommends:     pattern() = multimedia
Recommends:     pattern() = imaging
Recommends:     libreoffice-gtk3
Recommends:     MozillaThunderbird
Recommends:     pidgin
Recommends:     remmina
Recommends:     remmina-plugin-rdp
Recommends:     remmina-plugin-vnc
Recommends:     remmina-plugin-xdmcp
Recommends:     shotwell
Recommends:     transmission-gtk
Provides:       patterns-openSUSE-xfce_extra = %{version}
Obsoletes:      patterns-openSUSE-xfce_extra < %{version}
Provides:       patterns-openSUSE-xfce_office = %{version}
Obsoletes:      patterns-openSUSE-xfce_office < %{version}
Provides:       patterns-xfce-xfce_office = %{version}
Obsoletes:      patterns-xfce-xfce_office < %{version}

%description xfce_extra
Extra packages for the XFCE Desktop Environment

%files xfce_extra
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/xfce_extra.txt

################################################################################


%package xfce_basis
%pattern_graphicalenvironments
Summary:        XFCE Base System
Group:          Metapackages
Provides:       pattern() = xfce_basis
Provides:       pattern-extends() = xfce
Provides:       pattern-icon() = pattern-xfce
Provides:       pattern-order() = 1300
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Provides:       patterns-openSUSE-xfce_basis = %{version}
Obsoletes:      patterns-openSUSE-xfce_basis < %{version}
# This defines a bare minimum Xfce desktop used, for example, as
# base for the openSUSE Rescue CD
Requires:       thunar
Requires:       thunar-volman
Requires:       xfce4-appfinder
Requires:       xfce4-notifyd
Requires:       xfce4-panel
Requires:       xfce4-power-manager
Requires:       xfce4-session
Requires:       xfce4-settings
Requires:       xfconf
Requires:       xfdesktop
Requires:       xfwm4
Recommends:     pavucontrol
Recommends:     xfce4-pulseaudio-plugin

#
# low level functionality
#
Recommends:     avahi
Recommends:     dbus-1-x11
# bnc#540627
Recommends:     xdg-utils
Recommends:     xdg-user-dirs-gtk
Recommends:     desktop-file-utils
Recommends:     shared-mime-info
Recommends:     NetworkManager
Recommends:     NetworkManager-applet
# without polkit-gnome, NetworkManager-applet is not that useful
# we need a polkit-authentication-agent (bnc#1047500)
Recommends:     polkit-gnome
# use gnomesu as su wrapper
Recommends:     libgnomesu
# bnc#440285
Recommends:     pinentry-gtk2
# For screenlocking to work in xfce
Recommends:     xfce4-screensaver
Recommends:     xfce4-notifyd
Recommends:     xfce4-terminal
Recommends:     libxfce4ui-tools
Recommends:     xfce4-xkb-plugin
#
# core desktop functionality
#
Recommends:     libyui-qt-pkg
Recommends:     yast2-control-center-qt
#
# branding
#
Suggests:       exo-branding-openSUSE
Suggests:       gconf2-branding-openSUSE
Suggests:       libgarcon-branding-openSUSE
Suggests:       libxfce4ui-branding-openSUSE
Suggests:       lightdm-gtk-greeter-branding-openSUSE
Suggests:       thunar-volman-branding-openSUSE
Suggests:       wallpaper-branding-openSUSE
Suggests:       xfce4-notifyd-branding-openSUSE
Suggests:       xfce4-panel-branding-openSUSE
Suggests:       xfce4-session-branding-openSUSE
Suggests:       xfce4-settings-branding-openSUSE
Suggests:       xfdesktop-branding-openSUSE
Suggests:       xfwm4-branding-openSUSE
Suggests:       desktop-branding

Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
# bnc#508120
Recommends:     xdg-user-dirs
# metalink downloader
Suggests:       aria2

%description xfce_basis
Base packages for the XFCE Desktop Environment

%files xfce_basis
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/xfce_basis.txt

################################################################################

%package xfce_laptop
%pattern_xfcedesktop
Summary:        XFCE Laptop
Group:          Metapackages
Provides:       pattern() = xfce_laptop
Provides:       pattern-extends() = laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 5180
Supplements:    packageand(patterns-xfce-xfce:patterns-desktop-laptop)
Requires:       pattern() = xfce
Requires:       pattern() = xfce_basis
Provides:       patterns-openSUSE-xfce_laptop = %{version}
Obsoletes:      patterns-openSUSE-xfce_laptop < %{version}

%description xfce_laptop
XFCE Laptop

%files xfce_laptop
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/xfce_laptop.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns
for i in xfce xfce_basis xfce_laptop xfce_extra; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog
