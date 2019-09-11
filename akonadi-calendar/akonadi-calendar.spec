#
# spec file for package akonadi-calendar
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
Name:           akonadi-calendar
Version:        19.08.0
Release:        0
Summary:        Akonadi calendar integration
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-contact-devel
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= 5.17.0
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kidentitymanagement-devel
BuildRequires:  kio-devel
BuildRequires:  kmailtransport-devel >= %{_kapp_version}
BuildRequires:  kwallet-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This library provides calendar integration for Akonadi based Applications.

%package -n libKF5AkonadiCalendar5
Summary:        KDE PIM Libraries: AkonadiCalendar
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5AkonadiCalendar5
This library provides calendar integration for Akonadi based Applications.

%package -n akonadi-plugin-calendar
Summary:        Akonadi calendar integration - serializer plugin
Group:          System/Libraries
Requires:       libKF5AkonadiCalendar5 = %{version}

%description -n akonadi-plugin-calendar
This package provides plugins required by PIM applications to read and write calendar data.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       akonadi-contact-devel >= %{_kapp_version}
Requires:       akonadi-server-devel >= %{_kapp_version}
Requires:       kcalcore-devel >= %{_kapp_version}
Requires:       libKF5AkonadiCalendar5 = %{version}
Obsoletes:      akonadi5-calendar-devel < %{version}
Provides:       akonadi5-calendar-devel = %{version}

%description devel
Development package for akonadi-calendar.

%lang_package

%prep
%setup -q -n akonadi-calendar-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AkonadiCalendar5 -p /sbin/ldconfig
%postun -n libKF5AkonadiCalendar5 -p /sbin/ldconfig

%files -n libKF5AkonadiCalendar5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiCalendar.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n akonadi-plugin-calendar
%{_kf5_plugindir}/akonadi_serializer_kcalcore.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop

%files devel
%license COPYING*
%dir %{_kf5_includedir}/Akonadi
%dir %{_kf5_includedir}/akonadi
%{_kf5_includedir}/Akonadi/Calendar/
%{_kf5_includedir}/akonadi-calendar_version.h
%{_kf5_includedir}/akonadi/calendar/
%{_kf5_cmakedir}/KF5AkonadiCalendar/
%{_kf5_libdir}/libKF5AkonadiCalendar.so
%{_kf5_mkspecsdir}/qt_AkonadiCalendar.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
