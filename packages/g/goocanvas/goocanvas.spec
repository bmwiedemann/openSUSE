#
# spec file for package goocanvas
#
# Copyright (c) 2025 SUSE LLC
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


# Option to easily enable/disable introspection building.
%define with_introspection 1
Name:           goocanvas
Version:        3.0.0
Release:        0
Summary:        A Cairo-based canvas widget for GTK+
License:        LGPL-2.0-only
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/GooCanvas
Source0:        https://download.gnome.org/sources/goocanvas/3.0/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix-gcc14-build.patch -- Fix building with GCC 14
Patch1:         fix-gcc14-build.patch

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
%if %{with_introspection}
BuildRequires:  gobject-introspection-devel
%endif

%description
GooCanvas is a canvas widget for GTK+ that uses the Cairo 2D library
for drawing. It has an optional model/view split, and uses interfaces
for items and models, so any application object can be turned into a
canvas item or model.

%package devel
Summary:        Development files for GooCanvas
Group:          Development/Libraries/GNOME
Requires:       libgoocanvas-3_0-9 = %{version}
%if %{with_introspection}
Requires:       typelib-1_0-GooCanvas-3_0 = %{version}
%endif

%description devel
GooCanvas is a canvas widget for GTK+ that uses the Cairo 2D library
for drawing.

This subpackage contains the header files for developing
applications that want to make use of libgoocanvas.

%package -n libgoocanvas-3_0-9
Summary:        A Cairo-based canvas widget for GTK+
# Needed to make lang package installable
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgoocanvas-3_0-9
GooCanvas is a canvas widget for GTK+ that uses the Cairo 2D library
for drawing. It has an optional model/view split, and uses interfaces
for items and models, so any application object can be turned into a
canvas item or model.

%if %{with_introspection}
%package -n typelib-1_0-GooCanvas-3_0
Summary:        Introspection bindings for GooCanvas
Group:          System/Libraries

%description -n typelib-1_0-GooCanvas-3_0
GooCanvas is a canvas widget for GTK+ that uses the Cairo 2D library
for drawing.

This package provides the GObject Introspection bindings for GooCanvas.
%endif

%lang_package

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
%if %{with_introspection}
    --enable-introspection
%else
    --disable-introspection
%endif
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.*a
%find_lang goocanvas3

%ldconfig_scriptlets -n libgoocanvas-3_0-9

%files -n libgoocanvas-3_0-9
%doc AUTHORS NEWS README TODO
%{_libdir}/*.so.*

%if %{with_introspection}
%files -n typelib-1_0-GooCanvas-3_0
%{_libdir}/girepository-1.0/GooCanvas-3.0.typelib
%endif

%files devel
%{_includedir}/%{name}-3.0/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%if %{with_introspection}
%{_datadir}/gir-1.0/GooCanvas-3.0.gir
%endif
%doc %{_datadir}/gtk-doc/

%files lang -f goocanvas3.lang

%changelog
