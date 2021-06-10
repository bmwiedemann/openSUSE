#
# spec file for package libfwps
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


Name:           libfwps
%define lname	libfwps1
Version:        20210421
Release:        0
Summary:        Library for Windows Property Store data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfwps
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfole) >= 20170502
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libfwps is a library for Windows Property Store data types.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for Windows Property Store data types
Group:          System/Libraries

%description -n %lname
libfwps is a library for Windows Property Store data types.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfwps
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfwps is a library for Windows Property Store data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwps.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfwps
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
Python 3 bindings for libfwps, which can read Windows Property Store data types.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-python3
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfwps.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n python3-%name
%python3_sitearch/*.so

%changelog
