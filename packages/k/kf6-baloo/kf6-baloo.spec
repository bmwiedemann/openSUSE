#
# spec file for package kf6-baloo
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

%define rname baloo
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-baloo
Version:        6.3.0
Release:        0
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  libattr-devel
BuildRequires:  lmdb-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6IdleTime) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Solid) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Baloo is a framework for searching and managing metadata.

%package -n libKF6Baloo6
Summary:        Core library for Baloo Framework

%description -n libKF6Baloo6
Baloo is a framework for searching and managing metadata. This
package contains Baloo's core library.

%package -n libKF6BalooEngine6
Summary:        Baloo Engine library
Recommends:     libKF6Baloo6-lang

%description -n libKF6BalooEngine6
Baloo is a framework for searching and managing metadata. This
package contains Baloo's Engine library.

%package file
Summary:        Filesearch components for Baloo Framework
Requires:       qt6-sql-sqlite
Recommends:     libKF6Baloo6-lang
Conflicts:      baloo5-file

%description file
Baloo is a framework for searching and managing metadata. This
package contains filesearch components.

%package kioslaves
Summary:        KIO slave components for Baloo Framework
Requires:       kf6-kded
Recommends:     libKF6Baloo6-lang

%description kioslaves
Baloo is a framework for searching and managing metadata. This
package contains KIO slave components.

%package tools
Summary:        Aditional components for Baloo Framework
Recommends:     libKF6Baloo6-lang

%description tools
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities.

%package imports
Summary:        QML components for Baloo Framework
Recommends:     libKF6Baloo6-lang

%description imports
Baloo is a framework for searching and managing metadata. This
package contains QML imports.

%package devel
Summary:        Development package for baloo6
Requires:       libKF6Baloo6 = %{version}
Requires:       libKF6BalooEngine6 = %{version}
Requires:       lmdb-devel
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6FileMetaData) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Conflicts:      baloo5-devel

%description devel
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities. Development files.

%lang_package -n libKF6Baloo6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang kf6-baloo --all-name

%ldconfig_scriptlets -n libKF6Baloo6
%ldconfig_scriptlets -n libKF6BalooEngine6

%post file
%{systemd_user_post kde-baloo.service}

%preun file
%{systemd_user_preun kde-baloo.service}

%postun file
%{systemd_user_postun kde-baloo.service}

%files -n libKF6Baloo6
%license LICENSES/*
%{_kf6_libdir}/libKF6Baloo.so.*

%files -n libKF6BalooEngine6
%{_kf6_libdir}/libKF6BalooEngine.so.*

%files file
%{_kf6_bindir}/balooctl6
%{_kf6_configdir}/autostart/baloo_file.desktop
%{_kf6_debugdir}/baloo.categories
%{_kf6_debugdir}/baloo.renamecategories
%{_kf6_libexecdir}/baloo_file
%{_kf6_libexecdir}/baloo_file_extractor
%{_userunitdir}/kde-baloo.service

%files kioslaves
%{_kf6_plugindir}/kf6/kded/baloosearchmodule.so
%{_kf6_plugindir}/kf6/kio/baloosearch.so
%{_kf6_plugindir}/kf6/kio/tags.so
%{_kf6_plugindir}/kf6/kio/timeline.so

%files tools
%{_kf6_bindir}/baloosearch6
%{_kf6_bindir}/balooshow6

%files imports
%{_kf6_qmldir}/org/kde/baloo/

%files devel
%doc %{_kf6_qchdir}/KF6Baloo.*
%{_kf6_includedir}/Baloo/
%{_kf6_cmakedir}/KF6Baloo/
%{_kf6_libdir}/libKF6Baloo.so
%{_kf6_pkgconfigdir}/KF6Baloo.pc
%{_kf6_sharedir}/dbus-1/interfaces/*.xml

%files -n libKF6Baloo6-lang -f kf6-baloo.lang

%changelog
