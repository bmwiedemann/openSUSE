#
# spec file for package librsvg
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# Don't forget to update this in baselibs.conf too!
%define librsvg_sover 2

Name:           librsvg
### FIXME ### - Please check on every versionupgrade if adwaita-fonts are still needed for tests
Version:        2.61.2
Release:        0
Summary:        A Library for Rendering SVG Data
License:        LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/LibRsvg
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source99:       baselibs.conf

# Needed for tests (pdf)
BuildRequires:  adwaita-fonts
#
BuildRequires:  cargo-c >= 0.10.12
BuildRequires:  cargo-packaging >= 1.3.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo) >= 1.18.0
BuildRequires:  pkgconfig(cairo-png) >= 1.2.0
BuildRequires:  pkgconfig(dav1d)
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

%package -n rsvg-convert
Summary:        SVG Convert using the GNOME Render SVG library
License:        LGPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
Conflicts:      rsvg-view <= 2.45.7

%description -n rsvg-convert
This package contains a tool to convert SVG (scalable vector
graphics) data. This format has been specified by the W3C (see
http://www.w3c.org).

%prep
%autosetup -p1 -a1

%build
%meson \
	-Dpixbuf-loader=disabled \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n librsvg-2-%{librsvg_sover}

%check
export LANG=C
%ifnarch %{ix86} %{arm}
%{cargo_test}
%endif

%files -n librsvg-2-%{librsvg_sover}
%license COPYING.LIB
%doc NEWS README.md
%{_libdir}/librsvg-2.so.*

%files -n typelib-1_0-Rsvg-2_0
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib

%files -n rsvg-convert
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1%{?ext_man}

%files devel
%doc AUTHORS
%doc %{_datadir}/doc/Rsvg-2.0/
%{_includedir}/librsvg-2.0/
%{_libdir}/librsvg-2.so
%{_libdir}/pkgconfig/librsvg-2.0.pc
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%{_datadir}/vala/vapi/librsvg-2.0.deps

%changelog
