#
# spec file for package hyprlang
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


%define sover 2

Name:           hyprlang
Version:        0.5.2
License:        LGPL-3.0-only
Release:        0
Summary:        A configuration language for Linux applications
URL:            https://github.com/hyprwm/hyprlang
Source0:        https://github.com/hyprwm/hyprlang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
The hypr configuration language is a configuration language for Linux
applications.

%package -n     lib%{name}%{sover}
Summary:        Library for Hypr, a config language
Group:          System/Libraries

%description -n lib%{name}%{sover}
The hypr configuration language is a configuration language for Linux
applications.

%package devel
Summary:        Development files for Hyprlang
Group:          Development/Libraries/Other
Requires:       lib%{name}%{sover} = %{version}

%description devel
The hypr configuration language is a configuration language for Linux
applications.

This subpackeg contains headers for hyprlang.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files devel
%doc README.md
%{_includedir}/%{name}.hpp
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%changelog
