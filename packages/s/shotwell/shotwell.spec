#
# spec file for package shotwell
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           shotwell
Version:        0.30.11
Release:        0
Summary:        Photo Manager for GNOME
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://wiki.gnome.org/Apps/Shotwell

Source0:        https://download.gnome.org/sources/%{name}/0.30/%{name}-%{version}.tar.xz
Source99:       shotwell-rpmlintrc

BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.7
BuildRequires:  libraw-devel-static
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8) >= 0.10.0
BuildRequires:  pkgconfig(gexiv2) >= 0.11.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.26

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment. It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dunity-support=false \
	-Dextra-plugins=true \
	-Ddupe-detection=false \
	-Dinstall-apport-hook=false \
	%{nil}
%meson_build

%install
%meson_install

%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS THANKS
%doc %{_datadir}/help/C/%{name}/
%{_mandir}/man1/shotwell.1%{?ext_man}
%{_bindir}/shotwell
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/shotwell.appdata.xml
%{_datadir}/applications/shotwell*.desktop
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell-extras.gschema.xml
%{_datadir}/icons/hicolor/*/apps/shotwell*
%{_libdir}/shotwell/
# This is not split as the only consumer is shotwell itself.
%{_libdir}/libshotwell-authenticator.so
%{_libdir}/libshotwell-authenticator.so.0
%{_libdir}/libshotwell-authenticator.so.%{version}
%{_libdir}/libshotwell-plugin-common.so
%{_libdir}/libshotwell-plugin-common.so.0
%{_libdir}/libshotwell-plugin-common.so.%{version}
%{_libdir}/libshotwell-plugin-dev-1.0.so
%{_libdir}/libshotwell-plugin-dev-1.0.so.0
%{_libdir}/libshotwell-plugin-dev-1.0.so.%{version}
%dir %{_libexecdir}/shotwell
%{_libexecdir}/shotwell/shotwell-settings-migrator
%{_libexecdir}/shotwell/shotwell-video-thumbnailer

%files lang -f %{name}.lang

%changelog
