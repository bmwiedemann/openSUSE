#
# spec file for package amberol
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
Name:           amberol
Version:        2025.1
Release:        0
Summary:        A small and simple sound and music player that is well integrated with GNOME
License:        CC-BY-SA-3.0 AND CC0-1.0 AND GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/amberol
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  m4
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  reuse
BuildRequires:  mpfrcx-devel
BuildRequires:  cargo-c
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.16
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(gmp)
ExclusiveArch:  %{rust_tier1_arches}

%description
A small and simple sound and music player that is well integrated with GNOME.
Amberol aspires to be as small, unintrusive, and simple as possible. It does
not manage your music collection; it does not let you manage playlists, smart
or otherwise; it does not let you edit the metadata for your songs; it does
not show you lyrics for your songs, or the Wikipedia page for your bands.
Amberol plays music, and nothing else.

%lang_package

%prep
%autosetup -n %{name}-%{version} -a1 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license LICENSES/{GPL-3.0-or-later,CC-BY-SA-3.0,CC0-1.0}.txt
%doc README.md CHANGES.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/io.bassi.Amberol.metainfo.xml
%{_datadir}/applications/io.bassi.Amberol.desktop
%{_datadir}/dbus-1/services/io.bassi.Amberol.service
%{_datadir}/glib-2.0/schemas/io.bassi.Amberol.gschema.xml
%{_datadir}/icons/*/*/*/*.svg

%files lang -f %{name}.lang

%changelog
