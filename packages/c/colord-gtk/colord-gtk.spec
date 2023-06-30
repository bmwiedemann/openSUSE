#
# spec file for package colord-gtk
#
# Copyright (c) 2023 SUSE LLC
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


Name:           colord-gtk
Version:        0.3.0
Release:        0
Summary:        System Daemon for Managing Color Devices -- GTK Integration
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://www.freedesktop.org/software/colord
Source0:        https://www.freedesktop.org/software/colord/releases/colord-gtk-%{version}.tar.xz
Source1:        https://www.freedesktop.org/software/colord/releases/colord-gtk-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM Fix-the-callback-signature-to-fix-a-crash.patch bsc#1212840 gh#hughsie/colord-gtk#22 -- Fix segfault when turning monitor back on
Patch1:         Fix-the-callback-signature-to-fix-a-crash.patch
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  gtk-doc
BuildRequires:  meson
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
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(lcms2) >= 2.2

%description
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n libcolord-gtk1
Summary:        System Daemon for Managing Color Devices -- GTK Integration Library
Group:          System/Libraries
Suggests:       colord
# for the -lang package to be installable
Provides:       %{name} = %{version}

%description -n libcolord-gtk1
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n libcolord-gtk4-1
Summary:        System Daemon for Managing Color Devices -- GTK Integration Library
Group:          System/Libraries
Suggests:       colord
# for the -lang package to be installable
#Provides:       %%{name} = %%{version}

%description -n libcolord-gtk4-1
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package -n typelib-1_0-ColordGtk-1_0
Summary:        GTK Integration Introspection bindings for colord-gtk
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
Requires:       libcolord-gtk4-1 = %{version}
Requires:       typelib-1_0-ColordGtk-1_0 = %{version}

%description -n libcolord-gtk-devel
colord is a system activated daemon that maps devices to color profiles.
It is used by gnome-color-manager for system integration and use when
there are no users logged in.

%package doc
Summary:        Development Documentation for colord-gtk
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains development documentation for the colord-gtk packages.


%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dvapi=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%ldconfig_scriptlets -n libcolord-gtk1
%ldconfig_scriptlets -n libcolord-gtk4-1

%files lang -f %{name}.lang

%files
%{_bindir}/cd-convert
%{_mandir}/man1/cd-convert.1%{ext_man}

%files -n libcolord-gtk1
%license COPYING
%{_libdir}/libcolord-gtk.so.*

%files -n libcolord-gtk4-1
%{_libdir}/libcolord-gtk4.so.*

%files -n typelib-1_0-ColordGtk-1_0
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib

%files -n libcolord-gtk-devel
%{_includedir}/colord-1/colord-gtk.h
%{_includedir}/colord-1/colord-gtk/
%{_libdir}/libcolord-gtk.so
%{_libdir}/pkgconfig/colord-gtk.pc
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
%{_datadir}/vala/vapi/colord-gtk.vapi
%{_datadir}/vala/vapi/colord-gtk.deps
%{_libdir}/libcolord-gtk4.so
%{_libdir}/pkgconfig/colord-gtk4.pc

%files doc
%doc AUTHORS NEWS README
%{_datadir}/gtk-doc/html/%{name}

%changelog
