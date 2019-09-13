#
# spec file for package wlc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define wayland_minimal 1.7
Name:           wlc
Version:        0.0.11
Release:        0
Summary:        A Wayland Compositor Library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/Cloudef/wlc
Source0:        https://github.com/Cloudef/wlc/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        https://github.com/Cloudef/wlc/releases/download/v%{version}/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  Mesa-devel
BuildRequires:  chck-devel
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client) >= %{wayland_minimal}
BuildRequires:  pkgconfig(wayland-cursor) >= %{wayland_minimal}
BuildRequires:  pkgconfig(wayland-egl) >= %{wayland_minimal}
BuildRequires:  pkgconfig(wayland-protocols) >= %{wayland_minimal}
BuildRequires:  pkgconfig(wayland-scanner) >= %{wayland_minimal}
BuildRequires:  pkgconfig(wayland-server) >= %{wayland_minimal}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-screensaver)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xf86dri)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcb-xvmc)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)

%description
A Wayland compositor library. Used by sway or orbment.

%package -n libwlc0
Summary:        A Wayland Compositor Library
Group:          System/Libraries

%description -n libwlc0
Wayland Compositor Library itself.

%package devel
Summary:        Development files for the wlc Wayland Compositor Library
Group:          Development/Libraries/C and C++
Requires:       chck-devel
Requires:       cmake
Requires:       libwlc0 = %{version}
Requires:       pkgconfig(wayland-client) >= %{wayland_minimal}
Requires:       pkgconfig(wayland-cursor) >= %{wayland_minimal}
Requires:       pkgconfig(wayland-egl) >= %{wayland_minimal}
Requires:       pkgconfig(wayland-scanner) >= %{wayland_minimal}
Requires:       pkgconfig(wayland-server) >= %{wayland_minimal}

%description devel
Development files for Wayland Compositor Library.

%prep
%setup -q

# make sure that chck from tarball is not used
rm -r lib/chck/*

%build
%cmake \
       -DSOURCE_CHCK=OFF

make %{?_smp_mflags}

%install
%cmake_install

%post   -n libwlc0 -p /sbin/ldconfig
%postun -n libwlc0 -p /sbin/ldconfig

%files -n libwlc0
%doc LICENSE README.rst
%{_libdir}/libwlc.so.*

%files devel
%{_libdir}/libwlc.so
%{_libdir}/pkgconfig/wlc.pc
%{_includedir}/wlc/

%changelog
