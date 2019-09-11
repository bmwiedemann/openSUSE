#
# spec file for package akonadi-search
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.56.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-search
Version:        19.08.1
Release:        0
Summary:        Framework for searching and managing PIM metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-mime-devel >= %{_kapp_version}
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kcalcore-devel
BuildRequires:  kcmutils-devel >= %{kf5_version}
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kcontacts-devel
BuildRequires:  kcrash-devel >= %{kf5_version}
BuildRequires:  kdbusaddons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kmime-devel
BuildRequires:  krunner-devel >= %{kf5_version}
BuildRequires:  libxapian-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
Obsoletes:      baloo-pim < %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

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
Requires:       akonadi-mime-devel
Requires:       akonadi-server-devel >= %{_kapp_version}
Requires:       kcalcore-devel
Requires:       kcontacts-devel
Requires:       kcoreaddons-devel
Requires:       kmime-devel
Requires:       libKF5AkonadiSearch = %{version}
Requires:       pkgconfig(Qt5Core)

%description devel
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities. Development files.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AkonadiSearch -p /sbin/ldconfig
%postun -n libKF5AkonadiSearch -p /sbin/ldconfig

%files -n libKF5AkonadiSearch
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiSearchCore.so.*
%{_kf5_libdir}/libKF5AkonadiSearchPIM.so.*
%{_kf5_libdir}/libKF5AkonadiSearchXapian.so.*
%{_kf5_libdir}/libKF5AkonadiSearchDebug.so.*

%files
%license COPYING*
%{_kf5_debugdir}/akonadi-search.categories
%{_kf5_debugdir}/akonadi-search.renamecategories
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/agents
%{_kf5_bindir}/akonadi_indexing_agent
%{_kf5_plugindir}/akonadi/
%{_kf5_plugindir}/kcm_krunner_pimcontacts.so
%{_kf5_plugindir}/krunner_pimcontacts.so
%{_kf5_servicesdir}/plasma-krunner-pimcontacts.desktop
%{_kf5_servicesdir}/plasma-krunner-pimcontacts_config.desktop
%{_kf5_sharedir}/akonadi/agents/akonadiindexingagent.desktop

%files devel
%license COPYING*
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
%license COPYING*
%endif

%changelog
