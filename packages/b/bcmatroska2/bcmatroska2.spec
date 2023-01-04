#
# spec file for package bcmatroska2
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


%define sover   0
Name:           bcmatroska2
Version:        5.2.1
Release:        0
Summary:        C Library to Deal with Matroska Files
License:        BSD-3-Clause AND Zlib AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://gitlab.linphone.org/BC/public/bcmatroska2
Source:         https://gitlab.linphone.org/BC/public/bcmatroska2/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         bcmatroska2-include-subdir.patch
Patch1:         fix-cmakelist-version.patch
Patch2:         remove-file.patch
Patch3:         fix-libmatroska-cmake.patch
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  pkgconfig(bctoolbox) >= 5.2.0

%description
Bcmatroska2 is a C library to parse Matroska files (.mkv and .mka).

%package -n lib%{name}-%{sover}
Summary:        C Library to Deal with Matroska Files
Group:          Development/Libraries/C and C++

%description -n lib%{name}-%{sover}
Bcmatroska2 is a C library to parse Matroska files (.mkv and .mka).

%package devel
Summary:        Development files for bcmatroska2
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{sover} = %{version}
# Needed by mediastreamer2. This is a fake minor version because upstream didn't release
# a '.1', therefore we've gotta use this workaround.
Provides:       %{name}-devel = 5.2.1

%description devel
This package includes the files necessary for compiling and linking
applications which will use libbcmatroska2.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

chrpath -d %{buildroot}%{_libdir}/lib%{name}.so.%{sover}*

%post -n lib%{name}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-%{sover} -p /sbin/ldconfig

%files -n lib%{name}-%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/corec
%dir %{_includedir}/%{name}/ebml
%dir %{_includedir}/%{name}/matroska
%{_includedir}/%{name}/corec/*
%{_includedir}/%{name}/ebml/*
%{_includedir}/%{name}/matroska/*
%{_libdir}/libbcmatroska2.so
%dir %{_datadir}/bcmatroska2
%dir %{_datadir}/bcmatroska2/cmake
%{_datadir}/bcmatroska2/cmake/*

%changelog
