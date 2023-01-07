#
# spec file for package ktp-accounts-kcm
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
Name:           ktp-accounts-kcm
Version:        22.12.1
Release:        0
Summary:        Configuration module to set up Telepathy accounts
License:        LGPL-2.1-or-later
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  kaccounts-providers
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
Requires:       telepathy-mission-control
Recommends:     telepathy-gabble
Recommends:     telepathy-haze
Recommends:     telepathy-idle
Recommends:     telepathy-rakia
Recommends:     telepathy-salut
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
# Only build on archs where kaccounts-providers/QtWebEngine are available
ExcludeArch:    ppc ppc64 ppc64le s390 s390x

%description
This is a KControl Module which handles adding/editing/removing Telepathy
Accounts. It interacts with any Telepathy Spec compliant AccountManager,
such as telepathy-accountmanager-kwallet to manipulate the accounts. It is
modular in design, with each ConnectionManager-Protocol combination having a
plugin that provides customised forms for adding or editing their accounts,
and also with a generic plugin which can be used as a fallback for
ConnectionManager-Protocol combinations where no plugin exists.

%package -n libktpaccountskcminternal9
Summary:        Library for KDE Telepathy accounts kcm

%description -n libktpaccountskcminternal9
This is a KControl Module which handles adding/editing/removing Telepathy
Accounts. It interacts with any Telepathy Spec compliant AccountManager,
such as telepathy-accountmanager-kwallet to manipulate the accounts. It is
modular in design, with each ConnectionManager-Protocol combination having a
plugin that provides customised forms for adding or editing their accounts,
and also with a generic plugin which can be used as a fallback for
ConnectionManager-Protocol combinations where no plugin exists.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

# remove no longer supported/working providers and services
rm %{buildroot}%{_kf5_sharedir}/accounts/providers/kde/ktp-haze-yahoo.provider
rm %{buildroot}%{_kf5_sharedir}/accounts/services/kde/ktp-haze-yahoo-im.service

%fdupes %{buildroot}

%post   -n libktpaccountskcminternal9 -p /sbin/ldconfig
%postun -n libktpaccountskcminternal9 -p /sbin/ldconfig

%files -n libktpaccountskcminternal9
%{_kf5_libdir}/libktpaccountskcminternal.so.*

%files
%license COPYING
%doc README
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/accounts/
%{_kf5_sharedir}/telepathy/

%files lang -f %{name}.lang

%changelog
