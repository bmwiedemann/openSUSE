#
# spec file for package libnvidia-egl-wayland
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
%define lname libnvidia-egl-wayland%{so_ver}
%define rname egl-wayland
Name:           libnvidia-egl-wayland
Version:        1.1.17
Release:        0
Summary:        The EGLStream-based Wayland external platform
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/NVIDIA/egl-wayland
Source0:        https://github.com/NVIDIA/egl-wayland/archive/%{version}/%{rname}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.50
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)

%description
This is an implementation of a EGL External Platform library to add client-side
Wayland support to EGL on top of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

%package -n %{lname}
Summary:        The EGLStream-based Wayland external platform
Group:          System/Libraries

%description -n %{lname}
This is an implementation of a EGL External Platform library to add client-side
Wayland support to EGL on top of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

%package -n libnvidia-egl-wayland-devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}-%{release}

%description -n libnvidia-egl-wayland-devel
This is an implementation of a EGL External Platform library to add client-side
Wayland support to EGL on top of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

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
%license COPYING
%doc README.md
%{_libdir}/libnvidia-egl-wayland.so.%{so_ver}*
%{_datadir}/wayland-eglstream/
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files -n libnvidia-egl-wayland-devel
%license COPYING
%doc README.md
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc

%changelog
