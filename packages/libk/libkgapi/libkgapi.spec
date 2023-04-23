#
# spec file for package libkgapi
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


%bcond_without released
Name:           libkgapi
Version:        23.04.0
Release:        0
Summary:        Extension for accessing Google data
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Conflicts:      libKPimGAPICore5 < %{version}

%description
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPIBlogger5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPIBlogger5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPICalendar5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPICalendar5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPICore5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}
%requires_eq    libkgapi
Requires:       sasl2-kdexoauth2 >= %{version}

%description -n libKPim5GAPICore5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPIDrive5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPIDrive5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPILatitude5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPILatitude5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPIMaps5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPIMaps5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPIPeople5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPIPeople5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPim5GAPITasks5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPim5GAPITasks5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n sasl2-kdexoauth2
Summary:        Cyrus SASL plugin for using Google's XOAUTH
Provides:       sasl2-kdexoauth2-3 = %{version}
Obsoletes:      sasl2-kdexoauth2-3 < %{version}

%description -n sasl2-kdexoauth2
This package provides a Cyrus SASL plugin to use Google's XOAUTH authentication
for receiving and sending mail through Google servers.

%package devel
Summary:        Build environment for libkgapi
Requires:       libKPim5GAPIBlogger5 = %{version}
Requires:       libKPim5GAPICalendar5 = %{version}
Requires:       libKPim5GAPICore5 = %{version}
Requires:       libKPim5GAPIDrive5 = %{version}
Requires:       libKPim5GAPILatitude5 = %{version}
Requires:       libKPim5GAPIMaps5 = %{version}
Requires:       libKPim5GAPIPeople5 = %{version}
Requires:       libKPim5GAPITasks5 = %{version}
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Contacts)
Obsoletes:      libkgapi5-devel < %{version}
Provides:       libkgapi5-devel = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n libkgapi-%{version}

%build
# workaround, kio-gdrive crashes when loading libKPim5GAPIDrive5 if built with LTO (boo#1148217)
%define _lto_cflags %{nil}
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --with-qt --all-name

%ldconfig_scriptlets -n libKPim5GAPIBlogger5
%ldconfig_scriptlets -n libKPim5GAPICalendar5
%ldconfig_scriptlets -n libKPim5GAPICore5
%ldconfig_scriptlets -n libKPim5GAPIDrive5
%ldconfig_scriptlets -n libKPim5GAPILatitude5
%ldconfig_scriptlets -n libKPim5GAPIMaps5
%ldconfig_scriptlets -n libKPim5GAPIPeople5
%ldconfig_scriptlets -n libKPim5GAPITasks5

%files
%license LICENSES/*
%{_kf5_debugdir}/libkgapi.categories

%files -n libKPim5GAPIBlogger5
%{_kf5_libdir}/libKPim5GAPIBlogger.so.*

%files -n libKPim5GAPICalendar5
%{_kf5_libdir}/libKPim5GAPICalendar.so.*

%files -n libKPim5GAPICore5
%{_kf5_libdir}/libKPim5GAPICore.so.*

%files -n libKPim5GAPIDrive5
%{_kf5_libdir}/libKPim5GAPIDrive.so.*

%files -n libKPim5GAPILatitude5
%{_kf5_libdir}/libKPim5GAPILatitude.so.*

%files -n libKPim5GAPIMaps5
%{_kf5_libdir}/libKPim5GAPIMaps.so.*

%files -n libKPim5GAPIPeople5
%{_kf5_libdir}/libKPim5GAPIPeople.so.*

%files -n libKPim5GAPITasks5
%{_kf5_libdir}/libKPim5GAPITasks.so.*

%files -n sasl2-kdexoauth2
%dir %{_kf5_libdir}/sasl2/
%{_kf5_libdir}/sasl2/libkdexoauth2.so*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KGAPI/
%{_includedir}/KPim5/kgapi_version.h
%{_kf5_cmakedir}/KPimGAPI/
%{_kf5_cmakedir}/KPim5GAPI/
%{_kf5_libdir}/libKPim5GAPIBlogger.so
%{_kf5_libdir}/libKPim5GAPICalendar.so
%{_kf5_libdir}/libKPim5GAPICore.so
%{_kf5_libdir}/libKPim5GAPIDrive.so
%{_kf5_libdir}/libKPim5GAPILatitude.so
%{_kf5_libdir}/libKPim5GAPIMaps.so
%{_kf5_libdir}/libKPim5GAPIPeople.so
%{_kf5_libdir}/libKPim5GAPITasks.so
%{_kf5_mkspecsdir}/qt_KGAPIBlogger.pri
%{_kf5_mkspecsdir}/qt_KGAPICalendar.pri
%{_kf5_mkspecsdir}/qt_KGAPICore.pri
%{_kf5_mkspecsdir}/qt_KGAPIDrive.pri
%{_kf5_mkspecsdir}/qt_KGAPILatitude.pri
%{_kf5_mkspecsdir}/qt_KGAPIMaps.pri
%{_kf5_mkspecsdir}/qt_KGAPIPeople.pri
%{_kf5_mkspecsdir}/qt_KGAPITasks.pri

%files lang -f %{name}.lang

%changelog
