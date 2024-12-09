#
# spec file for package sqlitebrowser
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


Name:           sqlitebrowser
Version:        3.13.1
Release:        0
Summary:        Spreadsheet-like interface to SQLite databases
License:        GPL-3.0-or-later AND MPL-2.0
Group:          Productivity/Office/Organizers
URL:            https://sqlitebrowser.org
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
Source1:        sqlitebrowser.1
# PATCH-FIX-UPSTREAM switch_case_return.patch -- fisiu@opensuse.org
Patch0:         switch_case_return.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqscintilla_qt5-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(qcustomplot)
BuildRequires:  pkgconfig(qhexedit2)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(sqlite3)
# not on SLE-12
%if 0%{?suse_version} != 1315 || 0%{?is_opensuse}
BuildRequires:  antlr-devel
%endif

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
  -DQSCINTILLA_INCLUDE_DIR=%{_includedir}/qt5/Qsci \
  -DQSCINTILLA_LIBRARY=%{_libdir}/libqscintilla2_qt5.so \
  -DBUILD_STABLE_VERSION=ON \
  -DFORCE_INTERNAL_QCUSTOMPLOT=OFF \
  -DFORCE_INTERNAL_QHEXEDIT=OFF \
%if 0%{?suse_version} && 0%{?suse_version} <= 1500
  -DFORCE_INTERNAL_QSCINTILLA=ON \
%endif
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
