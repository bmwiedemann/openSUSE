#
# spec file for package libdazzle
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


Name:           libdazzle
Version:        3.34.1
Release:        0
Summary:        Collection of fancy features for GLib and Gtk+
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://gitlab.gnome.org/GNOME/libdazzle
Source0:        https://download.gnome.org/sources/libdazzle/3.34/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.55.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:  pkgconfig(vapigen)

%description
This library is a companion library to GObject and Gtk+.
It provides various features that are wished in the underlying
library but are not for various reasons. In most cases, they are
wildly out of scope for those libraries. In other cases, the design
isn't quite generic enough to work for everyone.

%package -n     dazzle-list-counters
Summary:        Collection of fancy features for GLib and Gtk+
Group:          Development/Tools/Other

%description -n dazzle-list-counters
This package provides the dazzle-list-counters binary.


%package -n     libdazzle-1_0-0
Summary:        Collection of fancy features for GLib and Gtk+ -- Library file
Group:          System/Libraries

%description -n libdazzle-1_0-0
This library is a companion library to GObject and Gtk+.
It provides various features that are wished in the underlying
library but are not for various reasons. In most cases, they are
wildly out of scope for those libraries. In other cases, the design
isn't quite generic enough to work for everyone.

This package provides the libdazzle shared library.

%package -n     typelib-1_0-libdazzle-1_0
Summary:        Collection of fancy features for GLib and Gtk+ -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-libdazzle-1_0
This library is a companion library to GObject and Gtk+.
It provides various features that are wished in the underlying
library but are not for various reasons. In most cases, they are
wildly out of scope for those libraries. In other cases, the design
isn't quite generic enough to work for everyone..

This package provides the GObject Introspection bindings for libdazzle.

%package        devel
Summary:        Collection of fancy features for GLib and Gtk+ -- Development Files
Group:          Development/Tools/Other
Requires:       dazzle-list-counters = %{version}
Requires:       libdazzle-1_0-0 = %{version}
Requires:       typelib-1_0-libdazzle-1_0 = %{version}

%description    devel
This library is a companion library to GObject and Gtk+.
It provides various features that are wished in the underlying
library but are not for various reasons. In most cases, they are
wildly out of scope for those libraries. In other cases, the design
isn't quite generic enough to work for everyone. -- Development Files

This package provides the development files, and its documentation, for libdazzle.

%prep
%autosetup -p1

%build
%meson \
	-Denable_tracing=false \
	-Denable_profiling=false \
	-Denable_rdtscp=false \
	-Denable_tools=true \
	-Dwith_introspection=true \
	-Dwith_vapi=true \
	-Denable_gtk_doc=true \
	-Denable_tests=false \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install

%post -n libdazzle-1_0-0 -p /sbin/ldconfig
%postun -n libdazzle-1_0-0 -p /sbin/ldconfig

%files -n dazzle-list-counters
%doc NEWS README.md
%{_bindir}/dazzle-list-counters

%files -n libdazzle-1_0-0
%license COPYING
%{_libdir}/libdazzle-1.0.so.*

%files -n typelib-1_0-libdazzle-1_0
%{_libdir}/girepository-1.0/Dazzle-1.0.typelib

%files devel
%doc AUTHORS CONTRIBUTING.md
%doc %{_datadir}/gtk-doc/html/libdazzle/
%{_includedir}/libdazzle-1.0/
%{_datadir}/gir-1.0/Dazzle-1.0.gir
%{_libdir}/libdazzle-1.0.so
%{_libdir}/pkgconfig/libdazzle-1.0.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libdazzle-1.0.deps
%{_datadir}/vala/vapi/libdazzle-1.0.vapi

%changelog
