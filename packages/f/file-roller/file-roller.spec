#
# spec file for package file-roller
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           file-roller
Version:        3.32.2
Release:        0
Summary:        An Archive Manager for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://wiki.gnome.org/Apps/FileRoller
Source0:        https://download.gnome.org/sources/file-roller/3.32/%{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE file-roller-3.4-change-archiver-priority.patch bnc#767386 gankov@opensuse.org -- Give unzip a higher priority than 7z when unpackging zip files. Gives better results for non-latin charsets.
Patch0:         file-roller-3.4-change-archiver-priority.patch
# PATCH-FEATURE-OPENSUSE file-roller-pkg-match.patch bnc#696530 dimstar@opensuse.org -- List package match names for automatic installation using PK.
Patch1:         file-roller-pkg-match.patch
# PATCH-FIX-OPENSUSE file-roller-ignore-unrar-if-wrapper.patch bsc#1072118 mgorse@suse.com -- if unrar is a wrapper script for unar, then ignore it, and use unar instead.
Patch2:         file-roller-ignore-unrar-if-wrapper.patch

# Needed for directory ownership
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.2
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.14.0
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libnotify) >= 0.4.3
# Formats that we likely want to support by default
Recommends:     bzip2
Recommends:     cpio
Recommends:     gzip
Recommends:     p7zip-full
Recommends:     rpm
Recommends:     unar
Recommends:     unzip
Recommends:     xz
Recommends:     zip
# Additional formats that are supported
Suggests:       lzip
Suggests:       lzop
Suggests:       rzip
Suggests:       zoo
# FIXME: Formats for which we don't have packages. Some are free software that
# we could package.
#Suggests:       lha
#Suggests:       lrzip
#Suggests:       arj
#Suggests:       ncompress
#Suggests:       rar
#Suggests:       theunarchiver
#Suggests:       unace
#Suggests:       unalz
#Suggests:       unstuff
Obsoletes:      nautilus-file-roller
DocDir:         %{_defaultdocdir}

%description
File Roller is an archive manager for GNOME. With it, you can create
and modify archives, view the contents of an archive, view a file
contained in the archive, and extract files from the archive.

%lang_package

%prep
%autosetup -N
%patch0 -p1
%patch1 -p1
%patch2 -p1
translation-update-upstream po %{name}

%build
%meson \
	-D notification=true \
	-D libarchive=true \
	-D magic=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/file-roller
%{_libexecdir}/file-roller/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.FileRoller.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/dbus-1/services/org.gnome.FileRoller.ArchiveManager1.service
%{_datadir}/file-roller/
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*

%files lang -f %{name}.lang

%changelog
