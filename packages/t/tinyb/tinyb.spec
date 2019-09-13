#
# spec file for package tinyb
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


%define         sover 0
Name:           tinyb
Version:        0.5.1
Release:        0
Summary:        Tiny Bluetooth LE Library
License:        MIT
Group:          Hardware/Other
URL:            https://github.com/intel-iot-devkit/tinyb
Source:         https://github.com/intel-iot-devkit/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40

%description
TinyB provides an API for Bluetooth LE (Low Energy).
TinyB exposes the BLE GATT API for C++, Java and other languages,
using BlueZ over DBus.

%prep
%setup -q

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
TinyB provides an API for Bluetooth LE (Low Energy).
TinyB exposes the BLE GATT API for C++, Java and other languages,
using BlueZ over DBus.

This package contains shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
TinyB provides an API for Bluetooth LE (Low Energy).
TinyB exposes the BLE GATT API for C++, Java and other languages,
using BlueZ over DBus.

This package contains development files for %{name}.

%build
%cmake
%make_jobs

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
