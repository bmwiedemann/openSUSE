#
# spec file for package libxpp
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


%define commit 8273a92

Name:           libxpp
Version:        0.2
Release:        0
Summary:        An object oriented C++ wrapper for parts of the X11 API
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/gerstner-hub/libxpp
Source0:        libxpp-%{commit}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libcosmos-devel
BuildRequires:  pkgconfig
BuildRequires:  scons

%description
This is *libxpp*, a library providing an object oriented C++ API wrapper for
parts of the X11 API. It is intended for low level programming against the X
server on Linux systems.

%package -n libxpp-0_2_0
Summary:        An object oriented C++ wrapper for parts of the X11 API
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libxpp-0_2_0
A library providing an object oriented C++ API wrapper for 37 parts of the X11
API.

The runtime library files for libxpp.

%package devel
Summary:        A library providing a modern C++ API for the Linux operating system
Group:          Development/Libraries/C and C++
Requires:       libxpp-0_2_0 = %{version}
Requires:       libstdc++-devel

%description devel
A library providing an object oriented C++ API wrapper for 37 parts of the X11
API.

Header and development files for libxpp.

%prep
%setup -q -n libxpp-%{commit}

%build
scons libtype=shared use-system-pkgs=1

%install
scons install instroot=%{buildroot}/usr use-system-pkgs=1

# the tests rely on a running X server so skip them for now
#%%check
#scons run_tests

%ldconfig_scriptlets -n libxpp-0_2_0

%files -n libxpp-0_2_0
%license LICENSE
%doc README.md
%{_libdir}/libxpp.so.*

%files devel
%{_libdir}/libxpp.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xpp/

%changelog
