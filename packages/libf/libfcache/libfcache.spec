#
# spec file for package libfcache
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


Name:           libfcache
%define lname	libfcache1
Version:        20230115
Release:        0
Summary:        Library to provide generic file data cache functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfcache
Source:         https://github.com/libyal/libfcache/releases/download/%version/libfcache-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfcache/releases/download/%version/libfcache-alpha-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20210625
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcthreads) >= 20220102
# Various notes: https://en.opensuse.org/libyal

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
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
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
