#
# spec file for package Bear
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with     tests
Name:           Bear
Version:        3.1.4
Release:        0
Summary:        Tool to generate compilation database for clang tooling
License:        GPL-3.0-or-later
URL:            https://github.com/rizsotto/Bear
Source:         %{URL}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(nlohmann_json) >= 3.7.3
BuildRequires:  pkgconfig(absl_synchronization)
BuildRequires:  pkgconfig(fmt) >= 6.1
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(grpc++) >= 1.26
BuildRequires:  pkgconfig(protobuf) >= 3.11
BuildRequires:  pkgconfig(spdlog)
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
%if %{with tests}
BuildRequires:  fakeroot
# the fakeroot test requires xargs
BuildRequires:  findutils
# additional binaries for specific tests
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-fortran
%else
BuildRequires:  gcc-fortran
%endif
BuildRequires:  python3-lit
BuildRequires:  python3-setuptools
# one of the tests requires /usr/bin/more
BuildRequires:  util-linux
BuildRequires:  valgrind
BuildRequires:  pkgconfig(gmock) >= 1.10
BuildRequires:  pkgconfig(gtest) >= 1.10
BuildRequires:  pkgconfig(gtest_main) >= 1.10
%endif

%description
Bear is a tool to generate compilation database for clang tooling.

One way to get compilation database is to use cmake as build tool. When the
project compiles with no cmake, but another build system, there is no free json
file. Bear is a tool to generate such file during the build process.

%prep
%autosetup -p1

%build
for f in $(ls test/bin/); do
    sed -i "s|^#\!%{_bindir}/env\s\+python\s\?$|#!python3|" test/bin/$f
done
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
export CC=gcc-13
export CXX=g++-13
%endif
%cmake \
%if %{without tests}
  -DENABLE_UNIT_TESTS=OFF \
  -DENABLE_FUNC_TESTS=OFF
%else
  -DENABLE_UNIT_TESTS=ON \
  -DENABLE_FUNC_TESTS=ON
%endif
%cmake_build

%install
%cmake_install
# Let RPM install it correctly
rm -rf %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc README.md
%{_bindir}/bear
%{_mandir}/man1/bear.1%{?ext_man}
%{_mandir}/man1/bear-citnames.1%{?ext_man}
%{_mandir}/man1/bear-intercept.1%{?ext_man}
%{_libdir}/bear/

%changelog
