#
# spec file for package libfcache
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


Name:           libfcache
%define lname	libfcache1
Version:        20210413
Release:        0
Summary:        Library to provide generic file data cache functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfcache
Source:         %{name}-%{version}.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcthreads) >= 20200508

%description
Library to provide generic file data cache functions for the libyal family of libraries.

%package -n %{lname}
Summary:        Library to provide generic file data cache functions
Group:          System/Libraries

%description -n %{lname}
Library to provide generic file data cache functions for the libyal family of libraries.

%package devel
Summary:        Development files for libfcache
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide generic file data cache functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfcache.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfcache.so.*

%files devel
%license COPYING*
%{_includedir}/libfcache.h
%{_includedir}/libfcache/
%{_libdir}/libfcache.so
%{_libdir}/pkgconfig/libfcache.pc
%{_mandir}/man3/libfcache.3*

%changelog
