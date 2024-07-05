#
# spec file for package libkgapi6
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

%define rname libkgapi
%bcond_without released
Name:           libkgapi6
Version:        24.05.2
Release:        0
Summary:        Extension for accessing Google data
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPIBlogger6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPIBlogger6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPICalendar6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPICalendar6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPICore6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}
Requires:       libkgapi6 >= %{version}
Requires:       sasl2-kdexoauth2 >= %{version}

%description -n libKPim6GAPICore6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPIDrive6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPIDrive6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPILatitude6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPILatitude6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPIMaps6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPIMaps6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPIPeople6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPIPeople6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim6GAPITasks6
Summary:        Extension for accessing Google data
Recommends:     libkgapi6-lang = %{version}

%description -n libKPim6GAPITasks6
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package sasl2-kdexoauth2
Summary:        Cyrus SASL plugin for using Google's XOAUTH
# libkgapi and libkgapi6 have to coexist. The sasl2 plugin can replace the
# one shipped with libkgapi
Provides:       sasl2-kdexoauth2 = %{version}
Obsoletes:      sasl2-kdexoauth2 < %{version}
Provides:       sasl2-kdexoauth2-3 = %{version}
Obsoletes:      sasl2-kdexoauth2-3 < %{version}

%description sasl2-kdexoauth2
This package provides a Cyrus SASL plugin to use Google's XOAUTH authentication
for receiving and sending mail through Google servers.

%package devel
Summary:        Build environment for libkgapi6
Requires:       libKPim6GAPIBlogger6 = %{version}
Requires:       libKPim6GAPICalendar6 = %{version}
Requires:       libKPim6GAPICore6 = %{version}
Requires:       libKPim6GAPIDrive6 = %{version}
Requires:       libKPim6GAPILatitude6 = %{version}
Requires:       libKPim6GAPIMaps6 = %{version}
Requires:       libKPim6GAPIPeople6 = %{version}
Requires:       libKPim6GAPITasks6 = %{version}
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}
Requires:       cmake(KF6Contacts) >= %{kf6_version}

%description devel
This package contains all necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# workaround, kio-gdrive crashes when loading libKPim6GAPIDrive6 if built with LTO (boo#1148217)
%define _lto_cflags %{nil}
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-qt --all-name

%ldconfig_scriptlets -n libKPim6GAPIBlogger6
%ldconfig_scriptlets -n libKPim6GAPICalendar6
%ldconfig_scriptlets -n libKPim6GAPICore6
%ldconfig_scriptlets -n libKPim6GAPIDrive6
%ldconfig_scriptlets -n libKPim6GAPILatitude6
%ldconfig_scriptlets -n libKPim6GAPIMaps6
%ldconfig_scriptlets -n libKPim6GAPIPeople6
%ldconfig_scriptlets -n libKPim6GAPITasks6

%files
%{_kf6_debugdir}/libkgapi.categories

%files -n libKPim6GAPIBlogger6
%{_kf6_libdir}/libKPim6GAPIBlogger.so.*

%files -n libKPim6GAPICalendar6
%{_kf6_libdir}/libKPim6GAPICalendar.so.*

%files -n libKPim6GAPICore6
%license LICENSES/*
%{_kf6_libdir}/libKPim6GAPICore.so.*

%files -n libKPim6GAPIDrive6
%{_kf6_libdir}/libKPim6GAPIDrive.so.*

%files -n libKPim6GAPILatitude6
%{_kf6_libdir}/libKPim6GAPILatitude.so.*

%files -n libKPim6GAPIMaps6
%{_kf6_libdir}/libKPim6GAPIMaps.so.*

%files -n libKPim6GAPIPeople6
%{_kf6_libdir}/libKPim6GAPIPeople.so.*

%files -n libKPim6GAPITasks6
%{_kf6_libdir}/libKPim6GAPITasks.so.*

%files sasl2-kdexoauth2
%dir %{_kf6_libdir}/sasl2/
%{_kf6_libdir}/sasl2/libkdexoauth2.so*

%files devel
%doc %{_kf6_qchdir}/KPim6GAPI*.*
%{_includedir}/KPim6/KGAPI/
%{_kf6_cmakedir}/KPim6GAPI/
%{_kf6_libdir}/libKPim6GAPIBlogger.so
%{_kf6_libdir}/libKPim6GAPICalendar.so
%{_kf6_libdir}/libKPim6GAPICore.so
%{_kf6_libdir}/libKPim6GAPIDrive.so
%{_kf6_libdir}/libKPim6GAPILatitude.so
%{_kf6_libdir}/libKPim6GAPIMaps.so
%{_kf6_libdir}/libKPim6GAPIPeople.so
%{_kf6_libdir}/libKPim6GAPITasks.so

%files lang -f %{name}.lang

%changelog
