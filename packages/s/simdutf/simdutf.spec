#
# spec file for package simdutf
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define lib_ver 24.0.0
%define so_ver 24
Name:       simdutf
Version:    7.2.1
Release:    0
Summary:    Unicode validation and transcoding at billions of characters per second

License:    Apache-2.0 AND BSD-3-Clause
URL:        https://github.com/simdutf/simdutf
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  c++_compiler

%description
Unicode (UTF8, UTF16, UTF32) validation and transcoding at billions of 
characters per second using SSE2, AVX2, NEON, AVX-512.

%package -n lib%{name}%so_ver
Summary: Shared libraries for %{name}

%description -n lib%{name}%so_ver
The package contains shared libraries.

%package devel
Summary: Development files for %{name}
Requires: lib%{name}%so_ver = %{version}

%description devel
The package contains libraries and header files for developing applications
that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DSIMDUTF_BENCHMARKS=OFF \
	-DSIMDUTF_TOOLS=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%so_ver

%check
%ctest

%files -n lib%{name}%so_ver
%license LICENSE-APACHE
%doc AUTHORS README.md
%{_libdir}/lib%{name}.so.%{lib_ver}
%{_libdir}/lib%{name}.so.%{so_ver}

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
