#
# spec file for package kmail-account-wizard
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
Name:           kmail-account-wizard
Version:        22.12.0
Release:        0
Summary:        Account wizard for KMail
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Obsoletes:      akonadi_resources
Obsoletes:      kdepim
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
An application which assists you with the configuration of accounts in KMail.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%files
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.accountwizard.desktop
%{_kf5_bindir}/accountwizard
%{_kf5_bindir}/ispdb
%{_kf5_debugdir}/accountwizard.categories
%{_kf5_debugdir}/accountwizard.renamecategories
%{_kf5_knsrcfilesdir}/accountwizard.knsrc
%{_kf5_plugindir}/accountwizard_plugin.so
%{_kf5_sharedir}/akonadi/accountwizard/
%{_kf5_sharedir}/mime/packages/accountwizard-mime.xml

%files lang -f %{name}.lang

%changelog
