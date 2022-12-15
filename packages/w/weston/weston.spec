#
# spec file for package weston
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


Name:           weston
%define lname	libweston0
%define major   11
%define realver	11.0.1
Version:        11
Release:        0
Summary:        Wayland Reference Compositor
License:        CC-BY-SA-3.0 AND MIT
Group:          System/X11/Servers
URL:            https://wayland.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/wayland/weston
#Git-Web:	https://cgit.freedesktop.org/wayland/weston/
Source:         https://gitlab.freedesktop.org/wayland/weston/uploads/f5648c818fba5432edc3ea63c4db4813/weston-11.0.1.tar.xz
Source2:        https://gitlab.freedesktop.org/wayland/weston/uploads/bb54e28b5ee47aaccb30a8ffbc31f977/weston-11.0.1.tar.xz.sig
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake >= 1.11
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel >= 2.27
BuildRequires:  libjpeg-devel
BuildRequires:  libtool >= 2.2
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  xkeyboard-config
BuildRequires:  xz
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-egl) >= 1.11.3
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(colord) >= 0.1.27
BuildRequires:  pkgconfig(dbus-1) >= 1.6
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.108
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 0.8.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pixman-1) >= 0.25.2
BuildRequires:  pkgconfig(wayland-client) >= 1.18.0
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.18.0
BuildRequires:  pkgconfig(xcb) >= 1.8
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb) >= 1.9
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
Requires:       vpx-tools
Requires:       xkeyboard-config

%description
Weston is the reference implementation of a Wayland compositor, and a
useful compositor in its own right. Weston has various backends that
lets it run on Linux kernel modesetting and evdev input as well as
under X11. Weston ships with a few example clients, from simple
clients that demonstrate certain aspects of the protocol to more
complete clients and a simplistic toolkit. There is also a quite
capable terminal emulator (weston-terminal) and an toy/example
desktop shell. Finally, weston also provides integration with the
Xorg server and can pull X clients into the Wayland desktop and act
as a X window manager.

%package -n libweston-%major
Summary:        Weston rendering backend collection
Group:          System/Libraries

%description -n libweston-%major
This subpackage contains backend renderer plugins, used by
libweston-%major-0.

%package -n libweston-%major-0
Summary:        The Weston compositor as a shared library
Group:          System/Libraries
Requires:       libweston-%major >= %version

%description -n libweston-%major-0
The libweston library is intended for use by other compositor efforts
(projects) that want to more easily utilize Weston's internal
functionalities. Weston's own reference compositor also makes use of
this.

%package devel
Summary:        Development files for Weston plugins
Group:          Development/Libraries/C and C++
Requires:       libweston-%major-0 = %version

%description devel
Weston is the reference implementation of a Wayland compositor, and a
useful compositor in its own right. Weston has various backends that
lets it run on Linux kernel modesetting and evdev input as well as
under X11.

This package contains all necessary include files and libraries needed
to develop plugins for Weston.

%prep
%autosetup -n %name-%realver -p1

%build
echo "Workaround broken weston that fails to cope with -Wl,--no-undefined injected by meson/ninja"
export LDFLAGS="%{?build_ldflags} -Wl,-z,undefs"
%meson -Ddemo-clients=false -Dremoting=false -Dsimple-clients= \
	-Dtest-junit-xml=false -Dpipewire=false \
	--includedir="%_includedir/%name"
%meson_build

%install
%meson_install

%check
%if !0%{?qemu_user_space_build}
export XDG_RUNTIME_DIR="$PWD/xdg"
mkdir -pm go-rwx "$XDG_RUNTIME_DIR"
export BACKEND=headless-backend.so
pushd %_vpath_builddir/;
if ! meson test; then
	cat meson-logs/testlog.txt
	# make check can not pass completely without an actual screen.
	#exit 1
fi
popd
%endif

%post   -n libweston-%major-0 -p /sbin/ldconfig
%postun -n libweston-%major-0 -p /sbin/ldconfig

%files
%license COPYING
%_bindir/w*
%_libexecdir/%name-*
%_libdir/%name/
%_datadir/%name/
%_datadir/wayland-sessions/
%_datadir/libweston-%major/
%_mandir/man?/*.*

%files -n libweston-%major-0
%_libdir/libweston-%major.so.0*

%files -n libweston-%major
%_libdir/libweston-%major/

%files devel
%_includedir/%name/
%_libdir/pkgconfig/*.pc
%_libdir/libweston*.so
%_datadir/pkgconfig/*.pc

%changelog
