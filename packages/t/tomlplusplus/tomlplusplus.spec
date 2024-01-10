#
# spec file for package tomlplusplus
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


%bcond_without check
%define  sover  3
Name:           tomlplusplus
Version:        3.4.0
Release:        0
Summary:        TOML config file parser and serializer for C++17
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/marzer/tomlplusplus
Source0:        https://github.com/marzer/tomlplusplus/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.61.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
%if %{with check}
BuildRequires:  Catch2-2-devel
#pkgconfig(catch2)
%endif

%description
toml++ is a TOML config parser and serializer for C++.

%package -n lib%{name}%{sover}
Summary:        TOML config file parser and serializer for C++17
Group:          System/Libraries

%description -n lib%{name}%{sover}
toml++ is a TOML config parser and serializer for C++.

* Supports the TOML release v1.0.0, plus optional support for
  some unreleased TOML features
* Supports serialization to JSON and YAML
* C++17 (plus some C++20 features where available, e.g. experimental
  support for char8_t strings)
* No requirement for RTTI and exceptions

%package devel
Summary:        Development libraries and header files for %{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%if %{with check}
%check
%meson_test
%endif

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/toml++/
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%license LICENSE

%changelog
