#
# spec file for package wlroots10
#
# Copyright (c) 2022 SUSE LLC
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


%define libname libwlroots10
%bcond_without  drm_backend
%bcond_without  libinput_backend
%bcond_without  x11_backend
%bcond_without  xwayland
%bcond_without  xcb_errors

Name:           wlroots10
Version:        0.15.1
Release:        0
Summary:        Modular Wayland compositor library
License:        MIT
Group:          System/GUI/Other
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
Source0:        %{name}-%{version}.tar.gz
Patch0:         https://gitlab.freedesktop.org/wlroots/wlroots/-/merge_requests/3456.patch
BuildRequires:  glslang-devel
BuildRequires:  meson >= 0.58.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
%if %{with libinput_backend}
BuildRequires:  pkgconfig(libinput) >= 1.14.0
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20
BuildRequires:  pkgconfig(xkbcommon)
%if %{with x11_backend} || %{with xwayland}
BuildRequires:  xorg-x11-server-wayland
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
%if %{with xcb_errors}
BuildRequires:  pkgconfig(xcb-errors)
%endif
%endif

%description
Pluggable, composable modules for building a Wayland compositor.

%package devel
Summary:        Modular Wayland compositor library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Conflicts:      wlroots-devel

%description devel
Pluggable, composable modules for building a Wayland compositor.

%package -n %{libname}
Summary:        Modular Wayland compositor library
Group:          System/Libraries

%description -n %{libname}
Pluggable, composable modules for building a Wayland compositor.

%prep
%setup -n wlroots-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags} -I/usr/include/wayland -Wno-redundant-decls"
%meson \
  "-Dbackends=[
    %{?with_drm_backend:'drm',}
    %{?with_libinput_backend:'libinput',}
    %{?with_x11_backend:'x11',}
  ]" \
  %{?with_xwayland:-Dxwayland=enabled} \
  %{?with_xcb_errors:-Dxcb-errors=enabled}
%meson_build

%install
%meson_install

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_includedir}/wlr/
%{_libdir}/pkgconfig/wlroots.pc
%{_libdir}/libwlroots.so

%files -n %{libname}
%{_libdir}/libwlroots.so.*

%changelog
