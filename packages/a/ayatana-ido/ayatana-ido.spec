#
# spec file for package ayatana-ido
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libayatana-ido3-0_4
%define soname  libayatana-ido3-0.4
%define sover   0
%define typelib typelib-1_0-AyatanaIdo3-0_4
Name:           ayatana-ido
Version:        0.8.2
Release:        0
Summary:        Ayatana Indicator Display Objects
License:        GPL-3.0-only AND LGPL-3.0-only AND LGPL-2.1-only
URL:            https://github.com/AyatanaIndicators/ayatana-ido
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM pkgconfig-requires.patch -- https://github.com/AyatanaIndicators/ayatana-ido/issues/37
Patch0:         pkgconfig-requires.patch
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

%package -n %{lname}-%{sover}
Summary:        Shared library providing extra GTK+ menu items in system indicators

%description -n %{lname}-%{sover}
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
Requires:       %{lname}-%{sover} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig(gobject-introspection-1.0)

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

%post -n %{lname}-%{sover} -p /sbin/ldconfig
%postun -n %{lname}-%{sover} -p /sbin/ldconfig

%files -n %{lname}-%{sover}
%license COPYING*
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{typelib}
%{_libdir}/girepository-1.0/AyatanaIdo3-0.4.typelib

%files devel
%license COPYING*
%doc AUTHORS* ChangeLog
%{_includedir}/%{soname}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc
%{_datadir}/gir-1.0/AyatanaIdo3-0.4.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/AyatanaIdo3-0.4.vapi

%changelog
