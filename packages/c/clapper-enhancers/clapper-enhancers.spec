#
# spec file for package clapper-enhancers
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Florian "sp1rit"
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


%define clapper_libver 0.0
%define clapper_altlibver %(sed s/[.]/_/g <<< %{clapper_libver})
%define clapper_sover 0
%define clapper_ver 0.10.0

%bcond_without control_hub
%bcond_without lbry
%bcond_without media_scanner
%bcond_without mpris
%bcond_without parser_m3u
%bcond_without peertube
%bcond_without recall
%bcond_without yt_dlp

Name:           clapper-enhancers
Version:        0.10.0
Release:        0
Summary:        Plugins enhancing Clapper library capabilities
License:        LGPL-2.1-or-later
URL:            https://rafostar.github.io/clapper/
Source0:        https://github.com/Rafostar/clapper-enhancers/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig(clapper-%{clapper_libver}) >= %{clapper_ver}
BuildRequires:  pkgconfig(gio-2.0) >= 2.76.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.76.0

%if %{with control_hub} || %{with lbry} || %{with media_scanner} || %{with mpris} || %{with parser_m3u} || %{with peertube} || %{with recall}
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20.0
BuildRequires:  pkgconfig(libpeas-2)
%endif

%if %{with lbry} || %{with media_scanner} || %{with mpris} || %{with parser_m3u} || %{with peertube}
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.20.0
%endif

%if %{with control_hub} || %{with lbry} || %{with peertube}
BuildRequires:  pkgconfig(libsoup-3.0)
%endif

%if %{with control_hub}
BuildRequires:  pkgconfig(microdns) >= 0.2.0
%endif

%if %{with lbry} || %{with peertube}
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
%endif

%if %{with recall}
BuildRequires:  pkgconfig(sqlite3)
%endif

%if %{with yt_dlp}
BuildRequires:  libpeas2-loader-python
BuildRequires:  python3-gobject
%endif

%description
Plugins enhancing Clapper library capabilities

%if %{with control_hub}
%package control-hub
Summary:        Clapper Enhancer Control Hub

%description control-hub
Allows to control playback remotely
%endif

%if %{with lbry}
%package lbry
Summary:        Clapper Enhancer LBRY

%description lbry
Stream LBRY vidoes within Clapper
%endif

%if %{with media_scanner}
%package media-scanner
Summary:        Clapper Enhancer Media Scanner

%description media-scanner
Discovers queued media information
%endif

%if %{with mpris}
%package mpris
Summary:        Clapper Enhancer MPRIS

%description mpris
MPRIS support
%endif

%if %{with parser_m3u}
%package parser-m3u
Summary:        Clapper Enhancer Parser M3U

%description parser-m3u
M3U playlists support
%endif

%if %{with peertube}
%package peertube
Summary:        Clapper Enhancer PeerTube

%description peertube
Stream PeerTube vidoes within Clapper
%endif

%if %{with recall}
%package recall
Summary:        Clapper Enhancer Recall
%if 0%{?suse_version}
Requires:       sqlite3
%else
Requires:       sqlite
%endif

%description recall
Recalls the last playback position
%endif

%if %{with yt_dlp}
%package yt-dlp
Summary:        Clapper Enhancer yt-dlp
Requires:       python3-gobject
%if 0%{?suse_version}
Requires:       libpeas2-loader-python
Requires:       python3-yt-dlp
Requires:       typelib(Clapper) = %{clapper_libver}
Requires:       typelib(GLib) = 2.0
Requires:       typelib(GObject) = 2.0
Requires:       typelib(Gio) = 2.0
Requires:       typelib(Gst) = 1.0
%else
Requires:       glib2
Requires:       gstreamer1
Requires:       libclapper-%{clapper_altlibver}-%{clapper_sover}
Requires:       libpeas-loader-python
Requires:       yt-dlp
%endif

%description yt-dlp
Stream a subset of services provided by yt-dlp within clapper
%endif

%prep
%autosetup -p1

%build
%meson \
	-Dcontrol-hub=%{?with_control_hub:enabled}%{!?with_control_hub:disabled} \
	-Dlbry=%{?with_lbry:enabled}%{!?with_lbry:disabled} \
	-Dmedia-scanner=%{?with_media_scanner:enabled}%{!?with_media_scanner:disabled} \
	-Dmpris=%{?with_mpris:enabled}%{!?with_mpris:disabled} \
	-Dparser-m3u=%{?with_parser_m3u:enabled}%{!?with_parser_m3u:disabled} \
	-Dpeertube=%{?with_peertube:enabled}%{!?with_peertube:disabled} \
	-Drecall=%{?with_recall:enabled}%{!?with_recall:disabled} \
	-Dyt-dlp=%{?with_yt_dlp:enabled}%{!?with_yt_dlp:disabled} \
	%{nil}
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/

%if %{with control_hub}
%files control-hub
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/control-hub/
%endif

%if %{with lbry}
%files lbry
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/lbry/
%endif

%if %{with media_scanner}
%files media-scanner
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/media-scanner/
%endif

%if %{with mpris}
%files mpris
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/mpris/
%endif

%if %{with parser_m3u}
%files parser-m3u
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/parser-m3u/
%endif

%if %{with peertube}
%files peertube
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/peertube/
%endif

%if %{with recall}
%files recall
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/recall/
%endif

%if %{with yt_dlp}
%files yt-dlp
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/yt-dlp/
%endif

%changelog
