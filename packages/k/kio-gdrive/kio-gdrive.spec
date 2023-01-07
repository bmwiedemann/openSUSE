#
# spec file for package kio-gdrive
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
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kio-gdrive
Version:        22.12.1
Release:        0
Summary:        Google Drive KIO slave for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KPimGAPI)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
# Used by the .desktop file
Recommends:     dolphin
# libkgapi has no ABI stability
%requires_eq    libKPimGAPICore5

%description
Google Drive KIO slave for KDE applications.
KIO GDrive requires a KIO-enabled file manager at runtime,
otherwise there is no way to setup a Google Drive account.
This can be Dolphin or Gwenview or Konqueror.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang kio5_gdrive %{name}.lang
%kf5_find_htmldocs

%files
%license COPYING
%doc README.md README.packagers
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/gdrive/
%dir %{_kf5_sharedir}/remoteview
%{_kf5_appstreamdir}/org.kde.kio_gdrive.metainfo.xml
%{_kf5_notifydir}/gdrive.notifyrc
%{_kf5_plugindir}/kaccounts/
%{_kf5_plugindir}/kf5/
%{_kf5_sharedir}/accounts/
%{_kf5_sharedir}/remoteview/gdrive-network.desktop

%files lang -f %{name}.lang

%changelog
