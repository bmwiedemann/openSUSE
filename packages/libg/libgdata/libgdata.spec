#
# spec file for package libgdata
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


# Update baselibs.conf when changing this
%define _sover 22
Name:           libgdata
Version:        0.17.13
Release:        0
Summary:        GLib-based library for accessing online service APIs using the GData protocol
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://live.gnome.org/libgdata
Source:         https://download.gnome.org/sources/libgdata/0.17/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.14
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(goa-1.0) >= 3.8
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.15
# Note: as of 0.10.0, gtk+-3.0 is only needed to build a demo that isn't
# installed, so no need to depend on it
#BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.55.90
BuildRequires:  pkgconfig(libuhttpmock-0.0) >= 0.5.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oauth) >= 0.9.4
BuildRequires:  pkgconfig(vapigen)

%description
libgdata is a GLib-based library for accessing online service APIs using
the GData protocol — most notably, Google's services. It provides APIs
to access the common Google services, and has full asynchronous support.

%package -n libgdata%{_sover}
Summary:        GLib-based library for accessing online service APIs using the GData protocol
# Needed for the lang package to be installable:
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgdata%{_sover}
libgdata is a GLib-based library for accessing online service APIs using
the GData protocol — most notably, Google's services. It provides APIs
to access the common Google services, and has full asynchronous support.

%package -n typelib-1_0-GData-0_0
Summary:        Introspection bindings for libgdata
Group:          System/Libraries

%description -n typelib-1_0-GData-0_0
libgdata is a GLib-based library for accessing online service APIs using
the GData protocol — most notably, Google's services. It provides APIs
to access the common Google services, and has full asynchronous support.

This package provides the GObject Introspection bindings for the
libgdata library.

%package devel
Summary:        Development files for libgdata, a library for accessing online service APIs
Group:          Development/Libraries/GNOME
Requires:       libgdata%{_sover} = %{version}
Requires:       typelib-1_0-GData-0_0 = %{version}

%description devel
libgdata is a GLib-based library for accessing online service APIs using
the GData protocol.

This subpackage contains the header files for developing
applications that want to make use of libgdata.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson \
	-Dalways_build_tests=false \
	-Dinstalled_tests=false \
	-Dgtk_doc=true \
	-Dvapi=true \
	-Doauth1=enabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang gdata

%post -n libgdata%{_sover} -p /sbin/ldconfig
%postun -n libgdata%{_sover} -p /sbin/ldconfig

%files -n libgdata%{_sover}
%license COPYING
%doc AUTHORS HACKING NEWS README
%{_libdir}/%{name}.so.*

%files -n typelib-1_0-GData-0_0
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files devel
%{_includedir}/libgdata/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgdata.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/gdata/
%{_datadir}/vala/vapi/%{name}.*

%files lang -f gdata.lang

%changelog
