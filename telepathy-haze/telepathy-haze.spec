#
# spec file for package telepathy-haze
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


Name:           telepathy-haze
Version:        0.8.0
Release:        0
Summary:        A libpurple connection manager for Telepathy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            http://telepathy.freedesktop.org/wiki/
Source:         http://telepathy.freedesktop.org/releases/telepathy-haze/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM telepathy-haze-pidgin-2.10.12-compat.patch sor.alexei@meowr.ru -- Fix compatibility with recent versions of Pidgin.
Patch0:         telepathy-haze-pidgin-2.10.12-compat.patch
# PATCH-FIX-UPSTREAM th_contact_list_dont_crash_contact_in_roster.patch fdo#47005 zaitor@opensuse.org -- contact-list: Don't crash if a contact is already in the roster
Patch1:         th_contact_list_dont_crash_contact_in_roster.patch
BuildRequires:  pkgconfig
BuildRequires:  python-Twisted
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.73
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.22
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(purple) >= 2.7
BuildRequires:  pkgconfig(telepathy-glib) >= 0.21

%description
A connection manager for Telepathy that provides support for XMPP,
AIM, ICQ, Yahoo! and Groupwise using Pidgin's libpurple.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libexecdir}/telepathy-haze
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.haze.service
%{_mandir}/man8/telepathy-haze.8%{?ext_man}

%changelog
