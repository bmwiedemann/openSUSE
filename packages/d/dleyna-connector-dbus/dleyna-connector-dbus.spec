#
# spec file for package dleyna-connector-dbus
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


Name:           dleyna-connector-dbus
Version:        0.3.0
Release:        0
Summary:        dLeyna connector interface -- DBus
License:        LGPL-2.1
Group:          System/Libraries
Url:            http://01.org/dleyna
Source:         https://01.org/sites/default/files/downloads/dleyna/%{name}-%{version}.tar_1.gz

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dleyna-core-1.0) >= 0.6.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
Provides:       dleyna-connector(dbus)

%description
D-Bus connector for dLeyna services.

%prep
%setup -q

%build
autoreconf -fi
%configure \
	--disable-static \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print
# There is no reason to install the .pc file: it's a dlopen()'d connector, not linked
# Not providing this file until it makes sense avoids us from having to split a -devel package
rm %{buildroot}%{_libdir}/pkgconfig/dleyna-connector-dbus-1.0.pc

%files
%license COPYING
%doc ChangeLog README
%dir %{_libdir}/dleyna-1.0
%dir %{_libdir}/dleyna-1.0/connectors
%{_libdir}/dleyna-1.0/connectors/libdleyna-connector-dbus.so

%changelog
