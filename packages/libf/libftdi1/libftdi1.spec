#
# spec file for package libftdi1
#
# Copyright (c) 2023 SUSE LLC
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


%define sover -2
%define libname %{name}%{sover}
Name:           libftdi1
Version:        1.5.12+git.0684c1b
Release:        0
Summary:        Library to program and control the FTDI USB controller
License:        LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-with-classpath-exception
Group:          Hardware/Other
URL:            https://www.intra2net.com/en/developer/libftdi
Source:         libftdi1-%{version}.tar.xz
# PATCH-FIX-UPSTREAM: http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00005.html
Patch1:         0001-Fix-race-during-build-of-python-bindings.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-xml
BuildRequires:  swig
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(python3)

%description
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package -n %{libname}
Summary:        Library to program and control the FTDI USB controller
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n %{libname}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package -n python3-%{name}
Summary:        Python 3 binding for libftdi1
License:        LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-with-classpath-exception
Group:          Development/Languages/Python

%description -n python3-%{name}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

This package provides the python binding for libftdi.

%package devel
Summary:        Header files for libftdi1
License:        LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-with-classpath-exception
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libusb-1.0)

%description devel
Header files and static libraries for libftdi.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%prep
%autosetup -p1

%build
%cmake \
  -DDOCUMENTATION=ON \
  -DFTDI_EEPROM=ON \
  -DPYTHON_BINDINGS=ON \
  -DBUILD_TESTS=ON \
  -DSTATICLIBS=OFF \
  -Wno-dev
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man3
install -pm 0644 build/doc/man/man3/[^_]*.3 \
  %{buildroot}%{_mandir}/man3

%check
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING* LICENSE
%doc AUTHORS README
%{_libdir}/libftdi*.so.*

%files -n python3-%{name}
%doc python/examples/*.py
%{python3_sitearch}/_ftdi1.so
%{python3_sitearch}/ftdi1.py

%files devel
%doc ftdi_eeprom/example.conf
%{_bindir}/libftdi*-config
%{_bindir}/ftdi_eeprom
%{_includedir}/%{name}
%{_libdir}/libftdi*.so
%{_libdir}/pkgconfig/libftdi*.pc
%{_libdir}/cmake/%{name}
%{_mandir}/man3/*%{ext_man}

%changelog
