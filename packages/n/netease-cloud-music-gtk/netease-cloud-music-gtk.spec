#
# spec file for package netease-cloud-music-gtk
#
# Copyright (c) 2020 SUSE LLC
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


Name:           netease-cloud-music-gtk
Version:        1.1.2
Release:        0
Summary:        Linux 平台下基于 Rust + GTK 开发的网易云音乐播放器
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/gmg137/netease-cloud-music-gtk
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.41
BuildRequires:  rust-std
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(openssl)
Requires:       gstreamer
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly
Requires:       openssl

%description
netease-cloud-music-gtk 是基于 Rust + GTK 开发的网易云音乐播放器，专为 Linux 系统打造。

%prep
%setup -q -a1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
export CARGO_HOME=$PWD
%if 0%{?suse_version} <= 1510
cargo build --release --no-default-features --features gtk_3_18
%else
cargo build --release
%endif

%install
install -Dm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 644 icons/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
