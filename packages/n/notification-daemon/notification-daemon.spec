#
# spec file for package notification-daemon
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


%define _version 3.20
Name:           notification-daemon
Version:        3.20.0
Release:        0
Summary:        Notification Daemon
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            http://galago-project.org/
Source:         https://download.gnome.org/sources/notification-daemon/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.27.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.5
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
Provides:       dbus(org.freedesktop.Notifications)

%description
D-BUS notification daemon.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
# README is empty
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files lang -f %{name}.lang

%changelog
