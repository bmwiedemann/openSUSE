#
# spec file for package xtrx_lms7002m
#
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define sover   0_0_0-SUSE
%define libname libxtrx_lms7002m%{sover}
Name:           xtrx_lms7002m
Version:        0.0.0+git.20171206
Release:        0
Summary:        XTRX's fork from myriadrf/LMS7002M-driver
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
Source:         %{name}-%{version}.tar.xz
Patch0:         xtrx_lms7002m-set-soversion.patch
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig

%description
XTRX's fork from myriadrf/LMS7002M-driver.

%package -n %{libname}
Summary:        XTRX's fork from myriadrf/LMS7002M-driver
Group:          System/Libraries

%description -n %{libname}
XTRX's fork from myriadrf/LMS7002M-driver.

%package devel
Summary:        XTRX's fork from myriadrf/LMS7002M-driver - devel
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
XTRX's fork from myriadrf/LMS7002M-driver.

This subpackage contains libraries and header files for developing
applications that want to make use of xtrx_lms7002m.


%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DLIB_LMS7002M_NAME="xtrx_lms7002m" \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_jobs

%install
%cmake_install

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc LICENSE-2.0.txt README.md
%{_libdir}/libxtrx_lms7002m.so.*

%files devel
%dir %{_includedir}/LMS7002M
%{_includedir}/LMS7002M/LMS7002M.h
%{_includedir}/LMS7002M/LMS7002M_*.h
%{_libdir}/libxtrx_lms7002m.so

%changelog
