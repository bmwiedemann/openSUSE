#
# spec file for package libdmapsharing
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libdmapsharing
Version:        2.9.38
Release:        0
Summary:        Library implementing the Digital Media Access Protocol family
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
Url:            http://www.flyn.org/projects/libdmapsharing/
Source0:        http://flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM Fix build with vala >= 0.43 https://gitlab.gnome.org/GNOME/libdmapsharing/issues/7 mlin@suse.com
Patch0:         new_vala_build.patch
BuildRequires:  pkg-config
BuildRequires:  vala
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.48.0

%description
Libdmapsharing is a library you may use to access, share and control the
playback of media content using DMAP (DAAP, DPAP & DACP). Libdmapsharing
also detects audio AirPlay services; coupled with the AirPlay support
in PulseAudio or GStreamer, this can allow an application to stream audio
to an AirPlay device. The DMAP family of protocols are used by products
such as Apple iTunes, Apple iPhoto, and the Roku SoundBridge family to
share media such as music and photos.

%package -n libdmapsharing-3_0-2
Summary:        Library implementing the Digital Media Access Protocol family
Group:          System/Libraries

%description -n libdmapsharing-3_0-2
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
Requires:       libdmapsharing-3_0-2 = %{version}

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
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libdmapsharing-3_0-2 -p /sbin/ldconfig

%postun -n libdmapsharing-3_0-2 -p /sbin/ldconfig

%files -n libdmapsharing-3_0-2
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libdmapsharing-3.0.so.2*

%files devel
%defattr(-, root, root)
%{_datadir}/gtk-doc/html/libdmapsharing-3.0/
%{_datadir}/vala/vapi/libdmapsharing-3.0.vapi
%{_includedir}/libdmapsharing-3.0/
%{_libdir}/libdmapsharing-3.0.so
%{_libdir}/pkgconfig/libdmapsharing-3.0.pc

%changelog
