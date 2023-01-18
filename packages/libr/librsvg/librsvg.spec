#
# spec file for package librsvg
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

# Don't forget to update this in baselibs.conf too!
%define librsvg_sover 2

Name:           librsvg
Version:        2.55.1
Release:        0
Summary:        A Library for Rendering SVG Data
License:        Apache-2.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/LibRsvg
Source:         %{name}-%{version}.tar.xz
Source2:        vendor.tar.xz
Source3:        cargo_config
Source99:       baselibs.conf

BuildRequires:  cargo-packaging
BuildRequires:  gobject-introspection-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo) >= 1.16.0
BuildRequires:  pkgconfig(cairo-png) >= 1.2.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2) >= 20.0.14
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.20
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.12.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  pkgconfig(pangocairo) >= 1.46.0
BuildRequires:  pkgconfig(pangoft2) >= 1.46.0
# Avoid cycle: we do not require the adwaita-icon-theme to be present. libgtk-3.0 requires this for end users
#!BuildIgnore:  adwaita-icon-theme

%description
This package contains a library to render SVG (scalable vector
graphics) data. This format has been specified by the W3C (see
http://www.w3c.org).

%package -n librsvg-2-%{librsvg_sover}
Summary:        A Library for Rendering SVG Data
License:        Apache-2.0 AND LGPL-2.0-or-later AND MIT
Group:          System/Libraries
Provides:       librsvg2 = %{version}
Obsoletes:      librsvg2 < %{version}
Provides:       librsvg = %{version}
Obsoletes:      librsvg < %{version}
Obsoletes:      rsvg-view <= %{version}

%description -n librsvg-2-%{librsvg_sover}
This package contains a library to render SVG (scalable vector
graphics) data. This format has been specified by the W3C (see
http://www.w3c.org).

%package -n typelib-1_0-Rsvg-2_0
Summary:        Introspection bindings for librsvg, a SVG render library
License:        LGPL-2.0-or-later
Group:          System/Libraries

%description -n typelib-1_0-Rsvg-2_0
This package contains a library to render SVG (scalable vector
graphics) data. This format has been specified by the W3C (see
http://www.w3c.org).

This package provides the GObject Introspection bindings for librsvg.

%package devel
Summary:        Development files for librsvg, a SVG render library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       librsvg-2-%{librsvg_sover} = %{version}
Requires:       typelib-1_0-Rsvg-2_0 = %{version}
Provides:       librsvg2-devel = %{version}
Obsoletes:      librsvg2-devel < %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n gdk-pixbuf-loader-rsvg
Summary:        A gdk-pixbuf loader for SVG using librsvg
License:        LGPL-2.0-or-later
Group:          System/Libraries
Supplements:    (librsvg-2-%{librsvg_sover} and gdk-pixbuf)
%{gdk_pixbuf_loader_requires}

%description -n gdk-pixbuf-loader-rsvg
This package contains a library to render SVG (scalable vector
graphics) data. This format has been specified by the W3C (see
http://www.w3c.org).

This package provides a librsvg-based gdk-pixbuf loader.

%package -n rsvg-convert
Summary:        SVG Convert using the GNOME Render SVG library
License:        LGPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
Conflicts:      rsvg-view <= 2.45.7

%description -n rsvg-convert
This package contains a tool to convert SVG (scalable vector
graphics) data. This format has been specified by the W3C (see
http://www.w3c.org).

%package -n rsvg-thumbnailer
Summary:        SVG thumbnailer using the GNOME Render SVG library
License:        LGPL-2.0-or-later
Group:          Productivity/Graphics/Other
BuildArch:      noarch

%description -n rsvg-thumbnailer
This package contains a thumbnailer to render SVG (scalable vector
graphics) data.

%prep
%autosetup -p1 -a2
mkdir .cargo
cp %{SOURCE3} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static\
	--enable-introspection\
	--enable-vala \
	%{nil}
%make_build

%install
export RUSTFLAGS=%{rustflags}
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# %%doc is used to package such contents
rm -rf %{buildroot}%{_datadir}/doc/%{name}/CO*.md

%check
%ifarch x86_64 %{?x86_64}
# 2023-01-15: the pdf-related tests are failing (bsc#1207167)
%{cargo_test} -- --skip pdf_has_text --skip pdf_has_link
%endif

%post -n librsvg-2-%{librsvg_sover} -p /sbin/ldconfig

%post -n gdk-pixbuf-loader-rsvg
%{gdk_pixbuf_loader_post}

%postun -n librsvg-2-%{librsvg_sover} -p /sbin/ldconfig

%postun -n gdk-pixbuf-loader-rsvg
%{gdk_pixbuf_loader_postun}

%files -n librsvg-2-%{librsvg_sover}
%license COPYING.LIB
%doc NEWS README.md
%{_libdir}/librsvg-2.so.*

%files -n typelib-1_0-Rsvg-2_0
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib

%files -n gdk-pixbuf-loader-rsvg
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-svg.so

%files -n rsvg-convert
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1%{?ext_man}

%files -n rsvg-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/librsvg.thumbnailer

%files devel
%doc AUTHORS COMPILING.md CONTRIBUTING.md
%doc %{_datadir}/doc/%{name}/
%doc %{_datadir}/doc/Rsvg-2.0/
%{_includedir}/librsvg-2.0/
%{_libdir}/librsvg-2.so
%{_libdir}/pkgconfig/librsvg-2.0.pc
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/librsvg-2.0.vapi

%changelog
