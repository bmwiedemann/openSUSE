#
# spec file for package akonadi-search
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

%define soversion 5
%define kf5_version 5.99.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           akonadi-search
Version:        22.12.0
Release:        0
Summary:        Framework for searching and managing PIM metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libxapian-devel
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
Obsoletes:      baloo-pim < %{version}

%description
AkonadiSearch is a framework for searching and managing PIM metadata

%package -n libKF5AkonadiSearch%{soversion}
Summary:        Core libraries for AkonadiSearch
Provides:       libKF5AkonadiSearch = 22.04.0
Obsoletes:      libKF5AkonadiSearch < 22.04.0

%description -n libKF5AkonadiSearch%{soversion}
AkonadiSearch is a framework for searching and managing PIM metadata.
This package contains the core libraries

%package devel
Summary:        Development package for baloo5
Requires:       libKF5AkonadiSearch%{soversion} = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KF5Mime)
Requires:       cmake(Qt5Core)

%description devel
Development files for the AkonadiSearch library.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5AkonadiSearch%{soversion} -p /sbin/ldconfig
%postun -n libKF5AkonadiSearch%{soversion} -p /sbin/ldconfig

%files -n libKF5AkonadiSearch%{soversion}
%license LICENSES/*
%{_kf5_libdir}/libKF5AkonadiSearchCore.so.%{soversion}*
%{_kf5_libdir}/libKF5AkonadiSearchDebug.so.%{soversion}*
%{_kf5_libdir}/libKF5AkonadiSearchPIM.so.%{soversion}*
%{_kf5_libdir}/libKF5AkonadiSearchXapian.so.%{soversion}*

%files
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/krunner
%dir %{_kf5_plugindir}/kf5/krunner/kcms
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/agents
%dir %{_kf5_plugindir}/pim5
%{_kf5_bindir}/akonadi_indexing_agent
%{_kf5_debugdir}/akonadi-search.categories
%{_kf5_debugdir}/akonadi-search.renamecategories
%{_kf5_plugindir}/pim5/akonadi/
%{_kf5_plugindir}/kf5/krunner/krunner_pimcontacts.so
%{_kf5_plugindir}/kf5/krunner/kcms/kcm_krunner_pimcontacts.so
%{_kf5_sharedir}/akonadi/agents/akonadiindexingagent.desktop

%files devel
%{_kf5_cmakedir}/KF5AkonadiSearch/
%{_kf5_includedir}/AkonadiSearch/
%{_kf5_libdir}/libKF5AkonadiSearchCore.so
%{_kf5_libdir}/libKF5AkonadiSearchDebug.so
%{_kf5_libdir}/libKF5AkonadiSearchPIM.so
%{_kf5_libdir}/libKF5AkonadiSearchXapian.so

%files lang -f %{name}.lang

%changelog
