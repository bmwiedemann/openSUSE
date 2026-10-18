#
# spec file for package simdjson
#
# Copyright (c) 2026 SUSE LLC
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

# Sync with SIMDJSON_LIB_SOVERSION in CMakeLists.txt
%define sover 33
Name:           simdjson
Version:        4.6.11
Release:        0
Summary:        Parsing gigabytes of JSON per second
License:        Apache-2.0 AND MIT
URL:            https://github.com/simdjson/simdjson
Source:         https://github.com/simdjson/simdjson/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
JSON is everywhere on the Internet. Servers spend a lot of time parsing it.
The simdjson library uses commonly available SIMD instructions and
microparallel algorithms to parse JSON 4x faster than RapidJSON and 25x
faster than JSON for Modern C++.

%package -n libsimdjson%{sover}
Summary:        Parsing gigabytes of JSON per second

%description -n libsimdjson%{sover}
JSON is everywhere on the Internet. Servers spend a lot of time parsing it.
The simdjson library uses commonly available SIMD instructions and
microparallel algorithms to parse JSON 4x faster than RapidJSON and 25x
faster than JSON for Modern C++.

%package devel
Summary:        Development files for simdjson
Requires:       libsimdjson%{sover} = %{version}

%description devel
The simdjson-devel package contains libraries and header files for
developing applications that use simdjson.

%prep
%autosetup

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
# Upstream's own suite builds only under SIMDJSON_DEVELOPER_MODE, which fetches
# test dependencies over the network (CPM) — unavailable in the build sandbox.
# Smoke-test the freshly built library instead.
cat > smoke.cc <<'EOF'
#include <cstdint>
#include <iostream>
#include "simdjson.h"
using namespace simdjson;
int main() {
  dom::parser parser;
  dom::element doc = parser.parse("[1,2,3]"_padded);
  int64_t v0 = doc.at(0);
  int64_t v2 = doc.at(2);
  if (v0 != 1 || v2 != 3) { std::cerr << "bad values" << std::endl; return 1; }
  std::cout << "smoke ok" << std::endl;
  return 0;
}
EOF
g++ %{optflags} -I singleheader smoke.cc -o smoke -L%{buildroot}%{_libdir} -lsimdjson -Wl,-rpath,%{buildroot}%{_libdir}
./smoke

%files -n libsimdjson%{sover}
%license LICENSE LICENSE-MIT
%{_libdir}/libsimdjson.so.%{sover}*

%files devel
%license LICENSE LICENSE-MIT
%doc README.md
%{_includedir}/simdjson.h
%{_libdir}/libsimdjson.so
%{_libdir}/cmake/simdjson/
%{_libdir}/pkgconfig/simdjson.pc

%ldconfig_scriptlets -n libsimdjson%{sover}

%changelog
