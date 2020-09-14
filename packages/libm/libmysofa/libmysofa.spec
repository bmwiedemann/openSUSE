#
# spec file for package libmysofa
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 1
%define __builder ninja
Name:           libmysofa
Version:        1.1
Release:        0
Summary:        Reader for AES SOFA HRTF files
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/hoene/libmysofa
Source0:        https://github.com/hoene/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  ninja
# for tests
# BuildRequires:  nodejs-common
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(zlib)

%description
This is a C library to read AES SOFA files that contain HRTFs stored
according to the AES69-2015 standard.

%package -n %{name}%{sover}
Summary:        Reader for AES SOFA HRTF files
Group:          System/Libraries

%description -n %{name}%{sover}
This is a C library to read AES SOFA files that contain HRTFs stored
according to the AES69-2015 standard.

%package devel
Summary:        Development headers and libraries for libmysofa
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
This is a C library to read AES SOFA files that contain HRTFs stored
according to the AES69-2015 standard.

This package contains the development libraries and headers for libmysofa.

%prep
%autosetup -p1

%build
%cmake -DCODE_COVERAGE=OFF
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/%{name}.a

# test suite is broken
# %%check
# %%cmake_build -C build test

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%doc README.md
%license LICENSE
%{_bindir}/mysofa2json
%{_datadir}/%{name}
%{_libdir}/%{name}.so.%{sover}*

%files devel
%{_includedir}/mysofa.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
