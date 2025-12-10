#
# spec file for package gstreamer-plugins-rs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%define _name gst-plugins-rs
%define gst_branch 1.0

%bcond_with aws

Name:           gstreamer-plugins-rs
Version:        1.26.9
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gitlab.freedesktop.org/gstreamer/gst-plugins-rs

Source:         %{_name}-%{version}.tar.zst
Source2:        vendor.tar.zst
Source4:        gstreamer-plugins-rs.appdata.xml
#PATCH-FIX-UPSTREAM https://gitlab.freedesktop.org/gstreamer/gst-plugins-rs/-/merge_requests/2162
Patch1:         0001-cargo_wrapper-deduplicate-Libs_private.patch

BuildRequires:  cargo-c >= 0.10.12
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  llvm
BuildRequires:  meson >= 0.60
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  python3-tomli
BuildRequires:  zstd
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(dav1d) >= 1.3.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-webrtc-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
Requires:       gstreamer
Requires:       gstreamer-plugins-base
Enhances:       gstreamer
ExclusiveArch:  %{rust_tier1_arches}

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new
plug-ins.

This package provides various plugins written in Rust.

%prep
%autosetup -n %{_name}-%{version} -a2 -p1

# Legaldb complains that there's a reference to a proprietary plugin (that is not built in any case) in the json file, so let's remove it
python3 -c "import json; \
  j = json.load(open('docs/plugins/gst_plugins_cache.json', 'r')) ; \
  j.pop('elevenlabs') ;  \
  json.dump(j, open('docs/plugins/gst_plugins_cache.json', 'wt'), indent=4, ensure_ascii=False)"

%build
%meson \
	--default-library=shared \
	-Ddoc=disabled \
	-Ddav1d=auto \
	-Dsodium=enabled \
	-Dcsound=disabled \
	-Dvvdec=disabled \
	-Dskia=disabled \
%if %{without aws}
	-Daws=disabled \
%endif
	%{nil}

%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE4} %{buildroot}%{_datadir}/appdata/

%files
%license LICENSE-APACHE LICENSE-LGPLv2 LICENSE-MIT
%doc README.md
%dir %{_libdir}/gstreamer-%{gst_branch}
%if %{with aws}
%{_libdir}/gstreamer-%{gst_branch}/libgstaws.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstcdg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstclaxon.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdav1d.so
%{_libdir}/gstreamer-%{gst_branch}/libgstelevenlabs.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfallbackswitch.so
%{_libdir}/gstreamer-%{gst_branch}/libgstffv1.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfmp4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgif.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgopbuffer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgtk4.so
%{_libdir}/gstreamer-%{gst_branch}/libgsthlssink3.so
%{_libdir}/gstreamer-%{gst_branch}/libgsthsv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjson.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlewton.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlivesync.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmp4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpegtslive.so
%{_libdir}/gstreamer-%{gst_branch}/libgstndi.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoriginalbuffer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstquinn.so
%{_libdir}/gstreamer-%{gst_branch}/libgstraptorq.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrav1e.so
%{_libdir}/gstreamer-%{gst_branch}/libgstregex.so
%{_libdir}/gstreamer-%{gst_branch}/libgstreqwest.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsanalytics.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsaudiofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsclosedcaption.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsfile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsflv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsinter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsonvif.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrspng.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsrtsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrstracers.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsvideofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrswebp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrswebrtc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsodium.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspotify.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttextahead.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttextwrap.so
%{_libdir}/gstreamer-%{gst_branch}/libgstthreadshare.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttogglerecord.so
%{_libdir}/gstreamer-%{gst_branch}/libgsturiplaylistbin.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwebrtchttp.so
%{_libdir}/gstreamer-%{gst_branch}/libgsthlsmultivariantsink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspeechmatics.so
%{_libdir}/gstreamer-%{gst_branch}/libgststreamgrouper.so
%dir %{_datadir}/appdata
%{_datadir}/appdata/gstreamer-plugins-rs.appdata.xml
%{_bindir}/gst-webrtc-signalling-server

%changelog
