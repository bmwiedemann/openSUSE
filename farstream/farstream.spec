#
# spec file for package farstream
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define gst_pluginsdir %(pkg-config --variable pluginsdir gstreamer-1.0)
Name:           farstream
Version:        0.2.8
Release:        0
# License note: the only GPL-2.0+ files are farstream-0.1.1/common/coverage/*
# and common/gstdoc-scangobj; those are just used during the build and do not
# affect the license of the binary packages
Summary:        GStreamer modules and libraries for videoconferencing
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            http://farsight.freedesktop.org/
Source:         http://freedesktop.org/software/farstream/releases/farstream/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FEATURE-OPENSUSE farstream-plugin-path.patch fcrozat@suse.com -- Use library policy compliant path for plugin
Patch0:         farstream-plugin-path.patch
# PATCH-FIX-UPSTREAM
Patch1:         farstream-0.2.8-rtpbitrateadapter-no-adaptation.patch
#needed by patch0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gobject-introspection-devel >= 0.10.1
BuildRequires:  gstreamer-devel >= 1.4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.16
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.4
BuildRequires:  pkgconfig(gupnp-igd-1.0) >= 0.2
BuildRequires:  pkgconfig(nice) >= 0.1.8
BuildRequires:  pkgconfig(pygobject-2.0) >= 2.16.0

%description
Farstream is a collection of GStreamer modules and libraries for
videoconferencing.

%package -n libfarstream-0_2-5
Summary:        GStreamer modules and libraries for videoconferencing
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-data
# While not strictly needed, apps using farstream will need the gstreamer
# plugins, so simply put a Requires here instead of in all apps
Requires:       gstreamer-plugins-farstream

%description -n libfarstream-0_2-5
Farstream is a collection of GStreamer modules and libraries for
videoconferencing.

%package -n typelib-1_0-Farstream-0_2
Summary:        GStreamer modules and libraries for videoconferencing -- Introspection bindings
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-Farstream-0_2
Farstream is a collection of GStreamer modules and libraries for
videoconferencing.

This package provides the GObject Introspection bindings for Farstream.

%package -n gstreamer-plugins-farstream
Summary:        GStreamer Plug-Ins for videoconferencing
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
Requires:       gstreamer-plugins-bad >= 0.11
Requires:       gstreamer-plugins-good >= 0.11
# Unfortunately, the gstreamer elements have the same name; since we're
# dropping farsight, let's Obsolete the old package for a smooth transition
Obsoletes:      libgstfarsight-0_10-0

%description -n gstreamer-plugins-farstream
Farstream is a collection of GStreamer modules and libraries for
videoconferencing.

%package data
Summary:        GStreamer modules and libraries for videoconferencing -- Codec preferences
License:        LGPL-2.1-or-later
Group:          System/Libraries
BuildArch:      noarch

%description data
Farstream is a collection of GStreamer modules and libraries for
videoconferencing.

This package contains data (codec preferences, element properties)
used by the library.

%package devel
Summary:        GStreamer modules and libraries for videoconferencing -- Development files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libfarstream-0_2-5 = %{version}
Requires:       typelib-1_0-Farstream-0_2 = %{version}

%description devel
Farstream is a collection of GStreamer modules and libraries for
videoconferencing.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#needed by patch0
autoreconf -f

%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}/gtk-doc/html/

%post -n libfarstream-0_2-5 -p /sbin/ldconfig
%postun -n libfarstream-0_2-5 -p /sbin/ldconfig

%files -n libfarstream-0_2-5
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libfarstream-0.2.so.*
%dir %{_libdir}/farstream-0.2-5/
%{_libdir}/farstream-0.2-5/libmulticast-transmitter.so
%{_libdir}/farstream-0.2-5/libnice-transmitter.so
%{_libdir}/farstream-0.2-5/librawudp-transmitter.so
%{_libdir}/farstream-0.2-5/libshm-transmitter.so

%files -n typelib-1_0-Farstream-0_2
%{_libdir}/girepository-1.0/Farstream-0.2.typelib

%files -n gstreamer-plugins-farstream
%{gst_pluginsdir}/libfsmsnconference.so
%{gst_pluginsdir}/libfsrawconference.so
%{gst_pluginsdir}/libfsrtpconference.so
%{gst_pluginsdir}/libfsrtpxdata.so
%{gst_pluginsdir}/libfsvideoanyrate.so

%files data
%dir %{_datadir}/farstream/
%dir %{_datadir}/farstream/0.2/
%dir %{_datadir}/farstream/0.2/fsrawconference/
%{_datadir}/farstream/0.2/fsrawconference/default-element-properties
%dir %{_datadir}/farstream/0.2/fsrtpconference/
%{_datadir}/farstream/0.2/fsrtpconference/default-codec-preferences
%{_datadir}/farstream/0.2/fsrtpconference/default-element-properties

%files devel
%{_includedir}/farstream-0.2/
%{_libdir}/libfarstream-0.2.so
%{_libdir}/pkgconfig/farstream-0.2.pc
%{_datadir}/gir-1.0/Farstream-0.2.gir
%doc %{_datadir}/gtk-doc/html/farstream-libs-0.2/
%doc %{_datadir}/gtk-doc/html/farstream-plugins-0.2/

%changelog
