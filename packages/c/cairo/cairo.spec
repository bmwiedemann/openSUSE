#
# spec file for package cairo
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


%define build_xcb_backend 1

Name:           cairo
Version:        1.17.8
Release:        0
Summary:        Vector Graphics Library with Cross-Device Output Support
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          Development/Libraries/C and C++
URL:            https://cairographics.org/
Source0:        https://cairographics.org/snapshots/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

# PATCH-FIX-UPSTREAM cairo-xlib-endianness.patch fdo#63461 bnc#882951 fcrozat@suse.com -- Fix crash when client and server have different endianness
Patch0:         cairo-xlib-endianness.patch
# PATCH-FIX-UPSTREAM cairo-get_bitmap_surface-bsc1036789-CVE-2017-7475.diff alarrosa@suse.com -- Fix segfault in get_bitmap_surface
Patch1:         cairo-get_bitmap_surface-bsc1036789-CVE-2017-7475.diff
# PATCH-FIX-UPSTREAM cairo-1.17.8-fix-tee-compilation.patch --  https://gitlab.freedesktop.org/cairo/cairo/-/issues/634 tee: Fix cairo wrapper functions
Patch2:         cairo-1.17.8-fix-tee-compilation.patch
# PATCH-FIX-UPSTREAM cairo-1.17.8-ft-font-missing-glyph.patch -- https://gitlab.freedesktop.org/cairo/cairo/-/merge_requests/467 ft: Use normal font size when detecting the format
Patch3:         cairo-1.17.8-ft-font-missing-glyph.patch

BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1) >= 0.36.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
# These libraries are needed only for tests.
# Do not enable tests in build systems, it causes build loop!
#BuildRequires:  librsvg-devel poppler-devel
%if %{build_xcb_backend}
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xcb-render) >= 1.6
BuildRequires:  pkgconfig(xcb-shm)
%endif

%description
Cairo is a vector graphics library with cross-device output support.
Currently supported output targets include the X Window System,
in-memory image buffers, and PostScript. Cairo is designed to produce
identical output on all output media while taking advantage of display
hardware acceleration when available.

%package -n libcairo2
Summary:        Vector Graphics Library with Cross-Device Output Support
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          System/Libraries
Provides:       cairo = %{version}
Obsoletes:      cairo < %{version}

%description -n libcairo2
Cairo is a vector graphics library with cross-device output support.
Currently supported output targets include the X Window System,
in-memory image buffers, and PostScript. Cairo is designed to produce
identical output on all output media while taking advantage of display
hardware acceleration when available.

%package -n libcairo-gobject2
Summary:        Vector Graphics Library with Cross-Device Output Support
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          System/Libraries

%description -n libcairo-gobject2
Cairo is a vector graphics library with cross-device output support.
Currently supported output targets include the X Window System,
in-memory image buffers, and PostScript. Cairo is designed to produce
identical output on all output media while taking advantage of display
hardware acceleration when available.

This library contains GType declarations for Cairo types. It is also
meant to support gobject-introspection binding creation.

%package -n libcairo-script-interpreter2
Summary:        Vector Graphics Library with Cross-Device Output Support
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          System/Libraries

%description -n libcairo-script-interpreter2
Cairo is a vector graphics library with cross-device output support.
Currently supported output targets include the X Window System,
in-memory image buffers, and PostScript. Cairo is designed to produce
identical output on all output media while taking advantage of display
hardware acceleration when available.

%package tools
Summary:        Utilities for cairo, a Vector Graphics Library with Cross-Device Output Support
# We need an explicit requires since nothing links to the cairo library
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
Requires:       libcairo2 = %{version}
# Named changed during  development of 11.4
Provides:       %{name}-utils = %{version}
Obsoletes:      %{name}-utils < %{version}

%description tools
Cairo is a vector graphics library with cross-device output support.
Currently supported output targets include the X Window System,
in-memory image buffers, and PostScript. Cairo is designed to produce
identical output on all output media while taking advantage of display
hardware acceleration when available.

This package contains various cairo utilities.

%package devel
Summary:        Development environment for cairo
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          Development/Libraries/X11
Requires:       libcairo-gobject2 = %{version}
Requires:       libcairo-script-interpreter2 = %{version}
Requires:       libcairo2 = %{version}
Provides:       cairo-doc = %{version}
Obsoletes:      cairo-doc < %{version}

%description devel
This package contains all files necessary to build binaries using
cairo.

%prep
%autosetup -p1

%build
%meson \
%if %{build_xcb_backend}
	-D xcb=enabled \
%endif
	-D freetype=enabled \
	-D fontconfig=enabled \
	-D glib=enabled \
	-D gtk_doc=true \
	-D spectre=disabled \
	-D symbol-lookup=disabled \
	-D tee=enabled \
	-D tests=disabled \
	-D xlib=enabled \
	-D xml=disabled
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libcairo2
%ldconfig_scriptlets -n libcairo-gobject2
%ldconfig_scriptlets -n libcairo-script-interpreter2

%files -n libcairo2
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{_libdir}/libcairo.so.*

%files -n libcairo-gobject2
%{_libdir}/libcairo-gobject.so.2*

%files -n libcairo-script-interpreter2
%license util/cairo-script/COPYING
%{_libdir}/libcairo-script-interpreter.so.*

%files tools
%license util/cairo-trace/COPYING util/cairo-trace/COPYING-GPL-3
%{_bindir}/cairo-sphinx
%{_bindir}/cairo-trace
%dir %{_libdir}/cairo
%{_libdir}/cairo/libcairo-fdr.so
%{_libdir}/cairo/libcairo-sphinx.so
%{_libdir}/cairo/libcairo-trace.so

%files devel
%doc AUTHORS NEWS README.md
%doc %{_datadir}/gtk-doc/html/cairo
%{_includedir}/cairo/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
