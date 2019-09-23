#
# spec file for package mate-notification-daemon
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


%define _version 1.23
Name:           mate-notification-daemon
Version:        1.23.0
Release:        0
Summary:        Notification daemon for MATE
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
Provides:       dbus(org.freedesktop.Notifications)
%glib2_gsettings_schema_requires

%description
D-Bus notification daemon for MATE.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name} \
  --disable-static                    \
  --disable-schemas-install
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file mate-notification-properties

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
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/mate-notification-properties
%dir %{_libexecdir}/mate-notification-daemon/
%{_libexecdir}/mate-notification-daemon/mate-notification-daemon
%dir %{_libdir}/mate-notification-daemon/
%dir %{_libdir}/mate-notification-daemon/engines/
%{_libdir}/mate-notification-daemon/engines/lib*.so
%{_datadir}/applications/mate-notification-properties.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/mate-notification-daemon/
%{_datadir}/mate-notification-daemon/mate-notification-properties.ui
%{_datadir}/glib-2.0/schemas/*.xml
%{_mandir}/man1/mate-notification-properties.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
