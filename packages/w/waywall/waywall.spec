#
# spec file for package waywall
#
# Copyright (c) 2026 SUSE LLC
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

%global __provides_exclude_from ^%{_libdir}/waywall-glfw/.*$
Name:           waywall
Version:        0.2026.06.13
Release:        0
Summary:        Wayland compositor for Minecraft speedrunning
License:        GPL-3.0-only AND Zlib
Group:          Amusements/Games/Other
URL:            https://github.com/tesselslate/waywall
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/glfw/glfw/archive/refs/tags/3.4.tar.gz#/glfw-3.4.tar.gz
Source2:        README.SUSE
BuildRequires:  meson >= 1.3.0
BuildRequires:  ninja
BuildRequires:  c_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(spng)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(xkbcommon)
# only in waywall meson.build:
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

# glfw specific
BuildRequires:  cmake
# for x11 support (not needed with -DGLFW_BUILD_X11=OFF)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xi)
# only in waywall RPM build script, check if needed
BuildRequires:  pkgconfig(x11)

# Runtime dependencies:
Requires:       xwayland

# waywall is a Minecraft desktop gaming tool, only 64-bit PC and ARM make sense
ExclusiveArch:  x86_64 aarch64

%description
Waywall is a Wayland compositor that provides various convenient features for Minecraft speedrunning.

%prep
%autosetup -a1
cp %{SOURCE2} .

# apply waywall patch to GLFW
cd glfw-3.4
patch -p1 < ../contrib/glfw.patch
cd -


%build
# build waywall
%meson
%meson_build

# build patched GLFW (create .so with wayland support)
cd glfw-3.4
%cmake -DBUILD_SHARED_LIBS=ON -DGLFW_BUILD_WAYLAND=ON
%cmake_build

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/waywall/waywall %{buildroot}%{_bindir}/waywall

install -d -m 0755 %{buildroot}%{_libdir}/waywall-glfw
# cp -a to preserve symlinks
cp -a glfw-3.4/build/src/libglfw.so.3* %{buildroot}%{_libdir}/waywall-glfw/


%check
%meson_test


%post
echo "======================================================================="
cat %{_defaultdocdir}/%{name}/README.SUSE
echo "======================================================================="


%files
%license LICENSE
%doc README.md README.SUSE
%{_bindir}/waywall

%license glfw-3.4/LICENSE.md
%dir %{_libdir}/waywall-glfw
%{_libdir}/waywall-glfw/libglfw.so*

%changelog
