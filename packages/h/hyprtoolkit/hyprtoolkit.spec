#
# spec file for package hyprtoolkit
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 5
%define libname lib%{name}%{sover}
Name:           hyprtoolkit
Version:        0.5.2
Release:        0
Summary:        A C++ GUI toolkit for native Wayland applications
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprtoolkit
Source0:        https://github.com/hyprwm/hyprtoolkit/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 14
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aquamarine) >= 0.9.5
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(hyprgraphics) >= 0.5.0
BuildRequires:  pkgconfig(hyprlang) >= 0.6.0
BuildRequires:  pkgconfig(hyprutils) >= 0.9.0
BuildRequires:  pkgconfig(hyprwayland-scanner) >= 0.4.0
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
Hyprtoolkit is C++ toolkit for making Wayland GUI apps with animations.

%package -n %{libname}
Summary:        A C++ GUI toolkit for native Wayland applications
Group:          System/Libraries

%description -n %{libname}
Hyprtoolkit is a C++ toolkit for making Wayland GUI apps.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libname}
%{_libdir}/*.so.*%{sover}*

%changelog
