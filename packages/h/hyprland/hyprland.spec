#
# spec file for package hyprland
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2022-24 Florian "sp1rit" <packaging@sp1rit.anonaddy.me>
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


%bcond_without devel

Name:           hyprland
Version:        0.38.1
Release:        0
Summary:        Dynamic tiling Wayland compositor
License:        BSD-3-Clause
URL:            https://hyprland.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 11
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  jq
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprcursor)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.118
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libseat) >= 0.2.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.26
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
%if 0%{?suse_version}
BuildRequires:  Mesa-libGLESv3-devel
%bcond_without  xcb_errors
%else
%bcond_with  xcb_errors
%endif
%if %{with xcb_errors}
BuildRequires:  pkgconfig(xcb-errors)
%endif
Recommends:     %{name}-wallpapers
%if %{with devel}
Suggests:       %{name}-devel
%endif

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots
that doesn't sacrifice on its looks.

It supports multiple layouts, fancy effects, has a very flexible IPC
model allowing for a lot of customization, and more.

%package wallpapers
Summary:        Hyprland wallpapers
BuildArch:      noarch

%description wallpapers
Additional wallpapers for hyprland.

%if %{with devel}
%package devel
Summary:        Files required to build Hyprland plugins
Requires:       %{name}
BuildArch:      noarch

%description devel
This package contains the neccessary files that are required to
build plugins for hyprland.
%endif

%prep
%autosetup -p1

%build
%meson \
	 -Dwlroots:xcb-errors=%{?with_xcb_errors:enabled}%{!?with_xcb_errors:disabled}
%meson_build

%install
%meson_install --tags runtime,man%{?with_devel:,devel}
%if %{with devel}
rm %{buildroot}/%{_libdir}/libwlroots.a %{buildroot}/%{_libdir}/pkgconfig/wlroots.pc
rm -rf %{buildroot}/%{_includedir}/wlr/
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_bindir}/hyprpm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/hyprland.conf
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/%{name}.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/Hyprland.*
%{_mandir}/man1/hyprctl.*

%files wallpapers
%{_datadir}/%{name}/wall*

%if %{with devel}
%files devel
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%endif

%changelog
