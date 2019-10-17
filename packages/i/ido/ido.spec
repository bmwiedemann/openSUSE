#
# spec file for package ido
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname   libido3-0_1-0
%define soname  libido3-0.1
%define sover   0
%define typelib typelib-1_0-Ido3-0_1
%define _version 13.10.0+17.04.20161028
Name:           ido
Version:        13.10.0+bzr20161028
Release:        0
Summary:        Indicator Display Objects
License:        GPL-3.0-only AND LGPL-3.0-only AND LGPL-2.1-only
Group:          System/GUI/Other
Url:            https://launchpad.net/ido
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE ido-optional-ubuntu-private.patch sor.alexei@meowr.ru -- Make Ubuntu GTK+ Private API optional.
Patch0:         ido-optional-ubuntu-private.patch
# PATCH-FIX-OPENSUSE ido-fix-maintainer-cflags.patch dimstar@opensuse.org -- Strip -Werror from unconditional CFLAGS. This is part of maintainer_CFLAGS; fixes build with more recent toolchains/gnome stacks
Patch1:         ido-fix-maintainer-cflags.patch
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
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
Group:          System/Libraries

%description -n %{lname}
Shared library providing extra GTK+ menu items for display in
system indicators.

This package contains shared libraries.

%package -n %{typelib}
Summary:        Indicator Display Objects typelib
Group:          System/Libraries

%description -n %{typelib}
Shared library providing extra GTK+ menu items for display in
system indicators.

This package provides the GObject Introspection bindings for Ido.

%package devel
Summary:        Development files for Indicator Display Objects
Group:          Development/Libraries/C and C++
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
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --disable-ubuntu-private-api
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%if 0%{?suse_version} >= 1500
%license COPYING*
%else
%doc COPYING*
%endif
%doc AUTHORS NEWS
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{typelib}
%{_libdir}/girepository-1.0/Ido3-0.1.typelib

%files devel
%{_includedir}/%{soname}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc
%{_datadir}/gir-1.0/Ido3-0.1.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/Ido3-0.1.vapi

%changelog
