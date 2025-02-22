#
# spec file for package labwc
#
# Copyright (c) 2025 mantarimay
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


%bcond_with     warp
%bcond_without  xwayland
%define swname  wlroots
%define swver   0.17.4
%define slname  libsfdo
%define slver   0.1.3
Name:           labwc
Version:        0.8.3
Release:        0
Summary:        A Wayland window-stacking compositor
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://gitlab.freedesktop.org/vyivel/libsfdo/-/archive/v%{slver}/%{slname}-v%{slver}.tar.bz2
%if %{with warp}
Source2:        https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/%{swver}/%{swname}-%{swver}.tar.bz2
Provides:       bundled(wlroots)
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
%if %{with xwayland}
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xwayland)
%endif
BuildRequires:  pkgconfig(xwaylandproto)
%else
BuildRequires:  pkgconfig(wlroots-0.18)
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
Recommends:     alacritty
Recommends:     xwayland
Suggests:       rofi-wayland
Suggests:       grim
Suggests:       swaybg
Suggests:       waybar

%description
Labwc is a wlroots-based window-stacking compositor for wayland, inspired
by openbox.

%lang_package

%prep
%autosetup
%if %{with warp}
mkdir subprojects/%{swname}
tar -xf %{SOURCE2} --strip-components 1 -C subprojects/%{swname}
%endif

mkdir subprojects/%{slname}
tar -xf %{SOURCE1} --strip-components 1 -C subprojects/%{slname}

%build
%meson \
    -Dman-pages=enabled \
%if %{with xwayland}
    -Dxwayland=enabled \
%else
    -Dxwayland=disabled \
%endif
    -Dnls=enabled
%meson_build

%install
%meson_install --skip-subprojects
install -Dm 0644 docs/*.xml -t %{buildroot}%{_sysconfdir}/xdg/%{name}/

%find_lang %{name}

%files
%license LICENSE
%doc NEWS.md README.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/menu.xml
%config(noreplace) %{_sysconfdir}/xdg/%{name}/rc.xml
%dir %{_datadir}/wayland-sessions
%{_datadir}/xdg-desktop-portal
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/labwc*.svg
%{_mandir}/man?/%{name}*.?%{?ext_man}
%{_datadir}/doc/%{name}/

%files lang -f %{name}.lang

%changelog
