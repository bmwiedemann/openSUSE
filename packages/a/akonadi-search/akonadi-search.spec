#
# spec file for package akonadi-search
#
# Copyright (c) 2023 SUSE LLC
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
%define kf5_version 5.104.0
%define libname libKPim5AkonadiSearch5
%bcond_without released
Name:           akonadi-search
Version:        23.04.0
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
BuildRequires:  cmake(KF5CalendarCore) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5Contacts) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
Obsoletes:      baloo-pim < %{version}

%description
AkonadiSearch is a framework for searching and managing PIM metadata

%package -n %{libname}
Summary:        Core libraries for AkonadiSearch

%description -n %{libname}
AkonadiSearch is a framework for searching and managing PIM metadata.
This package contains the core libraries

%package devel
Summary:        Development package for baloo5
Requires:       %{libname} = %{version}
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KPim5AkonadiMime)
Requires:       cmake(KPim5Mime)
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

%ldconfig_scriptlets -n %{libname}

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

%files -n %{libname}
%license LICENSES/*
%{_kf5_libdir}/libKPim5AkonadiSearchCore.so.%{soversion}*
%{_kf5_libdir}/libKPim5AkonadiSearchDebug.so.%{soversion}*
%{_kf5_libdir}/libKPim5AkonadiSearchPIM.so.%{soversion}*
%{_kf5_libdir}/libKPim5AkonadiSearchXapian.so.%{soversion}*

%files devel
%dir %{_includedir}/KPim5
%{_kf5_cmakedir}/KF5AkonadiSearch/
%{_kf5_cmakedir}/KPim5AkonadiSearch/
%{_includedir}/KPim5/AkonadiSearch/
%{_kf5_libdir}/libKPim5AkonadiSearchCore.so
%{_kf5_libdir}/libKPim5AkonadiSearchDebug.so
%{_kf5_libdir}/libKPim5AkonadiSearchPIM.so
%{_kf5_libdir}/libKPim5AkonadiSearchXapian.so

%files lang -f %{name}.lang

%changelog
