#
# spec file for package graphene
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


Name:           graphene
Version:        1.10.0
Release:        0
Summary:        Thin type layer for graphic libraries
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://ebassi.github.io/graphene/
Source:         https://download.gnome.org/sources/graphene/1.10/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.0

%description
The Graphene library provides types and their relative API for affine
matrices, 4×4 matrices, projections, transformations, vectors and
quaternions.

%package -n libgraphene-1_0-0
Summary:        Thin type layer for graphic libraries
Group:          System/Libraries

%description -n libgraphene-1_0-0
When creating graphic libraries you most likely end up dealing with points
and rectangles. If you're particularly unlucky, you may end up dealing
with affine matrices and 2D transformations. If you're writing a graphic
library with 3D transformations, though, you are going to hit the jackpot:
4x4 matrices, projections, transformations, vectors, and quaternions.

This library provides types and their relative API; it does not deal with
windowing system surfaces, drawing, scene graphs, or input. You're
supposed to do that yourself, in your own canvas implementation, which is
the whole point of writing the library in the first place.

%package -n typelib-1_0-Graphene-1_0
Summary:        GObject introspection for libgraphene, a thin type layer for graphic libraries
Group:          System/Libraries

%description -n typelib-1_0-Graphene-1_0
The Graphene library provides types and their relative API for affine
matrices, 4×4 matrices, projections, transformations, vectors and
quaternions.

%package -n libgraphene-devel
Summary:        Development files for libgraphene, a thin type layer for graphic libraries
Group:          Development/Languages/C and C++
Requires:       libgraphene-1_0-0 = %{version}
Requires:       typelib-1_0-Graphene-1_0 = %{version}

%description -n libgraphene-devel
The Graphene library provides types and their relative API for affine
matrices, 4×4 matrices, projections, transformations, vectors and
quaternions.

This subpackage contains the development files for the Graphene library.

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	-Dgobject_types=true \
	-Dintrospection=true \
	-Dgcc_vector=true \
	-Dsse2=true \
	-Darm-neon=true \
	-Dtests=true \
	-Dbenchmarks=true \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_libdir}/pkgconfig

%check
%meson_test

%post   -n libgraphene-1_0-0 -p /sbin/ldconfig
%postun -n libgraphene-1_0-0 -p /sbin/ldconfig

%files -n libgraphene-1_0-0
%license LICENSE.txt
%{_libdir}/libgraphene-1.0.so.*

%files -n typelib-1_0-Graphene-1_0
%{_libdir}/girepository-1.0/Graphene-1.0.typelib

%files -n libgraphene-devel
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/graphene-1.0/
%{_libexecdir}/installed-tests/
%{_libdir}/libgraphene-1.0.so
%{_libdir}/pkgconfig/graphene-1.0.pc
%{_libdir}/pkgconfig/graphene-gobject-1.0.pc
%dir %{_libdir}/graphene-1.0
%dir %{_libdir}/graphene-1.0/include
%{_libdir}/graphene-1.0/include/graphene-config.h
%{_datadir}/gir-1.0/Graphene-1.0.gir
%dir %{_datadir}/installed-tests
%dir %{_datadir}/installed-tests/graphene-1.0
%{_datadir}/installed-tests/graphene-1.0/*

%changelog
