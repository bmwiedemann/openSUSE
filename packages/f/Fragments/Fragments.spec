#
# spec file for package Fragments
#
# Copyright (c) 2024 SUSE LLC
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


# Disable LTO, fails to build with GCC 14
#%%global _lto_cflags %%{?_lto_cflags} -ffat-lto-objects
%define _lto_cflags %{nil}

Name:           Fragments
Version:        3.0.1
Release:        0
Summary:        A GTK4 BitTorrent Client
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://gitlab.gnome.org/World/Fragments
Source:         %{name}-%{version}.tar.xz
Source2:        vendor.tar.zst

BuildRequires:  appstream-glib
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.0.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.0
BuildRequires:  pkgconfig(sqlite3) >= 3.20
Requires:       transmission-daemon
ExcludeArch:    s390x

%description
Fragments is an easy to use BitTorrent client which follows the
GNOME HIG and includes well thought-out features.

%lang_package

%prep
%autosetup -p1 -a2

%build
export RUSTFLAGS="%{build_rustflags}"
%meson
%meson_build

%install
export RUSTFLAGS="%{build_rustflags}"
%meson_install
%find_lang fragments %{?no_lang_C}

%check
export RUSTFLAGS="%{build_rustflags}"
%meson_test
%cargo_test

%files
%license COPYING.md
%doc README.md
%{_bindir}/fragments
%{_datadir}/applications/de.haeckerfelix.Fragments.desktop
%{_datadir}/glib-2.0/schemas/de.haeckerfelix.Fragments.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/de.haeckerfelix.Fragments.metainfo.xml
%{_datadir}/dbus-1/services/de.haeckerfelix.Fragments.service
%{_datadir}/fragments/

%files lang -f fragments.lang

%changelog
