#
# spec file for package file-roller
#
# Copyright (c) 2025 SUSE LLC
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
Version:        44.5
Release:        0
Summary:        An Archive Manager for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://wiki.gnome.org/Apps/FileRoller
Source0:        %{name}-%{version}.tar.zst

# PATCH-FIX-OPENSUSE file-roller-3.4-change-archiver-priority.patch bnc#767386 gankov@opensuse.org -- Give unzip a higher priority than 7z when unpackging zip files. Gives better results for non-latin charsets.
Patch0:         file-roller-3.4-change-archiver-priority.patch
# PATCH-FEATURE-OPENSUSE file-roller-pkg-match.patch bnc#696530 dimstar@opensuse.org -- List package match names for automatic installation using PK.
Patch1:         file-roller-pkg-match.patch
# PATCH-FIX-OPENSUSE file-roller-ignore-unrar-if-wrapper.patch bsc#1072118 mgorse@suse.com -- if unrar is a wrapper script for unar, then ignore it, and use unar instead.
Patch2:         file-roller-ignore-unrar-if-wrapper.patch

# Needed for directory ownership
BuildRequires:  dbus-1
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.14.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
# Formats that we likely want to support by default
Recommends:     bzip2
Recommends:     7zip
Recommends:     cpio
Recommends:     gzip
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
Suggests:       lhasa
Suggests:       arj
# FIXME: Formats for which we don't have packages. Some are free software that
# we could package.
#Suggests:       lrzip
#Suggests:       ncompress
#Suggests:       rar
#Suggests:       theunarchiver
#Suggests:       unace
#Suggests:       unalz
#Suggests:       unstuff
DocDir:         %{_defaultdocdir}

%description
File Roller is an archive manager for GNOME. With it, you can create
and modify archives, view the contents of an archive, view a file
contained in the archive, and extract files from the archive.

%package -n nautilus-file-roller
Summary:        File-roller extension for Nautilus
Group:          Productivity/Archiving/Compression
BuildRequires:  pkgconfig(gtk4)
Requires:       %{name} = %{version}
Requires:       nautilus

%description -n nautilus-file-roller
File Roller is an archive manager for GNOME. With it, you can create
and modify archives, view the contents of an archive, view a file
contained in the archive, and extract files from the archive.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D notification=enabled \
	-D libarchive=enabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/file-roller
%{_datadir}/file-roller/
%{_libexecdir}/file-roller/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.FileRoller.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/dbus-1/services/org.gnome.ArchiveManager1.service
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml

%files -n nautilus-file-roller
%{_libdir}/nautilus/extensions-4/libnautilus-fileroller.so

%files lang -f %{name}.lang

%changelog
