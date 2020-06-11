#
# spec file for package cogl
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


%define with_GLES2 1
%define with_COGLGST 0
Name:           cogl
Version:        1.22.8
Release:        0
Summary:        An object oriented GL/GLES Abstraction/Utility Layer
License:        MIT
Group:          Development/Libraries/GNOME
URL:            http://clutter-project.org/
Source0:        https://download.gnome.org/sources/cogl/1.22/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  gtk-doc >= 1.13
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.10
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pangocairo) >= 1.20
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite) >= 0.4
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes) >= 3
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr) >= 1.2
%if %{with_COGLGST}
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
%endif

%description
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

%package -n libcogl20
Summary:        An object oriented GL/GLES Abstraction/Utility Layer
Group:          System/Libraries
Requires:       Mesa
# To make the lang package installable
Provides:       %{name} = %{version}

%description  -n libcogl20
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

%package -n libcogl-gles2-20
Summary:        OpenGL ES 2 support for the cogl GL/GLES abstraction/utility layer
Group:          System/Libraries

%description -n libcogl-gles2-20
Cogl is a library for using 3D graphics hardware to draw
pretty pictures

%package -n typelib-1_0-Cogl-1_0
Summary:        Introspection bindings for the cogl GL/GLES abstraction/utility layer
Group:          System/Libraries

%description -n typelib-1_0-Cogl-1_0
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

This package provides the GObject Introspection bindings for Cogl.

%package -n typelib-1_0-Cogl-2_0
Summary:        Introspection bindings for the cogl GL/GLES abstraction/utility layer
Group:          System/Libraries

%description -n typelib-1_0-Cogl-2_0
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

This package provides the GObject Introspection bindings for Cogl.

%package -n typelib-1_0-CoglGst-2_0
Summary:        Introspection bindings for the cogl GL/GLES abstraction/utility layer
Group:          System/Libraries

%description -n typelib-1_0-CoglGst-2_0
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

This package provides the GObject Introspection bindings for CoglGst.

%package -n libcogl-pango20
Summary:        Pango integration for the cogl GL/GLES abstraction/utility layer
Group:          System/Libraries

%description  -n libcogl-pango20
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

%package -n typelib-1_0-CoglPango-1_0
Summary:        Pango Integration, Introspection bindings for cogl
Group:          System/Libraries

%description -n typelib-1_0-CoglPango-1_0
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

This package provides the GObject Introspection bindings for the Pango
integration in Cogl.

%package -n typelib-1_0-CoglPango-2_0
Summary:        Pango Integration, Introspection bindings for cogl
Group:          System/Libraries

%description -n typelib-1_0-CoglPango-2_0
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

This package provides the GObject Introspection bindings for the Pango
integration in Cogl.

%package -n gstreamer-plugins-cogl
Summary:        Gstreamer cogl plugins
Group:          System/Libraries
Supplements:    packageand(libcogl20:gstreamer)

%description -n gstreamer-plugins-cogl
Cogl is a library for using 3D graphics hardware to draw
pretty pictures.

This package provides the Gstreamer plugings for Cogl.

%package devel
Summary:        Development files for the cogl GL/GLES abstraction/utility layer
# cogl-defines.h includes GL/gl.h
Group:          Development/Libraries/GNOME
Requires:       Mesa-devel
Requires:       libcogl-pango20 = %{version}
Requires:       libcogl20 = %{version}
Requires:       typelib-1_0-Cogl-1_0 = %{version}
Requires:       typelib-1_0-Cogl-2_0 = %{version}
Requires:       typelib-1_0-CoglPango-1_0 = %{version}
Requires:       typelib-1_0-CoglPango-2_0 = %{version}
%if %{with_GLES2}
Requires:       libcogl-gles2-20 = %{version}
%endif
%if %{with_COGLGST}
Requires:       gstreamer-plugins-cogl = %{version}
%endif
%if %{with_COGLGST}
Requires:       typelib-1_0-CoglGst-2_0 = %{version}
%endif

