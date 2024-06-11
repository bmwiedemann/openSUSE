#
# spec file for package hyprcursor
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

Name:           hyprcursor
Version:        0.1.9
Release:        0
Summary:        Library and utilities for the hyprland cursor format
License:        BSD-3-Clause
URL:            https://wiki.hyprland.org/hypr-ecosystem/hyprcursor/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprlang) >= 0.4.2
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(tomlplusplus) >= 3.4.0

%description
Utilities for the hyprland cursor format.

%package -n lib%{name}%{sover}
Summary:        Library for the hyprland cursor format
Group:          System/Libraries

%description -n lib%{name}%{sover}
Library for handling the hyprlang cursor format.

%package devel
Summary:        Development files for hyprcursor
Group:          Development/Libraries/Other
Requires:       lib%{name}%{sover} = %{version}

%description devel
Library for handling the hyprland cursor format.

This subpackage contains development files for hyprcursor.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_includedir}/

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%doc docs/MAKING_THEMES.md
%{_bindir}/%{name}-util

%files -n lib%{name}%{sover}
%license LICENSE
%doc docs/END_USERS.md
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc docs/DEVELOPERS.md
%{_includedir}/%{name}
%{_includedir}/%{name}.hpp
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
