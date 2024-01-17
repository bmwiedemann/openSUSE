#
# spec file for package libfvalue
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


Name:           libfvalue
%define lname	libfvalue1
Version:        20220120
Release:        0
Summary:        Library to provide generic file value functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfvalue
Source:         https://github.com/libyal/libfvalue/releases/download/%version/libfvalue-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfvalue/releases/download/%version/libfvalue-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfwnt) >= 20210906
BuildRequires:  pkgconfig(libuna) >= 20220102
# Various notes: https://en.opensuse.org/libyal

%description
Library to provide generic file value functions for the libyal family of libraries.

%package -n %{lname}
Summary:        Library to provide generic file value functions
Group:          System/Libraries

%description -n %{lname}
Library to provide generic file value functions for the libyal family of libraries.

%package devel
Summary:        Development files for libfvalue
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide generic file value functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfvalue.

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
%{_libdir}/libfvalue.so.*

%files devel
%{_includedir}/libfvalue.h
%{_includedir}/libfvalue/
%{_libdir}/libfvalue.so
%{_libdir}/pkgconfig/libfvalue.pc
%{_mandir}/man3/libfvalue.3*

%changelog
