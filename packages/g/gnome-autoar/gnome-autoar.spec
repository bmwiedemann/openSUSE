#
# spec file for package gnome-autoar
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


Name:           gnome-autoar
Version:        0.2.3
Release:        0
Summary:        Automatic archives creating and extracting library
License:        LGPL-2.0-or-later
Group:          System/GUI/GNOME
Url:            https://git.gnome.org/browse/gnome-autoar
Source:         https://download.gnome.org/sources/gnome-autoar/0.2/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.35.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.6
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2
BuildRequires:  pkgconfig(libarchive) >= 3.2.0
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
%autosetup

%build
%configure \
	--disable-static \
	--enable-gtk \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libgnome-autoar-0-0 -p /sbin/ldconfig
%postun -n libgnome-autoar-0-0 -p /sbin/ldconfig
%post   -n libgnome-autoar-gtk-0-0 -p /sbin/ldconfig
%postun -n libgnome-autoar-gtk-0-0 -p /sbin/ldconfig

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

%files -n typelib-1_0-GnomeAutoar-0_1
%{_libdir}/girepository-1.0/GnomeAutoar-0.1.typelib

%files -n typelib-1_0-GnomeAutoarGtk-0_1
%{_libdir}/girepository-1.0/GnomeAutoarGtk-0.1.typelib

%files -n libgnome-autoar-0-0
%license COPYING
%{_libdir}/libgnome-autoar-0.so.0
%{_libdir}/libgnome-autoar-0.so.0.0.0

%files -n libgnome-autoar-gtk-0-0
%{_libdir}/libgnome-autoar-gtk-0.so.0
%{_libdir}/libgnome-autoar-gtk-0.so.0.0.0

%changelog
