#
# spec file for package kcalc
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
Name:           kcalc
Version:        24.05.2
Release:        0
Summary:        Scientific Calculator
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kcalc
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  gmp-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  mpfr-devel
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kcalc5 < %{version}
Provides:       kcalc5 = %{version}

%description
KCalc is the KDE calculator tool.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kcalc/
%{_kf6_applicationsdir}/org.kde.kcalc.desktop
%{_kf6_appstreamdir}/org.kde.kcalc.appdata.xml
%{_kf6_bindir}/kcalc
%{_kf6_configkcfgdir}/kcalc.kcfg
%{_kf6_sharedir}/kconf_update/kcalcrc.upd
%dir %{_kf6_sharedir}/kglobalaccel
%{_kf6_sharedir}/kglobalaccel/org.kde.kcalc.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcalc/

%changelog
