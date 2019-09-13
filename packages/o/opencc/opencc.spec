#
# spec file for package opencc
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


Name:           opencc
Version:        1.0.5
Release:        0
Summary:        Open Chinese Convert
License:        Apache-2.0
Group:          System/I18n/Chinese
Url:            https://github.com/BYVoid/OpenCC
Source:         https://github.com/BYVoid/OpenCC/archive/ver.1.0.5/OpenCC-ver.1.0.5.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# needed to generate some docu files
BuildRequires:  python3-base

%description
OpenCC is an opensource project for conversion between Traditional
Chinese and Simplified Chinese, which supports phrase-level conversion
and regional idioms among Mainland China, Taiwan and Hong kong.

%package -n libopencc2
Summary:        Open Chinese Convert
Group:          System/Libraries
Requires:       %{name}-data

%description -n libopencc2
OpenCC is an opensource project for conversion between Traditional
Chinese and Simplified Chinese, which supports phrase-level conversion
and regional idioms among Mainland China, Taiwan and Hong kong.

This package provides shared libraries of OpenCC.

%package data
Summary:        Dictionaries for Open Chinese Convert
Group:          System/I18n/Chinese

%description data
OpenCC is an opensource project for conversion between Traditional
Chinese and Simplified Chinese, which supports phrase-level conversion
and regional idioms among Mainland China, Taiwan and Hong kong.

This package provides dictionaries and patterns used by libraries/
binaries of OpenCC.

%package devel
Summary:        Open Chinese Convert
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
OpenCC is an opensource project for conversion between Traditional
Chinese and Simplified Chinese, which supports phrase-level conversion
and regional idioms among Mainland China, Taiwan and Hong kong.

This package provides development headers for OpenCC.

%prep
%setup -q -n OpenCC-ver.%{version}
# call python3 with path
sed -i \
    -e 's:BIN python:BIN /usr/bin/python3:g' \
    data/CMakeLists.txt

%build
%cmake \
  -DCMAKE_SKIP_RPATH=OFF
%make_jobs

%install
%cmake_install
find %{buildroot} -name "*.a" -delete -print

%post -n libopencc2 -p /sbin/ldconfig
%postun -n libopencc2 -p /sbin/ldconfig

%files
%doc AUTHORS NEWS.md LICENSE README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_dict
%{_bindir}/%{name}_phrase_extract

%files data
%{_datadir}/%{name}/

%files -n libopencc2
%{_libdir}/libopencc.so.2
%{_libdir}/libopencc.so.1.0.0

%files devel
%{_includedir}/%{name}/
%{_libdir}/libopencc.so
%{_libdir}/pkgconfig/opencc.pc

%changelog
