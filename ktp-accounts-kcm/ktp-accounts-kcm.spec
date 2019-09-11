#
# spec file for package ktp-accounts-kcm
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
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktp-accounts-kcm
Version:        19.08.1
Release:        0
Summary:        KCM Module for configuring Telepathy Instant Messaging Accounts
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  kaccounts-integration-devel
BuildRequires:  kaccounts-providers
BuildRequires:  kcmutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libaccounts-qt5-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-qt5-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       telepathy-mission-control
Recommends:     %{name}-lang
Recommends:     telepathy-gabble
Recommends:     telepathy-haze
Recommends:     telepathy-idle
Recommends:     telepathy-rakia
Recommends:     telepathy-salut
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

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
Group:          System/Libraries

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
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

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

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
