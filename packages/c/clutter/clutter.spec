#
# spec file for package clutter
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


Name:           clutter
Version:        1.26.4
Release:        0
Summary:        Library for creating dynamic user interfaces
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://clutter-project.org/
Source0:        https://download.gnome.org/sources/clutter/1.26/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(atk) >= 2.5.3
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cogl-1.0) >= 1.21.2
BuildRequires:  pkgconfig(cogl-path-1.0)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22.6
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.12
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 0.19.0
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(pangocairo) >= 1.30
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)

%description
Clutter is a library for creating fast, visually rich and animated
graphical user interfaces. It uses OpenGL (or GLES) for rendering.

%package -n libclutter-1_0-0
Summary:        Library for creating dynamic graphical user interfaces
# To make the lang package installable
Group:          System/Libraries
Provides:       %{name} = %{version}
# This is technically wrong, but we need this for smooth upgrades so that
# typelib-1_0-Clutter-1_0 can be installed
Obsoletes:      libclutter-glx-1_0-0 < 1.9.0

%description  -n libclutter-1_0-0
Clutter is a library for creating fast, visually rich and animated
graphical user interfaces. It uses OpenGL (or GLES) for rendering.

%package -n typelib-1_0-Clutter-1_0
Summary:        Introspection bindings for the Clutter library
# The library got renamed to libclutter-1_0-0. Installation of both
# packages conflicts (on filelevel: the .typelib kept the name).
Group:          System/Libraries
Conflicts:      libclutter-glx-1_0-0

%description -n typelib-1_0-Clutter-1_0
Clutter is a library for creating fast, visually rich and animated
graphical user interfaces. It uses OpenGL (or GLES) for rendering.

This package provides the GObject Introspection bindings for Clutter.

%package devel
Summary:        Development files for the Clutter library
Group:          Development/Libraries/GNOME
Requires:       libclutter-1_0-0 = %{version}
Requires:       typelib-1_0-Clutter-1_0 = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description  devel
Clutter is a library for creating fast, visually rich and animated
graphical user interfaces.
This package contains the files for development.

%lang_package

%prep
%autosetup -p1
# we delete here to regenerate them without variations in xsltproc id attributes for bit-reproducible builds results
find doc/cookbook/html -name \*.html -type f -delete

%build
%define _lto_cflags %{nil}
%configure \
        --disable-static \
        --enable-xinput \
        --enable-evdev-input \
        --enable-wayland-backend \
        --enable-wayland-compositor \
        --enable-egl-backend \
        --enable-docs
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang clutter-1.0
%fdupes -s %{buildroot}%{_datadir}/gtk-doc/html
%fdupes %{buildroot}

%check
# make check disabled, as clutter needs access to $DISPLAY to actually work
# make %{?_smp_mflags} check V=1

%post -n libclutter-1_0-0 -p /sbin/ldconfig
%postun -n libclutter-1_0-0 -p /sbin/ldconfig

%files -n libclutter-1_0-0
%license COPYING
%doc README.md ChangeLog
%{_libdir}/*.so.*

%files -n typelib-1_0-Clutter-1_0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/*.so
%{_includedir}/clutter-1.0
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/clutter-1.0/valgrind
%{_datadir}/clutter-1.0/valgrind/clutter.supp
%dir %{_datadir}/clutter-1.0/
%doc %{_datadir}/clutter-1.0/cookbook/
%doc %{_datadir}/gtk-doc/html/clutter/
%doc %{_datadir}/gtk-doc/html/clutter-cookbook/

%files lang -f clutter-1.0.lang

%changelog
