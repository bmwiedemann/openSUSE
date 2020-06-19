#
# spec file for package gjiten
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.6
Release:        0
Summary:        Japanese Dictionary Browser for GNOME/GTK+
License:        GPL-2.0-or-later
Group:          Productivity/Office/Dictionary
URL:            http://gjiten.sourceforge.net/

# CVS version is here:
#  cvs -d:pserver:anonymous@gjiten.cvs.sourceforge.net:/cvsroot/gjiten login
#  (empty password)
#  cvs -d:pserver:anonymous@gjiten.cvs.sourceforge.net:/cvsroot/gjiten checkout gjiten
Source:         %url/%name-%version.tar.gz

Patch0:         %name.patch
Patch1:         %name-desktop.patch
Patch2:         configure-set-foreign.patch
Patch3:         stop-using-gnome-common.patch
Patch4:         skip-validation.patch
Patch5:         gjiten-automake-fix.diff
Patch6:         stop-using-libgnome-ui.patch
Patch7:         switch-to-GtkBuilder.patch
Patch8:         port-to-GSettings.patch
Patch9:         bugzilla-348100-empty-radicals-window.patch

BuildRequires:  autoconf-archive
BuildRequires:  edict
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  update-desktop-files
BuildRequires:  w3m
BuildRequires:  xmlto
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.14
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
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install
b="%buildroot"
ln -fsv "%_datadir/edict/radkfile" "$b/%_datadir/%name/radkfile.utf8"
mkdir "$b/%_datadir/%name/dics"
for i in %_datadir/edict/*; do
	ln -s "$i" "$b/%_datadir/%name/dics/"
done
# Drop legacy GNOME 1 content
rm -rf %{buildroot}%_datadir/application-registry/
%find_lang %name
%suse_update_desktop_file %name Office Dictionary

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*
%_datadir/doc/*
%_datadir/GConf/
%_datadir/glib-2.0/
%_datadir/omf/
%_datadir/%name/
%_datadir/pixmaps/*
%_datadir/gnome/
%_mandir/man1/*.1*

%changelog
