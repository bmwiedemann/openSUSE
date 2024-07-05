#
# spec file for package akonadi-search
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.2

%bcond_without released
Name:           akonadi-search
Version:        24.05.2
Release:        0
Summary:        Framework for searching and managing PIM metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        vendor.tar.zst
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libxapian-devel
BuildRequires:  zstd
BuildRequires:  cmake(Corrosion)
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Obsoletes:      baloo-pim < %{version}

%description
AkonadiSearch is a framework for searching and managing PIM metadata

%package -n libKPim6AkonadiSearch6
Summary:        Core libraries for AkonadiSearch
Obsoletes:      libKF5AkonadiSearch5 < %{version}
Obsoletes:      libKPim5AkonadiSearch5 < %{version}

%description -n libKPim6AkonadiSearch6
AkonadiSearch is a framework for searching and managing PIM metadata.
This package contains the core libraries

%package devel
Summary:        Development package for baloo5
Requires:       libKPim6AkonadiSearch6 = %{version}
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}
Requires:       cmake(KF6Contacts) >= %{kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}
Requires:       cmake(KPim6AkonadiMime) >= %{kpim6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Development files for the AkonadiSearch library.

%lang_package

%prep
%autosetup -p1 -a3

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6AkonadiSearch6

%files
%{_kf6_bindir}/akonadi_html_to_text
%{_kf6_bindir}/akonadi_indexing_agent
%{_kf6_debugdir}/akonadi-search.categories
%{_kf6_debugdir}/akonadi-search.renamecategories
%dir %{_kf6_plugindir}/kf6/krunner
%dir %{_kf6_plugindir}/kf6/krunner/kcms
%{_kf6_plugindir}/kf6/krunner/krunner_pimcontacts.so
%{_kf6_plugindir}/kf6/krunner/kcms/kcm_krunner_pimcontacts.so
%{_kf6_plugindir}/pim6/akonadi/
%dir %{_kf6_sharedir}/akonadi
%dir %{_kf6_sharedir}/akonadi/agents
%{_kf6_sharedir}/akonadi/agents/akonadiindexingagent.desktop

%files -n libKPim6AkonadiSearch6
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiSearchCore.so.*
%{_kf6_libdir}/libKPim6AkonadiSearchDebug.so.*
%{_kf6_libdir}/libKPim6AkonadiSearchPIM.so.*
%{_kf6_libdir}/libKPim6AkonadiSearchXapian.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6AkonadiSearchPIM.*
%{_includedir}/KPim6/AkonadiSearch/
%{_kf6_cmakedir}/KPim6AkonadiSearch/
%{_kf6_libdir}/libKPim6AkonadiSearchCore.so
%{_kf6_libdir}/libKPim6AkonadiSearchDebug.so
%{_kf6_libdir}/libKPim6AkonadiSearchPIM.so
%{_kf6_libdir}/libKPim6AkonadiSearchXapian.so

%files lang -f %{name}.lang

%changelog
