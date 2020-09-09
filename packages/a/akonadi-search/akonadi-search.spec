#
# spec file for package akonadi-search
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-search
Version:        20.08.1
Release:        0
Summary:        Framework for searching and managing PIM metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
AkonadiSearch is a framework for searching and managing PIM metada

%package -n libKF5AkonadiSearch
Summary:        Core libraries for AkonadiSearch
Group:          System/Libraries

%description -n libKF5AkonadiSearch
AkonadiSearch is a framework for searching and managing PIM metada. This package
holds the core libraries

%package devel
Summary:        Development package for baloo5
Group:          Development/Libraries/KDE
Requires:       libKF5AkonadiSearch = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KF5Mime)
Requires:       cmake(Qt5Core)

%description devel
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities. Development files.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AkonadiSearch -p /sbin/ldconfig
%postun -n libKF5AkonadiSearch -p /sbin/ldconfig

%files -n libKF5AkonadiSearch
%license LICENSES/*
%{_kf5_libdir}/libKF5AkonadiSearchCore.so.*
%{_kf5_libdir}/libKF5AkonadiSearchPIM.so.*
%{_kf5_libdir}/libKF5AkonadiSearchXapian.so.*
%{_kf5_libdir}/libKF5AkonadiSearchDebug.so.*

%files
%license LICENSES/*
%{_kf5_debugdir}/akonadi-search.categories
%{_kf5_debugdir}/akonadi-search.renamecategories
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/agents
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/krunner
%{_kf5_bindir}/akonadi_indexing_agent
%{_kf5_plugindir}/akonadi/
%{_kf5_plugindir}/kcm_krunner_pimcontacts.so
%{_kf5_plugindir}/kf5/krunner/krunner_pimcontacts.so
%{_kf5_servicesdir}/plasma-krunner-pimcontacts_config.desktop
%{_kf5_sharedir}/akonadi/agents/akonadiindexingagent.desktop

%files devel
%license LICENSES/*
%dir %{_kf5_includedir}
%{_kf5_includedir}/*.h
%{_kf5_includedir}/AkonadiSearch/
%{_kf5_cmakedir}/KF5AkonadiSearch/
%{_kf5_libdir}/libKF5AkonadiSearchCore.so
%{_kf5_libdir}/libKF5AkonadiSearchDebug.so
%{_kf5_libdir}/libKF5AkonadiSearchPIM.so
%{_kf5_libdir}/libKF5AkonadiSearchXapian.so

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
