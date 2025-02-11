#
# spec file for package mangohud
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


%define internal_ver %{version}
%define imgui_ver 1.89.9
%define imgui_wrap 1
%define implot_ver 0.16
%define vulkan_ver 1.2.158
Name:           mangohud
Version:        0.8.0
Release:        0
Summary:        A Vulkan and OpenGL overlay for monitoring
License:        MIT
URL:            https://github.com/flightlessmango/MangoHud
Source0:        %{url}/archive/v%{internal_ver}.tar.gz#/%{name}-%{internal_ver}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v2/imgui_%{imgui_ver}-%{imgui_wrap}/get_patch#/imgui-%{imgui_ver}-%{imgui_wrap}-wrap.zip
Source3:        https://wrapdb.mesonbuild.com/v2/vulkan-headers_%{vulkan_ver}-2/get_patch#/vulkan-headers-%{vulkan_ver}-2-wrap.zip
Source4:        https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{vulkan_ver}.tar.gz#/vulkan-headers-%{vulkan_ver}.tar.gz
Source5:        https://github.com/epezent/implot/archive/refs/tags/v%{implot_ver}.zip#/implot-%{implot_ver}.tar.gz
Source6:        https://wrapdb.mesonbuild.com/v2/implot_%{implot_ver}-1/get_patch#/implot-%{implot_ver}-1-wrap.zip
Source99:       baselibs.conf
BuildRequires:  AppStream
%if 0%{?suse_version} < 1550 && 0%{?sle_version} >= 150500
BuildRequires:  gcc12-c++
%endif
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-mako
BuildRequires:  unzip
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
Suggests:       goverlay
Provides:       bundled(ImGui)
Provides:       bundled(Vulkan-Headers-sdk)

%description
A Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load and more.

%package -n mangoapp
Summary:        A transparent background application with a built-in MangoHud for gamescope
Group:          Games
Requires:       %{name}

%description -n mangoapp
A transparent background OpenGL application with a built-in MangoHud designed to be run inside a gamescope instance.

%package -n mangoplot
Summary:        Local visualization
Group:          Games
Requires:       %{name}
BuildArch:      noarch

%description -n mangoplot
mangoplot is a plotting script that is shipped with MangoHud: on a given folder,
it takes each log file, makes a 1D heatmap of its framerates,
then stacks the heats maps vertically to form a 2D graph for
easy visual comparison between benchmarks.

%prep
%autosetup -n MangoHud-%{internal_ver} -p1
%setup -n MangoHud-%{internal_ver} -DTa1
%setup -n MangoHud-%{internal_ver} -DTa2
%setup -n MangoHud-%{internal_ver} -DTa3
%setup -n MangoHud-%{internal_ver} -DTa4
%setup -n MangoHud-%{internal_ver} -DTa5
%setup -n MangoHud-%{internal_ver} -DTa6
sed -i -e '1d;2i#!%{_bindir}/bash' bin/mangohud.in
sed -i 's,^@ld_libdir_mangohud@ ,%{_prefix}/\$LIB/mangohud/,' bin/mangohud.in
sed -i 's|@ld_libdir_mangohud_abs@|%{_prefix}/\$LIB/mangohud|g' src/mangohud.json.in
mv imgui-%{imgui_ver} subprojects/
mv implot-%{implot_ver} subprojects/
mv Vulkan-Headers-%{vulkan_ver} subprojects/
sed -i 's/0.60.0/0.59/g' meson.build

# Fix tests building with GCC 13
sed -i -e '1i#include <cstdint>' tests/test_amdgpu.cpp

# Force system cmocka instead of bundled cmocka
sed -i "s/  cmocka = subproject('cmocka')//g" meson.build
sed -i "s/cmocka_dep = cmocka.get_variable('cmocka_dep')/cmocka_dep = dependency('cmocka')/g" meson.build

%build
%if 0%{?suse_version} < 1550 && 0%{?sle_version} >= 150500
export CC=gcc-12
export CXX=g++-12
%endif
%meson \
    -Dinclude_doc=true \
    -Duse_system_spdlog=enabled \
    -Dwith_wayland=enabled \
    -Dwith_xnvctrl=disabled \
    -Dtests=enabled \
    -Dmangoapp=true \
    -Dmangohudctl=true
    %{nil}
%meson_build

%install
%meson_install
sed -i "s@#!/usr/bin/env python@#!/usr/bin/python3@" %{buildroot}%{_bindir}/mangoplot

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_libdir}/%{name}/
%{_datadir}/doc/%{name}/
%{_datadir}/vulkan/implicit_layer.d/
%{_mandir}/man1/mangohud.1%{?ext_man}
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/metainfo/*.metainfo.xml

%files -n mangoapp
%{_bindir}/mangoapp
%{_mandir}/man1/mangoapp.1%{?ext_man}

%files -n mangoplot
%{_bindir}/mangoplot

%changelog
