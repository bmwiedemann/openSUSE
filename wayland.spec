#
# spec file for package wayland
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


%define _version 1.23.0
%if 0%{?suse_version} >= 1500 && 0%{?suse_version} < 1550
%define eglversion 99~%_version
%else
%define eglversion %_version
%endif
%define lname	libwayland0
%bcond_with doc
Name:           wayland
Version:        %_version
Release:        0
Summary:        Wayland Compositor Infrastructure
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://wayland.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/wayland/wayland
#Git-Web:	http://cgit.freedesktop.org/wayland/wayland/
Source:         https://gitlab.freedesktop.org/wayland/wayland/-/releases/%version/downloads/wayland-%version.tar.xz
Source2:        https://gitlab.freedesktop.org/wayland/wayland/-/releases/%version/downloads/wayland-%version.tar.xz.sig
Source3:        %name.keyring
Source4:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  graphviz-gnome
BuildRequires:  xmlto
%endif

%description
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n libwayland-client0
Summary:        Wayland core client library
Group:          System/Libraries

%description -n libwayland-client0
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n libwayland-cursor0
Summary:        Wayland cursor library
Group:          System/Libraries

%description -n libwayland-cursor0
The purpose of this library is to be the equivalent of libXcursor in
the X world. This library is compatible with X cursor themes and
loads them directly into an shm pool making it easy for the clients
to get buffer for each cursor image.

%package -n libwayland-egl1
Version:        %eglversion
Summary:        Additional egl functions for wayland
Group:          System/Libraries

%description -n libwayland-egl1
This package provides additional functions for EGL-using programs
that run within the Wayland framework. This allows for applications
that need not run full-screen and cooperate with a compositor.

%package -n libwayland-server0
Summary:        Wayland core server library
Group:          System/Libraries

%description -n libwayland-server0
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package devel
Summary:        Development files for the Wayland Compositor Infrastructure
Group:          Development/Libraries/C and C++
Requires:       libwayland-client0 = %_version
Requires:       libwayland-cursor0 = %_version
Requires:       libwayland-egl1 = %eglversion
Requires:       libwayland-server0 = %_version
%if 0%{?suse_version} >= 1500
# egl1 was once provided by Mesa 17.x.
%if (0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400)
Provides:       libwayland-egl-devel = 18.1.5
Obsoletes:      libwayland-egl-devel < 18.1.5
%else
Provides:       libwayland-egl-devel = 18.0.2
Obsoletes:      libwayland-egl-devel < 18.0.2
%endif
%endif

%description devel
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:        Wayland development documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This subpackage contains the documentation to Wayland.

%prep
%autosetup -p1
sed -i 's/<eglversion>/%eglversion/' "%_sourcedir/baselibs.conf"

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%meson \
	--includedir="%_includedir/%name" \
%if %{with doc}
	--docdir="%_defaultdocdir/%name"
%else
	-D documentation=false
%endif
%meson_build

%install
%meson_install

%check
%meson_test

%if 0%{?suse_version} >= 1550
%ldconfig_scriptlets -n libwayland-client0
%ldconfig_scriptlets -n libwayland-cursor0
%ldconfig_scriptlets -n libwayland-egl1
%ldconfig_scriptlets -n libwayland-server0
%else
%post   -n libwayland-client0 -p /sbin/ldconfig
%postun -n libwayland-client0 -p /sbin/ldconfig
%post   -n libwayland-cursor0 -p /sbin/ldconfig
%postun -n libwayland-cursor0 -p /sbin/ldconfig
%post   -n libwayland-egl1 -p /sbin/ldconfig
%postun -n libwayland-egl1 -p /sbin/ldconfig
%post   -n libwayland-server0 -p /sbin/ldconfig
%postun -n libwayland-server0 -p /sbin/ldconfig
%endif

%files -n libwayland-client0
%_libdir/libwayland-client.so.0*
%license COPYING

%files -n libwayland-cursor0
%_libdir/libwayland-cursor.so.0*

%files -n libwayland-egl1
%_libdir/libwayland-egl.so.1*

%files -n libwayland-server0
%_libdir/libwayland-server.so.0*

%files devel
%_bindir/wayland-scanner
%_includedir/%name/
%_libdir/libwayland-*.so
%_libdir/pkgconfig/wayland-*.pc
%_datadir/aclocal/
%_datadir/wayland/

%if %{with doc}
%files doc
%_mandir/man3/wl*.3*
%_docdir/%name/
%endif

%changelog
