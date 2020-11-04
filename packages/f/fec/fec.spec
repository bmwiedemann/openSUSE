#
# spec file for package fec
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   3
Name:           fec
Version:        3.0.0+git.20160910
Release:        0
Summary:        Library with several forward error correction (FEC) functions
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            https://github.com/Opendigitalradio/ka9q-fec
Source:         %{name}-%{version}.tar.xz
Patch0:         fec-fix-cmake-libdir.patch
Patch1:         fec-fix-cmake-pkgconfig-whitespace.patch
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkg-config

%description
A library that provides a set of functions that implement several
popular forward error correction (FEC) algorithms and several low-level routines
useful in modems implemented with digital signal processing (DSP).

%package -n libfec%{sover}
Summary:        Library with several forward error correction (FEC) functions
Group:          System/Libraries

%description -n libfec%{sover}
A library that provides a set of functions that implement several
popular forward error correction (FEC) algorithms and several low-level routines
useful in modems implemented with digital signal processing (DSP).

%package devel
Summary:        Development files for the libfec library
Group:          Development/Libraries/C and C++
Requires:       libfec%{sover} = %{version}

%description devel
A library that provides a set of functions that implement several
popular forward error correction (FEC) algorithms and several low-level routines
useful in modems implemented with digital signal processing (DSP).

This subpackage contains libraries and header files for developing
applications that want to make use of libfec.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake
%make_jobs

%install
%cmake_install

%post   -n libfec%{sover} -p /sbin/ldconfig
%postun -n libfec%{sover} -p /sbin/ldconfig

%files -n libfec%{sover}
%doc LICENSE README README.x86-64
%{_libdir}/libfec.so.%{sover}

%files devel
%{_includedir}/fec.h
%{_libdir}/libfec.so
%{_libdir}/pkgconfig/libfec.pc

%changelog
