#
# spec file for package warp
#
# Copyright (c) 2023 SUSE LLC
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
Name:           warp
Version:        0.6.2
Release:        0
Summary:        App to securely send files via the internet or local network
License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/en-GB/app/app.drey.Warp/
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(libadwaita-1)
# Binary /usr/bin/warp conflicts with same name binary from totally different app ghc-wai-app-static
Conflicts:      ghc-wai-app-static

%description
Warp allows you to securely send files to each other via the internet or local
network by exchanging a word-based code.

The best transfer method will be determined using the "Magic Wormhole" protocol
which includes local network transfer if possible.

%lang_package

%prep
%autosetup -a1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md
%{_bindir}/warp
%{_datadir}/applications/*.desktop
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.metainfo.xml

%files lang -f %{name}.lang

%changelog
