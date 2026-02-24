#
# spec file for package Komikku
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


%define         appid info.febvre.Komikku
Name:           Komikku
Version:        1.103.0
Release:        0
Summary:        A manga reader for GNOME
# appdata.xml is CC-BY-4.0
License:        CC-BY-4.0 AND GPL-3.0-or-later
URL:            https://codeberg.org/valos/Komikku
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         convert-to-modern-colorthief.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson >= 0.59.0
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(glycin-gtk4-2) >= 2.0.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(python3)
Requires:       WebKitGTK-6.0
Requires:       python3-Brotli >= 1.1.0
Requires:       python3-Pillow >= 10.3.0
Requires:       python3-PyJWT
Requires:       python3-Unidecode
Requires:       python3-beautifulsoup4
Requires:       python3-cffi
Requires:       python3-cloudscraper
Requires:       python3-cryptography
Requires:       python3-dateparser >= 1.1.6
Requires:       python3-ebooklib
Requires:       python3-emoji
Requires:       python3-gobject
Requires:       python3-keyring >= 21.6.0
Requires:       python3-lxml >= 5.2.1
Requires:       python3-modern-colorthief >= 0.1.3
Requires:       python3-natsort >= 7.1.1
Requires:       python3-piexif
Requires:       python3-pure-protobuf >= 3.0.0
Requires:       python3-pycairo
Requires:       python3-pypdf
Requires:       python3-python-magic
Requires:       python3-pytz
Requires:       python3-rarfile
Requires:       python3-regex
Requires:       python3-requests >= 2.32.2
Requires:       python3-setuptools-gettext
Requires:       python3-typing_extensions
Requires:       python3-tzlocal
Requires:       python3-urllib3
Requires:       python3-wheel
Requires:       unrar_wrapper
BuildArch:      noarch

%description
Komikku is a manga reader for GNOME. It focuses on providing a clean, intuitive
and adaptive interface.

Keys features
* Online reading from dozens of servers
* Offline reading of downloaded comics
* Categories to organize your library
* RTL, LTR, Vertical and Webtoon reading modes
* Several types of navigation:
  * Keyboard arrow keys
  * Right and left navigation layout via mouse click or tapping
    (touchpad/touch screen)
  * Mouse wheel
  * 2-fingers swipe gesture (touchpad)
  * Swipe gesture (touch screen)
* Automatic update of comics
* Automatic download of new chapters
* Reading history
* Light and dark themes

%lang_package

%prep
%autosetup -p1 -n komikku

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%find_lang komikku

%check
%meson_test

%files
%license LICENSES/*
%doc README.md CONTRIBUTING.md
%{_bindir}/komikku
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/komikku
%{_datadir}/dbus-1/services/%{appid}.service
%{python_sitelib}/komikku

%files lang -f komikku.lang

%changelog
