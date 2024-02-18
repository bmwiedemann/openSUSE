#
# spec file for package newsflash
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


%define         _lto_cflags %{nil}
Name:           newsflash
Version:        3.1.3
Release:        0
Summary:        The spiritual successor to FeedReader
License:        GPL-3.0-only
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        news_flash_gtk-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  blueprint-compiler
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib-networking
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  webkit2gtk4-devel
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(webkitgtk-6.0)

%description
NewsFlash is a program designed to complement an already existing web-based RSS reader account.
It combines all the advantages of web based services like syncing across all your devices with everything you expect
from a modern desktop program: Desktop notifications, fast search and filtering, tagging, handy keyboard shortcuts
and having access to all your articles as long as you like.

%lang_package

%prep
%autosetup -p1 -a1 -n news_flash_gtk-%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/io.gitlab.news_flash.NewsFlash
%{_datadir}/applications/io.gitlab.news_flash.NewsFlash.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/io.gitlab.news_flash.NewsFlash.appdata.xml

%files lang -f %{name}.lang

%changelog
