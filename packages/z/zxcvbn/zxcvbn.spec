#
# spec file for package zxcvbn
#
# Copyright (c) 2025 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%{!?set_build_flags:%global set_build_flags \
  CONFIG_SHELL="${CONFIG_SHELL:-/usr/bin/bash}" ; export CONFIG_SHELL ; \
  CFLAGS="${CFLAGS:-%{?build_cflags}}" ; export CFLAGS ; \
  CXXFLAGS="${CXXFLAGS:-%{?build_cxxflags}}" ; export CXXFLAGS ; \
  FFLAGS="${FFLAGS:-%{?build_fflags}}" ; export FFLAGS ; \
  FCFLAGS="${FCFLAGS:-%{?build_fflags}}" ; export FCFLAGS ; \
  LDFLAGS="${LDFLAGS:-%{?build_ldflags}}" ; export LDFLAGS
}

%define soversion 0.0.0

Name:           zxcvbn
Version:        2.5
Release:        0
Summary:        Password strength estimation library for C/C++
License:        MIT
URL:            https://github.com/tsyrogit/%{name}-c
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/tsyrogit/zxcvbn-c/commit/b9f30993c88d9057d7d95a1b059989f7853fd1b0
Patch0:         zxcvbn-gcc15.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
This is a C/C++ implementation of the zxcvbn password strength
estimation library.

%package -n lib%{name}0
Summary:        Password strength estimation library for C/C++

%description -n lib%{name}0
This is a C/C++ implementation of the zxcvbn password strength
estimation library.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}0 = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%prep
%autosetup -p1 -n %{name}-c-%{version}

%build
%set_build_flags
%make_build

%check
%make_build test

%install
# main package
install -v -s -m 0755 lib%{name}.so.%{soversion} -D -t %{buildroot}/%{_libdir}
ln -s lib%{name}.so.%{soversion} %{buildroot}/%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0 %{buildroot}/%{_libdir}/lib%{name}.so
# devel package
install -v -m 0644 %{name}.h -D -t %{buildroot}%{_includedir}

# SLE12 doed not define this macro
%if %{undefined ldconfig_scriptlets}
%post -n lib%{name}0 -p /sbin/ldconfig
%postun  -n lib%{name}0 -p /sbin/ldconfig
%else
%ldconfig_scriptlets -n lib%{name}0
%endif

%files -n lib%{name}0
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}.h

%changelog
