#
# spec file for package bstring
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


%define sover 1
%define libname libbstring%{sover}
Name:           bstring
Version:        1.1.1
Release:        0
Summary:        C library for a length-tracked string data type
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/msteinert/bstring
Source:         https://github.com/msteinert/bstring/releases/download/v%{version}/bstring-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(check)

%description
The Better String Library is an abstraction of a string data type for
use with C. Similar to the C++ std::string type, bstring tracks
string length and allocations, so the developer does not have to,
which makes operations like concatenation less error-prone.

%package -n %{libname}
Summary:        C library for a length-tracked string data type
Group:          System/Libraries

%description -n %{libname}
The Better String Library is an abstraction of a string data type for
use with C. Similar to the C++ std::string type, bstring tracks
string length and allocations, so the developer does not have to,
which makes operations like concatenation less error-prone.

This package contains M. Steinert's version of bstring where the C++
wrapper of the original implementation from P. Hsieh was removed.

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description    devel
Development files for Paul Hsieh's Better String Library.

%prep
%autosetup -p1

%build
%meson \
  -Denable-tests=true
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%{_libdir}/libbstring.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/bstraux.h
%{_includedir}/bstrlib.h
%{_includedir}/buniutil.h
%{_includedir}/utf8util.h
%{_libdir}/libbstring.so
%{_libdir}/pkgconfig/bstring.pc

%changelog
