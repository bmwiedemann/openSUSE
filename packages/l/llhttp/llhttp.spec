#
# spec file for package llhttp
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define library_version 9.3.1
%define library_soversion 9.3
%define library_sosuffix 9_3
Name:           llhttp
Version:        9.3.1
Release:        0
Summary:        Port of http_parser to llparse
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/nodejs/llhttp
Source0:        %{url}/archive/refs/tags/release/v%{version}/llhttp-release-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
llhttp is a port of http_parser to llparse. It's written in TypeScript
and transpiled into C code. This package is based on the transpiled
C code available upstream.

%package -n lib%{name}%{library_sosuffix}
Summary:        Shared library files for llhttp library
Group:          System/Libraries

%description -n lib%{name}%{library_sosuffix}
Port of http_parser to llparse

This package contains the dynamically linked library.

%package devel
Summary:        Development files for llhttp library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_sosuffix} = %{version}

%description devel
Port of http_parser to llparse

This package contains the development files.

%prep
%autosetup -p1 -n llhttp-release-v%{version}

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%make_jobs

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%{library_sosuffix}

%files -n lib%{name}%{library_sosuffix}
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{library_soversion}
%{_libdir}/lib%{name}.so.%{library_version}

%files devel
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/llhttp.h

%changelog
