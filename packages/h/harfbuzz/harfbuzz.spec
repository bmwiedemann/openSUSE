#
# spec file for package harfbuzz
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


Name:           harfbuzz
Version:        2.7.2
Release:        0
Summary:        An OpenType text shaping engine
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/HarfBuzz
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.8.0
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(freetype2) >= 12.0.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.19.1
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(icu-uc)
Conflicts:      cantarell-fonts < 0.0.23

%description
HarfBuzz is an OpenType text shaping engine.

%package -n libharfbuzz0
Summary:        An OpenType text shaping engine

%description -n libharfbuzz0
HarfBuzz is an OpenType text shaping engine.

%package -n libharfbuzz-icu0
Summary:        ICU integration into the HarfBuzz OpenType text shaping engine

%description -n libharfbuzz-icu0
HarfBuzz is an OpenType text shaping engine.
This package contains the ICU library.

%package -n libharfbuzz-gobject0
Summary:        GObject wrapper around the HarfBuzz OpenType text shaping engine

%description -n libharfbuzz-gobject0
HarfBuzz is an OpenType text shaping engine.
This package contains the GObject library.

%package -n libharfbuzz-subset0
Summary:        An OpenType text shaping engine

%description -n libharfbuzz-subset0
HarfBuzz is an OpenType text shaping engine.
This package contains the subset library

%package -n typelib-1_0-HarfBuzz-0_0
Summary:        Introspection bindings for the HarfBuzz/GObject library

%description -n typelib-1_0-HarfBuzz-0_0
HarfBuzz is an OpenType text shaping engine.
This package provides the GObject Introspection bindings for HarfBuzz.

%package tools
Summary:        Tools from the HarfBuzz text shaping software

%description tools
HarfBuzz is an OpenType text shaping engine.
This package provides a set of tools for HarfBuzz.

%package devel
Summary:        Development files for the HarfBuzz OpenType text shaping engine
Requires:       libharfbuzz-gobject0 = %{version}
Requires:       libharfbuzz-icu0 = %{version}
Requires:       libharfbuzz-subset0 = %{version}
Requires:       libharfbuzz0 = %{version}
Requires:       typelib-1_0-HarfBuzz-0_0 = %{version}
Requires:       pkgconfig(freetype2) >= 12.0.6

%description devel
HarfBuzz is an OpenType text shaping engine.
This package contains the development files.

%prep
%autosetup

%build
%configure \
	--disable-static \
	--with-glib \
	--with-freetype \
	--with-cairo \
	--with-icu \
	--with-graphite2 \
	--with-gobject=yes \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libharfbuzz0 -p /sbin/ldconfig
%postun -n libharfbuzz0 -p /sbin/ldconfig
%post -n libharfbuzz-icu0 -p /sbin/ldconfig
%postun -n libharfbuzz-icu0 -p /sbin/ldconfig
%post -n libharfbuzz-gobject0 -p /sbin/ldconfig
%postun -n libharfbuzz-gobject0 -p /sbin/ldconfig
%post -n libharfbuzz-subset0 -p /sbin/ldconfig
%postun -n libharfbuzz-subset0 -p /sbin/ldconfig

%files -n libharfbuzz0
%license COPYING
%doc NEWS
%{_libdir}/libharfbuzz.so.0*

%files -n libharfbuzz-icu0
%{_libdir}/libharfbuzz-icu.so.0*

%files -n libharfbuzz-gobject0
%{_libdir}/libharfbuzz-gobject.so.0*

%files -n libharfbuzz-subset0
%{_libdir}/libharfbuzz-subset.so.0*

%files -n typelib-1_0-HarfBuzz-0_0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib

%files tools
%{_bindir}/hb-ot-shape-closure
%{_bindir}/hb-shape
%{_bindir}/hb-view
%{_bindir}/hb-subset

%files devel
%doc AUTHORS README THANKS
%docdir %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/html/harfbuzz/
%{_includedir}/harfbuzz/
%{_libdir}/*.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/pkgconfig/harfbuzz-gobject.pc
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/harfbuzz
%{_libdir}/cmake/harfbuzz/harfbuzz-config.cmake

%changelog
