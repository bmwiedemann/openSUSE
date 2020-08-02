#
# spec file for package libftdi
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


%define libname %{name}1
Name:           libftdi
Version:        0.20
Release:        0
Summary:        Library to program and control the FTDI USB controller
License:        LGPL-2.1-or-later AND GPL-2.0-with-classpath-exception
URL:            https://www.intra2net.com/en/developer/libftdi
Source:         http://www.intra2net.com/en/developer/libftdi/download/libftdi-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libusb)

%description
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package -n %{libname}
Summary:        Library to program and control the FTDI USB controller

%description -n %{libname}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package devel
Summary:        Header files and static libraries for libftdi
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libusb)
Provides:       libftdi0-devel
Obsoletes:      libftdi0-devel

%description devel
Header files and static libraries for libftdi.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%prep
%setup -q

%build
%configure \
    --disable-python-binding \
    --without-examples \
    --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING.GPL COPYING.LIB LICENSE
%doc AUTHORS README
%{_libdir}/libftdi*.so.*

%files devel
%{_bindir}/libftdi-config
%{_includedir}/ftdi.h
%{_includedir}/ftdi.hpp
%{_libdir}/libftdi*.so
%{_libdir}/pkgconfig/libftdi*.pc

%changelog
