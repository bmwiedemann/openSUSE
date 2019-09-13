#
# spec file for package kio-gdrive
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without lang
Name:           kio-gdrive
Version:        1.2.7
Release:        0
Summary:        Google Drive KIO slave for KDE applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://community.kde.org/KIO_GDrive
Source:         https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n) >= 5.14.0
BuildRequires:  cmake(KF5KIO) >= 5.14.0
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KPimGAPI) >= 5.5.0
BuildRequires:  cmake(Qt5Network) >= 5.2.0
BuildRequires:  cmake(Qt5Widgets) >= 5.2.0
# Used by the .desktop file
Recommends:     dolphin
# libkgapi has no ABI stability
%requires_eq    libKPimGAPICore5

%lang_package

%description
Google Drive KIO slave for KDE applications.
KIO GDrive requires a KIO-enabled file manager at runtime,
otherwise there is no way to setup a Google Drive account.
This can be Dolphin or Gwenview or Konqueror.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
  %find_lang kio5_gdrive %{name}.lang
  %kf5_find_htmldocs
  %endif

%files
%license COPYING
%doc README.md README.packagers
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/gdrive/
%{_kf5_plugindir}/kaccounts/
%{_kf5_plugindir}/kf5/
%dir %{_datadir}/remoteview
%{_datadir}/remoteview/gdrive-network.desktop
%{_kf5_appstreamdir}/org.kde.kio-gdrive.appdata.xml
%{_datadir}/accounts/
%{_kf5_notifydir}/gdrive.notifyrc

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
