#
# spec file for package kraft
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kraft
Url:            http://volle-kraft-voraus.de

Version:        0.82
Release:        0
Summary:        KDE software to manage office documents in the office
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Other

%bcond_without akonadi
%bcond_with qpdfview

Source0:        kraft-%{version}.tar.xz
%if %{with qpdfview}
# PATCH-FEATURE-UPSTREAM use_qpdfview.path Open PDFs in qpdfview in appimages
Patch0:         use_qpdfview.patch
%endif
# PATCH-FIX-UPSTREAM fix_install_appdata.patch Install appdata in correct place
Patch1:         fix_install_appdata.patch
# PATCH-FIX-UPSTREAM fix build with Qt 5.12. Can be applied regardless of Qt version, but needed for Qt 5.12
Patch2:         fix_sql_qt12.patch
# PATCH-FIX-UPSTREAM Do not show the compiler warnings for wrong nullptr initialization, too much noise
Patch3:         fix_nullptr_warning.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
# requires need to be python2-PyPDF2 for later distros
Requires:       python-PyPDF2
Requires:       python-libxml2
Requires:       python-reportlab

%if %{with akonadi}
BuildRequires:  akonadi-contact-devel
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcontacts-devel
BuildRequires:  ki18n-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libctemplate-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
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
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
chmod 755 %{buildroot}%{_datadir}/kraft/tools/erml2pdf.py

%if %{?suse_version:1}0
%suse_update_desktop_file -G kraft de.volle_kraft_voraus.kraft Office Finance
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%clean
  rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/kraft
%if %{with akonadi}
%{_bindir}/findcontact
%endif
%{_datadir}/applications/de.volle_kraft_voraus.kraft.desktop
%{_datadir}/metainfo/de.volle_kraft_voraus.kraft.appdata.xml
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/config.kcfg/*
%{_datadir}/kraft/
%{_datadir}/kxmlgui5/kraft/kraftui.rc
%{_datadir}/kxmlgui5/kraft/katalogview.rc
%{_datadir}/locale/*/LC_MESSAGES/kraft.mo

%dir %{_datadir}/config.kcfg
%dir %{_datadir}/kxmlgui5/kraft
%doc AUTHORS README.md Changes.txt Releasenotes.txt TODO
%license COPYING

%changelog
