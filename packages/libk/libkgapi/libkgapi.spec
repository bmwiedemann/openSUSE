#
# spec file for package libkgapi
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkgapi
Version:        22.12.0
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

%description
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPIBlogger5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPIBlogger5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPICalendar5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPICalendar5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPIContacts5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPIContacts5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPICore5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}
Provides:       %{name} = %{version}
Requires:       sasl2-kdexoauth2 >= %{version}

%description -n libKPimGAPICore5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPIDrive5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPIDrive5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPILatitude5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPILatitude5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPIMaps5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPIMaps5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n libKPimGAPITasks5
Summary:        Extension for accessing Google data
Recommends:     %{name}-lang = %{version}

%description -n libKPimGAPITasks5
An extension for accessing some Google services, such as Google Calendar,
Google Contacts and Google tasks.

%package -n sasl2-kdexoauth2
Summary:        Cyrus SASL plugin for using Google's XOAUTH
Conflicts:      kdepim-runtime < %{_kapp_version}
Provides:       sasl2-kdexoauth2-3 = %{version}
Obsoletes:      sasl2-kdexoauth2-3 < %{version}

%description -n sasl2-kdexoauth2
This package provides a Cyrus SASL plugin to use Google's XOAUTH authentication
for receiving and sending mail through Google servers.

%package devel
Summary:        Build environment for libkgapi
Requires:       libKPimGAPIBlogger5 = %{version}
Requires:       libKPimGAPICalendar5 = %{version}
Requires:       libKPimGAPIContacts5 = %{version}
Requires:       libKPimGAPICore5 = %{version}
Requires:       libKPimGAPIDrive5 = %{version}
Requires:       libKPimGAPILatitude5 = %{version}
Requires:       libKPimGAPIMaps5 = %{version}
Requires:       libKPimGAPITasks5 = %{version}
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
# workaround, kio-gdrive crashes when loading libKPimGAPIDrive5 if built with LTO (boo#1148217)
%define _lto_cflags %{nil}
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --with-qt --all-name

%post -n libKPimGAPIBlogger5 -p /sbin/ldconfig
%postun -n libKPimGAPIBlogger5 -p /sbin/ldconfig
%post -n libKPimGAPICalendar5 -p /sbin/ldconfig
%postun -n libKPimGAPICalendar5 -p /sbin/ldconfig
%post -n libKPimGAPIContacts5 -p /sbin/ldconfig
%postun -n libKPimGAPIContacts5 -p /sbin/ldconfig
%post -n libKPimGAPICore5 -p /sbin/ldconfig
%postun -n libKPimGAPICore5 -p /sbin/ldconfig
%post -n libKPimGAPIDrive5 -p /sbin/ldconfig
%postun -n libKPimGAPIDrive5 -p /sbin/ldconfig
%post -n libKPimGAPILatitude5 -p /sbin/ldconfig
%postun -n libKPimGAPILatitude5 -p /sbin/ldconfig
%post -n libKPimGAPIMaps5 -p /sbin/ldconfig
%postun -n libKPimGAPIMaps5 -p /sbin/ldconfig
%post -n libKPimGAPITasks5 -p /sbin/ldconfig
%postun -n libKPimGAPITasks5 -p /sbin/ldconfig

%files -n libKPimGAPIBlogger5
%{_kf5_libdir}/libKPimGAPIBlogger.so.*

%files -n libKPimGAPICalendar5
%{_kf5_libdir}/libKPimGAPICalendar.so.*

%files -n libKPimGAPIContacts5
%{_kf5_libdir}/libKPimGAPIContacts.so.*

%files -n libKPimGAPICore5
%license LICENSES/*
%{_kf5_debugdir}/libkgapi.categories
%{_kf5_libdir}/libKPimGAPICore.so.*

%files -n libKPimGAPIDrive5
%{_kf5_libdir}/libKPimGAPIDrive.so.*

%files -n libKPimGAPILatitude5
%{_kf5_libdir}/libKPimGAPILatitude.so.*

%files -n libKPimGAPIMaps5
%{_kf5_libdir}/libKPimGAPIMaps.so.*

%files -n libKPimGAPITasks5
%{_kf5_libdir}/libKPimGAPITasks.so.*

%files -n sasl2-kdexoauth2
%dir %{_kf5_libdir}/sasl2/
%{_kf5_libdir}/sasl2/libkdexoauth2.so*

%files devel
%{_includedir}/KPim/
%{_kf5_cmakedir}/KPimGAPI/
%{_kf5_libdir}/libKPimGAPIBlogger.so
%{_kf5_libdir}/libKPimGAPICalendar.so
%{_kf5_libdir}/libKPimGAPIContacts.so
%{_kf5_libdir}/libKPimGAPICore.so
%{_kf5_libdir}/libKPimGAPIDrive.so
%{_kf5_libdir}/libKPimGAPILatitude.so
%{_kf5_libdir}/libKPimGAPIMaps.so
%{_kf5_libdir}/libKPimGAPITasks.so
%{_kf5_mkspecsdir}/qt_KGAPIBlogger.pri
%{_kf5_mkspecsdir}/qt_KGAPICalendar.pri
%{_kf5_mkspecsdir}/qt_KGAPIContacts.pri
%{_kf5_mkspecsdir}/qt_KGAPICore.pri
%{_kf5_mkspecsdir}/qt_KGAPIDrive.pri
%{_kf5_mkspecsdir}/qt_KGAPILatitude.pri
%{_kf5_mkspecsdir}/qt_KGAPIMaps.pri
%{_kf5_mkspecsdir}/qt_KGAPITasks.pri

%files lang -f %{name}.lang

%changelog
