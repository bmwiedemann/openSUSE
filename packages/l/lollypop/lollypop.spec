#
# spec file for package lollypop
#
# Copyright (c) 2022 SUSE LLC
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


Name:           lollypop
Version:        1.4.37
Release:        0
Summary:        GNOME music playing application
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://wiki.gnome.org/Apps/Lollypop
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson >= 0.46
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.29.1
Requires:       dbus-1-python3
Requires:       gstreamer-plugins-base
Requires:       python3-Pillow
Requires:       python3-beautifulsoup4
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gst
Recommends:     easytag
Recommends:     kid3-cli
Recommends:     yt-dlp
Suggests:       python3-textblob
BuildArch:      noarch

%description
Lollypop is a GNOME music playing application. It provides the following
features:
* Supports mp3/4, ogg and flac
* Genre/Cover browsing
* Genre/Artist/Cover browsing
* Search
* Main playlist (called queue in other apps)
* Party mode
* Replay gain
* Cover art downloader
* Context artist view
* MTP sync
* Fullscreen view
* Last.fm support
* Auto install codecs
* HiDPI support
* Tunein support.

%package -n gnome-shell-search-provider-lollypop
Summary:        GNOME music playing application - gnome-shell search provider
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-lollypop
Lollypop is a GNOME music playing application.

This package contains a search provider to enable GNOME Shell to get
search results from %{name}.

%lang_package

%prep
%autosetup -p1
# Don't use env interpreter so that the rpm dependency detection works
sed -i 's;/usr/bin/env python3;/usr/bin/python3;' lollypop.in search-provider/lollypop-sp.in

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/org.gnome.Lollypop.appdata.xml
%{_datadir}/applications/org.gnome.Lollypop.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Lollypop.gschema.xml
%{_datadir}/icons/hicolor/*/*/org.gnome.Lollypop*
%{_mandir}/man1/lollypop.1%{?ext_man}
%{python3_sitelib}/lollypop/

%files -n gnome-shell-search-provider-%{name}
%{_libexecdir}/lollypop-sp
%{_datadir}/dbus-1/services/org.gnome.Lollypop.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Lollypop.SearchProvider.ini

%files lang -f %{name}.lang

%changelog
