#
# spec file for package libgit2-glib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           libgit2-glib
Version:        0.28.0.1
Release:        0
Summary:        GLib wrapper library around libgit2
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/Libgit2-glib
Source0:        https://download.gnome.org/sources/libgit2-glib/0.28/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
# Needed to create the vala bindings
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:  pkgconfig(libgit2) >= 0.25.0
BuildRequires:  pkgconfig(libssh2)

%description
libgit2-glib is a GLib wrapper library around the libgit2 git access library.

%package -n libgit2-glib-1_0-0
Summary:        GLib wrapper library around libgit2
Group:          System/Libraries

%description -n libgit2-glib-1_0-0
libgit2-glib is a GLib wrapper library around the libgit2 git access library.

%package -n typelib-1_0-Ggit-1_0
Summary:        GObject introspection for libgit2-glib
Group:          System/Libraries

%description -n typelib-1_0-Ggit-1_0
libgit2-glib is a GLib wrapper library around the libgit2 git access library.

%package devel
Summary:        Development files for libgit2-glib, a GLib wrapper library around libgit2
Group:          Development/Languages/C and C++
Requires:       libgit2-glib-1_0-0 = %{version}
Requires:       typelib-1_0-Ggit-1_0 = %{version}

%description devel
libgit2-glib is a GLib wrapper library around the libgit2 git access library.

%prep
%autosetup -p1

%build
%meson \
    -D gtk_doc=true \
    -D introspection=true \
    -D python=false \
    -D ssh=true \
    -D vapi=true \
    %{nil}
%meson_build

%install
%meson_install

%post -n libgit2-glib-1_0-0 -p /sbin/ldconfig
%postun -n libgit2-glib-1_0-0 -p /sbin/ldconfig

%files -n libgit2-glib-1_0-0
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libgit2-glib-1.0.so.*

%files -n typelib-1_0-Ggit-1_0
%{_libdir}/girepository-1.0/Ggit-1.0.typelib

%files devel
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/libgit2-glib-1.0/
%{_includedir}/libgit2-glib-1.0/
%{_libdir}/libgit2-glib-1.0.so
%{_libdir}/pkgconfig/libgit2-glib-1.0.pc
%{_datadir}/gir-1.0/Ggit-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/ggit-1.0.*
%{_datadir}/vala/vapi/libgit2-glib-1.0.*

%changelog
