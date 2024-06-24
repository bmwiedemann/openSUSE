#
# spec file for package tuba
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


%define         appname dev.geopjr.Tuba
Name:           tuba
Version:        0.8.1
Release:        0
Summary:        Browse the Fediverse
License:        GPL-3.0-only
URL:            https://github.com/GeopJr/Tuba
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.48
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.4.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(libsecret-1) >= 0.20
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.10

%lang_package

%description
%{summary}.

%prep
%autosetup -n Tuba-%{version}

%build
%make_build release=1

%install
%make_install
%find_lang %{appname}
%suse_update_desktop_file %{appname}

%check
%make_build test

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md README.md
%{_bindir}/%{appname}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/dev.geopjr.Tuba.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/fedi-*.lang
%{_datadir}/gtksourceview-5/styles/fedi*
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_mandir}/man1/%{appname}.1.gz
%{_datadir}/metainfo/%{appname}.metainfo.xml

%files lang -f %{appname}.lang

%changelog
