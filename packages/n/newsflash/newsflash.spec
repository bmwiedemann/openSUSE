#
# spec file for package newsflash
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         appid io.gitlab.news_flash.NewsFlash
Name:           newsflash
Version:        5.0.0
Release:        0
Summary:        The spiritual successor to FeedReader
License:        GPL-3.0-only
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  clang-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib-networking
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  rust+cargo >= 1.92
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(clapper-gtk-0.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkitgtk-6.0)

%description
NewsFlash is a program designed to complement an already existing web-based RSS reader account.
It combines all the advantages of web based services like syncing across all your devices with everything you expect
from a modern desktop program: Desktop notifications, fast search and filtering, tagging, handy keyboard shortcuts
and having access to all your articles as long as you like.

%lang_package

%prep
%autosetup -a1

# show the actual version in the about page
sed -i "s|version: '0.0.0'|version: '%{version}'|g" meson.build Cargo.toml

%build
%{__meson} setup \
        --buildtype=plain \
        --prefix=%{_prefix} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --includedir=%{_includedir} \
        --datadir=%{_datadir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --localedir=%{_datadir}/locale \
        --sysconfdir=%{_sysconfdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --wrap-mode=%{__meson_wrap_mode} \
        --auto-features=%{__meson_auto_features} \
        %{_vpath_srcdir} %{_vpath_builddir} \
        %{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/%{appid}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appid}-symbolic.svg

%files lang -f %{name}.lang

%changelog
