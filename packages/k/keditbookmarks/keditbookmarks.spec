#
# spec file for package keditbookmarks
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           keditbookmarks
Version:        22.12.1
Release:        0
Summary:        KDE Bookmark Editor
License:        GPL-2.0-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)

%description
This is an editor to edit your KDE-wide bookmark set.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/keditbookmarks/
%{_kf5_applicationsdir}/org.kde.keditbookmarks.desktop
%{_kf5_bindir}/kbookmarkmerger
%{_kf5_bindir}/keditbookmarks
%{_kf5_configkcfgdir}/keditbookmarks*.kcfg
%{_kf5_debugdir}/keditbookmarks.categories
%{_kf5_libdir}/libkbookmarkmodel_private.so*
%{_kf5_mandir}/man1/kbookmarkmerger.1%{ext_man}

%files lang -f %{name}.lang

%changelog
