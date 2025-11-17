#
# spec file for package kf6-knotifyconfig
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname knotifyconfig
# Full KF6 version (e.g. 6.20.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-knotifyconfig
Version:        6.20.0
Release:        0
Summary:        Configuration dialog for desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Completion) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libcanberra)

%description
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package -n libKF6NotifyConfig6
Summary:        Configuration dialog for desktop notifications
Requires:       kf6-knotifyconfig >= %{version}

%description -n libKF6NotifyConfig6
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package devel
Summary:        Configuration dialog for desktop notifications
Requires:       libKF6NotifyConfig6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application. Development files.

%lang_package -n libKF6NotifyConfig6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang knotifyconfig6

%ldconfig_scriptlets -n libKF6NotifyConfig6

%files
%{_kf6_debugdir}/knotifyconfig.categories

%files -n libKF6NotifyConfig6
%license LICENSES/*
%{_kf6_libdir}/libKF6NotifyConfig.so.*

%files devel
%{_kf6_cmakedir}/KF6NotifyConfig/
%{_kf6_includedir}/KNotifyConfig/
%{_kf6_libdir}/libKF6NotifyConfig.so

%files -n libKF6NotifyConfig6-lang -f knotifyconfig6.lang

%changelog
