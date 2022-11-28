#
# spec file for package libcdatetime
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


%define lname	libcdatetime1
Name:           libcdatetime
Version:        20220104
Release:        0
Summary:        Library for C date and time functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libcdatetime
Source:         https://github.com/libyal/libcdatetime/releases/download/%version/libcdatetime-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libcdatetime/releases/download/%version/libcdatetime-alpha-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101

%description
Library for C date and time functions.

Part of the libyal library family.

%package -n %{lname}
Summary:        Library for C date and time functions
Group:          System/Libraries

%description -n %{lname}
Library for C date and time functions.

libcdatetime is a low level member of the libyal library family.

%package devel
Summary:        Development files for libcdatetime, a PFF/OFF file format library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libcdatetime is a library C date and time functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcdatetime.

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
%{_libdir}/libcdatetime.so.*

%files devel
%{_includedir}/libcdatetime.h
%{_includedir}/libcdatetime/
%{_libdir}/libcdatetime.so
%{_libdir}/pkgconfig/libcdatetime.pc
%{_mandir}/man3/libcdatetime.3*

%changelog
