#
# spec file for package k4dirstat
#
# Copyright (c) 2022 SUSE LLC
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


Name:           k4dirstat
Version:        3.4.2
Release:        0
Summary:        Graphical Disk Usage Utility
License:        GPL-2.0-only AND LGPL-2.0-only
Group:          Productivity/File utilities
URL:            https://github.com/jeromerobert/k4dirstat
Source0:        https://github.com/jeromerobert/k4dirstat/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Add-the-missing-cassert-include.patch
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.14
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)

%description
K4DirStat (KDE Directory Statistics) is a small utility program that sums up
disk usage for directory trees, very much like the Unix 'du' command. It
displays the disk space used up by a directory tree, both numerically and
graphically.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%suse_update_desktop_file -r k4dirstat Qt KDE Utility Filesystem

%find_lang k4dirstat %{name}.lang

%files
%license COPYING*
%doc AUTHORS CREDITS
%doc %lang(en) %{_kf5_htmldir}/en/k4dirstat
%dir %{_kf5_configkcfgdir}
%{_kf5_applicationsdir}/k4dirstat.desktop
%{_kf5_bindir}/k4dirstat
%{_kf5_configkcfgdir}/k4dirstat.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/k4dirstat.*
%{_kf5_mandir}/man1/k4dirstat.*

%files lang -f %{name}.lang
%exclude %{_kf5_htmldir}/en/k4dirstat

%changelog
