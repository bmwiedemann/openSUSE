#
# spec file for package cinnamon-settings-daemon
#
# Copyright (c) 2025 SUSE LLC
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


Name:           cinnamon-settings-daemon
Version:        6.4.3
Release:        0
Summary:        The settings Daemon for the Cinnamon Desktop
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-settings-daemon
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  docutils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xf86-input-wacom
BuildRequires:  pkgconfig(cinnamon-desktop) >= 4.8.0
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(cvc)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgnomekbd)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(xorg-wacom)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang
Recommends:     colord
Recommends:     pulseaudio

%description
This package contains the settings Daemon for the Cinnamon Desktop.

%package devel
Summary:        The settings Daemon for the Cinnamon Desktop -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains the settings Daemon for the Cinnamon Desktop.

This package contains development files for cinnamon-settings-daemon.

%prep
%setup -q

%build
%meson \
 --libexecdir=%{_libdir}

%meson_build

%install
%meson_install

%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING*
%doc AUTHORS README.rst debian/changelog
%config %{_datadir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_sysconfdir}/xdg/autostart/%{name}-*.desktop
%{_bindir}/csd-*
%{_libdir}/%{name}-3.0/
%{_datadir}/%{name}-3.0/
%{_libdir}/csd-*
%{_datadir}/%{name}/
%{_datadir}/applications/csd-*.desktop
%{_datadir}/icons/hicolor/*/apps/csd-*.*
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon.*.xml
%{_datadir}/polkit-1/actions/org.cinnamon.settings-daemon.plugins.*.policy
%{_datadir}/polkit-1/actions/org.cinnamon.settingsdaemon.datetimemechanism.policy
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_libdir}/cinnamon-settings-daemon

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}-3.0/

%changelog
