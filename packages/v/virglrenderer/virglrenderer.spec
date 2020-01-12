#
# spec file for package virglrenderer
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


%define         libname lib%{name}1
Name:           virglrenderer
Version:        0.8.1
Release:        0
Summary:        Virgl Rendering library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://virgil3d.github.io/
Source0:        https://gitlab.freedesktop.org/virgl/%{name}/-/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  meson >= 0.46
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  python3-base
BuildRequires:  pkgconfig(epoxy) >= 1.5.4
BuildRequires:  pkgconfig(gbm) >= 18.0.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.50
BuildRequires:  pkgconfig(x11)

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package -n %{libname}
Summary:        Virgil3D renderer
Group:          System/Libraries

%description -n %{libname}
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary:        Virgil3D renderer development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.
This package contains the virgil3d renderer development
files.

%package test-server
Summary:        Virgil3D renderer development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description test-server
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.
This package contains a server to test virgl rendering
without GL.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
