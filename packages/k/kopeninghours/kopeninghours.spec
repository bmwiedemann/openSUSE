#
# spec file for package kopeninghours
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


%bcond_without lang
Name:           kopeninghours
Version:        21.04.0
Release:        0
Summary:        OSM opening hours expression parser and evaluator
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.14
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)

%description
A library for parsing and evaluating OSM opening hours expressions.

%package -n libKOpeningHours1
Summary:        OSM opening hours expression parser and evaluator
Recommends:     %{name}

%description -n libKOpeningHours1
A library for parsing and evaluating OSM opening hours expressions.

%package devel
Summary:        Development files for KOpeningHours
Requires:       libKOpeningHours1 = %{version}

%description devel
Include files and libraries needed to build programs that use the KOpeningHours
library.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%if %{with lang}
  %find_lang %{name} --with-man
%endif

%check
export QT_QPA_PLATFORM=offscreen
%ctest

%post -n libKOpeningHours1 -p /sbin/ldconfig
%postun -n libKOpeningHours1 -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/kopeninghours/

%files -n libKOpeningHours1
%license LICENSES/*
%{_kf5_debugdir}/org_kde_kopeninghours.categories
%{_kf5_libdir}/libKOpeningHours.so.*

%files devel
%license LICENSES/*
%{_includedir}/KOpeningHours/
%{_includedir}/kopeninghours/
%{_includedir}/kopeninghours_version.h
%{_kf5_cmakedir}/KOpeningHours/
%{_kf5_libdir}/libKOpeningHours.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
