#
# spec file for package gnome-internet-radio-locator
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gnome-internet-radio-locator
Version:        4.0.2
Release:        0
Summary:        Live Internet radio broadcaster discovery program
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://wiki.gnome.org/Apps/InternetRadioLocator
Source0:        https://download.gnome.org/sources/%{name}/4.0/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 0001-Fix-prototype-of-gtk_internet_radio_locator_radius.patch dimstar@opensuse.org -- Fix prototype of gtk_internet_radio_locator_radius
Patch0:         0001-Fix-prototype-of-gtk_internet_radio_locator_radius.patch

BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.10
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.28
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 0.29.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0
BuildRequires:  pkgconfig(pangoft2) >= 0.28
Provides:       girl < 11
Obsoletes:      girl = 11

%description
GNOME Internet Radio Locator is a program that allows locating free
Internet radio stations by broadcasters with the help of a map.
It is developed with GNOME Maps, libchamplain and geocode-lib.

You can view all the stations in src/gnome-internet-radio-locator.xml
and enter city names in the GUI search input field in order to locate
radio stations in the city using the text search with auto-completion.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--with-recording \
	%{nil}
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
%find_lang %{name} %{?no_lang_C} %{name}.lang

%files
%license COPYING
%doc AUTHORS ChangeLog README THANKS NEWS
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/gnome-internet-radio-locator-4.0.dtd
%{_datadir}/%{name}/gnome-internet-radio-locator.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
