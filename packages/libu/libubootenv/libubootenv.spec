#
# spec file for package libubootenv
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


%global sover   0
%global libname %{name}%{sover}
Name:           libubootenv
Version:        0.3.7
Release:        0
Summary:        U-Boot libraries and tools to access environment
License:        LGPL-2.1-or-later
Group:          System/Boot
URL:            https://github.com/sbabic/libubootenv
Source:         https://github.com/sbabic/libubootenv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)

%description
U-Boot libraries and tools to access environment.

%package -n %{libname}
Summary:        Library to read and modify U-Boot environment
Group:          System/Libraries

%description -n %{libname}
Library to read and modify U-Boot environment.

%package devel
Summary:        Development files for libubootenv
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Library to read and modify U-Boot environment.

This subpackage contains libraries and header files for developing
applications that want to make use of libubootenv.

%package -n u-boot-fw-utils
Summary:        Replacement for fw_printenv/setenv utilities provided by U-Boot
Group:          System/Boot

%description -n u-boot-fw-utils
Hardware-independent replacement for fw_printenv/setenv utilities
provided by U-Boot.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# Only keep the shared library
rm %{buildroot}%{_libdir}/libubootenv.a

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%{_libdir}/libubootenv.so.%{sover}*

%files devel
%{_includedir}/libuboot.h
%{_libdir}/libubootenv.so
%{_libdir}/pkgconfig/libubootenv.pc

%files -n u-boot-fw-utils
%{_bindir}/fw_printenv
%{_bindir}/fw_setenv

%changelog
