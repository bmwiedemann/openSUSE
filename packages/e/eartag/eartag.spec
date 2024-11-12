#
# spec file for package eartag
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


Name:           eartag
Version:        0.6.3
Release:        0
Summary:        Edit audio file tags
License:        MIT
URL:            https://gitlab.gnome.org/World/eartag
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  blueprint-compiler
BuildRequires:  meson
BuildRequires:  python3-Pillow
BuildRequires:  python3-gobject
BuildRequires:  python3-mutagen
BuildRequires:  python3-pyacoustid
BuildRequires:  python3-python-magic
BuildRequires:  pkgconfig(gtk4) >= 4.16
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
Requires:       chromaprint-fpcalc
Requires:       python3-Pillow
Requires:       python3-gobject
Requires:       python3-mutagen
Requires:       python3-pyacoustid
Requires:       python3-python-magic

%description
Ear Tag is a simple audio file tag editor. It is primarily geared towards making quick edits or bulk-editing tracks in albums/EPs.
Unlike other tagging programs, Ear Tag does not require the user to set up a music library folder.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang app.drey.EarTag

%files
%license COPYING
%doc README.md
%{_bindir}/eartag
%{_datarootdir}/applications/app.drey.EarTag.desktop
%dir %{_datarootdir}/eartag
%{_datarootdir}/eartag/*
%{_datarootdir}/icons/*
%{_datarootdir}/metainfo/app.drey.EarTag.metainfo.xml
%{_datarootdir}/glib-2.0/schemas/app.drey.EarTag.gschema.xml

%files lang -f app.drey.EarTag.lang

%changelog
