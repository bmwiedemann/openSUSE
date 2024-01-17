#
# spec file for package liblms7002m
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


%define sover   0
%define libname liblms7compact%{sover}
Name:           liblms7002m
Version:        0.0.0+git.20200518
Release:        0
Summary:        Compact LMS7002 library suitable for MCU
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/liblms7002m.git
Source:         %{name}-%{version}.tar.xz
Patch0:         liblms7002m-shared-library-versioning.patch
BuildRequires:  cmake
BuildRequires:  python3
BuildRequires:  python3-Cheetah3

%description
Compact LMS7002 library suitable for MCU.

%package -n %{libname}
Summary:        Compact LMS7002 library suitable for MCU
Group:          System/Libraries

%description -n %{libname}
Compact LMS7002 library suitable for MCU.

%package devel
Summary:        Development files for liblms7compact
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Compact LMS7002 library suitable for MCU.

This subpackage contains libraries and header files for developing
applications that want to make use of liblms7compact.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_jobs

%install
%cmake_install

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/liblms7compact.so.%{sover}*

%files devel
%{_includedir}/liblms7002m.h
%{_libdir}/liblms7compact.so

%changelog
