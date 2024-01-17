#
# spec file for package cinema
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cinema
Version:        1.1.2
Release:        0
Summary:        A video player for local files
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://artemanufrij.github.io
Source:         https://github.com/artemanufrij/playmyvideos/archive/%{version}.tar.gz#/playmyvideos-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(granite) >= 5.1.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
Recommends:     %{name}-lang

%description
A video player for watching local video files.

%lang_package

%prep
%setup -q -n playmyvideos-%{version}

cp --no-preserve='mode' debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.artemanufrij.playmyvideos %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/com.github.artemanufrij.playmyvideos
%{_datadir}/applications/com.github.artemanufrij.playmyvideos.desktop
%{_datadir}/glib-2.0/schemas/com.github.artemanufrij.playmyvideos.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.artemanufrij.playmyvideos.??g
%{_datadir}/metainfo/com.github.artemanufrij.playmyvideos.appdata.xml

%files lang -f %{name}.lang

%changelog
