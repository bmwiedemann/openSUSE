#
# spec file for package kraft
#
# Copyright (c) 2025 SUSE LLC
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


# Build without akonadi integration on repositories providing KDE PIM 6 libraries
%if 0%{?suse_version} > 1500 || "%{_repository}" == "KDE_Applications_openSUSE_Leap_15.5" || "%{_repository}" == "KDE_Applications_openSUSE_Leap_15.6"
%define with_akonadi 0
%else
%define with_akonadi 1
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150600
%define akonadi_legacy 1
%endif
%endif
%bcond_with qpdfview
Name:           kraft
Version:        1.2.2
Release:        0
Summary:        KDE software to manage office documents in the office
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Other
URL:            https://volle-kraft-voraus.de
Source0:        kraft-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  libctemplate-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(sqlite3)
Requires:       libQt5Sql5-sqlite
Requires:       python3-PyPDF2
Requires:       python3-base
Requires:       python3-reportlab
Requires:       python3-six
Recommends:     python3-Weasyprint
%if %{with qpdfview}
# PATCH-FEATURE-UPSTREAM use_qpdfview.path Open PDFs in qpdfview in appimages
Patch0:         use_qpdfview.patch
%endif
%if %{with_akonadi}
BuildRequires:  cmake(KF5ContactEditor)
%if 0%{?akonadi_legacy}
BuildRequires:  cmake(KF5AkonadiContact)
%else
BuildRequires:  cmake(KPim5AkonadiContact)
%endif
%endif

%description
Kraft is KDE software to help to create and manage office documents such as
offers and invoices in the small enterprise.

It supports easy document creation, templates with calculation, customer management
through the KDE addressbook, highly configurable PDF output and more.

See the website http://volle-kraft-voraus.de for more information.

%prep
%setup -q
%if %{with qpdfview}
%patch -P 0 -p1
%endif

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# Create the .tag file that is read by cmake with the version.
# Workaround since the github created tarball does not contain the .tag file with
# the latest commit.

[ -f .tag ] && echo ".tag file exists in tarball." || echo "%{version}" > .tag

%cmake_kf5 -d build %{?akonadi_legacy:-- -DAKONADI_LEGACY_BUILD=ON}

%cmake_build

%install
%kf5_makeinstall -C build
chmod 755 %{buildroot}%{_datadir}/kraft/tools/erml2pdf.py

%if 0%{?suse_version}
%suse_update_desktop_file -G kraft de.volle_kraft_voraus.kraft Office Finance
%endif

%ldconfig_scriptlets

%files
%{_bindir}/kraft
%if %{with_akonadi}
%{_bindir}/findcontact
%endif
%{_datadir}/applications/de.volle_kraft_voraus.kraft.desktop
%{_datadir}/metainfo/de.volle_kraft_voraus.kraft.appdata.xml
%{_datadir}/config.kcfg/*
%{_datadir}/kraft/
%{_datadir}/kxmlgui5/kraft/kraftui.rc
%{_datadir}/kxmlgui5/kraft/katalogview.rc
%{_datadir}/icons/hicolor/scalable/apps/kraft.svg
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/kraft.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/kraft.mo

%dir %{_datadir}/config.kcfg
%dir %{_datadir}/kxmlgui5/kraft
%doc AUTHORS README.md INSTALL.md Changes.txt Releasenotes.txt TODO
%license COPYING

%changelog
