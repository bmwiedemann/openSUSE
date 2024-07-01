#
# spec file for package pybind11_protobuf
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


%global _lto_cflags %{nil}
Name:           pybind11_protobuf
Version:        0~git20240103.3b11990
Release:        0
Summary:        Pybind11 bindings for Protocol Buffers
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11_protobuf
Source:         pybind11_protobuf-%{version}.tar.gz
# See https://github.com/pybind/pybind11_protobuf/issues/127
# PATCH-FIX-UPSTREAM
Patch0:         0001-Make-protobuf-python_api-fully-optional.patch
# PATCH-FIX-UPSTREAM
Patch1:         0002-Add-ENABLE_PYPROTO_API-option-to-CMake-build-clean-u.patch
# PATCH-FIX-UPSTREAM
Patch2:         0003-Make-the-pybind11_-_proto_caster-libraries-STATIC.patch
# PATCH-FIX-UPSTREAM
Patch3:         0004-Fix-handling-of-external-dependencies-allow-forcing-.patch
# PATCH-FIX-UPSTREAM
Patch4:         0005-Build-and-run-the-test-cases.patch
# PATCH-FIX-OPENSUSE
Patch5:         0006-Add-install-target-for-CMake-builds.patch
# PATCH-FIX-OPENSUSE
Patch6:         0007-CMake-Use-Python-Module.patch
BuildRequires:  cmake >= 3.24
BuildRequires:  fdupes
BuildRequires:  protobuf-devel
%if 0%{?sle_version} >= 150500
BuildRequires:  python311-pybind11-devel >= 2.11.1
%else
BuildRequires:  python3-pybind11-devel >= 2.11.1
%endif
BuildRequires:  cmake(absl) >= 20230125
# TESTS
%if 0%{?sle_version} >= 150500
BuildRequires:  python311-abseil
BuildRequires:  python311-protobuf
%else
BuildRequires:  python3-abseil
BuildRequires:  python3-protobuf
%endif
# TESTS

%description
These adapters make Protocol Buffer message types work with Pybind11 bindings.

%prep
%autosetup -p1

%package devel
Summary:       Development files for %name
Requires:      %{name}

%description devel
Headers and other development files for %name

%build
%cmake \
  -DUSE_SYSTEM_ABSEIL:BOOL=ON \
  -DUSE_SYSTEM_PROTOBUF:BOOL=ON \
  -DUSE_SYSTEM_PYBIND:BOOL=ON \
  %{nil}
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_libdir}

%check
%ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md

%files devel
%{_includedir}/pybind11_protobuf/
%{_libdir}/cmake/pybind11_protobuf/
%{_libdir}/lib*.a

%changelog
