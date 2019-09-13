#
# spec file for package nlohmann_json
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.7.0
Release:        0
Summary:        C++ header-only JSON library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nlohmann.github.io/json/
#Git-Clone:     https://github.com/nlohmann/json.git
Source:         https://github.com/nlohmann/json/archive/v%{version}.tar.gz#/json-%{version}.tar.gz
BuildRequires:  cmake >= 3.1
BuildRequires:  memory-constraints
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif

%description
C++11 header-only JSON class

%package devel
Summary:        C++11 headeri-only JSON class
Group:          Development/Libraries/C and C++
Requires:       libstdc++-devel

%description devel
JSON for Modern C++, a C++11 header-only JSON library.

%prep
%setup -q -n json-%{version}

%build
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
%endif
%cmake \
  -DJSON_BuildTests:BOOL=ON \
  -DNLOHMANN_JSON_CONFIG_INSTALL_DIR="%{_libdir}/cmake/nlohmann_json"
# require 2GB mem per thread
%limit_build
%make_jobs

%install
%cmake_install

%check
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
FLAGS="`echo %{optflags} | sed -e 's/\-fstack-clash-protection//g'`"
export CFLAGS=$FLAGS
export CXXFLAGS=$FLAGS
%endif
%if 0%{?suse_version} >= 1550
%ctest --timeout 6000
%else
%ctest
%endif

%files devel
%license LICENSE.MIT
%doc README.md
%dir %{_includedir}/nlohmann
%{_includedir}/nlohmann/json.hpp
%dir %{_libdir}/cmake/nlohmann_json
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfigVersion.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonTargets.cmake

%changelog
