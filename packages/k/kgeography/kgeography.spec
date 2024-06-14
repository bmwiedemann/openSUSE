#
# spec file for package kgeography
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kgeography
Version:        24.05.1
Release:        0
Summary:        Geography Trainer
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kgeography
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kgeography5 < %{version}
Provides:       kgeography5 = %{version}

%description
KGeography is a geography learning program.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%fdupes %{buildroot}

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/kgeography/
%{_kf6_applicationsdir}/org.kde.kgeography.desktop
%{_kf6_appstreamdir}/org.kde.kgeography.appdata.xml
%{_kf6_bindir}/kgeography
%{_kf6_configkcfgdir}/kgeography.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/kgeography.*
%{_kf6_sharedir}/kgeography/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kgeography/
# The files below aren't detected by find-lang.sh
%dir %{_kf6_sharedir}/locale/fi/LC_SCRIPTS
%dir %{_kf6_sharedir}/locale/fr/LC_SCRIPTS
%dir %{_kf6_sharedir}/locale/ja/LC_SCRIPTS
%dir %{_kf6_sharedir}/locale/ml/LC_SCRIPTS
%dir %{_kf6_sharedir}/locale/pl/LC_SCRIPTS
%dir %{_kf6_sharedir}/locale/uk/LC_SCRIPTS
%lang (fi) %{_kf6_sharedir}/locale/fi/LC_SCRIPTS/kgeography
%lang (fr) %{_kf6_sharedir}/locale/fr/LC_SCRIPTS/kgeography
%lang (ja) %{_kf6_sharedir}/locale/ja/LC_SCRIPTS/kgeography
%lang (ml) %{_kf6_sharedir}/locale/ml/LC_SCRIPTS/kgeography
%lang (pl) %{_kf6_sharedir}/locale/pl/LC_SCRIPTS/kgeography
%lang (uk) %{_kf6_sharedir}/locale/uk/LC_SCRIPTS/kgeography

%changelog
