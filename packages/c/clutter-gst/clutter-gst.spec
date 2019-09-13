#
# spec file for package clutter-gst
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define debug_package_requires libclutter-gst-3_0-0 = %{version}-%{release}
Name:           clutter-gst
Version:        3.0.27
Release:        0
Summary:        GStreamer integration for Clutter
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://clutter-project.org/
Source0:        http://download.gnome.org/sources/clutter-gst/3.0/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(clutter-1.0) >= 1.20.0
BuildRequires:  pkgconfig(cogl-2.0-experimental) >= 2.0.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gudev-1.0)

%description
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

%package -n  libclutter-gst-3_0-0
Summary:        GStreamer integration for Clutter
Group:          System/Libraries

%description -n libclutter-gst-3_0-0
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

%package -n typelib-1_0-ClutterGst-3_0
Summary:        GStreamer integration for Clutter -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-ClutterGst-3_0
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

This package provides the GObject Introspection bindings for Clutter
GStreamer.

%package -n gstreamer-plugin-cluttergst3
Summary:        GStreamer Clutter Plug-In
Group:          Productivity/Multimedia/Other
Supplements:    packageand(gstreamer:libclutter-gst-3_0-0)

%description -n gstreamer-plugin-cluttergst3
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

This plug-in for GStreamer contains elements to render to Clutter
textures.

%package devel
Summary:        GStreamer integration for Clutter
Group:          Development/Libraries/C and C++
Requires:       gstreamer-plugin-cluttergst3 = %{version}
Requires:       libclutter-gst-3_0-0 = %{version}
Requires:       typelib-1_0-ClutterGst-3_0 = %{version}
Provides:       clutter-doc = %{version}
Obsoletes:      clutter-doc < %{version}

%description  devel
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libclutter-gst-3_0-0 -p /sbin/ldconfig
%postun -n libclutter-gst-3_0-0 -p /sbin/ldconfig

%files -n libclutter-gst-3_0-0
%license COPYING
%doc README
%{_libdir}/*.so.*

%files -n typelib-1_0-ClutterGst-3_0
%{_libdir}/girepository-1.0/ClutterGst-3.0.typelib

%files -n gstreamer-plugin-cluttergst3
%{_libdir}/gstreamer-1.0/libcluttergst3.so

%files devel
%{_libdir}/*.so
%{_includedir}/clutter-gst-3.0/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/ClutterGst-3.0.gir
%doc %{_datadir}/gtk-doc/html/clutter-gst-3.0

%changelog
