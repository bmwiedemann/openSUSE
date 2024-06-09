#
# spec file for package kf6-kstatusnotifieritem
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

%define rname kstatusnotifieritem
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kstatusnotifieritem
Version:        6.3.0
Release:        0
Summary:        Implementation of Status Notifier Items
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Implementation of Status Notifier Items.

%package -n libKF6StatusNotifierItem6
Summary:        Implementation of Status Notifier Items
Requires:       kf6-kstatusnotifieritem >= %{version}

%description -n libKF6StatusNotifierItem6
Implementation of Status Notifier Items.

%package devel
Summary:        Development files for kstatusnotifieritem
Requires:       libKF6StatusNotifierItem6 = %{version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description devel
Development files for kstatusnotifieritem

%lang_package -n libKF6StatusNotifierItem6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kstatusnotifieritem6 --with-qt

%ldconfig_scriptlets -n libKF6StatusNotifierItem6

%files
%{_kf6_debugdir}/kstatusnotifieritem.categories

%files -n libKF6StatusNotifierItem6
%license LICENSES/*
%{_kf6_libdir}/libKF6StatusNotifierItem.so.*

%files devel
%doc %{_kf6_qchdir}/KF6StatusNotifierItem.*
%{_kf6_libdir}/libKF6StatusNotifierItem.so
%{_kf6_cmakedir}/KF6StatusNotifierItem/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.StatusNotifierItem.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.StatusNotifierWatcher.xml
%{_kf6_includedir}/KStatusNotifierItem/

%files -n libKF6StatusNotifierItem6-lang -f kstatusnotifieritem6.lang

%changelog
