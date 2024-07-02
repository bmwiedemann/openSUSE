#
# spec file for package gstreamer-plugins-ugly
#
# Copyright (c) 2024 SUSE LLC
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
# Get minimum gstreamer and gstreamer-plugins-base required versions from configure.ac
%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")

Name:           gstreamer-plugins-ugly
Version:        1.24.5
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/%{_name}/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  gcc-c++
BuildRequires:  liba52-devel
BuildRequires:  libcdio-devel >= 0.76
BuildRequires:  libdvdread-devel
BuildRequires:  meson >= 1.1
BuildRequires:  orc >= 0.4.16
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(libmpeg2) >= 0.5.1
Requires:       gstreamer-plugins-base >= %{gstreamer_req_version}
Enhances:       gstreamer
# Generic name, never used in SUSE:
Provides:       gst-plugins-ugly = %{version}
%if 0%{?BUILD_ORIG}
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

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
export PYTHON=%{_bindir}/python3
%meson \
%if ! 0%{?BUILD_ORIG}
	-D package-name='openSUSE gstreamer-plugins-ugly package' \
	-D package-origin='http://www.opensuse.org/' \
	-D x264=disabled \
%endif
	-D gpl=enabled \
	-D sidplay=disabled \
	-D doc=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{_name}-%{gst_branch}

%files
%license COPYING
%doc AUTHORS NEWS README.md RELEASE REQUIREMENTS
%{_libdir}/gstreamer-%{gst_branch}/libgsta52dec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstasf.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcdio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdread.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdsub.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrealmedia.so

%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}
%files orig-addon
%endif
%{_datadir}/gstreamer-%{gst_branch}/presets/GstX264Enc.prs
%{_libdir}/gstreamer-%{gst_branch}/libgstx264.so
%endif

%files lang -f %{_name}-%{gst_branch}.lang

%changelog
