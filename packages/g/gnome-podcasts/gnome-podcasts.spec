#
# spec file for package gnome-podcasts
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019 Bjørn Lie, Bryne, Norway.
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           gnome-podcasts
Version:        0.6.1
Release:        0
Summary:        Podcast app for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/podcasts
Source:         %{name}-%{version}.tar.zst
Source2:        vendor.tar.zst
Source3:        cargo_config

BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.16
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  pkgconfig(sqlite3) >= 3.20

%lang_package

%description
A Podcast application for GNOME.
Listen to your favorite podcasts, right from your desktop.

%prep
%autosetup -p1 -a2
mkdir .cargo
cp %{SOURCE3} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
%meson \
	-Dprofile=default \
	%{nil}
%meson_build

%install
export RUSTFLAGS=%{rustflags}
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Podcasts.desktop
%{_datadir}/dbus-1/services/org.gnome.Podcasts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Podcasts.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Podcasts*.svg
%{_datadir}/metainfo/org.gnome.Podcasts.appdata.xml

%files lang -f %{name}.lang

%changelog
