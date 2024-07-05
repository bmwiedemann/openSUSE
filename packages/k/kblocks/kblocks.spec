#
# spec file for package kblocks
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
Name:           kblocks
Version:        24.05.2
Release:        0
Summary:        A classic falling blocks game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kblocks
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kblocks5 < %{version}
Provides:       kblocks5 = %{version}

%description
KBlocks is the KDE version of the classic falling blocks game.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license COPYING COPYING.DOC
%doc %lang(en) %{_kf6_htmldir}/en/kblocks/
%{_kf6_applicationsdir}/org.kde.kblocks.desktop
%{_kf6_appstreamdir}/org.kde.kblocks.appdata.xml
%{_kf6_bindir}/kblocks
%{_kf6_configkcfgdir}/kblocks.kcfg
%{_kf6_debugdir}/kblocks.categories
%{_kf6_iconsdir}/hicolor/*/*/kblocks.*
%{_kf6_knsrcfilesdir}/kblocks.knsrc
%{_kf6_sharedir}/kblocks/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kblocks/

%changelog
