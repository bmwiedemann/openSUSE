#
# spec file for package unshield
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define libname lib%{name}%{sover}
Name:           unshield
Version:        1.4.3
Release:        0
Summary:        A Program to Extract InstallShield Cabinet Files
License:        MIT
URL:            https://github.com/twogood/unshield
Source0:        https://github.com/twogood/unshield/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM armv7l-fpic.patch matwey.kornilov@gmail.com -- fix armv7l build
Patch1:         armv7l-fpic.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Cabinet (.CAB) files are a form of archive, which is used by the
InstallShield installer software. The unshield program simply unpacks
such files. This is the binary executable.

%package -n %{libname}
Summary:        A Program to Extract InstallShield Cabinet Files

%description -n %{libname}
Cabinet (.CAB) files are a form of archive, which is used by the
InstallShield installer software. The unshield program simply unpacks
such files. This is the shared library.

%package devel
Summary:        Header files, libraries and development documentation for %{libname}
Requires:       %{libname} = %{version}
Provides:       lib%{name} = %{version}
Obsoletes:      lib%{name} < %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{libname}. If you like to develop programs using %{libname},
you will need to install %{name}-devel.

%prep
%setup -q
%patch1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/lib%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
