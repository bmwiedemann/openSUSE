#
# spec file for package kio-gdrive
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           kio-gdrive
Version:        24.05.1
Release:        0
Summary:        Google Drive KIO slave for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KPim6GAPI) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain) >= 0.6.0
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Used by the .desktop file
Recommends:     dolphin
# libkgapi has no ABI stability
%requires_eq    libKPim6GAPICore6

%description
Google Drive KIO slave for KDE applications.
KIO GDrive requires a KIO-enabled file manager at runtime, otherwise there is
no way to setup a Google Drive account.
This can be Dolphin or Gwenview.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%files
%license COPYING
%doc README.md README.packagers
%doc %lang(en) %{_kf6_htmldir}/en/kioslave5/gdrive/
%{_kf6_appstreamdir}/org.kde.kio_gdrive.metainfo.xml
%{_kf6_notificationsdir}/gdrive.notifyrc
%{_kf6_plugindir}/kaccounts/
%{_kf6_plugindir}/kf6/
%{_kf6_sharedir}/accounts/
%dir %{_kf6_sharedir}/purpose
%{_kf6_sharedir}/purpose/purpose_gdrive_config.qml
%dir %{_kf6_sharedir}/remoteview
%{_kf6_sharedir}/remoteview/gdrive-network.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kioslave5/gdrive/

%changelog
