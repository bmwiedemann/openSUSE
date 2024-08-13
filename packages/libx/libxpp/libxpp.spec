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


%define version 0.3.1

Name:           libxpp
Version:        %{version}
Release:        0
Summary:        An object oriented C++ wrapper for parts of the X11 API
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/gerstner-hub/libxpp
Source0:        libxpp-v0.3.1.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libcosmos-devel
BuildRequires:  pkgconfig
BuildRequires:  scons

%description
This is *libxpp*, a library providing an object oriented C++ API wrapper for
parts of the X11 API. It is intended for low level programming against the X
server on Linux systems.

%package -n libxpp-3
Summary:        An object oriented C++ wrapper for parts of the X11 API
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
# renamed from broken package name that didn't follow SONAME
Provides:       libxpp-0_2_0 = %{version}
Obsoletes:      libxpp-0_2_0 < %{version}

%description -n libxpp-3
A library providing an object oriented C++ API wrapper for parts of the X11
API.

The runtime library files for libxpp.

%package devel
Summary:        A library providing a modern C++ API for the Linux operating system
Group:          Development/Libraries/C and C++
Requires:       libstdc++-devel
Requires:       libxpp-3 = %{version}

%description devel
A library providing an object oriented C++ API wrapper for parts of the X11
API.

Header and development files for libxpp.

%prep
%setup -q -n %{name}-v%{version}

%build
scons libtype=shared use-system-pkgs=1

%install
scons install instroot=%{buildroot}/usr use-system-pkgs=1

# the tests rely on a running X server so skip them for now
#%%check
#scons run_tests

%ldconfig_scriptlets -n libxpp-3

%files -n libxpp-3
%license LICENSE
%doc README.md
%{_libdir}/libxpp.so.*

%files devel
%{_libdir}/libxpp.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xpp/

%changelog
