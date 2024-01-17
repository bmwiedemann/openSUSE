#
# spec file for package littleb
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         sover 0
Name:           littleb
Version:        0.1.2
Release:        0
Summary:        Bluetooth Low Energy Library
License:        MIT
Group:          Hardware/Other
Url:            https://github.com/intel-iot-devkit/littleb
Source:         https://github.com/intel-iot-devkit/littleb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd) >= 221

%description
LittleB provides a Bluetooth Low Energy API. It exposes the BLE GATT
API for C using BlueZ over SD-Bus.

%prep
%setup -q

%package -n lib%{name}%{sover}
Summary:        Bluetooth Low Energy library
Group:          System/Libraries

%description -n lib%{name}%{sover}
LittleB provides a Bluetooth Low Energy API. It exposes the BLE GATT
API for C using BlueZ over SD-Bus.

This package contains shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
LittleB provides a Bluetooth Low Energy API. It exposes the BLE GATT
API for C using BlueZ over SD-Bus.

This package contains development files for %{name}.

%package examples
Summary:        Examples for %{name}
Group:          Hardware/Other

%description examples
LittleB provides a Bluetooth Low Energy API. It exposes the BLE GATT
API for C using BlueZ over SD-Bus.

This package contains examples for %{name}.

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags}

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%doc COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%files examples
%doc COPYING
%{_datadir}/%{name}

%changelog
