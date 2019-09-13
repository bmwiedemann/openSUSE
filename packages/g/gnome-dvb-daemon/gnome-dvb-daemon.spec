#
# spec file for package gnome-dvb-daemon
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-dvb-daemon
Version:        0.2.90
Release:        0
Summary:        Daemon to use DVB devices
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://live.gnome.org/DVBDaemon
Source0:        http://download.gnome.org/sources/gnome-dvb-daemon/0.2/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.2
BuildRequires:  totem-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.25.1
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-mpegts-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.2.1
BuildRequires:  pkgconfig(sqlite3)

%description
DVB Daemon is a daemon written in Vala to setup your DVB devices,
record and watch TV shows and browse EPG. It can be controlled directly
via its D-Bus interface or with UI applications that come with it.

%package -n python-gnome-dvb-daemon
Summary:        Daemon to use DVB devices -- Python Library
Group:          Productivity/Multimedia/Other
URL:            http://live.gnome.org/DVBDaemon
Requires:       %{name} = %{version}
# Note: we put the Recommends for the lang package here and not in the main
# package because that's where the translatable strings live. We could change
# the name of the lang package, but the .mo files are named gnome-dvb-daemon,
# so it's better this way.
Recommends:     %{name}-lang
# For tuning data
Recommends:     dvb
Provides:       python-gnomedvb = %{version}

%description -n python-gnome-dvb-daemon
DVB Daemon is a daemon written in Vala to setup your DVB devices,
record and watch TV shows and browse EPG. It can be controlled directly
via its D-Bus interface or with UI applications that come with it.

This package contains a a Python library to use the D-Bus interfaces
of DVB Daemon.

%package -n totem-plugin-gnome-dvb-daemon
Summary:        Daemon to use DVB devices -- Totem Plugin
Group:          Productivity/Multimedia/Other
URL:            http://live.gnome.org/DVBDaemon
Requires:       python-gnome-dvb-daemon = %{version}
Requires:       totem
Supplements:    packageand(%{name}:totem)

%description -n totem-plugin-gnome-dvb-daemon
DVB Daemon is a daemon written in Vala to setup your DVB devices,
record and watch TV shows and browse EPG. It can be controlled directly
via its D-Bus interface or with UI applications that come with it.

This package contains a Totem plugin to use your DVB devices.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure \
        --enable-totem-plugin
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file gnome-dvb-control
%suse_update_desktop_file gnome-dvb-setup
# Two different calls, since the files are not in the same package
%fdupes %{buildroot}%{python_sitelib}
%fdupes %{buildroot}%{_libdir}/totem/

%post -n python-gnome-dvb-daemon
%desktop_database_post
%icon_theme_cache_post

%postun -n python-gnome-dvb-daemon
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gnome-dvb-daemon
%{_datadir}/dbus-1/services/org.gnome.DVB.service
%{_datadir}/dbus-1/services/org.gnome.UPnP.MediaServer2.DVBDaemon.service

%files -n python-gnome-dvb-daemon
%{_bindir}/gnome-dvb-control
%{_bindir}/gnome-dvb-setup
%{_datadir}/applications/gnome-dvb-control.desktop
%{_datadir}/applications/gnome-dvb-setup.desktop
%{_datadir}/icons/hicolor/*/apps/gnome-dvb-daemon.*
%{_datadir}/icons/hicolor/*/apps/gnome-dvb-setup.*
%{python3_sitelib}/gnomedvb/

%files -n totem-plugin-gnome-dvb-daemon
%{_libdir}/totem/plugins/dvb-daemon/

%files lang -f %{name}.lang

%changelog
