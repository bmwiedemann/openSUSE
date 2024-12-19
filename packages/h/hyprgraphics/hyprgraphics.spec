#
# spec file for package hyprgraphics
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

Name:           hyprgraphics
Version:        0.1.1
Release:        0
Summary:        Hyprland graphics / resource utilities
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprgraphics
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_cms)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pixman-1)

%define _description %{expand:
Hyprgraphics is a small C++ library with graphics / resource related
utilities used across the hypr* ecosystem.}

%description %{_description}

%package -n lib%{name}%{sover}
Summary:        Hyprland graphics / resource utilities
Group:          System/Libraries

%description -n lib%{name}%{sover} %{_description}

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel %{_description}

This subpackage contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%{_libdir}/libhyprgraphics.so.%{sover}
%{_libdir}/libhyprgraphics.so.%{version}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
