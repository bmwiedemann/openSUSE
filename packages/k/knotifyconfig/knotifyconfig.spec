#
# spec file for package knotifyconfig
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


%define lname   libKF5NotifyConfig5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           knotifyconfig
Version:        5.101.0
Release:        0
Summary:        Configuration dialog for desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Bookmarks) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Completion) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5TextToSpeech) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  pkgconfig(libcanberra)

%description
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package -n %{lname}
Summary:        Configuration dialog for desktop notifications

%description -n %{lname}
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package devel
Summary:        Configuration dialog for desktop notifications
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Widgets) >= 5.15.0

%description devel
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang knotifyconfig5

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f knotifyconfig5.lang

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5NotifyConfig.so.*
%{_kf5_debugdir}/knotifyconfig.categories

%files devel
%{_kf5_libdir}/libKF5NotifyConfig.so
%{_kf5_libdir}/cmake/KF5NotifyConfig/
%{_kf5_includedir}/KNotifyConfig/
%{_kf5_mkspecsdir}/qt_KNotifyConfig.pri

%changelog
