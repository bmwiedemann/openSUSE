#
# spec file for package ktp-common-internals
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
Name:           ktp-common-internals
Version:        22.12.0
Release:        0
Summary:        Telepathy common module
License:        LGPL-2.1-or-later
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-accounts-signon
BuildRequires:  telepathy-logger-qt5-devel
BuildRequires:  telepathy-mission-control-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libotr) >= 4.0.0
Requires:       ktp-icons
Requires:       telepathy-accounts-signon
Provides:       libktpcommoninternals6 = %{version}
Provides:       libktpcommoninternals7 = %{version}
Provides:       libktpcommoninternals8 = %{version}
Obsoletes:      %{name}5 < %{version}
Obsoletes:      libktpcommoninternals6 < %{version}
Obsoletes:      libktpcommoninternals7 < %{version}
Obsoletes:      libktpcommoninternals8 <= %{version}
Provides:       %{name}5 = %{version}
Obsoletes:      ktp-kpeople < %{version}

%description
ktp-common-internals is the base library for all the KDE Telepathy packages.

%package devel
Summary:        Telepathy common module
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       pkgconfig
Requires:       telepathy-logger-qt5-devel
Requires:       telepathy-qt5-devel
Requires:       cmake(KF5KCMUtils)
Requires:       cmake(KF5Wallet)
Requires:       cmake(Qt5Widgets)
Obsoletes:      %{name}5-devel < %{version}
Provides:       %{name}5-devel = %{version}

%description devel
ktp-common-internals is the base library for all the KDE Telepathy packages.

%package -n ktp-icons
Summary:        Icons for KDE Telepathy
Obsoletes:      ktp-icons5 < %{version}
Provides:       ktp-icons5 = %{version}

%description -n ktp-icons
icons for all the KDE Telepathy packages.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_bindir}/ktp-debugger
%{_kf5_libdir}/libKTpCommonInternals.so.*
%{_kf5_libdir}/libKTpLogger.so.*
%{_kf5_libdir}/libKTpModels.so.*
%{_kf5_libdir}/libKTpOTR.so.*
%{_kf5_libdir}/libKTpWidgets.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_configkcfgdir}/
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Proxy.service
%{_kf5_sharedir}/katepart5/
%{_kf5_sharedir}/telepathy/
%{_libexecdir}/ktp-proxy

%files -n ktp-icons
%{_kf5_iconsdir}/hicolor/

%files devel
%{_kf5_cmakedir}/KTp/
%{_kf5_libdir}/libKTpCommonInternals.so
%{_kf5_libdir}/libKTpLogger.so
%{_kf5_libdir}/libKTpModels.so
%{_kf5_libdir}/libKTpOTR.so
%{_kf5_libdir}/libKTpWidgets.so
%{_kf5_prefix}/include/KTp/

%files lang -f %{name}.lang

%changelog
