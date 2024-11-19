#
# spec file for package pantheon-photos
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


%define         appid io.elementary.photos
Name:           pantheon-photos
Version:        8.0.1
Release:        0
Summary:        The continuation of Shotwell in Granite
License:        LGPL-2.1-or-later
URL:            https://github.com/elementary/photos
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson >= 0.57.0
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.40
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sqlite3)
Provides:       elementary-photos = %{version}
Obsoletes:      elementary-photos < %{version}

%description
pantheon-photos is a digital photo organizer based on Shotwell and
designed for the Pantheon Desktop. It allows you to import
photos from disk or camera, organize them in various ways, view them
in full-window or fullscreen mode, and export them to share with
others.

%package        plugins
Summary:        A collection of plugins for %{name}
Requires:       %{name} = %{version}

%description    plugins
The continuation of Shotwell.

This package contains a collection of plugins: publishing, transitions and etc.

%lang_package

%prep
%autosetup -n photos-%{version}

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}{,.viewer}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}{,.viewer}.svg
%{_libexecdir}/%{appid}
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files plugins
%{_libdir}/%{appid}

%files lang -f %{appid}.lang

%changelog
