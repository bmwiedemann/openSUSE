#
# spec file for package libnvidia-egl-x11
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


%define so_ver 1
%define lname libnvidia-egl-x11%{so_ver}
%define rname egl-x11
Name:           libnvidia-egl-x11
Version:        1.0.1
Release:        0
Summary:        NVIDIA XLib and XCB EGL Platform Library
# src/x11/dma-buf.h:/* SPDX-License-Identifier: GPL-2.0 WITH Linux-syscall-note */
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/sndirsch/egl-x11
Source0:        https://github.com/sndirsch/egl-x11/archive/%{version}/%{rname}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.2
BuildRequires:  pkgconfig(gbm) >= 21.3.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.99
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb) >= 1.17.0
BuildRequires:  pkgconfig(xcb-dri3) >= 1.17.0
BuildRequires:  pkgconfig(xcb-present) >= 1.17.0

%description
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

In addition, this library depends on a (still somewhat experimental) interface
in the NVIDIA driver, which is supported only in 560 or later series drivers.

For full functionality, it also needs the explicit sync protocol added to
version 1.4 of the Present and DRI3 extensions, which is available in XWayland
24.1 and later. Without explicit sync support, you may get reduced performance
and out-of-order frames.

%package -n %{lname}
Summary:        NVIDIA XLib and XCB EGL Platform Library
Group:          System/Libraries

%description -n %{lname}
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

In addition, this library depends on a (still somewhat experimental) interface
in the NVIDIA driver, which is supported only in 560 or later series drivers.

For full functionality, it also needs the explicit sync protocol added to
version 1.4 of the Present and DRI3 extensions, which is available in XWayland
24.1 and later. Without explicit sync support, you may get reduced performance
and out-of-order frames.

%package -n libnvidia-egl-x11-devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}-%{release}

%description -n libnvidia-egl-x11-devel
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

In addition, this library depends on a (still somewhat experimental) interface
in the NVIDIA driver, which is supported only in 560 or later series drivers.

For full functionality, it also needs the explicit sync protocol added to
version 1.4 of the Present and DRI3 extensions, which is available in XWayland
24.1 and later. Without explicit sync support, you may get reduced performance
and out-of-order frames.

This package provides headers and libraries required to build software
using %{name}.

%prep
%autosetup -n %{rname}-%{version} -p1

%build
export LDFLAGS="-Wl,-z,noexecstack -Wl,-z,now -Wl,-z,relro %{?_lto_cflags}"
%meson
%meson_build

%install
%meson_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc README.md
%{_libdir}/libnvidia-egl-xcb.so.%{so_ver}*
%{_libdir}/libnvidia-egl-xlib.so.%{so_ver}*
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xcb.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xlib.json

%files -n libnvidia-egl-x11-devel
%license LICENSE
%doc README.md
%{_libdir}/libnvidia-egl-xcb.so
%{_libdir}/libnvidia-egl-xlib.so

%changelog
