#
# spec file for package plasma-phonebook
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.19.0
%define qt6_version 6.9.0

%bcond_without released
Name:           plasma-phonebook
Version:        26.04.0
Release:        0
Summary:        Plasma Mobile Phonebook
License:        GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6People) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kcontacts-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kpeople-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-qt5compat-imports >= %{qt6_version}

%lang_package

%description
A phone book application for Plasma Mobile.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.phonebook.desktop
%{_kf6_appstreamdir}/org.kde.phonebook.metainfo.xml
%{_kf6_bindir}/plasma-phonebook
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.phonebook.svg
%dir %{_kf6_pluginsdir}/kpeople
%dir %{_kf6_pluginsdir}/kpeople/actions
%{_kf6_pluginsdir}/kpeople/actions/phonebook_kpeople_plugin.so

%files lang -f %{name}.lang

%changelog
