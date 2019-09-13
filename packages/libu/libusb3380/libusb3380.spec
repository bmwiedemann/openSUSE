#
# spec file for package libusb3380
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   0
%define libname libusb3380-%{sover}
Name:           libusb3380
Version:        0.0.0+git.20190112
Release:        0
Summary:        USB3380 abstraction layer for libusb
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/libusb3380.git
Source:         %{name}-%{version}.tar.xz
Patch0:         libusb3380-cmake-fix-compiler-setup.patch
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)

%description
USB3380 abstraction layer for libusb.

%package -n %{libname}
Summary:        USB3380 abstraction layer for libusb
Group:          System/Libraries

%description -n %{libname}
USB3380 abstraction layer for libusb.

%package devel
Summary:        Development files for libusb3380
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libusb-1.0)

%description devel
USB3380 abstraction layer for libusb.

This subpackage contains libraries and header files for developing
applications that want to make use of libusb3380.

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
%license LICENSE
%doc README.md
%{_libdir}/libusb3380.so.%{sover}*

%files devel
%{_includedir}/libusb3380.h
%{_libdir}/libusb3380.so
%{_libdir}/pkgconfig/libusb3380.pc

%changelog
