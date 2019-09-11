#
# spec file for package gsound
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Bjørn Lie, Bryne, Norway.
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


%define soname lib%{name}0

Name:           gsound
Version:        1.0.2
Release:        0
Summary:        A library for playing system sounds
License:        LGPL-2.1-only
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/GSound
Source0:        https://download.gnome.org/sources/gsound/1.0/gsound-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gsound-gsound-play-Call-setlocale.patch -- gsound-play: Call setlocale in main function
Patch0:         gsound-gsound-play-Call-setlocale.patch

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(vapigen)

%description
GSound is a library for playing system sounds.
It's designed to be used via GObject Introspection,
and is a wrapper around the libcanberra C library.

%package -n %{soname}
Summary:        Shared library for gsound
Group:          System/Libraries

%description -n %{soname}
GSound is a library for playing system sounds.
It's designed to be used via GObject Introspection,
and is a wrapper around the libcanberra C library.

This package provides the shared library for gsound.

%package -n typelib-1_0-GSound-1_0
Summary:        Gobject introspection files for gsound
Group:          System/Libraries

%description -n typelib-1_0-GSound-1_0
GSound is a library for playing system sounds.
It's designed to be used via GObject Introspection,
and is a wrapper around the libcanberra C library.

%package devel
Summary:        Development files for gsound
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       typelib-1_0-GSound-1_0 = %{version}

%description devel
GSound is a library for playing system sounds.
It's designed to be used via GObject Introspection,
and is a wrapper around the libcanberra C library.

This package provides files needed for developing
applications with gsound.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-vala \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files
%doc ChangeLog README
%{_bindir}/gsound-play

%files -n %{soname}
%license COPYING
%{_libdir}/libgsound.so.*

%files devel
%{_datadir}/gir-1.0/GSound-1.0.gir
%{_datadir}/gtk-doc/html/gsound/
%{_datadir}/vala/vapi/gsound.deps
%{_datadir}/vala/vapi/gsound.vapi
%{_includedir}/gsound.h
%{_includedir}/gsound-attr.h
%{_includedir}/gsound-context.h
%{_libdir}/libgsound.so
%{_libdir}/pkgconfig/gsound.pc

%files -n typelib-1_0-GSound-1_0
%{_libdir}/girepository-1.0/GSound-1.0.typelib

%changelog
