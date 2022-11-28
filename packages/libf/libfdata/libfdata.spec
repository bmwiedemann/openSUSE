#
# spec file for package libfdata
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libfdata
%define lname	libfdata1
Version:        20220111
Release:        0
Summary:        Library to provide generic file data functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfdata
Source:         https://github.com/libyal/libfdata/releases/download/%version/libfdata-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfdata/releases/download/%version/libfdata-alpha-%version.tar.gz.asc
Source3:        %name.keyring
# The source code assumes 64bit integers for one of the function returns.  Fix that.
Patch2:         libfdata-20211023-1TB-fix.patch
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
# Various notes: https://en.opensuse.org/libyal

%description
Library to provide generic file data functions for the libyal family of libraries.

%package -n %{lname}
Summary:        Library to provide generic file data functions
Group:          System/Libraries

%description -n %{lname}
Library to provide generic file data functions for the libyal family of libraries.

%package devel
Summary:        Development files for libfdata
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide generic file data functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfdata.

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
%{_libdir}/libfdata.so.*

%files devel
%{_includedir}/libfdata.h
%{_includedir}/libfdata/
%{_libdir}/libfdata.so
%{_libdir}/pkgconfig/libfdata.pc
%{_mandir}/man3/libfdata.3*

%changelog
