#
# spec file for package mangohud
#
# Copyright (c) 2023 SUSE LLC
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


%define internal_ver 0.6.8
%define imgui_ver 1.81
%define imgui_wrap 1
%define vulkan_ver 1.2.158
Name:           mangohud
Version:        0.6.8
Release:        0
Summary:        A Vulkan and OpenGL overlay for monitoring
License:        MIT
URL:            https://github.com/flightlessmango/MangoHud
Source0:        %{url}/archive/v%{internal_ver}.tar.gz#/%{name}-%{internal_ver}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v1/projects/imgui/%{imgui_ver}/%{imgui_wrap}/get_zip#/imgui-%{imgui_ver}-%{imgui_wrap}-wrap.zip
Source3:        https://wrapdb.mesonbuild.com/v2/vulkan-headers_%{vulkan_ver}-2/get_patch#/vulkan-headers-%{vulkan_ver}-2-wrap.zip
Source4:        https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{vulkan_ver}.tar.gz
Source99:       baselibs.conf
BuildRequires:  AppStream
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-mako
BuildRequires:  unzip
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
Suggests:       goverlay
Provides:       bundled(ImGui)
Provides:       bundled(Vulkan-Headers-sdk)

%description
A Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load and more.

%prep
%autosetup -n MangoHud-%{version} -p1
%autosetup -n MangoHud-%{version} -DTa1
%autosetup -n MangoHud-%{version} -DTa2
%autosetup -n MangoHud-%{version} -DTa3
%autosetup -n MangoHud-%{version} -DTa4
sed -i -e '1d;2i#!%{_bindir}/bash' bin/mangohud.in
sed -i 's,^@ld_libdir_mangohud@ ,%{_prefix}/\$LIB/mangohud/,' bin/mangohud.in
mv imgui-%{imgui_ver} subprojects/
mv Vulkan-Headers-%{vulkan_ver} subprojects/
sed -i 's/0.60.0/0.59/g' meson.build

# Fix building with GCC 13 -- Workaround until the next release where the fix will be included
sed -i -e '1i#include <cstdint>' src/control.cpp
sed -i -e '1i#include <cstdint>' src/font.cpp
sed -i -e '1i#include <cstdint>' src/keybinds.cpp
sed -i -e '1i#include <cstdint>' src/overlay_params.cpp

%build
%meson \
 -Dwith_wayland=enabled \
 -Dwith_xnvctrl=disabled \
 -Duse_system_spdlog=enabled

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
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/metainfo/*.metainfo.xml

%changelog
