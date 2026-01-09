#
# spec file for package sqlitebrowser
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           sqlitebrowser
Version:        3.13.99
Release:        0
Summary:        Spreadsheet-like interface to SQLite databases
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Productivity/Office/Organizers
URL:            https://sqlitebrowser.org
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
Source1:        sqlitebrowser.1
# PATCH-FIX-UPSTREAM switch_case_return.patch -- fisiu@opensuse.org
Patch0:         switch_case_return.patch

BuildRequires:  antlr-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qscintilla-qt6-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(glib-2.0)
%if 0%{?suse_version} > 1600 && 0%{?is_opensuse}
BuildRequires:  pkgconfig(qhexedit2)
%endif
BuildRequires:  pkgconfig(sqlcipher)

%description
SQLite Database Browser is a visual tool for creating, designing and
editing database files compatible with SQLite. It provides a
spreadsheet-like interface, without the need to learn SQL commands.
Controls and guided dialogs are available for users to:

	* Create and compact database files
	* Create, define, modify and delete tables
	* Create, define and delete indexes
	* Browse, edit, add and delete records
	* Search records
	* Import and export records as text
	* Import and export tables from/to CSV files
	* Import and export databases from/to SQL dump files
	* Issue SQL queries and inspect the results
	* Examine a log of all SQL commands issued by the application

%prep
%setup -qn %{name}-%{version}
%patch -P 0 -p1

%build
%cmake \
  -DQT_MAJOR=Qt6 \
  -DBUILD_STABLE_VERSION=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DFORCE_INTERNAL_QCUSTOMPLOT=ON \
  -DFORCE_INTERNAL_QHEXEDIT=OFF \
  -Dsqlcipher=1 \
  -Wno-dev

%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/{applications,pixmaps}
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/%{name}.1
install    -m 0644 images/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Categories=Application;Network;GNOME;GTK;System;X-SuSE-ServiceConfiguration;
StartupNotify=true
Exec=%{_bindir}/%{name}
Name=%{name}
GenericName=SQLite Database browser
Terminal=false
Type=Application
Icon=%{name}
EOF
%suse_update_desktop_file %{name}

%files
%doc README.md currentrelease
%license LICENSE
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.desktop.appdata.xml
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/sqlitebrowser.png
%{_datadir}/icons/hicolor/scalable/apps/sqlitebrowser.svg

%changelog
