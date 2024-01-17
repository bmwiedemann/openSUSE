#
# spec file for package telepathy-idle
#
# Copyright (c) 2020 SUSE LLC
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


Name:           telepathy-idle
Version:        0.2.2
Release:        0
Summary:        IRC support for Telepathy
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/IRC
URL:            https://gitlab.freedesktop.org/telepathy/telepathy-idle
Source:         http://telepathy.freedesktop.org/releases/telepathy-idle/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(dbus-1) >= 0.51
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.51
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32.0
BuildRequires:  pkgconfig(telepathy-glib) >= 0.21

%description
Telepathy-idle provides IRC support for Telepathy.

%prep
%autosetup -p1

%build
%configure \
	--libexecdir=%{_prefix}/lib/%{name} \
	%{nil}
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers
%{_datadir}/telepathy/managers/idle.manager
%{_prefix}/lib/%{name}
%{_mandir}/man8/telepathy-idle.8%{ext_man}

%changelog
