#
# spec file for package libmodbuspp
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# Copyright (c) 2020-2026, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%define sover 1
Name:           libmodbuspp
Version:        1.2
Release:        0
Summary:        C++ wrapper for the libmodbus library
License:        LGPL-2.1-or-later
URL:            https://github.com/epsilonrt/libmodbuspp
Source:         https://github.com/epsilonrt/libmodbuspp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmodbus) >= 3.1.6
BuildRequires:  pkgconfig(nlohmann_json) >= 3.2.0

%description
A C++ wrapper for the libmodbus library, to send/receive data
with a device which respects the Modbus protocol. This library
can use a serial port or an Ethernet connection.

%package -n libmodbuspp%{sover}
Summary:        C++ wrapper for the libmodbus library
# shlib package renamed libmodbuspp1_0-0 -> libmodbuspp1 at 1.2 (same SONAME .so.1)
Provides:       libmodbuspp1_0-0 = %{version}-%{release}
Obsoletes:      libmodbuspp1_0-0 < %{version}-%{release}

%description -n libmodbuspp%{sover}
A C++ wrapper for the libmodbus library, to send/receive data
with a device which respects the Modbus protocol. This library
can use a serial port or an Ethernet connection.

%package -n libmodbuspp-devel
Summary:        Development files for the libmodbuspp library
Requires:       libmodbuspp%{sover} = %{version}

%description -n libmodbuspp-devel
A C++ wrapper for the libmodbus library, to send/receive data
with a device which respects the Modbus protocol. This library
can use a serial port or an Ethernet connection.

This subpackage contains libraries and header files for developing
applications that want to make use of libmodbuspp.

%prep
%autosetup -p1
sed -i 's/\r$//' AUTHORS

%build
%cmake \
    -DMODBUSPP_USE_EXTERNAL_JSON=ON \
    -DINSTALL_LIB_DIR=%{_libdir} \
    -DINSTALL_CMAKE_DIR=%{_libdir}/cmake \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/doc/modbuspp/README.md
rm %{buildroot}%{_datadir}/modbuspp/COPYING.LESSER
rm -Rf %{buildroot}%{_datadir}/codelite/

%ldconfig_scriptlets -n libmodbuspp%{sover}

%files -n libmodbuspp%{sover}
%license COPYING.LESSER
%doc AUTHORS README.md
%{_libdir}/libmodbuspp.so.1*

%files -n libmodbuspp-devel
%{_includedir}/modbuspp.h
%{_includedir}/modbuspp
%{_libdir}/libmodbuspp.so
%{_libdir}/cmake/modbuspp/
%{_libdir}/pkgconfig/modbuspp.pc

%changelog