%description  devel
This package contains the header files for developing
applications that want to make use of cogl.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-gtk-doc \
%if %{with_COGLGST}
	--enable-cogl-gst \
%endif
	--enable-kms-egl-platform \
	--enable-wayland-egl-platform \
	--enable-wayland-egl-server \
%if %{with_GLES2}
	--enable-gles2 --enable-cogl-gles2 \
%endif
	%{nil}

make V=1 # %{?_smp_mflags} disabled, as it randomly fails for now

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%find_lang cogl
%fdupes %{buildroot}%{_libdir}/pkgconfig/
%fdupes -s %{buildroot}%{_datadir}/gtk-doc/html
%fdupes -s %{buildroot}%{_includedir}/cogl/cogl/

%post -n libcogl20 -p /sbin/ldconfig
%postun -n libcogl20 -p /sbin/ldconfig

%if %{with_GLES2}
%post -n libcogl-gles2-20 -p /sbin/ldconfig
%postun -n libcogl-gles2-20 -p /sbin/ldconfig
%endif

%post -n libcogl-pango20 -p /sbin/ldconfig
%postun -n libcogl-pango20 -p /sbin/ldconfig

%files -n libcogl20
%license COPYING
%doc NEWS README ChangeLog
%{_libdir}/libcogl.so.*
%{_libdir}/libcogl-path.so.*
%if %{with_COGLGST}
%{_libdir}/libcogl-gst.so.*
%endif

%if %{with_COGLGST}
%files -n gstreamer-plugins-cogl
%{_libdir}/gstreamer-1.0/*.so
%endif

%if %{with_GLES2}
%files -n libcogl-gles2-20
%{_libdir}/libcogl-gles2.so.*
%endif

%files -n typelib-1_0-Cogl-1_0
%{_libdir}/girepository-1.0/Cogl-1.0.typelib

%files -n typelib-1_0-Cogl-2_0
%{_libdir}/girepository-1.0/Cogl-2.0.typelib

%if %{with_COGLGST}
%files -n typelib-1_0-CoglGst-2_0
%{_libdir}/girepository-1.0/CoglGst-2.0.typelib
%endif

%files -n libcogl-pango20
%license COPYING
%doc NEWS README ChangeLog
%{_libdir}/libcogl-pango.so.*

%files -n typelib-1_0-CoglPango-1_0
%{_libdir}/girepository-1.0/CoglPango-1.0.typelib

%files -n typelib-1_0-CoglPango-2_0
%{_libdir}/girepository-1.0/CoglPango-2.0.typelib

%files devel
%{_libdir}/*.so
%{_includedir}/cogl/
%dir %{_datadir}/cogl/
%{_datadir}/cogl/examples-data/
%{_libdir}/pkgconfig/cogl-1.0.pc
%{_libdir}/pkgconfig/cogl-2.0-experimental.pc
%if %{with_GLES2}
%{_libdir}/pkgconfig/cogl-gles2-1.0.pc
%{_libdir}/pkgconfig/cogl-gles2-2.0-experimental.pc
%endif
%{_libdir}/pkgconfig/cogl-gl-1.0.pc
%if %{with_COGLGST}
%{_libdir}/pkgconfig/cogl-gst-1.0.pc
%{_libdir}/pkgconfig/cogl-gst-2.0-experimental.pc
%endif
%{_libdir}/pkgconfig/cogl-pango-1.0.pc
%{_libdir}/pkgconfig/cogl-pango-2.0-experimental.pc
%{_libdir}/pkgconfig/cogl-path-1.0.pc
%{_libdir}/pkgconfig/cogl-path-2.0-experimental.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/cogl/
%if %{with_COGLGST}
%doc %{_datadir}/gtk-doc/html/cogl-gst/
%endif
%doc %{_datadir}/gtk-doc/html/cogl-2.0-experimental/

%files lang -f cogl.lang

%changelog
