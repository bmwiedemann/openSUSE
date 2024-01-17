#
# spec file for package libmodbuspp
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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

%define sover 1_0-0
Name:           libmodbuspp
Version:        0.2.3
Release:        0
Summary:        C++ wrapper for the libmodbus library
License:        LGPL-3.0-or-later
Group:          System/Libraries
URL:            https://github.com/epsilonrt/libmodbuspp
Source:         https://github.com/epsilonrt/libmodbuspp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmodbus) >= 3.1.4

%description
A C++ wrapper for the libmodbus library, to send/receive data
with a device which respects the Modbus protocol. This library
can use a serial port or an Ethernet connection.

%package -n libmodbuspp%{sover}
Summary:        C++ wrapper for the libmodbus library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libmodbuspp%{sover}
A C++ wrapper for the libmodbus library, to send/receive data
with a device which respects the Modbus protocol. This library
can use a serial port or an Ethernet connection.

%package -n libmodbuspp-devel
Summary:        Development files for the libmodbuspp library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libmodbuspp%{sover} = %{version}

%description -n libmodbuspp-devel
A C++ wrapper for the libmodbus library, to send/receive data
with a device which respects the Modbus protocol. This library
can use a serial port or an Ethernet connection.

This subpackage contains libraries and header files for developing
applications that want to make use of libmodbuspp.

%prep
%setup -q
sed -i 's/\r$//' AUTHORS

%build
%cmake \
    -DINSTALL_LIB_DIR=%{_libdir} \
    -DINSTALL_CMAKE_DIR=%{_libdir}/cmake \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/doc/modbuspp/README.md
rm %{buildroot}%{_datadir}/modbuspp/COPYING.LESSER
rm -Rf %{buildroot}%{_datadir}/codelite/

%post   -n libmodbuspp%{sover} -p /sbin/ldconfig
%postun -n libmodbuspp%{sover} -p /sbin/ldconfig

%files -n libmodbuspp%{sover}
%license COPYING.LESSER
%doc AUTHORS README.md
%{_libdir}/libmodbuspp.so.1*

%files -n libmodbuspp-devel
%{_includedir}/modbuspp
%{_libdir}/libmodbuspp.so
%{_libdir}/cmake/modbuspp/
%{_libdir}/pkgconfig/libmodbuspp.pc

%changelog
