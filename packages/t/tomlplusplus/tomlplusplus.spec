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
Version:        3.5.1
Release:        0
Summary:        TOML config file parser and serializer for C++17
License:        MIT
URL:            https://github.com/marzer/tomlplusplus
Source0:        https://github.com/marzer/tomlplusplus/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.61.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
%if %{with check}
BuildRequires:  pkgconfig(catch2) >= 3.0.0
%endif

%description
toml++ is a TOML config parser and serializer for C++.

%package examples
Summary:        Example programs for %{name}

%description examples
This package contains example programs built with %{name}. They
demonstrate parsing TOML documents, reporting parse errors,
generating and merging TOML data, and converting TOML to JSON.

%package -n lib%{name}%{sover}
Summary:        TOML config file parser and serializer for C++17

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
Requires:       lib%{name}%{sover} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -C -p1

%conf
%meson \
  -Dbuild_examples=true \
  -Dbuild_lib=true \
%if %{with check}
  -Dbuild_tests=true \
%endif

%build
%meson_build

%install
%meson_install
for example in error_printer simple_parser toml_generator toml_merger toml_to_json_transcoder; do
  mv %{buildroot}%{_bindir}/$example %{buildroot}%{_bindir}/toml++_$example
done

%if %{with check}
%check
%meson_test
%endif

%ldconfig_scriptlets -n lib%{name}%{sover}

%files examples
%{_bindir}/toml++_*

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
