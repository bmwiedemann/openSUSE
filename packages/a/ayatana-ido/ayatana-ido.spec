#
# spec file for package ayatana-ido
#
# Copyright (c) 2021-2024 SUSE LLC
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
Version:        0.10.2
Release:        0
Summary:        Ayatana Indicator Display Objects
License:        GPL-3.0-only AND LGPL-3.0-only AND LGPL-2.1-only
Group:          System/GUI/Other
URL:            https://github.com/AyatanaIndicators/ayatana-ido
Source:         https://github.com/AyatanaIndicators/ayatana-ido/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.16
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xorg-macros)

%description
Widgets and other objects used for indicators.

%package -n %{lname}
Summary:        Shared library providing extra GTK menu items in system indicators
Group:          System/Libraries

%description -n %{lname}
Shared library providing extra GTK menu items for display in
system indicators.

This package contains shared libraries.

%package -n %{typelib}
Summary:        Ayatana Indicator Display Objects typelib
Group:          System/Libraries

%description -n %{typelib}
Shared library providing extra GTK menu items for display in
system indicators.

This package provides the GObject Introspection bindings for
Ayatana Ido.

%package devel
Summary:        Development files for Ayatana Indicator Display Objects
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig(gobject-introspection-1.0)

%description devel
Shared library providing extra GTK menu items for display in
system indicators.

This package contains the development files for Ido.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
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
%{_datadir}/vala/vapi/libayatana-ido3-0.4.vapi

%changelog
