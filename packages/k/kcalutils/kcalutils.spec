#
# spec file for package kcalutils
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kcalutils
Version:        19.08.3
Release:        0
Summary:        Library with utility functions for handling calendar data
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  grantlee5-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcodecs-devel >= %{kf5_version}
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kdelibs4support-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kidentitymanagement-devel >= %{_kapp_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package -n libKF5CalendarUtils5
Summary:        Library with utility functions for handling calendar data
Group:          System/Libraries
Requires:       %{name} = %{version}

%description  -n libKF5CalendarUtils5
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package devel
Summary:        Development files for kcalutils
Group:          Development/Libraries/KDE
Requires:       kcalcore-devel
Requires:       kcoreaddons-devel >= %{kf5_version}
Requires:       kdelibs4support-devel >= %{kf5_version}
Requires:       libKF5CalendarUtils5
Obsoletes:      kcalutils5-devel < %{version}
Provides:       kcalutils5-devel = %{version}

%description devel
This package contains necessary include files and libraries needed
to develop applications wanting to use kcalutils.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kcalutils-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5CalendarUtils5 -p /sbin/ldconfig
%postun -n libKF5CalendarUtils5 -p /sbin/ldconfig

%files -n libKF5CalendarUtils5
%license COPYING*
%{_kf5_libdir}/libKF5CalendarUtils.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5CalendarUtils/
%{_kf5_includedir}/KCalUtils/
%{_kf5_includedir}/kcalutils_version.h
%{_kf5_libdir}/libKF5CalendarUtils.so
%{_kf5_mkspecsdir}/qt_KCalUtils.pri

%files
%license COPYING*
%{_libdir}/grantlee/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
