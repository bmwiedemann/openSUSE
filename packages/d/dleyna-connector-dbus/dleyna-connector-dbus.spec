#
# spec file for package dleyna-connector-dbus
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


Name:           dleyna-connector-dbus
Version:        0.4.1
Release:        0
Summary:        dLeyna connector interface -- DBus
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            https://github.com/phako/dleyna-connector-dbus
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dleyna-core-1.0) >= 0.7.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
Provides:       dleyna-connector(dbus)

%description
D-Bus connector for dLeyna services.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%files
%license COPYING
%doc ChangeLog README.md
%dir %{_libdir}/dleyna-1.0
%dir %{_libdir}/dleyna-1.0/connectors
%{_libdir}/dleyna-1.0/connectors/libdleyna-connector-dbus.so

%changelog
