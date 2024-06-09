#
# spec file for package kf6-kauth
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

%define rname   kauth
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kauth
Version:        6.3.0
Release:        0
Summary:        Framework which lets applications perform actions as a privileged user
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
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package -n libKF6AuthCore6
Summary:        Framework which lets applications perform actions as a privileged user
Requires:       kf6-kauth >= %{version}
Recommends:     kf6-kauth-lang = %{version}

%description -n libKF6AuthCore6
KAuth is a framework to let applications perform actions as a privileged user.

%package devel
Summary:        Framework which lets applications perform actions as a privileged user
Requires:       libKF6AuthCore6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}

%description devel
KAuth is a framework to let applications perform actions as a privileged user.
Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kauth6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6AuthCore6

%files
%license LICENSES/*
%doc README.md
%dir %{_kf6_plugindir}/kf6/kauth
%{_kf6_plugindir}/kf6/kauth/backend/
%{_kf6_dbuspolicydir}/org.kde.kf6auth.conf
%{_kf6_debugdir}/kauth.categories
%{_kf6_debugdir}/kauth.renamecategories
%{_kf6_libexecdir}/kauth/kauth-policy-gen
%{_kf6_plugindir}/kf6/kauth/helper/

%files -n libKF6AuthCore6
%{_kf6_libdir}/libKF6AuthCore.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Auth.*
%{_kf6_cmakedir}/KF6Auth/
%dir %{_kf6_datadir}/kauth
%{_kf6_datadir}/kauth/dbus_policy.stub
%{_kf6_datadir}/kauth/dbus_service.stub
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
%{_kf6_libdir}/libKF6AuthCore.so

%files lang -f kauth6.lang

%changelog
