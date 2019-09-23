#
# spec file for package libftdi0
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

%define realname libftdi
%define sover 1
%define libname %{realname}%{sover}

Name:           libftdi0
Version:        0.20
Release:        0
Summary:        Library to program and control the FTDI USB controller
License:        LGPL-2.1+ AND GPL-2.0-with-classpath-exception
Group:          Hardware/Other
Url:            http://www.intra2net.com/en/developer/libftdi
Source:         http://www.intra2net.com/en/developer/libftdi/download/libftdi-%{version}.tar.gz
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libconfuse-devel
BuildRequires:  libusb-compat-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-xml
BuildRequires:  swig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package -n %{libname}
Summary:        Library to program and control the FTDI USB controller
Group:          System/Libraries

%description -n %{libname}
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%package binding-python
Summary:        Python binding for libftdi
Group:          Development/Languages/Python
Requires:       %{libname} = %{version}
Requires:       swig

%description binding-python
Library to program and control the FTDI USB controller.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

This package provides the python binding for libftdi.

%package devel
Summary:        Header files and static libraries for libftdi
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libusb-compat-devel

%description devel
Header files and static libraries for libftdi.
This library is used by many programs accessing FTDI USB-to-RS232 converters.

%prep
%setup -q -n %{realname}-%{version}

%build
%configure \
    --enable-python-binding \
    --without-examples
make %{?_smp_mflags}

%install
%make_install
#mkdir -p %{buildroot}%{_mandir}/man3
#cp -p doc/man/man3/[^_]*.3 %{buildroot}%{_mandir}/man3
# delete unnecessary files
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
rm %{buildroot}/%{python_sitearch}/ftdi.pyc

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING.GPL COPYING.LIB LICENSE README
%{_libdir}/libftdi*.so.*

%files binding-python
%defattr(-,root,root)
%{python_sitearch}/_ftdi.so
%{python_sitearch}/ftdi.py
%{python_sitearch}/%{realname}-%{version}-py%{py_ver}.egg-info

%files devel
%defattr(-,root,root)
%{_bindir}/libftdi-config
%{_includedir}/ftdi.h
%{_includedir}/ftdi.hpp
%{_libdir}/libftdi*.so
%{_libdir}/pkgconfig/libftdi*.pc
#%{_mandir}/man3/*%{ext_man}

%changelog
