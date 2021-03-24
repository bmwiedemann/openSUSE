#
# spec file for package cld2
#
# Copyright (c) 2021 SUSE LLC
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


%{?!cmake_build:%global cmake_build() make %{?_smp_mflags} VERBOSE=1}

Name:           cld2
Version:        20150820
Release:        0
Summary:        A library to detect the natural language of text
# https://github.com/CLD2Owners/cld2
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/CLD2Owners/cld2
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 0001-fix-hebrew-iso-code.patch buschmann23@opensuse.org -- use correct ISO 639-1 language code for Hebrew
Patch1:         0001-fix-hebrew-iso-code.patch
# https://code.google.com/p/cld2/issues/detail?id=29
Source2:        CMakeLists.txt
Source3:        cld2.pc.in
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
A library that detects over 80 languages in UTF-8 text, based largely
on groups of four letters. Also tables for 160+ language versions.

%package -n libcld2-0
Summary:        A library to detect the natural language of text
Group:          System/Libraries

%description -n libcld2-0
A library that detects over 80 languages in UTF-8 text, based largely
on groups of four letters. Also tables for 160+ language versions.

%package devel
Summary:        Development files for cld2
Group:          Development/Libraries/C and C++
Requires:       libcld2-0 = %{version}

%description devel
A library that detects over 80 languages in UTF-8 text, based largely
on groups of four letters. Also tables for 160+ language versions.

This subpackage contains the headers for cld2.

%prep
%setup -q
%patch1 -p1
cp %{SOURCE2} .
cp %{SOURCE3} .

%build
export CXXFLAGS="%{optflags} -std=c++98"
%cmake
%cmake_build

%install
%cmake_install

%post -n libcld2-0 -p /sbin/ldconfig
%postun -n libcld2-0 -p /sbin/ldconfig

%files -n libcld2-0
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%{_libdir}/libcld2.so.*
%{_libdir}/libcld2_dynamic.so.*
%{_libdir}/libcld2_full.so.*

%files devel
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%doc docs/*
%{_includedir}/%{name}
%{_libdir}/libcld2.so
%{_libdir}/libcld2_dynamic.so
%{_libdir}/libcld2_full.so
%{_libdir}/pkgconfig/cld2.pc

%changelog
