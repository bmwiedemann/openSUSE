#
# spec file for package gstreamermm
#
# Copyright (c) 2021 SUSE LLC
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


%define	soname	-1_0-1
%define sover   1
%define _sver   1.10
%define _mver   1.0
Name:           gstreamermm
Version:        1.10.0
Release:        0
Summary:        C++ bindings for the GStreamer streaming multimedia library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://gstreamer.freedesktop.org/bindings/cplusplus.html
Source0:        https://ftp.gnome.org/pub/gnome/sources/gstreamermm/%{_sver}/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc

# PATCH-FIX-UPSTREAM gstreamermm-copy_metadata_vfunc.patch bgo#794249 -- Fix bug tied to copy_metadata_vfunc
Patch0:         gstreamermm-copy_metadata_vfunc.patch
# PATCH-FIX-UPSTREAM gstreamermm-copy_metadata_vfunc.patch bgo#794250 -- Fix bug tied to copy_metadata_vfunc
Patch1:         gstreamermm-copy_metadata_vfunc2.patch
# PATCH-FIX-UPSTREAM gstreamermm-copy_metadata_vfunc.patch -- Fix bug tied to copy_metadata_vfunc
Patch2:         gstreamermm-copy_metadata_vfunc3.patch
# PATCH-FIX-UPSTREAM gstreamermm-non-volatile.patch dimstar@opensuse,org -- Fix build with glib 2.68
Patch3:         gstreamermm-non-volatile.patch

BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-allocators-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-check-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-controller-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-fft-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-net-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-riff-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-rtp-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-sdp-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires:  pkgconfig(libxml++-3.0)

%description
gstreamermm provides C++ bindings for the GStreamer streaming multimedia
library (http://gstreamer.freedesktop.org).  With gstreamermm it is possible to
develop applications that work with multimedia in C++.

%package        devel
Summary:        C++ bindings for the GStreamer streaming multimedia library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{soname} = %{version}

%description    devel
gstreamermm provides C++ bindings for the GStreamer streaming multimedia
library (http://gstreamer.freedesktop.org).  With gstreamermm it is possible to
develop applications that work with multimedia in C++.

%package        doc
Summary:        C++ bindings for the GStreamer streaming multimedia library
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
gstreamermm provides C++ bindings for the GStreamer streaming multimedia
library (http://gstreamer.freedesktop.org).  With gstreamermm it is possible to
develop applications that work with multimedia in C++.

%package     -n lib%{name}%{soname}
Summary:        C++ bindings for the GStreamer streaming multimedia library
Group:          System/Libraries

%description -n lib%{name}%{soname}
gstreamermm provides C++ bindings for the GStreamer streaming multimedia
library (http://gstreamer.freedesktop.org).  With gstreamermm it is possible to
develop applications that work with multimedia in C++.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files devel
%license COPYING
%doc ChangeLog README
%{_includedir}/%{name}-%{_mver}
%{_libdir}/%{name}-%{_mver}
%{_libdir}/lib%{name}-%{_mver}.so
%{_libdir}/pkgconfig/%{name}-%{_mver}.pc

%files doc
%license COPYING
%{_datadir}/devhelp/books/%{name}-%{_mver}
%{_datadir}/doc/%{name}-%{_mver}

%files -n lib%{name}%{soname}
%license COPYING
%{_libdir}/lib%{name}-%{_mver}.so.%{sover}*

%changelog
