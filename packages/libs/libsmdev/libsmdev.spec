#
# spec file for package libsmdev
#
# Copyright (c) 2021 SUSE LLC
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


%define lname	libsmdev1
Name:           libsmdev
Version:        20210418
Release:        0
Summary:        Library to access storage media devices
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsmdev
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libsmdev is a library to access and read storage media devices.

%package -n %{lname}
Summary:        Library to access storage media devices
Group:          System/Libraries

%description -n %{lname}
libsmdev is a library to access and read storage media devices.

%package devel
Summary:        Development files for libsmdev, a storage media access library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libsmdev is a library to access and read storage media devices.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmdev.

%package tools
Summary:        Utilities for reading storage media devices through libsmdev
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libsmdev, which
can access and read storage media devices and will determine
information about such.

%package -n python3-%{name}
Summary:        Python bindings for libsmdev
Group:          Development/Languages/Python
Provides:       pysmdev = %{version}

%description -n python3-%{name}
Python 3 bindings for libsmdev, which is a library to access and read storage media devices.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libsmdev.so.1*

%files devel
%license COPYING*
%{_includedir}/libsmdev*
%{_libdir}/libsmdev.so
%{_libdir}/pkgconfig/libsmdev.pc
%{_mandir}/man3/libsmdev.3*

%files tools
%license COPYING*
%{_bindir}/smdevinfo
%{_mandir}/man1/smdevinfo.1*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pysmdev.so

%changelog
