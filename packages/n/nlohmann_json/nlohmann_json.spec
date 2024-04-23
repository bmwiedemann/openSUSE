#
# spec file for package nlohmann_json
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           nlohmann_json
Version:        3.11.3
Release:        0
Summary:        JSON for Modern C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nlohmann.github.io/json/
Source:         https://github.com/nlohmann/json/releases/download/v%{version}/json.tar.xz#/json-%{version}.tar.xz
Source2:        https://github.com/nlohmann/json/releases/download/v%{version}/json.tar.xz.asc#/json-%{version}.tar.xz.asc
Source3:        https://keybase.io/nlohmann/pgp_keys.asc?fingerprint=797167ae41c0a6d9232e48457f3cea63ae251b69#/%{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.1
BuildRequires:  pkgconfig

%description
C++11 header-only JSON class

%package devel
Summary:        JSON for Modern C++
Group:          Development/Libraries/C and C++
Requires:       libstdc++-devel

%description devel
Development files for a header-only library
to make JSON a first-class datatype for C++11

%prep
%autosetup -p1 -n json

%build
%cmake \
  -DJSON_BuildTests:BOOL=OFF \
  -DJSON_MultipleHeaders=ON \
  -DNLOHMANN_JSON_CONFIG_INSTALL_DIR="%{_libdir}/cmake/nlohmann_json"
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.MIT
%{_datadir}/pkgconfig/nlohmann_json.pc
%{_includedir}/nlohmann
%dir %{_libdir}/cmake/nlohmann_json
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfigVersion.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonTargets.cmake

%changelog
