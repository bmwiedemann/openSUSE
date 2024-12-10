#
# spec file for package playmyvideos
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


%define         appid com.github.artemanufrij.playmyvideos
Name:           playmyvideos
Version:        1.1.2
Release:        0
Summary:        A video player for local files
License:        GPL-3.0-or-later
URL:            https://github.com/artemanufrij/playmyvideos
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(granite) >= 5.1.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
Provides:       cinema = %{version}
Obsoletes:      cinema < %{version}

%description
A video player for watching local video files.

%lang_package

%prep
%autosetup

cp --no-preserve='mode' debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f %{appid}.lang

%changelog
