#
# spec file for package aquamarine
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


%define sover   6
%define _description %{expand:
Aquamarine is a very light linux rendering backend library. It
provides basic abstractions for an application to render on a Wayland
session (in a window) or a native DRM session.}
Name:           aquamarine
Version:        0.7.2
Release:        0
Summary:        Rendering backend library
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/aquamarine
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(hyprwayland-scanner) >= 0.4.0
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprutils) >= 0.1.5
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.26.0
BuildRequires:  pkgconfig(libseat) >= 0.8.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description %{_description}

%package -n lib%{name}%{sover}
Summary:        Rendering backend library
Group:          System/Libraries

%description -n lib%{name}%{sover} %{_description}

%package devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}-%{release}

%description devel %{_description}

This package contains development files necessary to build against
%{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
