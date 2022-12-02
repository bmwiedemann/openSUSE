#
# spec file for package pango
#
# Copyright (c) 2022 SUSE LLC
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


Name:           pango
Version:        1.50.12
Release:        0
Summary:        Library for Layout and Rendering of Text
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://pango.gnome.org/
Source0:        %{name}-%{version}.tar.xz
Source2:        macros.pango
Source99:       baselibs.conf

BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  meson >= 0.55.3
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.12.10
BuildRequires:  pkgconfig(fontconfig) >= 2.13
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi) >= 1.0.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-2.0) >= 2.59.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(harfbuzz) >= 2.6
BuildRequires:  pkgconfig(libthai) >= 0.1.9
BuildRequires:  pkgconfig(xft) >= 2.0.0
BuildRequires:  pkgconfig(xrender)

%description
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

%package -n libpango-1_0-0
Summary:        Library for Layout and Rendering of Text
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      pango-modules < %{version}
Provides:       pango-modules = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      pango-64bit
%endif
#

%description -n libpango-1_0-0
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

%package -n typelib-1_0-Pango-1_0
Summary:        Introspection bindings for pango, a library for text layout and rendering
Group:          System/Libraries

%description -n typelib-1_0-Pango-1_0
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This package provides the GObject Introspection bindings for Pango.

%package tools
Summary:        Tools for pango, a library for text layout and rendering
Group:          System/Libraries

%description tools
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

%package devel
Summary:        Development files for pango, a library for text layout and rendering
Group:          Development/Libraries/GNOME
Requires:       libpango-1_0-0 = %{version}
Requires:       typelib-1_0-Pango-1_0 = %{version}
Provides:       pango-doc = %{version}
Obsoletes:      pango-doc < %{version}
# bug437293
%ifarch ppc64
Obsoletes:      pango-devel-64bit
%endif

%description devel
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%autosetup -p1

%build
%meson \
	-Dintrospection=enabled \
	-Dinstall-tests=false \
	%{nil}
%meson_build

%install
%meson_install

# Install rpm macros
mkdir -p %{buildroot}%_rpmmacrodir
cp %{SOURCE2} %{buildroot}%_rpmmacrodir

%ldconfig_scriptlets -n libpango-1_0-0

%files -n libpango-1_0-0
%license COPYING
%doc NEWS README.md
%{_libdir}/libpango-1.0.so.*
%{_libdir}/libpangocairo-1.0.so.*
%{_libdir}/libpangoft2-1.0.so.*
%{_libdir}/libpangoxft-1.0.so.*

%files -n typelib-1_0-Pango-1_0
%{_libdir}/girepository-1.0/Pango-1.0.typelib
%{_libdir}/girepository-1.0/PangoCairo-1.0.typelib
%{_libdir}/girepository-1.0/PangoFT2-1.0.typelib
%{_libdir}/girepository-1.0/PangoXft-1.0.typelib
%{_libdir}/girepository-1.0/PangoFc-1.0.typelib
%{_libdir}/girepository-1.0/PangoOT-1.0.typelib

%files tools
%{_bindir}/pango-list
%{_bindir}/pango-segmentation
%{_bindir}/pango-view
%{_mandir}/man1/pango-view.1%{ext_man}

%files devel
%doc CODING_STYLE.md THANKS
%_rpmmacrodir/macros.pango
%{_includedir}/pango-1.0/
%{_libdir}/libpango-1.0.so
%{_libdir}/libpangocairo-1.0.so
%{_libdir}/libpangoft2-1.0.so
%{_libdir}/libpangoxft-1.0.so
%{_libdir}/pkgconfig/pango.pc
%{_libdir}/pkgconfig/pangocairo.pc
%{_libdir}/pkgconfig/pangoft2.pc
%{_libdir}/pkgconfig/pangoxft.pc
%{_libdir}/pkgconfig/pangofc.pc
%{_libdir}/pkgconfig/pangoot.pc
%{_datadir}/gir-1.0/Pango-1.0.gir
%{_datadir}/gir-1.0/PangoCairo-1.0.gir
%{_datadir}/gir-1.0/PangoFT2-1.0.gir
%{_datadir}/gir-1.0/PangoFc-1.0.gir
%{_datadir}/gir-1.0/PangoOT-1.0.gir
%{_datadir}/gir-1.0/PangoXft-1.0.gir

%changelog
