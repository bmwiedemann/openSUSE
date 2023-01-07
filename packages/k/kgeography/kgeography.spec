#
# spec file for package kgeography
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
Name:           kgeography
Version:        22.12.1
Release:        0
Summary:        Geography Trainer
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kgeography
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
KGeography is a geography learning program.

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

%fdupes -s %{buildroot}

%files
%doc %lang(en) %{_kf5_htmldir}/en/kgeography/
%{_kf5_applicationsdir}/org.kde.kgeography.desktop
%{_kf5_appsdir}/kgeography/
%{_kf5_appstreamdir}/org.kde.kgeography.appdata.xml
%{_kf5_bindir}/kgeography
%{_kf5_configkcfgdir}/kgeography.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/kgeography.*
%{_kf5_kxmlguidir}/kgeography/

%files lang -f %{name}.lang
%license COPYING*
# The files below aren't detected by find-lang.sh
%dir %{_kf5_sharedir}/locale/fi/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/fr/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/ja/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/ml/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/pl/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/uk/LC_SCRIPTS
%lang (fi) %{_kf5_sharedir}/locale/fi/LC_SCRIPTS/kgeography
%lang (fr) %{_kf5_sharedir}/locale/fr/LC_SCRIPTS/kgeography
%lang (ja) %{_kf5_sharedir}/locale/ja/LC_SCRIPTS/kgeography
%lang (ml) %{_kf5_sharedir}/locale/ml/LC_SCRIPTS/kgeography
%lang (pl) %{_kf5_sharedir}/locale/pl/LC_SCRIPTS/kgeography
%lang (uk) %{_kf5_sharedir}/locale/uk/LC_SCRIPTS/kgeography

%changelog
