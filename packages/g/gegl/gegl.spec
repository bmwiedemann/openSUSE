#
# spec file for package gegl
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


# This is based on the ExcludeArch in https://build.opensuse.org/package/show/openSUSE:Factory/luajit
%ifarch riscv64 ppc64 ppc64le
%bcond_with    luajit
%else
%bcond_without luajit
%endif

%bcond_with gegl_docs

Name:           gegl
Version:        0.4.40
Release:        0
Summary:        Generic Graphics Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://gegl.org/
Source0:        https://download.gimp.org/pub/gegl/0.4/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  ImageMagick
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel >= 1.32.0
BuildRequires:  gtk-doc
BuildRequires:  libSDL2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libspiro-devel
BuildRequires:  libstdc++-devel
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  suitesparse-devel
BuildRequires:  pkgconfig(OpenEXR) >= 1.6.1
BuildRequires:  pkgconfig(babl) >= 0.1.90
BuildRequires:  pkgconfig(cairo) >= 1.12.2
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavutil) >= 55.92.100
BuildRequires:  pkgconfig(libpng) >= 1.6.0
BuildRequires:  pkgconfig(libraw) >= 0.15.4
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.0
BuildRequires:  pkgconfig(libv4l2) >= 1.0.1
BuildRequires:  pkgconfig(libwebp) >= 0.5.0
%if %{with luajit}
BuildRequires:  pkgconfig(luajit)
%endif
# TODO: BuildRequires:  pkgconfig(mrg)
# TODO: BuildRequires:  pkgconfig(maxflow)
BuildRequires:  pkgconfig(pango) >= 1.38.0
BuildRequires:  pkgconfig(pangocairo) >= 1.38.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.71.0
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(vapigen) >= 0.20.0
# since version 0.3.5, we no longer provide an orig-addon package, as ffmpeg/libav
# exists in Tumbleweed and we use it to build
Provides:       %{name}-0_3-orig-addon = %{version}
Obsoletes:      %{name}-0_3-orig-addon < 0.3.5
# Since 13/02/18 (version 0.3.28) gegl-unstable is obsolete, gegl is now on "0.4" branch.
Provides:       gegl-unstable = %{version}
Obsoletes:      gegl-unstable < 0.3.28

%description
GEGL provides infrastructure to do demand based cached non destructive
image editing on larger than RAM buffers. Through babl, it provides
support for a wide range of color models and pixel storage formats for
input and output.

%package -n %{name}-0_4
Summary:        Generic Graphics Library
Group:          System/Libraries

%description -n %{name}-0_4
GEGL provides infrastructure to do demand based cached non destructive
image editing on larger than RAM buffers. Through babl, it provides
support for a wide range of color models and pixel storage formats for
input and output.

%package -n libgegl-0_4-0
Summary:        Generic Graphics Library
# The plugins are required for the lib to be usable
Group:          System/Libraries
Requires:       %{name}-0_4 >= %{version}

%description -n libgegl-0_4-0
GEGL provides infrastructure to do demand based cached non destructive
image editing on larger than RAM buffers. Through babl, it provides
support for a wide range of color models and pixel storage formats for
input and output.

%package -n typelib-1_0-Gegl-0_4
Summary:        Introspection bindings for the GEGL "Generic Graphics Library"
Group:          System/Libraries

%description -n typelib-1_0-Gegl-0_4
GEGL provides infrastructure to do demand based cached non destructive
image editing on larger than RAM buffers. Through babl, it provides
support for a wide range of color models and pixel storage formats for
input and output.

This package provides the GObject Introspection bindings for the
libgegl library.

%package devel
Summary:        Development files for the GEGL "Generic Graphics Library"
Group:          Development/Libraries/C and C++
Requires:       libgegl-0_4-0 = %{version}
Requires:       typelib-1_0-Gegl-0_4 = %{version}

%description devel
GEGL provides infratructure to do demand based cached non destructive
image editing on larger than RAM buffers. Through babl, it provides
support for a wide range of color models and pixel storage formats for
input and output.

%package doc
Summary:        Documentation for the GEGL "Generic Graphics Library"
Group:          Documentation/HTML

%description doc
GEGL provides infrastructure to do demand based cached non destructive
image editing on larger than RAM buffers. Through babl, it provides
support for a wide range of color models and pixel storage formats for
input and output.

%lang_package -n %{name}-0_4

%prep
%autosetup -p1

%build
%ifarch aarch64
export LD_PRELOAD="/usr/lib64/libgomp.so.1"
%endif
%meson \
	-Dmrg=disabled \
	-Dmaxflow=disabled \
	%if ! %{with luajit}
	-Dlua=disabled \
	%endif
	-Dworkshop=true \
	-Djasper=disabled \
%if %{with gegl_docs}
	-Ddocs=true \
%else
	-Ddocs=false \
%endif
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-0.4 %{?no_lang_C}

%post -n gegl-0_4 -p /sbin/ldconfig
%postun -n gegl-0_4 -p /sbin/ldconfig

%post -n libgegl-0_4-0 -p /sbin/ldconfig
%postun -n libgegl-0_4-0 -p /sbin/ldconfig

%files
%{_bindir}/gegl
%{_bindir}/gegl-imgcmp

%files -n %{name}-0_4
%dir %{_libdir}/gegl-0.4/
%{_libdir}/gegl-0.4/*.so
# libgegl-sc-0.4.so is a support library for the seamless-clone module
%{_libdir}/libgegl-sc-0.4.so
%{_libdir}/libgegl-npd-0.4.so
%{_libdir}/gegl-0.4/grey2.json
%{_libdir}/gegl-0.4/dropshadow2.json
%if %{with luajit}
# lua files
%dir %{_datadir}/gegl-0.4/
%{_datadir}/gegl-0.4/lua/
%endif

%files -n libgegl-0_4-0
%license COPYING COPYING.LESSER
%{_libdir}/libgegl-0.4.so.*

%files -n typelib-1_0-Gegl-0_4
%{_libdir}/girepository-1.0/Gegl-0.4.typelib

%files devel
%{_includedir}/gegl-0.4/
%{_libdir}/libgegl-0.4.so
%{_libdir}/pkgconfig/gegl-0.4.pc
%{_libdir}/pkgconfig/gegl-sc-0.4.pc
%{_datadir}/gir-1.0/Gegl-0.4.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gegl-0.4.deps
%{_datadir}/vala/vapi/gegl-0.4.vapi

%files doc
%doc AUTHORS docs/ChangeLog NEWS
%if %{with gegl_docs}
%doc %{_datadir}/gtk-doc/html/gegl/
%endif

%files -n %{name}-0_4-lang -f %{name}-0.4.lang

%changelog
