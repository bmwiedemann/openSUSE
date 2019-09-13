#
# spec file for package virglrenderer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         libname lib%{name}0
Name:           virglrenderer
Version:        0.7.0
Release:        0
Summary:        Virgl Rendering library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://virgil3d.github.io/
Source0:        https://www.freedesktop.org/software/virgl/virglrenderer-%{version}.tar.bz2
Source1:        https://www.freedesktop.org/software/virgl/virglrenderer-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  Mesa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lbxutil)
BuildRequires:  pkgconfig(libdrm) >= 2.4.50
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

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
%setup -q

%build
sed -i -e 's|@CODE_COVERAGE_RULES@| |g' Makefile.am
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install
rm -f %{buildroot}%{_libdir}/libvirglrenderer.la

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc COPYING
%{_libdir}/lib*.so.*

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
