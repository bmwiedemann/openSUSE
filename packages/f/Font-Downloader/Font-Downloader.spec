#
# spec file for package Font-Downloader
#
# Copyright (c) 2023 SUSE LLC
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


Name:           Font-Downloader
Version:        10.0.0
Release:        0
Summary:        Install fonts from online sources
License:        GPL-3.0-or-later
URL:            https://github.com/GustavoPeredo/Font-Downloader
Source:         https://github.com/GustavoPeredo/Font-Downloader/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
Font-Downloader is an application allows you to search and install fonts
directly from the Google Fonts website.

%lang_package

%prep
%autosetup -p1

chmod -x COPYING README.md src/*.py data/*.gschema.xml
sed -Ei "1{\@^#!/usr/bin/env@d}" src/fsync.py

%build
%meson
%meson_build

%install
%meson_install

%find_lang fontdownloader

%files
%license COPYING
%doc README.md
%{_bindir}/fontdownloader
%{_datadir}/applications/*.desktop
%{_datadir}/fontdownloader/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.appdata.xml

%files lang -f fontdownloader.lang

%changelog
