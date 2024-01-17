#
# spec file for package libcircllhist
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover_major 0
%define sover_minor 0
%define sover_patch 1
%define libname libcircllhist%{sover_major}_%{sover_minor}_%{sover_patch}

Name:           libcircllhist
Version:        20180917
Release:        0
Summary:        A C implementation of Circonus log-linear histograms
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Url:            https://github.com/circonus-labs/libcircllhist
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  patchelf

%description
An implementation of Circonus log-linear histograms written in C.

%package -n %{libname}
Summary:        A C implementation of Circonus log-linear histograms
Group:          System/Libraries

%description -n %{libname}
Shared library for libcircllhist, an implementation of Circonus log-linear
histograms written in C.

%package devel
Summary:        Development files for libcircllhist
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for libcircllhist, an implementation of Circonus log-linear
histograms written in C.

%prep
%setup -q

%build
autoconf
%configure
%make_build

%install
%make_install
patchelf --set-soname libcircllhist.so.%{sover_major}.%{sover_minor}.%{sover_patch} %{buildroot}%{_libdir}/libcircllhist.so.%{sover_major}.%{sover_minor}.%{sover_patch}
rm %{buildroot}%{_libdir}/libcircllhist.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libcircllhist.so.%{sover_major}.%{sover_minor}.%{sover_patch}

%files devel
%{_includedir}/circllhist.h
%{_libdir}/libcircllhist.so
%{_datadir}/lua
%{_datadir}/lua/5.1
%{_datadir}/lua/5.1/ffi_libcircllhist.lua

%changelog

