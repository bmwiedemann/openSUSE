#
# spec file for package gamescope
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


%bcond_without  intree_libs
Name:           gamescope
Version:        3.14.18
Release:        0
Summary:        Micro-compositor optimized for running video games on Wayland
License:        BSD-2-Clause
Group:          Amusements/Games/Other
URL:            https://github.com/Plagman/gamescope
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  stb-devel
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xmu)
# for xxd
BuildRequires:  vim
%if %{without intree_libs}
BuildRequires:  (pkgconfig(libliftoff) >= 0.4.0 with pkgconfig(libliftoff) < 0.5.0)
BuildRequires:  (pkgconfig(wlroots) >= 0.17.0   with pkgconfig(wlroots) < 0.18.0)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(openvr)
%endif
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.113
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(xxf86vm)
%if %{with intree_libs}
# from wlroots.spec
BuildRequires:  glslang-devel
BuildRequires:  xorg-x11-server-wayland
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.21
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
#/from wlroots.spec
%endif

%description
%{name} is a micro-compositor optimized for running video games on Wayland

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1599
sed -i "s|dependency('stb')|declare_dependency(include_directories: include_directories('/usr/include/stb'))|g" src/meson.build
%endif
sed -i "s|#include <libei-1.0/libeis.h>|#include <libeis.h>|g" src/InputEmulation.cpp
%meson \
  -Dpipewire=enabled \
%{nil}

%meson_build

%install
%meson_install --skip-subprojects

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}stream
%{_libdir}/libVkLayer_FROG_gamescope_wsi_%{_arch}.so
%dir %{_datadir}/vulkan/implicit_layer.d/
%{_datadir}/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.%{_arch}.json

%changelog
