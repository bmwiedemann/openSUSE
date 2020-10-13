#
# spec file for package keditbookmarks
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           keditbookmarks
Version:        20.08.2
Release:        0
Summary:        KDE Bookmark Editor
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
This is an editor to edit your KDE-wide bookmark set.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/keditbookmarks/
%{_kf5_applicationsdir}/org.kde.keditbookmarks.desktop
%{_kf5_bindir}/kbookmarkmerger
%{_kf5_bindir}/keditbookmarks
%{_kf5_configkcfgdir}/keditbookmarks*.kcfg
%{_kf5_debugdir}/keditbookmarks.categories
%{_kf5_libdir}/libkbookmarkmodel_private.so*
%{_kf5_sharedir}/kxmlgui5/keditbookmarks/
%{_kf5_mandir}/man1/kbookmarkmerger.1%{ext_man}

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
