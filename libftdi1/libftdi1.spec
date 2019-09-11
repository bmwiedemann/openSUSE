#
# spec file for package libftdi1
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


%define sover -2
%define libname %{name}%{sover}
Name:           libftdi1
Version:        1.4
Release:        0
Summary:        Library to program and control the FTDI USB controller
License:        LGPL-2.1-or-later AND GPL-2.0-with-classpath-exception
Group:          Hardware/Other
URL:            http://www.intra2net.com/en/developer/libftdi
Source:         http://www.intra2net.com/en/developer/libftdi/download/libftdi1-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM libftdi-cmake.patch -- CMake: move options to a dedicated file
Patch1:         libftdi-cmake.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libconfuse-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  pkgconfig
BuildRequires:  swig
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
BuildRequires:  python3-devel
BuildRequires:  python3-xml
%else
BuildRequires:  boost-devel
BuildRequires:  python-devel
BuildRequires:  python-xml
%endif

%description
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package -n %{libname}
Summary:        Library to program and control the FTDI USB controller
Group:          System/Libraries

%description -n %{libname}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%if 0%{?suse_version} >= 1500
%package -n python3-%{name}
Summary:        Python 3 binding for libftdi1
Group:          Development/Languages/Python

%description -n python3-%{name}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

This package provides the python binding for libftdi.
%else
%package -n python2-%{name}
Summary:        Python 2 binding for libftdi1
Group:          Development/Languages/Python
Provides:       binding-python = %{version}
Obsoletes:      binding-python < %{version}

%description -n python2-%{name}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

This package provides the python binding for libftdi.
%endif

%package devel
Summary:        Header files and static libraries for libftdi
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libusb-1_0-devel

%description devel
Header files and static libraries for libftdi.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%prep
%setup -q
%if 0%{?suse_version} >= 01500
%patch1 -p1
%endif

%build
%cmake \
  -DDOCUMENTATION=ON \
  -DFTDI_EEPROM=ON \
  -DPYTHON_BINDINGS=ON
%make_jobs

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man3
cd build
cp -p doc/man/man3/[^_]*.3 %{buildroot}%{_mandir}/man3
find %{buildroot} -type f -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING* LICENSE
%doc AUTHORS README
%{_libdir}/libftdi*.so.*

%if 0%{?suse_version} >= 1500
%files -n python3-%{name}
%doc python/examples/*.py
%{python3_sitearch}/_ftdi1.so
%{python3_sitearch}/ftdi1.py
%else
%files -n python2-%{name}
%doc python/examples/*.py
%{python_sitearch}/_ftdi1.so
%{python_sitearch}/ftdi1.py
%endif

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
