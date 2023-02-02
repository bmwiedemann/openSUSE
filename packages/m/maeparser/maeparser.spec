#
# spec file for package maeparser
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


%define abiver 1
Name:           maeparser
Version:        1.3.1
Release:        0
Summary:        Maestro file parser
License:        MIT
URL:            https://github.com/schrodinger/maeparser
Source:         https://github.com/schrodinger/maeparser/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_test-devel
BuildRequires:  zlib-devel

%description
maeparser is a parser for Schrödinger Maestro files.

%package -n libmaeparser%{abiver}
Summary:        The maeparser shared library

%description -n libmaeparser%{abiver}
This package contains the maeparser shared library.

%package devel
Summary:        Development files for maeparser
Requires:       libmaeparser%{abiver} = %{version}
# boost/dynamic_bitset is included in maeparser headers
Requires:       libboost_headers-devel

%description devel
This package contains the development files for maeparser.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n libmaeparser%{abiver} -p /sbin/ldconfig
%postun -n libmaeparser%{abiver} -p /sbin/ldconfig

%check
%if %{defined sle_version} && 0%{?sle_version} < 150400
export LD_LIBRARY_PATH="$PWD/build"
%endif
%ctest

%files -n libmaeparser%{abiver}
%license LICENSE.txt
%{_libdir}/libmaeparser.so.%{abiver}*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/maeparser
%{_libdir}/cmake/maeparser-config.cmake
%{_libdir}/cmake/maeparser-config-relwithdebinfo.cmake
%{_libdir}/libmaeparser.so

%changelog
