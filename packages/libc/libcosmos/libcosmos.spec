#
# spec file for package libcosmos
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


%define version 0.4.0

Name:           libcosmos
Version:        %{version}
Release:        0
Summary:        A library providing a modern C++ API for the Linux operating system
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/gerstner-hub/libcosmos
Source0:        libcosmos-v%{version}.tar.xz
# PATCH-FIX-UPSTREAM - https://github.com/gerstner-hub/libcosmos/commit/54b144
Patch0:         libcosmos-fix-aarch64.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scons

%description
This is libcosmos, a library providing a modern C++ API for the Linux
operating system. It is intended for low level systems programming on Linux,
while relying on a strong C++ type model for robustness and expressiveness.

%package -n libcosmos-4
Summary:        A library providing a modern C++ API for the Linux operating system
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libcosmos-4
A library providing a modern C++ API for the Linux operating system.

The runtime library files for libcosmos.

%package devel
Summary:        A library providing a modern C++ API for the Linux operating system
Group:          Development/Libraries/C and C++
Requires:       libcosmos-4 = %{version}
Requires:       libstdc++-devel

%description devel
A library providing a modern C++ API for the Linux operating system.

Header and development files for libcosmos.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
scons libtype=shared

%install
scons install instroot=%{buildroot}/usr

# some of the tests rely on networking so skip them for now
#%%check
#scons run_tests

%ldconfig_scriptlets -n libcosmos-4

%files -n libcosmos-4
%license LICENSE
%doc README.md
%{_libdir}/libcosmos.so.*

%files devel
%{_libdir}/libcosmos.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cosmos/

%changelog
