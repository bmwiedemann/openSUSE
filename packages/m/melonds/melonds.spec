#
# spec file for package melonds
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define __builder ninja
%define _name melonDS
Name:           melonds
Version:        1.1
Release:        0
Summary:        Nintendo DS emulator
License:        GPL-3.0-or-later
URL:            https://github.com/melonDS-emu/%{name}
Source0:        https://github.com/melonDS-emu/%{name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  execstack
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(faad2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sdl2)

%description
%{_name} aims at providing fast and accurate Nintendo DS emulation.

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i '1s|^|include_directories("%{_includedir}/wayland")\n\n|' src/frontend/qt_sdl/CMakeLists.txt

%build
export CMAKE_GENERATOR=Ninja
%cmake -LA
%cmake_build

%install
%cmake_install
execstack -c %{buildroot}/%{_bindir}/%{_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}
%{_datadir}/applications/net.kuribo64.%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/net.kuribo64.%{_name}.png

%changelog
