#
# spec file for package sqliteman
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 Petr Vanek
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


Name:           sqliteman
Version:        1.2.2
Release:        0
Summary:        An Sqlite3 manager
License:        GPL-2.0+ AND LGPL-2.0+
Group:          Productivity/Databases/Tools
Url:            http://sqliteman.yarpen.cz/
Source0:        http://download.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM sqliteman-1.2.2-qt5.patch courtesy of gentoo team -- aloisio@gmx.com
Patch1:         sqliteman-1.2.2-qt5.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  libqscintilla-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       libQt5Sql5-sqlite

%description
Sqliteman is a graphical frontend for querying and editing SQLite3 databases.

%prep
%setup -q
%patch1 -p1
rm -rf %{name}/qscintilla2

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file -G "Toolkit for Sqlite3 database" %{name} Office Database
%fdupes %{buildroot}

%files
%doc README AUTHORS
%license COPYING
%dir %{_datadir}/sqliteman
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/sqliteman/*

%changelog
