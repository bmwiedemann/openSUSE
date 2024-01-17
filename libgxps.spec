#
# spec file for package libgxps
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libgxps
Version:        0.3.2+5
Release:        0
Summary:        Library for rendering XPS documents
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/libgxps
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.43.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.24
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(gobject-2.0) >= 2.24
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libarchive) >= 2.8.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%package -n libgxps2
Summary:        Library for rendering XPS documents
Group:          System/Libraries

%description -n libgxps2
libgxps is a GObject based library for handling and rendering XPS
documents.

%package -n typelib-1_0-GXPS-0_1
Summary:        Library for rendering XPS documents -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GXPS-0_1
libgxps is a GObject based library for handling and rendering XPS
documents.

This package provides the GObject Introspection bindings for libgxps.

%package tools
Summary:        Tools for rendering XPS documents
Group:          Productivity/Publishing/Other

%description tools
libgxps is a GObject based library for handling and rendering XPS
documents.

%package devel
Summary:        Development files for libgxps, a XPS document render library
Group:          Development/Libraries/C and C++
Requires:       libgxps2 = %{version}
Requires:       typelib-1_0-GXPS-0_1 = %{version}

%description devel
libgxps is a GObject based library for handling and rendering XPS
documents.

%prep
%autosetup -p1

%build
%meson \
	-Denable-gtk-doc=true \
	-Denable-man=true \
	-Denable-test=false \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libgxps2

%files -n libgxps2
%license COPYING
%{_libdir}/libgxps.so.2*

%files -n typelib-1_0-GXPS-0_1
%{_libdir}/girepository-1.0/GXPS-0.1.typelib

%files tools
%{_bindir}/xpstojpeg
%{_bindir}/xpstopdf
%{_bindir}/xpstopng
%{_bindir}/xpstops
%{_bindir}/xpstosvg
%{_mandir}/man1/xpstojpeg.1%{?ext_man}
%{_mandir}/man1/xpstopdf.1%{?ext_man}
%{_mandir}/man1/xpstopng.1%{?ext_man}
%{_mandir}/man1/xpstops.1%{?ext_man}
%{_mandir}/man1/xpstosvg.1%{?ext_man}

%files devel
%doc AUTHORS NEWS README
%doc %{_datadir}/gtk-doc/html/libgxps/
%{_includedir}/libgxps/
%{_libdir}/libgxps.so
%{_libdir}/pkgconfig/libgxps.pc
%{_datadir}/gir-1.0/GXPS-0.1.gir

%changelog
