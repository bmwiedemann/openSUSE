#
# spec file for package hyprutils
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Florian "sp1rit" <sp1rit@disroot.org>
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


%define sover 0

Name:           hyprutils
Version:        0.1.5
Release:        0
Summary:        Utilities used across the Hypr* ecosystem
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprutils
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 9
BuildRequires:  pkgconfig(pixman-1)

%package -n lib%{name}%{sover}
Summary:        Library for the hyprland cursor format
Group:          System/Libraries

%package devel
Summary:        Development files for hyprcursor
Group:          Development/Libraries/Other
Requires:       lib%{name}%{sover} = %{version}

%define _description %{expand:
Hyprutils is a small C++ library for utilities used across the Hypr*
ecosystem.}

%description %{_description}

%description -n lib%{name}%{sover} %{_description}

%description devel %{_description}

This subpackage contains development files for hyprcursor.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
