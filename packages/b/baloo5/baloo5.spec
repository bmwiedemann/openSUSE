#
# spec file for package baloo5
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           baloo5
Version:        5.101.0
Release:        0
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         baloo-%{version}.tar.xz
%if %{with released}
Source1:        baloo-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libattr-devel
BuildRequires:  lmdb-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5FileMetaData) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IdleTime) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Solid) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
Baloo is a framework for searching and managing metadata.

%package -n libKF5Baloo5
Summary:        Core library for Baloo Framework

# The -lang package was split into components
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
# baloo5-imports-lang is gone in 5.83
Obsoletes:      %{name}-imports-lang < 5.83

%description -n libKF5Baloo5
Baloo is a framework for searching and managing metadata. This
package contains Baloo's core library.

%package -n libKF5BalooEngine5
Summary:        Baloo Engine library
Recommends:     libKF5BalooEngine5-lang

%description -n libKF5BalooEngine5
Baloo is a framework for searching and managing metadata. This
package contains Baloo's Engine library.

%package file
Summary:        Filesearch components for Baloo Framework
Requires:       libQt5Sql5-sqlite
Recommends:     %{name}-file-lang
Provides:       baloo-file = %{version}
Obsoletes:      baloo-file < %{version}

%description file
Baloo is a framework for searching and managing metadata. This
package contains filesearch components.

%package kioslaves
Summary:        KIO slave components for Baloo Framework
Requires:       kded
Recommends:     %{name}-kioslaves-lang

%description kioslaves
Baloo is a framework for searching and managing metadata. This
package contains KIO slave components.

%package tools
Summary:        Aditional components for Baloo Framework
Recommends:     %{name}-tools-lang
Provides:       baloo-tools = %{version}
Obsoletes:      baloo-tools < %{version}

%description tools
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities.

%package imports
Summary:        QML components for Baloo Framework
Recommends:     %{name}-imports-lang

%description imports
Baloo is a framework for searching and managing metadata. This
package contains QML imports.

%package devel
Summary:        Development package for baloo5
Requires:       libKF5Baloo5 = %{version}
Requires:       libKF5BalooEngine5 = %{version}
Requires:       lmdb-devel
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5FileMetaData) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Core) >= 5.15.0
# DBus interface file
Conflicts:      baloo-devel

%description devel
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities. Development files.

%lang_package -n libKF5BalooEngine5
%lang_package -n %{name}-file
%lang_package -n %{name}-tools
%lang_package -n %{name}-kioslaves
%lang_package -n %{name}-imports

%prep
%autosetup -p1 -n baloo-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build

%{kf5_find_lang}
# Split manually, kf5_find_lang doesn't support it...
grep -E '^%%dir' %{name}.lang | tee %{name}-{file,tools,kioslaves}.lang >/dev/null
grep -E '/balooengine5.mo$' %{name}.lang >> libKF5BalooEngine5.lang
grep -E '/balooctl5.mo$' %{name}.lang >> %{name}-file.lang
grep -E '/(baloodb5|baloosearch5|balooshow5).mo$' %{name}.lang >> %{name}-tools.lang
grep -E '/(kio5_baloosearch|kio5_tags|kio5_timeline).mo$' %{name}.lang >> %{name}-kioslaves.lang

rm %{name}.lang

%post -n libKF5Baloo5 -p /sbin/ldconfig
%postun -n libKF5Baloo5 -p /sbin/ldconfig

%post file %{systemd_user_post kde-baloo.service}
%preun file %{systemd_user_preun kde-baloo.service}
%postun file %{systemd_user_postun kde-baloo.service}

%post -n libKF5BalooEngine5 -p /sbin/ldconfig
%postun -n libKF5BalooEngine5 -p /sbin/ldconfig

%files -n libKF5Baloo5
%license LICENSES/*
%{_kf5_libdir}/libKF5Baloo.so.*

%files -n libKF5BalooEngine5
%{_kf5_libdir}/libKF5BalooEngine.so.*

%files file
%{_kf5_bindir}/baloo_file
%{_kf5_bindir}/baloo_file_extractor
%{_kf5_bindir}/balooctl
%{_kf5_configdir}/autostart/baloo_file.desktop
%{_kf5_debugdir}/baloo.categories
%{_kf5_debugdir}/baloo.renamecategories
%{_libexecdir}/baloo_file
%{_libexecdir}/baloo_file_extractor
%{_userunitdir}/kde-baloo.service

%files kioslaves
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/baloosearchmodule.so
%dir %{_kf5_plugindir}/kf5/kio
%{_kf5_plugindir}/kf5/kio/baloosearch.so
%{_kf5_plugindir}/kf5/kio/tags.so
%{_kf5_plugindir}/kf5/kio/timeline.so

%files tools
%{_kf5_bindir}/baloosearch
%{_kf5_bindir}/balooshow

%files imports
%{_kf5_qmldir}/

%files devel
%{_kf5_includedir}/Baloo/
%{_kf5_libdir}/cmake/KF5Baloo/
%{_kf5_libdir}/libKF5Baloo.so
%{_kf5_libdir}/pkgconfig/Baloo.pc
%{_kf5_mkspecsdir}/qt_Baloo.pri
%{_kf5_sharedir}/dbus-1/interfaces/*.xml

%files -n libKF5BalooEngine5-lang -f libKF5BalooEngine5.lang

%files file-lang -f %{name}-file.lang

%files tools-lang -f %{name}-tools.lang

%files kioslaves-lang -f %{name}-kioslaves.lang

%changelog
