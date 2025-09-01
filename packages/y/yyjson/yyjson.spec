#
# spec file for package yyjson
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


%define         sover 0
Name:           yyjson
Version:        0.12.0
Release:        0
Summary:        A JSON library in C
License:        MIT
URL:            https://github.com/ibireme/yyjson
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-includedir.patch
BuildRequires:  cmake
BuildRequires:  c++_compiler
BuildRequires:  doxygen

%description
A JSON library compliant with the RFC 8259 JSON standard.

%package devel
Summary:        Headers for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description devel
A JSON library compliant with the RFC 8259 JSON standard.
This subpackage provides the headers for building with yyjson.

%package -n lib%{name}%{sover}
Summary:        A JSON library in C

%description -n lib%{name}%{sover}
A JSON library compliant with the RFC 8259 JSON standard. It enforces
strict number formats and UTF-8 validation. It offers options to
enable individual JSON5 features and custom allocators. It supports
querying and modifying with JSON Pointer (RFC 6901), JSON Patch
(6902), and JSON Merge Patch (7386). It also supports \u0000
characters and non-NUL-terminated strings.

An array or object is not stored using random-access memory, which
makes accessing elements by index or key slower than using an
iterator.

%prep
%autosetup -p1

%build
%cmake \
  -DYYJSON_BUILD_MISC=ON \
  -DYYJSON_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n lib%{name}%{sover}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%changelog
