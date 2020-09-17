#
# spec file for package gnonograms
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

Name:           gnonograms
Version:        1.4.5
Release:        0
Summary:        Program for creating and solving gnonogram puzzles
License:        GPL-3.0-or-later
Group:          Amusements/Games/Logic
URL:            https://github.com/jeremypw
Source:         https://github.com/jeremypw/gnonograms/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  AppStream
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0) > 3.22.0
Recommends:     %{name}-lang

%description
An implementation of the Japanese logic puzzle "Nonograms".

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name com.github.jeremypw.gnonograms-extra.mo -exec rm {} +

%suse_update_desktop_file -r com.github.jeremypw.gnonograms GTK Game LogicGame
%find_lang com.github.jeremypw.gnonograms %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license LICENSE
%doc README.md
%{_bindir}/com.github.jeremypw.gnonograms
%{_datadir}/metainfo/com.github.jeremypw.gnonograms.appdata.xml
%{_datadir}/applications/com.github.jeremypw.gnonograms.desktop
%{_datadir}/icons/hicolor/*/*/*.??g
%{_datadir}/glib-2.0/schemas/com.github.jeremypw.gnonograms.gschema.xml
%{_datadir}/mime/packages/com.github.jeremypw.gnonograms.mimeinfo.xml

%files lang -f %{name}.lang

%changelog
