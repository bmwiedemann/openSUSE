#
# spec file for package klettres
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
Name:           klettres
Version:        22.12.1
Release:        0
Summary:        Alphabet Learning Game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/klettres
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Helps to learn the alphabet and read some syllables.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.%{name} Education Languages

%files
%license LICENSES/*
%doc AUTHORS ChangeLog
%doc %lang(en) %{_kf5_htmldir}/en/klettres/
%{_kf5_applicationsdir}/org.kde.klettres.desktop
%{_kf5_appsdir}/klettres/
%{_kf5_appstreamdir}/org.kde.klettres.appdata.xml
%{_kf5_bindir}/klettres
%{_kf5_configkcfgdir}/klettres.kcfg
%{_kf5_debugdir}/klettres.categories
%{_kf5_iconsdir}/hicolor/*/apps/klettres.*
%{_kf5_knsrcfilesdir}/klettres.knsrc
%{_kf5_kxmlguidir}/klettres/

%files lang -f %{name}.lang

%changelog
