#
# spec file for package gstreamer-plugins-rs
#
# Copyright (c) 2022 SUSE LLC
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


%define _lto_cflags %{nil}

%define _name gstreamer-plugins-rs
%define gst_branch 1.0
%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
# Disable csound for now, bring issue upstream
#%%global __requires_exclude pkgconfig\\(csound\\)

Name:           gstreamer-plugins-rs
Version:        0.9+git20221113.274e57a
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org/

Source0:        %{_name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        gstreamer-plugins-rs.appdata.xml

BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  clang
# Disable csound for now, bring issue upstream
#BuildRequires:  csound-devel
BuildRequires:  llvm
BuildRequires:  git
BuildRequires:  meson >= 0.47.0
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  python3-tomli
BuildRequires:  rust >= 1.51
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(dav1d)
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
ExcludeArch:    ppc ppc64 ppc64le s390

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new
plug-ins.

%package devel
Summary:        GStreamer Streaming-Media Framework Plug-Ins development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
#Requires:       csound-devel

%description devel
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new
plug-ins.

This package contains the pkgconfig development files for the rust
plugins.

%prep
%autosetup -n %{_name}-%{version} -p1

%setup -q -D -T -a 1
%define cargo_registry $(pwd)/vendor
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
# Disable csound for now, bring issue upstream
#export CSOUND_LIB_DIR=%%{_libdir}
export RUSTFLAGS=%{rustflags}

%meson \
	--default-library=shared \
	-Ddoc=disabled \
	-Ddav1d=auto \
	-Dsodium=system \
	-Dcsound=disabled \
	%{nil}
%meson_build

%install
export RUSTFLAGS=%{rustflags}
%meson_install
mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE3} %{buildroot}%{_datadir}/appdata/

%files
%license LICENSE-APACHE LICENSE-LGPLv2 LICENSE-MIT
%doc README.md
%dir %{_libdir}/gstreamer-%{gst_branch}
%{_libdir}/gstreamer-%{gst_branch}/libgstaws.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcdg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstclaxon.so
# Disable csound for now, bring issue upstream
#%%{_libdir}/gstreamer-%%{gst_branch}/libgstcsound.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfallbackswitch.so
%{_libdir}/gstreamer-%{gst_branch}/libgstffv1.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfmp4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgif.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgtk4.so
%{_libdir}/gstreamer-%{gst_branch}/libgsthlssink3.so
%{_libdir}/gstreamer-%{gst_branch}/libgsthsv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlewton.so
%{_libdir}/gstreamer-%{gst_branch}/libgstndi.so
%{_libdir}/gstreamer-%{gst_branch}/libgstraptorq.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrav1e.so
%{_libdir}/gstreamer-%{gst_branch}/libgstreqwest.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsaudiofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsclosedcaption.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdav1d.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsfile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsflv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjson.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsonvif.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrspng.so
%{_libdir}/gstreamer-%{gst_branch}/libgstregex.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttextwrap.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrstracers.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrswebp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrswebrtc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsodium.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspotify.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttextahead.so
%{_libdir}/gstreamer-%{gst_branch}/libgstthreadshare.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttogglerecord.so
%{_libdir}/gstreamer-%{gst_branch}/libgsturiplaylistbin.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsvideofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwebrtchttp.so
%dir %{_datadir}/appdata
%{_datadir}/appdata/gstreamer-plugins-rs.appdata.xml
%{_bindir}/gst-webrtc-signalling-server

%files devel
%{_libdir}/pkgconfig/*.pc

%changelog
