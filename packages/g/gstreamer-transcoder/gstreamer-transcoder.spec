#
# spec file for package gstreamer-transcoder
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


%define _name   gst-transcoder
Name:           gstreamer-transcoder
Version:        1.16.0
Release:        0
Summary:        GStreamer Transcoding API
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Other
URL:            https://github.com/pitivi/gst-transcoder
Source:         https://github.com/pitivi/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.15.0

%description
GStreamer Transcoding API.
Used by Pitvi currently.

%package -n libgsttranscoder-1_0-0
Summary:        GStreamer Transcoder API
Group:          System/Libraries

%description -n libgsttranscoder-1_0-0
This subpackage contains the implementation of the GStreamer API.

%package -n typelib-1_0-GstTranscoder-1_0
Summary:        Introspection bindings for the GStreamer Transcoder API
Group:          System/Libraries

%description -n typelib-1_0-GstTranscoder-1_0
This subpackage contains the introspection bindings for the GStreamer Transcoding API.

%package devel
Summary:        Development files for the GStreamer Transcoding API
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
# Needed due to gh#pitivi/gst-transcoder#4
Requires:       gstreamer-devel
Requires:       libgsttranscoder-1_0-0 = %{version}
Requires:       typelib-1_0-GstTranscoder-1_0 = %{version}

%description devel
This subpackage contains the header files needed to build applications
making use of the GStreamer Transcoding API.

%prep
%setup -q -n %{_name}-%{version}

%build
%meson \
	-Ddisable_doc=false \
	-Ddisable_introspection=false \
	%{nil}
%meson_build

%install
%meson_install

%post -n libgsttranscoder-1_0-0 -p /sbin/ldconfig
%postun -n libgsttranscoder-1_0-0 -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/gst-transcoder-1.0
%{_libdir}/gstreamer-1.0/libgsttranscode.so
%{_datadir}/gstreamer-1.0/encoding-profiles/

%files -n libgsttranscoder-1_0-0
%{_libdir}/libgsttranscoder-1.0.so.0

%files -n typelib-1_0-GstTranscoder-1_0
%{_libdir}/girepository-1.0/GstTranscoder-1.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/gstreamer-transcoder/
%{_datadir}/gir-1.0/GstTranscoder-1.0.gir
%{_includedir}/gstreamer-1.0/gst/transcoder/
%{_libdir}/libgsttranscoder-1.0.so
%{_libdir}/pkgconfig/gst-transcoder-1.0.pc

%changelog
