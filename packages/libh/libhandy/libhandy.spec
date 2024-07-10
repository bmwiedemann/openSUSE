#
# spec file for package libhandy
#
# Copyright (c) 2024 SUSE LLC
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


%define so_major 1
%define shlib %{name}-%{so_major}-0
%define typelib typelib-1_0-Handy-%{so_major}_0
%define with_glade 1

Name:           libhandy
Version:        1.8.3
Release:        0
Summary:        A GTK+ library to develop UI for mobile devices
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/GNOME/libhandy
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  vala
%if 0%{?with_glade}
BuildRequires:  pkgconfig(gladeui-2.0)
%endif
BuildRequires:  pkgconfig(gi-docgen) >= 2021.1
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1

%description
libhandy is a library to help with developing UI for mobile devices
using GTK+/GNOME.

%package -n %{shlib}
Summary:        A GTK+ library to develop UI for mobile devices
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{shlib}
This package provides the shared library for libhandy, a library to
help with developing mobile UI using GTK+/GNOME.

%package devel
Summary:        Source and header files for %{name}
Group:          Development/Libraries/GNOME
Requires:       %{shlib} = %{version}
Requires:       %{typelib} = %{version}

%description devel
This package provides the source and header files for writing
software using %{name}, a library to help with developing mobile UI
using GTK+/GNOME.

%package -n %{typelib}
Summary:        Introspection bindings for libhandy
Group:          System/Libraries

%description -n %{typelib}
This package provides the GObject Introspection bindings for
%{name}, a library to help with developing mobile UI using
GTK+/GNOME.

%package -n glade-catalog-libhandy
Summary:        Glade catalog for libhandy
Group:          Development/Tools/GUI Builders
Requires:       glade
Supplements:    (glade and %{name}-devel)

%description -n glade-catalog-libhandy
libhandy is a library to help with developing UI for mobile devices
using GTK+/GNOME.

This package provides a catalog for libhandy, to allow the use
libhandy widgets in Glade.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D profiling=false \
	-D introspection=enabled \
	-D vapi=true \
	-D gtk_doc=true \
	-D tests=false \
	-D examples=false \
	-D glade_catalog=%{?with_glade:enabled}%{?!with_glade:disabled} \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%{_libdir}/libhandy-*.so.*

%files devel
%license COPYING
%doc AUTHORS README.md
%{_includedir}/libhandy-%{so_major}/
%{_libdir}/libhandy-*.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/libhandy-%{so_major}.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libhandy-*
%{_datadir}/doc/libhandy-%{so_major}/

%files -n %{typelib}
%{_libdir}/girepository-1.0/*.typelib

%if 0%{?with_glade}
%files -n glade-catalog-libhandy
%{_libdir}/glade/modules/*.so
%{_datadir}/glade/catalogs/*.xml
%endif

%files lang -f %{name}.lang

%changelog
