#
# spec file for package colord-gtk
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           colord-gtk
Version:        0.1.26
Release:        0
Summary:        System Daemon for Managing Color Devices -- GTK Integration
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            http://colord.hughsie.com/
Source0:        http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  intltool >= 0.35.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(colord) >= 0.1.27
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.9
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2) >= 2.2

%description
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n libcolord-gtk1
Summary:        System Daemon for Managing Color Devices -- GTK Integration Library
Group:          System/Libraries
Recommends:     %{name}-lang
Suggests:       colord
# for the -lang package to be installable
Provides:       %{name} = %{version}

%description -n libcolord-gtk1
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n typelib-1_0-ColordGtk-1_0
Summary:        System Daemon for Managing Color Devices -- GTK Integration Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-ColordGtk-1_0
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

This package provides the GObject Introspection bindings for the
libcolord-gtk library.

%package -n libcolord-gtk-devel
Summary:        System Daemon for Managing Color Devices -- GTK Integration Development Files
Group:          Development/Languages/C and C++
Requires:       libcolord-gtk1 = %{version}
Requires:       typelib-1_0-ColordGtk-1_0 = %{version}

%description -n libcolord-gtk-devel
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%lang_package

%prep
%setup -q

%build
%configure \
   --disable-static \
   --enable-vala
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n libcolord-gtk1 -p /sbin/ldconfig
%postun -n libcolord-gtk1 -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%{_bindir}/cd-convert

%files -n libcolord-gtk1
%{_libdir}/libcolord-gtk.so.*

%files -n typelib-1_0-ColordGtk-1_0
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib

%files -n libcolord-gtk-devel
%{_includedir}/colord-1/colord-gtk.h
%{_includedir}/colord-1/colord-gtk/
%{_libdir}/libcolord-gtk.so
%{_libdir}/pkgconfig/colord-gtk.pc
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
%{_datadir}/vala/vapi/colord-gtk.vapi

%changelog
