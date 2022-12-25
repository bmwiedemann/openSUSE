#
# spec file for package gstreamer-editing-services
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%define _name gst-editing-services

Name:           gstreamer-editing-services
Version:        1.20.5
Release:        0
Summary:        GStreamer Editing Services
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org/data/doc/gstreamer/head/gstreamer-editing-services/html/ges-architecture.html
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-editing-services/%{_name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject-devel
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.16
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gst-validate-1.0) >= 1.18.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-controller-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.3
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 2.91.3
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)

%description
The GStreamer multimedia framework and the accompanying GNonLin set
of plugins for non-linear editing offer all the building blocks
for:
Decoding and encoding to a wide variety of formats, through all the
available GStreamer plugins.
Easily choosing segments of streams and arranging them through time
through the GNonLin set of plugins.

But all those building blocks only offer stream-level access, which
results in developers who want to write non-linear editors to write
a consequent amount of code to get to the level of non-linear
editing notions which are closer and more meaningful for the
end-user (and therefore the application).

The GStreamer Editing Services (hereafter GES) aims to fill the gap
between GStreamer/GNonLin and the application developer by offering
a series of classes to simplify the creation of many kind of
editing-related applications.

%package -n libges-1_0-0
Summary:        GStreamer Editing Services - Libraries
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libges-1_0-0
The GStreamer multimedia framework and the accompanying GNonLin set
of plugins for non-linear editing offer all the building blocks
for:
Decoding and encoding to a wide variety of formats, through all the
available GStreamer plugins.
Easily choosing segments of streams and arranging them through time
through the GNonLin set of plugins.

But all those building blocks only offer stream-level access, which
results in developers who want to write non-linear editors to write
a consequent amount of code to get to the level of non-linear
editing notions which are closer and more meaningful for the
end-user (and therefore the application).

The GStreamer Editing Services (hereafter GES) aims to fill the gap
between GStreamer/GNonLin and the application developer by offering
a series of classes to simplify the creation of many kind of
editing-related applications.

%package -n typelib-1_0-GES-1_0
Summary:        GStreamer Editing Services - Libraries
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-GES-1_0
The GStreamer multimedia framework and the accompanying GNonLin set
of plugins for non-linear editing offer all the building blocks
for:
Decoding and encoding to a wide variety of formats, through all the
available GStreamer plugins.
Easily choosing segments of streams and arranging them through time
through the GNonLin set of plugins.

But all those building blocks only offer stream-level access, which
results in developers who want to write non-linear editors to write
a consequent amount of code to get to the level of non-linear
editing notions which are closer and more meaningful for the
end-user (and therefore the application).

The GStreamer Editing Services (hereafter GES) aims to fill the gap
between GStreamer/GNonLin and the application developer by offering
a series of classes to simplify the creation of many kind of
editing-related applications.

%package devel
Summary:        GStreamer Editing Services - Development files
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       libges-1_0-0 = %{version}
Requires:       typelib-1_0-GES-1_0 = %{version}

%description devel
The GStreamer multimedia framework and the accompanying GNonLin set
of plugins for non-linear editing offer all the building blocks
for:
Decoding and encoding to a wide variety of formats, through all the
available GStreamer plugins.
Easily choosing segments of streams and arranging them through time
through the GNonLin set of plugins.

But all those building blocks only offer stream-level access, which
results in developers who want to write non-linear editors to write
a consequent amount of code to get to the level of non-linear
editing notions which are closer and more meaningful for the
end-user (and therefore the application).

The GStreamer Editing Services (hereafter GES) aims to fill the gap
between GStreamer/GNonLin and the application developer by offering
a series of classes to simplify the creation of many kind of
editing-related applications.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
	-Ddoc=disabled \
	-Dintrospection=enabled \
	-Dtests=disabled \
	%{nil}
%meson_build

%install
%meson_install

%post -n libges-1_0-0 -p /sbin/ldconfig
%postun -n libges-1_0-0 -p /sbin/ldconfig

%files
%license COPYING
%{_mandir}/man1/ges-launch-1.0.1%{?ext_man}
%{_bindir}/ges-launch-1.0
%{_datadir}/bash-completion/completions/ges-launch-1.0
%{_datadir}/gstreamer-1.0/validate/scenarios/ges-edit-clip-while-paused.scenario
%{_libdir}/gst-validate-launcher/python/launcher/apps/geslaunch.py
%{python3_sitearch}/gi/overrides/GES.py

%files -n libges-1_0-0
%license COPYING
%{_libdir}/gstreamer-1.0/libgstges.so
%{_libdir}/gstreamer-1.0/libgstnle.so
%{_libdir}/libges-1.0.so.*

%files -n typelib-1_0-GES-1_0
%{_libdir}/girepository-1.0/GES-1.0.typelib

%files devel
%doc ChangeLog README
%{_datadir}/gir-1.0/GES-1.0.gir
%{_includedir}/gstreamer-1.0/ges/
%{_libdir}/libges-1.0.so
%{_libdir}/pkgconfig/gst-editing-services-1.0.pc

%changelog
