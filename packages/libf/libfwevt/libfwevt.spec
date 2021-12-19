#
# spec file for package libfwevt
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


%define lname	libfwevt1
Name:           libfwevt
Version:        20211219
Release:        0
Summary:        Library for Windows NT data types
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfwevt
Source:         https://github.com/libyal/libfwevt/releases/download/%version/libfwevt-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfwevt/releases/download/%version/libfwevt-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20210625
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcthreads) >= 20211115
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libuna) >= 20210801

%description
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwevt
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Windows NT data type support for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwevt.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfwevt.so.*

%files devel
%license COPYING*
%{_includedir}/libfwevt.h
%{_includedir}/libfwevt/
%{_libdir}/libfwevt.so
%{_libdir}/pkgconfig/libfwevt.pc
%{_mandir}/man3/libfwevt.3*

%changelog
