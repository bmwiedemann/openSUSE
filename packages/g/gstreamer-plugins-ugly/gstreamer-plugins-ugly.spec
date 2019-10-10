#
# spec file for package gstreamer-plugins-ugly
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


%define _name gst-plugins-ugly
%define gst_branch 1.0
# Patched code is built by default.
# Use rpmbuild -D 'BUILD_ORIG 1' to build original code.
# Use rpmbuild -D 'BUILD_ORIG 1' -D 'BUILD_ORIG_ADDON 1' to build patched build plus original as addon.
%define _experimental 0
# Get minimum gstreamer and gstreamer-plugins-base required versions from configure.ac
%define gstreamer_plugins_ugly_req %(xzgrep --text "^GST.*_REQ" %{SOURCE0} | sort -u | sed 's/GST_REQ=/gstreamer >= /;s/GSTPB_REQ=/gstreamer-plugins-base >= /' | tr '\\n' ' ')
# Currently disabled because plugin documentation isn't built
%define use_meson 0
Name:           gstreamer-plugins-ugly
Version:        1.16.1
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            http://gstreamer.freedesktop.org/
Source:         https://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  liba52-devel
BuildRequires:  libcdio-devel >= 0.76
BuildRequires:  libdvdread-devel
%if %{use_meson}
BuildRequires:  meson >= 0.47.0
%else
# Needed for patches 0 and 1
BuildRequires:  libtool
%endif
BuildRequires:  orc >= 0.4.16
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(libmpeg2) >= 0.5.1
Requires:       %{gstreamer_plugins_ugly_req}
Recommends:     %{name}-lang
Enhances:       gstreamer
# Generic name, never used in SUSE:
Provides:       gst-plugins-ugly = %{version}
%if 0%{?BUILD_ORIG}
BuildRequires:  pkgconfig(opencore-amrwb) >= 0.1.3
BuildRequires:  pkgconfig(x264) >= 0.120
%endif
%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}
Provides:       patched_subset
%else
Provides:       %{name}-orig-addon = %{version}
%endif
%else
Provides:       patched_subset
%endif

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing newplug-ins.

This package contains well-written plug-ins that can't be shipped in
gstreamer-plugins-good because:
- the license is not LGPL
- the license of the library is not LGPL
- there are possible licensing issues with the code.

%package orig-addon
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          Productivity/Multimedia/Other
Requires:       %{name} >= %{version}
Supplements:    %{name}

%description orig-addon
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added
simply by installing new plug-ins.

This package contains well-written plug-ins that can't be shipped in
openSUSE because of patent problems.

%package doc
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
GStreamer is a streaming media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

%lang_package

%prep
%setup -q -n %{_name}-%{version}

%build
export PYTHON=%{_bindir}/python3
%if %{use_meson}
%{meson} \
%if ! 0%{?BUILD_ORIG}
	-Dpackage-name='openSUSE gstreamer-plugins-ugly package' \
	-Dasfdemux=disabled \
	-Dpackage-origin='http://www.opensuse.org/' \
	-Damrnb=disabled \
	-Damrwbdec=disabled \
	-Dx264=disabled \
%endif
	-Dsidplay=disabled \
	%{nil}
%{meson_build}
%else
%configure \
%if ! 0%{?BUILD_ORIG}
	--with-package-name='openSUSE gstreamer-plugins-ugly package' \
	--disable-asfdemux \
	--with-package-origin='http://www.opensuse.org/' \
%endif
	--enable-gtk-doc \
%if 0%{?_experimental}
	--enable-experimental \
%endif
	--disable-static \
	%{nil}
make %{?_smp_mflags}
%endif

%install
%if %{use_meson}
%{meson_install}
%else
%make_install
%endif
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}-%{gst_branch}

%files
%license COPYING
%{_libdir}/gstreamer-%{gst_branch}/libgsta52dec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcdio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdread.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdsub.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrealmedia.so
%{_libdir}/gstreamer-%{gst_branch}/libgstxingmux.so

%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}
%files orig-addon
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstamrnb.so
%{_libdir}/gstreamer-%{gst_branch}/libgstamrwbdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstasf.so
%{_libdir}/gstreamer-%{gst_branch}/libgstx264.so
%{_datadir}/gstreamer-%{gst_branch}/presets/GstAmrnbEnc.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstX264Enc.prs
%endif

%files lang -f %{_name}-%{gst_branch}.lang

%files doc
%doc AUTHORS NEWS README RELEASE REQUIREMENTS
%{_datadir}/gtk-doc/html/gst-plugins-ugly-plugins-%{gst_branch}

%changelog
