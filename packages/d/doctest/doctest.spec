#
# spec file for package doctest
#
# Copyright (c) 2020 SUSE LLC
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


Name:           doctest
Version:        2.4.0
Release:        0
Summary:        Single-header testing framework
License:        MIT
URL:            http://bit.ly/doctest-docs
Source0:        https://github.com/onqtam/doctest/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
ExcludeArch:    %arm

%description
C++98/C++11 single-header testing framework for unit tests and TDD.

%package        devel
Summary:        Single-header testing framework

%description    devel
C++98/C++11 single-header testing framework for unit tests and TDD.

%prep
%autosetup
# fix cmake module path
sed -i 's|lib/cmake|%{_lib}/cmake|g' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

# creates support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/doctest.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: doctest
Description: Single-header testing framework
Version: %{version}
Libs:
Cflags: -I${includedir}/doctest
EOF

%files devel
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_includedir}/doctest
%{_libdir}/cmake/doctest
%{_libdir}/pkgconfig/doctest.pc

%changelog
