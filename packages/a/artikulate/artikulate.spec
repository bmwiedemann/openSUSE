#
# spec file for package artikulate
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define kf6_version 6.14.0
%define qt6_version 6.8.0

%bcond_without released
Name:           artikulate
Version:        25.08.3
Release:        0
Summary:        Pronunciation Self-Teaching
License:        LGPL-3.0-or-later AND GPL-2.0-only AND BSD-3-Clause
URL:            https://apps.kde.org/artikulate
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(libxml-2.0)
# Runtime deps
# Currently commented out
# Requires:       kqtquickcharts >= %%{_kapp_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-knewstuff-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Improve your pronunciation by listening to native speakers.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/artikulate/
%{_kf6_applicationsdir}/org.kde.artikulate.desktop
%{_kf6_appstreamdir}/org.kde.artikulate.appdata.xml
%{_kf6_bindir}/artikulate
%{_kf6_bindir}/artikulate_editor
%{_kf6_configkcfgdir}/artikulate.kcfg
%{_kf6_iconsdir}/hicolor/*/*/artikulate.*
%{_kf6_knsrcfilesdir}/artikulate.knsrc
%{_kf6_libdir}/libartikulatecore.so.*
%{_kf6_libdir}/libartikulatelearnerprofile.so.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/artikulate/

%changelog
