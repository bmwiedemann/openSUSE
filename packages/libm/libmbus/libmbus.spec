#
# spec file for package libmbus
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libmbus
Version:        0.9.0+59
Release:        0
Summary:        M-bus Library
License:        BSD-3-Clause
URL:            https://github.com/rscada/libmbus
Source:         %{name}-%{version}.tar.xz
Patch0:         libmbus-automake.patch
BuildRequires: libtool fdupes

%description
libmbus is an open source library for the M-bus (Meter-Bus) protocol.

The Meter-Bus is a standard for reading out meter data from electricity meters, heat meters, gas meters, etc. The M-bus standard deals with both the electrical signals on the M-Bus, and the protocol and data format used in transmissions on the M-Bus. The role of libmbus is to decode/encode M-bus data, and to handle the communication with M-Bus devices.

%package -n libmbus0
Summary:        M-bus Library

%description -n libmbus0
libmbus is an open source library for the M-bus (Meter-Bus) protocol.

The Meter-Bus is a standard for reading out meter data from electricity meters, heat meters, gas meters, etc. The M-bus standard deals with both the electrical signals on the M-Bus, and the protocol and data format used in transmissions on the M-Bus. The role of libmbus is to decode/encode M-bus data, and to handle the communication with M-Bus devices.

%package devel
Summary:        Development headers for the M-bus Library
Requires: libmbus0 = %{version}

%description devel
libmbus is an open source library for the M-bus (Meter-Bus) protocol.

This package allows you to write programs against libmbus.

%prep
%autosetup -p1
mkdir m4 libltdl

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libmbus.{a,la}
rm -rf %{buildroot}%{_datadir}/doc/
%fdupes %{buildroot}%{_mandir}

%ldconfig_scriptlets -n libmbus0

%files
%license COPYING
%{_bindir}/mbus-*
%{_mandir}/man1/mbus-*.1%{?ext_man}
%{_mandir}/man1/libmbus.1%{?ext_man}

%files -n libmbus0
%{_libdir}/libmbus.so.0*

%files devel
%{_includedir}/mbus/
%{_libdir}/pkgconfig/libmbus.pc
%{_libdir}/libmbus.so


%changelog
