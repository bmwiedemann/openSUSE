#
# spec file for package netease-cloud-music-gtk
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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
%define _lto_cflags %{nil}
Name:           netease-cloud-music-gtk
Version:        2.4.1
Release:        0
Summary:        Linux 平台下基于 Rust + GTK4 开发的网易云音乐播放器
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/gmg137/netease-cloud-music-gtk
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Patch1:         fix-dependencies.patch

BuildRequires:  cargo-packaging
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-play-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(openssl)
Requires:       gstreamer
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly
Requires:       openssl

%description
netease-cloud-music-gtk 是基于 Rust + GTK4 开发的网易云音乐播放器，专为 Linux 系统打造。

%lang_package

%prep
%setup -q -a1
%autopatch -p1
mkdir .cargo
cat >.cargo/config.toml <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = 'vendor'
EOF

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.gitee.gmg137.NeteaseCloudMusicGtk4 "GNOME;GTK;AudioVideo;Player;Audio;"
%find_lang %{name}4

%files
%license  COPYING
%{_bindir}/%{name}4
%{_datadir}/metainfo/com.gitee.gmg137.NeteaseCloudMusicGtk4.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/com.gitee.gmg137.NeteaseCloudMusicGtk4.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.gitee.gmg137.NeteaseCloudMusicGtk4.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.gitee.gmg137.NeteaseCloudMusicGtk4-symbolic.svg
%{_datadir}/netease-cloud-music-gtk4
%{_datadir}/netease-cloud-music-gtk4/%{name}4.gresource

%files lang -f %{name}4.lang

%changelog
