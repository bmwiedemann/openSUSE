#
# spec file for package warp
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


# Check license crate and data version from vendor.tar.zst
# The vendored dir will be named as vendor/license-<lic_crate_ver>+<lic_data_ver>/
%define lic_crate_ver 3.6.0
%define lic_data_ver 3.26.0
Name:           warp
Version:        0.9.2
Release:        0
Summary:        App to securely send files via the internet or local network
License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/en-GB/app/app.drey.Warp/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        https://github.com/spdx/license-list-data/archive/refs/tags/v%{lic_data_ver}.tar.gz#/license-list-data-%{version}.tar.gz
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.13.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(zbar)
# Binary /usr/bin/warp conflicts with same name binary from totally different app ghc-wai-app-static
Conflicts:      ghc-wai-app-static

%description
Warp allows you to securely send files to each other via the internet or local
network by exchanging a word-based code.

The best transfer method will be determined using the "Magic Wormhole" protocol
which includes local network transfer if possible.

%lang_package

%prep
%autosetup -p1 -a1 -b2
mkdir -p vendor/license-%{lic_crate_ver}+%{lic_data_ver}/license-list-data
cp -pr ../license-list-data-%{lic_data_ver}/* vendor/license-%{lic_crate_ver}+%{lic_data_ver}/license-list-data/

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
%{_datadir}/warp/

%files lang -f %{name}.lang

%changelog
