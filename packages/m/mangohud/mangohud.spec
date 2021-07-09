#
# spec file for package mangohud
#
# Copyright (c) 2021 SUSE LLC
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


%define imgui_ver 1.81
%define imgui_wrap 1
Name:           mangohud
Version:        0.6.5
Release:        0
Summary:        A Vulkan and OpenGL overlay for monitoring
License:        MIT
URL:            https://github.com/flightlessmango/MangoHud
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v1/projects/imgui/%{imgui_ver}/%{imgui_wrap}/get_zip#/imgui-%{imgui_ver}-%{imgui_wrap}-wrap.zip
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-mako
BuildRequires:  unzip
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
Suggests:       goverlay
Provides:       bundled(ImGui)

%description
A Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load and more.

%prep
%autosetup -n MangoHud-%{version}
%autosetup -n MangoHud-%{version} -DTa1
%autosetup -n MangoHud-%{version} -DTa2
sed -i -e '1d;2i#!/usr/bin/bash' bin/mangohud.in
sed -i 's,^@ld_libdir_mangohud@ ,/usr/\$LIB/mangohud/,' bin/mangohud.in
mkdir subprojects/imgui
mv imgui-%{imgui_ver}/* subprojects/imgui/

%build
%meson \
 -Duse_system_vulkan=enabled \
 -Dwith_wayland=enabled \
 -Dwith_xnvctrl=disabled

%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/doc/%{name}/
%{_datadir}/vulkan/implicit_layer.d/
%{_mandir}/man1/mangohud.1%{?ext_man}

%changelog
