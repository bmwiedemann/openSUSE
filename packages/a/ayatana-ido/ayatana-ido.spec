#
# spec file for package ayatana-ido
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


%define lname   libayatana-ido3-0_4-0
%define soname  libayatana-ido3-0.4
%define sover   0
%define typelib typelib-1_0-AyatanaIdo3-0_4
Name:           ayatana-ido
Version:        0.4.4
Release:        0
Summary:        Ayatana Indicator Display Objects
License:        GPL-3.0-only AND LGPL-3.0-only AND LGPL-2.1-only
URL:            https://github.com/AyatanaIndicators/ayatana-ido
Source:         https://github.com/AyatanaIndicators/ayatana-ido/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
#PATCH-FIX-UPSTREAM ayatana-ido-glib-2.58.patch g_type_class_add_private was deprecated since glib 2.58
Patch0:         ayatana-ido-glib-2.58.patch
# PATCH-FIX-UPSTREAM 0001-gtk_widget_get_state-is-deprecated.patch -- gtk_widget_get_state is deprecated
Patch1:         0001-gtk_widget_get_state-is-deprecated.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  mate-common
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.16
BuildRequires:  pkgconfig(gio-2.0) >= 2.37.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.37.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xorg-macros)

%description
Widgets and other objects used for indicators.

%package -n %{lname}
Summary:        Shared library providing extra GTK+ menu items in system indicators

%description -n %{lname}
Shared library providing extra GTK+ menu items for display in
system indicators.

This package contains shared libraries.

%package -n %{typelib}
Summary:        Ayatana Indicator Display Objects typelib

%description -n %{typelib}
Shared library providing extra GTK+ menu items for display in
system indicators.

This package provides the GObject Introspection bindings for
Ayatana Ido.

%package devel
Summary:        Development files for Ayatana Indicator Display Objects
Requires:       %{lname} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig(gio-2.0) >= 2.37.0
Requires:       pkgconfig(glib-2.0) >= 2.37.0
Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(gtk+-3.0) >= 3.8.2

%description devel
Shared library providing extra GTK+ menu items for display in
system indicators.

This package contains the development files for Ido.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%doc AUTHORS* ChangeLog
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{typelib}
%{_libdir}/girepository-1.0/AyatanaIdo3-0.4.typelib

%files devel
%{_includedir}/%{soname}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc
%{_datadir}/gir-1.0/AyatanaIdo3-0.4.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/AyatanaIdo3-0.4.vapi

%changelog
