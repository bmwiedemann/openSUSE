#
# spec file for package ktouch
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


%define kf6_version 6.14.0
%define qt6_version 6.8.0
#
%bcond_without released
Name:           ktouch
Version:        25.08.3
Release:        0
Summary:        Touch Typing Tutor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktouch
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       kf6-kcoreaddons-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kquickcharts >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-qt5compat-imports >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
A KDE program that helps you to learn and practice touch typing.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name --with-html

%files
%license LICENSES/*
%doc AUTHORS README.md
%doc %lang(en) %{_kf6_htmldir}/en/ktouch/
%{_kf6_applicationsdir}/org.kde.ktouch.desktop
%{_kf6_appstreamdir}/org.kde.ktouch.appdata.xml
%{_kf6_bindir}/ktouch
%{_kf6_configkcfgdir}/ktouch.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/ktouch.*
%{_kf6_mandir}/man1/ktouch.1.gz
%{_kf6_sharedir}/ktouch/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ktouch

%changelog
