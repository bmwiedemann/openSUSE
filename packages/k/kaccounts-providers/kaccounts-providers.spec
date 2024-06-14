#
# spec file for package kaccounts-providers
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


%global __requires_exclude org.kde.kaccounts.(next|own)cloud

# The nextcloud plugin will only be built on these archs
%ifarch x86_64 %{x86_64} aarch64 riscv64
%bcond_without qtwebengine
%endif

%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kaccounts-providers
Version:        24.05.1
Release:        0
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
%if %{with qtwebengine}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
%endif
Requires:       signon-plugin-oauth2

%description
KDE Accounts Providers.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# qtwebkit is long dead
rm -r %{buildroot}%{_kf6_sysconfdir}/signon-ui/

%find_lang %{name} --all-name

%files
%license LICENSES/*
%{_kf6_iconsdir}/hicolor/256x256/apps/kaccounts-owncloud.png
%if %{with qtwebengine}
%{_kf6_iconsdir}/hicolor/scalable/apps/kaccounts-nextcloud.svg
%endif
%{_kf6_plugindir}/kaccounts/
%dir %{_kf6_sharedir}/accounts
%dir %{_kf6_sharedir}/accounts/providers
%dir %{_kf6_sharedir}/accounts/providers/kde
%{_kf6_sharedir}/accounts/providers/kde/google.provider
%if %{with qtwebengine}
%{_kf6_sharedir}/accounts/providers/kde/nextcloud.provider
%endif
%{_kf6_sharedir}/accounts/providers/kde/owncloud.provider
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde
%if %{with qtwebengine}
%{_kf6_sharedir}/accounts/services/kde/nextcloud-contacts.service
%{_kf6_sharedir}/accounts/services/kde/nextcloud-storage.service
%endif
%{_kf6_sharedir}/accounts/services/kde/owncloud-storage.service
%dir %{_kf6_sharedir}/kpackage/
%{_kf6_sharedir}/kpackage/genericqml/

%files lang -f %{name}.lang

%changelog
