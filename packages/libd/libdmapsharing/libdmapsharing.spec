#
# spec file for package libdmapsharing
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


%define majorver 4.0
%define soname 4_0
%define sover 3

Name:           libdmapsharing
Version:        3.9.10
Release:        0
Summary:        Library implementing the Digital Media Access Protocol family
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.flyn.org/projects/libdmapsharing/
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(avahi-client) >= 0.6
BuildRequires:  pkgconfig(avahi-glib) >= 0.6
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.48.0

%description
Libdmapsharing is a library you may use to access, share and control the
playback of media content using DMAP (DAAP, DPAP & DACP). Libdmapsharing
also detects audio AirPlay services; coupled with the AirPlay support
in PulseAudio or GStreamer, this can allow an application to stream audio
to an AirPlay device. The DMAP family of protocols are used by products
such as Apple iTunes, Apple iPhoto, and the Roku SoundBridge family to
share media such as music and photos.

%package -n libdmapsharing-%{soname}-%{sover}
Summary:        Library implementing the Digital Media Access Protocol family
Group:          System/Libraries

%description -n libdmapsharing-%{soname}-%{sover}
Libdmapsharing is a library you may use to access, share and control the
playback of media content using DMAP (DAAP, DPAP & DACP). Libdmapsharing
also detects audio AirPlay services; coupled with the AirPlay support
in PulseAudio or GStreamer, this can allow an application to stream audio
to an AirPlay device. The DMAP family of protocols are used by products
such as Apple iTunes, Apple iPhoto, and the Roku SoundBridge family to
share media such as music and photos.

%package -n typelib-1_0-Dmap-4_0
Summary:        Typelib for libdmapsharing
Group:          Productivity/Multimedia/Other

%description -n typelib-1_0-Dmap-4_0
Libdmapsharing is a library you may use to access, share and control the
playback of media content using DMAP (DAAP, DPAP & DACP). Libdmapsharing
also detects audio AirPlay services; coupled with the AirPlay support
in PulseAudio or GStreamer, this can allow an application to stream audio
to an AirPlay device. The DMAP family of protocols are used by products
such as Apple iTunes, Apple iPhoto, and the Roku SoundBridge family to
share media such as music and photos.

%package devel
Summary:        Library implementing the DMAP family of protocols - Development Files
Group:          Development/Languages/C and C++
Requires:       libdmapsharing-%{soname}-%{sover} = %{version}
Requires:       typelib-1_0-Dmap-4_0 = %{version}

%description devel
Libdmapsharing is a library you may use to access, share and control the
playback of media content using DMAP (DAAP, DPAP & DACP). Libdmapsharing
also detects audio AirPlay services; coupled with the AirPlay support
in PulseAudio or GStreamer, this can allow an application to stream audio
to an AirPlay device. The DMAP family of protocols are used by products
such as Apple iTunes, Apple iPhoto, and the Roku SoundBridge family to
share media such as music and photos.

This package contains development files for libdmapsharing.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-tests \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libdmapsharing-%{soname}-%{sover} -p /sbin/ldconfig
%postun -n libdmapsharing-%{soname}-%{sover} -p /sbin/ldconfig

%files -n libdmapsharing-%{soname}-%{sover}
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libdmapsharing-%{majorver}.so.%{sover}*

%files -n typelib-1_0-Dmap-4_0
%{_libdir}/girepository-1.0/Dmap-4.0.typelib

%files devel
%{_datadir}/gtk-doc/html/libdmapsharing-%{majorver}/
%{_datadir}/vala/vapi/libdmapsharing-%{majorver}.vapi
%{_datadir}/gir-1.0/Dmap-4.0.gir
%{_includedir}/libdmapsharing-%{majorver}/
%{_libdir}/libdmapsharing-%{majorver}.so
%{_libdir}/pkgconfig/libdmapsharing-%{majorver}.pc

%changelog
