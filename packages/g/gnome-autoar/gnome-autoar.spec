#
# spec file for package gnome-autoar
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


Name:           gnome-autoar
Version:        0.4.4
Release:        0
Summary:        Automatic archives creating and extracting library
License:        LGPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-autoar
# Sourceurl disabled, as we are using a git checkout via source services
#Source0:       https://download.gnome.org/sources/gnome-autoar/0.4/%%{name}-%%{version}.tar.xz
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.35.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.6
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.6
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2
BuildRequires:  pkgconfig(libarchive) >= 3.4.0
BuildRequires:  pkgconfig(vapigen)

%description
gnome-autoar provides functions, widgets, and gschemas for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

%package -n libgnome-autoar-0-0
Summary:        Automatic archives creating and extracting library
Group:          System/Libraries
Obsoletes:      gnome-autoar-schema

%description -n libgnome-autoar-0-0
gnome-autoar provides functions, widgets, and gschemas for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

%package -n libgnome-autoar-gtk-0-0
Summary:        Automatic archives creating and extracting library
Group:          System/Libraries

%description -n libgnome-autoar-gtk-0-0
gnome-autoar provides functions, widgets, and gschemas for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

%package -n typelib-1_0-GnomeAutoar-0_1
Summary:        Automatic archives creating and extracting library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GnomeAutoar-0_1
gnome-autoar provides functions, widgets, and gschemas for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

%package -n typelib-1_0-GnomeAutoarGtk-0_1
Summary:        Automatic archives creating and extracting library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GnomeAutoarGtk-0_1
gnome-autoar provides functions, widgets, and gschemas for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

%package devel
Summary:        Automatic archives creating and extracting library
Group:          Development/Languages/C and C++
Requires:       libgnome-autoar-0-0 = %{version}
Requires:       libgnome-autoar-gtk-0-0 = %{version}
Requires:       typelib-1_0-GnomeAutoar-0_1 = %{version}
Requires:       typelib-1_0-GnomeAutoarGtk-0_1 = %{version}

%description devel
gnome-autoar provides functions, widgets, and gschemas for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

This package brings files required to develop against gnome-autoar

%prep
%autosetup -p1

%build
%meson \
	-D vapi=true \
	-D gtk_doc=true \
	-D tests=true \
	%{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libgnome-autoar-0-0
%ldconfig_scriptlets -n libgnome-autoar-gtk-0-0

%files devel
%{_includedir}/gnome-autoar-0/
%{_libdir}/libgnome-autoar-0.so
%{_libdir}/libgnome-autoar-gtk-0.so
%{_libdir}/pkgconfig/gnome-autoar-0.pc
%{_libdir}/pkgconfig/gnome-autoar-gtk-0.pc
%{_datadir}/gir-1.0/GnomeAutoar-0.1.gir
%{_datadir}/gir-1.0/GnomeAutoarGtk-0.1.gir
%{_datadir}/gtk-doc/html/%{name}/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gnome-autoar-0.vapi
%{_datadir}/vala/vapi/gnome-autoar-gtk-0.vapi
%{_datadir}/vala/vapi/gnome-autoar-0.deps
%{_datadir}/vala/vapi/gnome-autoar-gtk-0.deps

%files -n typelib-1_0-GnomeAutoar-0_1
%{_libdir}/girepository-1.0/GnomeAutoar-0.1.typelib

%files -n typelib-1_0-GnomeAutoarGtk-0_1
%{_libdir}/girepository-1.0/GnomeAutoarGtk-0.1.typelib

%files -n libgnome-autoar-0-0
%license COPYING
%{_libdir}/libgnome-autoar-0.so.*

%files -n libgnome-autoar-gtk-0-0
%{_libdir}/libgnome-autoar-gtk-0.so.*

%changelog
