#
# spec file for package artikulate
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


%define kf5_version 5.105.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           artikulate
Version:        24.05.2
Release:        0
Summary:        Pronunciation Self-Teaching
License:        LGPL-3.0-or-later AND GPL-2.0-only AND BSD-3-Clause
URL:            https://apps.kde.org/artikulate
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XmlPatterns)
# Runtime deps
Requires:       kirigami2
Requires:       knewstuff-imports
Requires:       kqtquickcharts >= %{_kapp_version}
Requires:       libqt5-qtquickcontrols
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Improve your pronunciation by listening to native speakers.

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

%ldconfig_scriptlets

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/artikulate/
%{_kf5_applicationsdir}/org.kde.artikulate.desktop
%{_kf5_appstreamdir}/org.kde.artikulate.appdata.xml
%{_kf5_bindir}/artikulate
%{_kf5_bindir}/artikulate_editor
%{_kf5_configkcfgdir}/artikulate.kcfg
%{_kf5_iconsdir}/hicolor/*/*/artikulate*.*
%{_kf5_knsrcfilesdir}/artikulate.knsrc
%{_kf5_libdir}/libartikulatecore.so.*
%{_kf5_libdir}/libartikulatelearnerprofile.so.*
%{_kf5_libdir}/libartikulatesound.so.*

%files lang -f %{name}.lang

%changelog
