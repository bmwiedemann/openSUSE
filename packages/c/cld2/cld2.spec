#
# spec file for package cld2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cld2
Version:        20150820
Release:        0
Summary:        A library to detect the natural language of text
# https://cld2.googlecode.com/svn/trunk/
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://code.google.com/p/cld2/
Source:         %{name}-%{version}.tar.xz
# https://code.google.com/p/cld2/issues/detail?id=29
Source2:        CMakeLists.txt
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++

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
cp %{SOURCE2} .

%build
%if 0%{?suse_vesion} >= 1310
%cmake
%else
mkdir build
cd build
# FIXME: you should use %%cmake macros
cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=release \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="%{optflags}" \
	-DCMAKE_CXX_FLAGS:STRING="%{optflags} -std=c++98"
%endif
make %{?_smp_mflags}

%install
%if 0%{?suse_version} >= 1310
%cmake_install
%else
cd build
%make_install
%endif

%post -n libcld2-0 -p /sbin/ldconfig
%postun -n libcld2-0 -p /sbin/ldconfig

%files -n libcld2-0
%doc LICENSE
%{_libdir}/libcld2.so.*
%{_libdir}/libcld2_dynamic.so.*
%{_libdir}/libcld2_full.so.*

%files devel
%doc LICENSE docs/*
%{_includedir}/%{name}
%{_libdir}/libcld2.so
%{_libdir}/libcld2_dynamic.so
%{_libdir}/libcld2_full.so

%changelog
