#
# spec file for package gjiten
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gjiten
Version:        3.2.1
Release:        0
Summary:        Japanese Dictionary Browser for GNOME/GTK+
License:        GPL-2.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://github.com/DarkTrick/gjiten
Source:         https://github.com/DarkTrick/gjiten/archive/refs/tags/v%version.tar.gz
Patch0:         %name.patch
Patch1:         %name-desktop.patch
BuildRequires:  edict
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  perl-XML-Parser
BuildRequires:  pkg-config
BuildRequires:  sgml-skel
BuildRequires:  update-desktop-files
BuildRequires:  w3m
BuildRequires:  xmlto
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
Requires:       edict
Provides:       locale(libgnome:ja)

%description
Gjiten is a GNOME-based Japanese dictionary program. It uses the
JMdict/edict word dictionary, KANJIDIC kanji dictionary, and some of
the xjdic code. Any combination of stroke count, radicals, and search
key can be used for Kanji lookups. It requires a working X input
method (such as ibus) for Japanese input.

%prep
%autosetup -p1

%build
%meson
# https://github.com/DarkTrick/gjiten/issues/10
perl -i -lpe 's{define GJITEN_DATADIR .*}{define GJITEN_DATADIR "%_datadir/%name"}g' */config.h
grep GJITEN_DATADIR */config.h
%meson_build

%install
%meson_install
b="%buildroot"
mkdir -pv "$b/%_datadir/%name/dics"
ln -fsv "%_datadir/edict/radkfile" "$b/%_datadir/%name/radkfile.utf8"
for i in %_datadir/edict/*; do
	ln -sv "$i" "$b/%_datadir/%name/dics/"
done
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*
%_datadir/%name/
%_datadir/pixmaps/*

%changelog
