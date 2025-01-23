#
# spec file for package clapper-enhancers
#
# Copyright (c) 2024 SUSE LLC
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
%define clapper_ver 0.8.0

%bcond_without lbry
%bcond_without peertube
%bcond_without yt_dlp

Name:           clapper-enhancers
Version:        0.8.1
Release:        0
Summary:        Plugins enhancing Clapper library capabilities
License:        LGPL-2.1-or-later
URL:            https://rafostar.github.io/clapper/
Source0:        https://github.com/Rafostar/clapper-enhancers/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.76.0
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(clapper-%{clapper_libver}) >= %{clapper_ver}
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0

%if %{with lbry} || %{with peertube}
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.20.0
BuildRequires:  pkgconfig(libsoup-3.0)
%endif

%description
Plugins enhancing Clapper library capabilities

%if %{with lbry}
%package lbry
Summary:  Clapper Enhancer LBRY

%description lbry
Stream LBRY vidoes within Clapper
%endif

%if %{with peertube}
%package peertube
Summary:  Clapper Enhancer PeerTube

%description peertube
Stream PeerTube vidoes within Clapper
%endif

%if %{with yt_dlp}
%package yt-dlp
Summary:  Clapper Enhancer yt-dlp
Requires: python3-gobject
%if 0%{?suse_version}
Requires: python3-yt-dlp
Requires: typelib(GLib) = 2.0
Requires: typelib(GObject) = 2.0
Requires: typelib(Gio) = 2.0
Requires: typelib(Gst) = 1.0
Requires: typelib(Clapper) = %{clapper_libver}
%else
Requires: yt-dlp
Requires: glib2
Requires: gstreamer1
Requires: libclapper-%{clapper_altlibver}-%{clapper_sover}
%endif

%description yt-dlp
Stream a subset of services provided by yt-dlp within clapper
%endif

%prep
%autosetup -p1

%build
%meson \
	-Dlbry=%{?with_lbry:enabled}%{!?with_lbry:disabled} \
	-Dpeertube=%{?with_peertube:enabled}%{!?with_peertube:disabled} \
	-Dyt-dlp=%{?with_yt_dlp:enabled}%{!?with_yt_dlp:disabled} \
	%{nil}
%meson_build
%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/

%if %{with lbry}
%files lbry
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/lbry/
%endif

%if %{with peertube}
%files peertube
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/peertube/
%endif

%if %{with yt_dlp}
%files yt-dlp
%dir %{_libdir}/clapper-%{clapper_libver}/enhancers/
%{_libdir}/clapper-%{clapper_libver}/enhancers/yt-dlp/
%endif

%changelog
