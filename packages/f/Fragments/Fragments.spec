#
# spec file for package Fragments
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           Fragments
Version:        1.4
Release:        0
Summary:        A GTK3 BitTorrent Client
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://gitlab.gnome.org/World/Fragments
Source:         %{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  libminiupnpc-devel
BuildRequires:  meson
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.10
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(zlib)

%description
Fragments is an easy to use BitTorrent client which follows the
GNOME HIG and includes well thought-out features.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang fragments %{?no_lang_C}
%suse_update_desktop_file -r de.haeckerfelix.Fragments Network FileTransfer P2P GTK


%files
%license COPYING
%doc README.md
%{_bindir}/fragments
%{_datadir}/applications/de.haeckerfelix.Fragments.desktop
%{_datadir}/glib-2.0/schemas/de.haeckerfelix.Fragments.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/de.haeckerfelix.Fragments.appdata.xml

%files lang -f fragments.lang

%changelog
