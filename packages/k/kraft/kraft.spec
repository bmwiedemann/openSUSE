#
# spec file for package kraft
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2007-2011 Klaas Freitag <freitag@kde.org>
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


%bcond_with qpdfview
Name:           kraft
Version:        2.0.0
Release:        0
Summary:        KDE software to manage office documents in the office
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Other
URL:            https://volle-kraft-voraus.de
Source0:        https://github.com/dragotin/kraft/archive/refs/tags/v%{version}.tar.gz#/kraft-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.11
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain) >= 0.12.0
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6TextTemplate)

BuildRequires:  pkgconfig(sqlite3)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6PimCommonAkonadi)

Requires:       python3-base
Requires:       python3-pypdf
Requires:       python3-six
Requires:       python3-weasyprint

Requires:       qt6-sql-mysql
Requires:       qt6-sql-sqlite

%if %{with qpdfview}
# PATCH-FEATURE-UPSTREAM use_qpdfview.path Open PDFs in qpdfview in appimages
Patch0:         use_qpdfview.patch
%endif

%description
Kraft is KDE software to help to create and manage office documents such as
offers and invoices in the small enterprise.

It supports easy document creation, templates with calculation, customer management
through the KDE addressbook, highly configurable PDF output and more.

See the website http://volle-kraft-voraus.de for more information.

%prep
%autosetup -p1 -n kraft-%{version}

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# Create the .tag file that is read by cmake with the version.
# Workaround since the github created tarball does not contain the .tag file with
# the latest commit.

[ -f .tag ] && echo ".tag file exists in tarball." || echo "%{version}" > .tag

%cmake_qt6

%qt6_build

%install
%{qt6_install}

%if 0%{?suse_version}
%suse_update_desktop_file -G kraft de.volle_kraft_voraus.kraft Office Finance
%endif

%ldconfig_scriptlets

%files
%{_bindir}/kraft
%{_bindir}/findcontact
%{_datadir}/applications/de.volle_kraft_voraus.kraft.desktop
%{_datadir}/metainfo/de.volle_kraft_voraus.kraft.appdata.xml
%{_datadir}/kraft/
%{_datadir}/icons/hicolor/scalable/apps/kraft.svg
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/kraft.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/kraft.mo

%doc AUTHORS README.md INSTALL.md Changes.txt Releasenotes.txt TODO
%license COPYING

%changelog
