#
# spec file for package wiiuse
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


%define libname libwiiuse0
Name:           wiiuse
Version:        0.15.5
Release:        0
Summary:        Connects with several Nintendo Wii remotes
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/wiiuse/wiiuse
Source0:        https://github.com/wiiuse/wiiuse/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         wiiuse-soname.patch
BuildRequires:  bluez-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl)

%description
Wiiuse is a library written in C that connects with several Nintendo
Wii remotes.  Supports motion sensing, IR tracking, nunchuk, classic
controller, and the Guitar Hero 3 controller.  Single threaded and
nonblocking makes a light weight and clean API.

%package -n %{libname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++

%description  -n %{libname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       bluez-devel

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

dos2unix CHANGELOG.mkd README.mkd

%build
%cmake
%make_build

%install
%cmake_install

# Docs will be installed by %%doc
rm -rf %{buildroot}%{_datadir}/doc/wiiuse

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc README.mkd RELEASE.md CHANGELOG.mkd
%{_includedir}/*
%{_libdir}/*.so
%{_bindir}/wiiuseexample
%{_bindir}/wiiuseexample-sdl

%changelog
