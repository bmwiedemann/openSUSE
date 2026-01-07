#
# spec file for package miniz
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 3
%define libpackage lib%{name}%{sover}
Name:           miniz
Version:        3.1.0
Release:        0
Summary:        Single C source file zlib-replacement library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/richgel999/miniz/
Source:         https://github.com/richgel999/miniz/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Miniz is a lossless, high performance data compression library in a single
source file that implements the zlib (RFC 1950) and Deflate (RFC 1951)
compressed data format specification standards. It supports the most commonly
used functions exported by the zlib library, but is a completely independent
implementation so zlib's licensing requirements do not apply. Miniz also
contains simple to use functions for writing .PNG format image files and
reading/writing/appending .ZIP format archives.

%package -n %{libpackage}
Summary:        Single C source file zlib-replacement library
Group:          System/Libraries

%description -n %{libpackage}
Miniz is a lossless, high performance data compression library in a single
source file that implements the zlib (RFC 1950) and Deflate (RFC 1951)
compressed data format specification standards. It supports the most commonly
used functions exported by the zlib library, but is a completely independent
implementation so zlib's licensing requirements do not apply. Miniz also
contains simple to use functions for writing .PNG format image files and
reading/writing/appending .ZIP format archives.

%package devel
Summary:        Development files for libminiz
Group:          Development/Libraries/C and C++
Requires:       %{libpackage} = %{version}

%description devel
Development files for miniz, a zlib-replacement library

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libpackage}

%files -n %{libpackage}
%license LICENSE
%doc readme.md
%{_libdir}/libminiz.so.%{sover}*

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/libminiz.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
