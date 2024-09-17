#
# spec file for package gnome-radio
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


Name:           gnome-radio
Version:        128
Release:        0
Summary:        Live Internet radio broadcaster discovery program
License:        GPL-3.0-or-later
URL:            https://www.gnomeradio.org
Source:         %{name}-%{version}.tar.zst
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.34
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangoft2)
Provides:       gnome-internet-radio-locator = %{version}
Obsoletes:      gnome-internet-radio-locator < 16
Provides:       girl < 11
Obsoletes:      girl = %{version}

%description
GNOME Radio is a Free Software program that allows you to easily
locate Free Internet Radio stations by broadcasters on the Internet
with the help of map and text search.  GNOME Radio is developed on
the GNOME desktop platform and it requires at least GStreamer 1.0
for playback.  Enjoy Free Internet Radio.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang gtk-internet-radio-locator

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/gtk-internet-radio-locator
%{_datadir}/icons/hicolor/*/apps/gtk-internet-radio-locator.*
%{_datadir}/appdata/gtk-internet-radio-locator.appdata.xml
%{_datadir}/applications/gtk-internet-radio-locator.desktop
%{_datadir}/gtk-internet-radio-locator/
%{_mandir}/man1/gtk-internet-radio-locator.1%{?ext_man}

%files lang -f gtk-internet-radio-locator.lang

%changelog
