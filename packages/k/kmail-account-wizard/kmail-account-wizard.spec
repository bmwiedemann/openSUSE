#
# spec file for package kmail-account-wizard
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kmail-account-wizard
Version:        19.08.2
Release:        0
Summary:        Account wizard for KMail
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2.0
Obsoletes:      akonadi_resources
Obsoletes:      kdepim
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
An application which assists you with the configuration of accounts in KMail.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%files
%license COPYING COPYING.LIB COPYING.DOC
%{_kf5_debugdir}/accountwizard.categories
%{_kf5_knsrcfilesdir}/accountwizard.knsrc
%{_kf5_debugdir}/accountwizard.renamecategories
%{_kf5_applicationsdir}/org.kde.accountwizard.desktop
%{_kf5_bindir}/accountwizard
%{_kf5_bindir}/ispdb
%{_kf5_plugindir}/accountwizard_plugin.so
%{_kf5_sharedir}/akonadi/accountwizard/
%{_kf5_sharedir}/mime/packages/accountwizard-mime.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
