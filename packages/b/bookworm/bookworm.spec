#
# spec file for package bookworm
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


%define         appid com.github.babluboy.bookworm
Name:           bookworm
Version:        1.1.2
Release:        0
Summary:        E-book reader
License:        GPL-3.0-or-later
URL:            https://github.com/babluboy/bookworm
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  html2text
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  poppler-tools
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.16.0
Recommends:     unrar
Recommends:     unzip

%description
An eBook reader for the Pantheon Desktop.

It uses poppler for decoding and read formats like EPUB, PDF, mobi, cbr, etc.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{appid}
%fdupes %{buildroot}

# fix shebangs
%python2_fix_shebang_path %{buildroot}%{_datadir}/%{appid}/scripts/mobi_lib/*.py
sed -i '1 i #!/usr/bin/sh' %{buildroot}%{_datadir}/%{appid}/scripts/tasks/%{appid}.dictionary.sh

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{appid}
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
