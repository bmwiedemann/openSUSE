#
# spec file for package kwallet
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libKF5Wallet5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kwallet
Version:        5.101.0
Release:        0
Summary:        Safe desktop-wide storage for passwords
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         kwallet-%{version}.tar.xz
%if %{with released}
Source1:        kwallet-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package -n %{lname}
Summary:        Safe desktop-wide storage for passwords

%description -n %{lname}
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package -n libkwalletbackend5-5
Summary:        Safe desktop-wide storage for passwords

%description -n libkwalletbackend5-5
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package -n kwalletd5
Summary:        Safe desktop-wide storage for passwords
Recommends:     %{name}-tools

%description -n kwalletd5
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package tools
Summary:        Safe desktop-wide storage for passwords

%description tools
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package tools-lang
Summary:        Safe desktop-wide storage for passwords
Requires:       %{name}-tools = %{version}

%description tools-lang
Provides translations to the package %{name}-tools-lang

%package devel
Summary:        Safe desktop-wide storage for passwords
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       libkwalletbackend5-5 = %{version}
Requires:       cmake(Qt5Gui) >= 5.15.0
# Was shortly present in K:F5
Obsoletes:      kwallet-framework-devel <= %{version}
Provides:       kwallet-framework-devel = %{version}

%description devel
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.
Development files.

%lang_package -n kwalletd5

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kwalletd5 kwalletd5.lang
%find_lang kwallet-query kwallet-query.lang

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libkwalletbackend5-5 -p /sbin/ldconfig
%postun -n libkwalletbackend5-5 -p /sbin/ldconfig

%files -n kwalletd5-lang -f kwalletd5.lang

%files -n kwallet-tools-lang -f kwallet-query.lang

%files -n kwalletd5
%{_kf5_bindir}/kwalletd5
%{_kf5_servicesdir}/kwalletd5.desktop
%{_kf5_notifydir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf5_applicationsdir}/org.kde.kwalletd5.desktop

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Wallet.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n libkwalletbackend5-5
%{_kf5_libdir}/libkwalletbackend5.so.*

%files tools
%{_kf5_bindir}/kwallet-query
%{_kf5_mandir}/man1/kwallet-query.1*

%files devel
%{_kf5_libdir}/libKF5Wallet.so
%{_kf5_libdir}/libkwalletbackend5.so
%{_kf5_libdir}/cmake/KF5Wallet/
%{_kf5_includedir}/KWallet/
%{_kf5_mkspecsdir}/qt_KWallet.pri
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KWallet.xml

%changelog
