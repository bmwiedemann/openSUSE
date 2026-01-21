#
# spec file for package minder
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


%define         appid com.github.phase1geo.minder
Name:           minder
Version:        2.0.4
Release:        0
Summary:        Mind-mapping app
License:        GPL-3.0-only
URL:            https://github.com/phase1geo/Minder
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-setuptools
BuildRequires:  vala >= 0.48.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libmarkdown) >= 3.0
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)

%description
A program to create, develop, visualize, organize and manage ideas.

%lang_package

%prep
%autosetup -n Minder-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/mime/packages/%{appid}.xml
%{_datadir}/%{name}

%files lang -f %{appid}.lang

%changelog
