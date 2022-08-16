#
# spec file for package nlohmann_json
#
# Copyright (c) 2022 SUSE LLC
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
Version:        3.11.2
Release:        0
Summary:        JSON for Modern C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nlohmann.github.io/json/
Source:         https://github.com/nlohmann/json/archive/v%{version}.tar.gz#/json-%{version}.tar.gz
BuildRequires:  cmake >= 3.1
BuildRequires:  pkgconfig
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif

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
%setup -q -n json-%{version}

%build
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
%endif
%cmake \
  -DJSON_BuildTests:BOOL=OFF \
  -DJSON_MultipleHeaders=ON \
  -DNLOHMANN_JSON_CONFIG_INSTALL_DIR="%{_libdir}/cmake/nlohmann_json"
# require 2GB mem per thread
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
%{_datadir}/pkgconfig/nlohmann_json.pc
%{_includedir}/nlohmann
%dir %{_libdir}/cmake/nlohmann_json
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfigVersion.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonTargets.cmake

%changelog
