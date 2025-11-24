#
# spec file for package ncspot
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%define _lto_cflags %{nil}
Name:           ncspot
Version:        1.3.1
Release:        0
Summary:        Cross-platform ncurses Spotify client written in Rust
Group:          Productivity/Multimedia/Sound/Players
License:        BSD-2-Clause
URL:            https://github.com/hrkfdn/ncspot
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(xcb)

%description
ncurses Spotify client written in Rust using librespot. It is heavily inspired by ncurses MPD clients, such as ncmpc. My motivation was to provide a simple and resource friendly alternative to the official client as well as to support platforms that currently don't have a Spotify client, such as the *BSDs.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}
# install the desktop file
install -Dm 0644 misc/ncspot.desktop %{buildroot}/%{_datadir}/applications/ncspot.desktop
install -Dm 0644 images/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/ncspot.svg

%files
%license LICENSE
%doc README.md
%{_bindir}/ncspot
%{_datadir}/applications/ncspot.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/ncspot.svg

%changelog
