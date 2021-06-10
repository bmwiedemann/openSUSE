#
# spec file for package libcaes
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


Name:           libcaes
%define lname	libcaes1
Version:        20210412
Release:        0
Summary:        Library for AES encryption
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcaes
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  pkgconfig(python3)

%description
libcaes is a library for AES encryption.

%package -n %lname
Summary:        Library for AES encryption
Group:          System/Libraries

%description -n %lname
libcaes is a library for AES encryption.

%package devel
Summary:        Development files for libcaes, a AES encryption library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libcaes is a library for AES encryption.

This subpackage contains libraries and header files for developing
applications that want to make use of libcaes.

%package -n python3-%name
Summary:        Python 3 bindings for libcaes
Group:          Development/Languages/Python
Requires:       %lname = %version

%description -n python3-%name
Python 3 bindings for libcaes, which provides functionality for
AES encryption.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-python3
%make_build

%install
%make_install
find "%buildroot" -name "*.la" -print -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libcaes.so.1*

%files devel
%_includedir/libcaes*
%_libdir/libcaes.so
%_libdir/pkgconfig/libcaes.pc
%_mandir/man3/libcaes.3*

%files -n python3-%name
%python3_sitearch/pycaes.so

%changelog
