#
# spec file for package grsync
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           grsync
Version:        1.2.8
Release:        0
Summary:        GUI for rsync
License:        GPL-2.0
Group:          Productivity/Archiving/Backup
Url:            http://www.opbyte.it/grsync/
Source:         http://www.opbyte.it/release/%{name}-%{version}.tar.gz
Patch0:         grsync.patch
Patch1:         fix-invalid-lc-messages-dir.patch
# PATCH-FIX-UPSTREAM grsync-appdata.patch badshah400@gmail.com -- Add, translate and install appdata file
Patch2:         grsync-appdata.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  intltool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.16
Requires:       rsync
Recommends:     %{name}-lang

%description
Grsync is a GUI (Graphical User Interface) for rsync, the commandline directory
and file synchronization tool. It can be effectively used to synchronize local
directories and it supports remote targets as well (even though it doesn't
support browsing the remote folder). Sample uses of grsync include: synchronize
a music collection with removable devices, backup personal files to a networked
drive, replication of a partition to another one, mirroring of files, etc.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--disable-unity
pushd po
mv ca_ES.po ca.po
mv cs_CZ.po cs.po
mv de_DE.po de.po
mv es_ES.po es.po
mv fr_FR.po fr.po
mv gl_ES.po gl.po
mv hr_HR.po hr.po
mv hu_HU.po hu.po
mv id_ID.po id.po
mv it_IT.po it.po
mv nb_NO.po nb.po
mv nl_NL.po nl.po
mv ru_RU.po ru.po
mv sv_SE.po sv.po
mv tr_TR.po tr.po
popd
dos2unix README NEWS AUTHORS

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -r %{name} Utility Archiving GTK

%files
%license COPYING
%doc AUTHORS README NEWS
%{_bindir}/grsync
%{_bindir}/grsync-batch
%{_datadir}/applications/grsync.desktop
%{_datadir}/pixmaps/grsync.png
%{_datadir}/pixmaps/grsync-busy.png
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-grsync-session.png
%{_datadir}/mime/packages/grsync.xml
%{_mandir}/man1/grsync*
%dir %{_datadir}/appdata
%{_datadir}/appdata/*.appdata.xml

%files lang -f %{name}.lang

%changelog
