#
# spec file for package wlroots
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without  libcap
%bcond_without  systemd
%bcond_with     elogind
%bcond_without  x11_backend
%bcond_without  xwayland
%bcond_without  xcb_errors
Name:           wlroots
Version:        0.10.1
Release:        0
Summary:        Modular Wayland compositor library
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/wlroots
Source0:        https://github.com/swaywm/wlroots/archive/%{version}.tar.gz
Patch0:         0001-Declare-wlr_seat-globals-as-extern.patch
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.9.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.16
BuildRequires:  pkgconfig(wayland-server) >= 1.16
BuildRequires:  pkgconfig(xkbcommon)
%if %{with libcap}
BuildRequires:  pkgconfig(libcap)
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd)
%endif
%if %{with elogind}
BuildRequires:  pkgconfig(libelogind)
%endif
%if %{with x11_backend} || %{with xwayland}
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
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
Requires:       libwlroots5 = %{version}

%description devel
Pluggable, composable modules for building a Wayland compositor.

%package -n libwlroots5
Summary:        Modular Wayland compositor library
Group:          System/Libraries

%description -n libwlroots5
Pluggable, composable modules for building a Wayland compositor.

%prep
%setup -q
%patch0 -p1
%build
export CFLAGS="%{optflags} -I/usr/include/wayland -Wno-redundant-decls"
%meson \
  %{?with_libcap:-Denable-libcap=true} \
%if 0%{?suse_version} >= 1550
  %{?with_systemd:-Denable-systemd=true} \
  %{?with_elogind:-Denable-elogind=true} \
%else
  -Dlogind=disabled \
%endif
  %{?with_x11_backend:-Denable-x11_backend=true} \
  %{?with_xwayland:-Denable-xwayland=true} \
  %{?with_xcb_errors:-Denable-xcb_errors=true}
%meson_build

%install
%meson_install

%post   -n libwlroots5 -p /sbin/ldconfig
%postun -n libwlroots5 -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_includedir}/wlr/
%{_libdir}/pkgconfig/wlroots.pc
%{_libdir}/libwlroots.so

%files -n libwlroots5
%{_libdir}/libwlroots.so.*

%changelog
