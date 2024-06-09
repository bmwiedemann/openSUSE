#
# spec file for package kf6-kwallet
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


%define qt6_version 6.6.0

%define rname kwallet
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kwallet
Version:        6.3.0
Release:        0
Summary:        Safe desktop-wide storage for passwords
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package -n libKF6Wallet6
Summary:        Safe desktop-wide storage for passwords
Requires:       kf6-kwallet >= %{version}

%description -n libKF6Wallet6
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package -n libKF6WalletBackend6
Summary:        Safe desktop-wide storage for passwords

%description -n libKF6WalletBackend6
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package -n kwalletd6
Summary:        Safe desktop-wide storage for passwords
Requires:       kf6-kwallet >= %{version}
Recommends:     kf6-kwallet-tools
# kwalletd6 ships a compat org.kde.kwalletd5.service file. It needs to replace
# kwalletd5 to keep using plasma5 with KF6-based apps
Provides:       kwalletd5 = %{version}
Obsoletes:      kwalletd5 < %{version}
Obsoletes:      kwalletd5-lang < %{version}

%description -n kwalletd6
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package tools
Summary:        Safe desktop-wide storage for passwords
Conflicts:      kwallet-tools

%description tools
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package devel
Summary:        Safe desktop-wide storage for passwords
Requires:       libKF6Wallet6 = %{version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.
Development files.

%lang_package -n kf6-kwallet-tools

%lang_package -n kwalletd6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kwalletd6
%find_lang kwallet6-query

%ldconfig_scriptlets -n libKF6Wallet6
%ldconfig_scriptlets -n libKF6WalletBackend6

%files
%{_kf6_debugdir}/kwallet.categories
%{_kf6_debugdir}/kwallet.renamecategories

%files -n kwalletd6
%{_kf6_applicationsdir}/org.kde.kwalletd6.desktop
%{_kf6_bindir}/kwalletd6
%{_kf6_notificationsdir}/kwalletd6.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kwalletd6.service
%dir %{_kf6_sharedir}/xdg-desktop-portal
%dir %{_kf6_sharedir}/xdg-desktop-portal/portals
%{_kf6_sharedir}/xdg-desktop-portal/portals/kwallet.portal

%files -n libKF6Wallet6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Wallet.so.*

%files -n libKF6WalletBackend6
%{_kf6_libdir}/libKF6WalletBackend.so.*

%files tools
%{_kf6_bindir}/kwallet-query
%{_kf6_mandir}/man1/kwallet-query.1%{?ext_man}

%files devel
%doc %{_kf6_qchdir}/KF6Wallet.*
%{_kf6_libdir}/libKF6Wallet.so
%{_kf6_cmakedir}/KF6Wallet/
%{_kf6_includedir}/KWallet/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.KWallet.xml

%files -n kwalletd6-lang -f kwalletd6.lang

%files -n kf6-kwallet-tools-lang -f kwallet6-query.lang

%changelog
