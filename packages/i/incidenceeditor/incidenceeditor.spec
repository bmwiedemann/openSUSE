#
# spec file for package incidenceeditor
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
Name:           incidenceeditor
Version:        22.12.0
Release:        0
Summary:        Incidenceeditor library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KChart)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
This package contains the incidenceeditor library.

%package -n libKF5IncidenceEditor5
Summary:        Incidenceeditor Library
License:        LGPL-2.1-or-later
Requires:       %{name} >= %{version}
Obsoletes:      libKF5IncidenceEditorsng5 < %{version}
Provides:       libKF5IncidenceEditorsng5 = %{version}

%description -n libKF5IncidenceEditor5
The IncidenceEditor library for KDE PIM applications.

%package devel
Summary:        Development package for incidenceeditor
License:        LGPL-2.1-or-later
Requires:       libKF5IncidenceEditor5 = %{version}
Requires:       cmake(KChart)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5CalendarSupport)
Requires:       cmake(KF5CalendarUtils)
Requires:       cmake(KF5EventViews)
Requires:       cmake(KF5MailTransport)
Requires:       cmake(KF5Mime)

%description devel
The development package for the incidenceeditor libraries.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5IncidenceEditor5  -p /sbin/ldconfig
%postun -n libKF5IncidenceEditor5 -p /sbin/ldconfig

%files devel
%{_kf5_cmakedir}/KF5IncidenceEditor/
%{_kf5_includedir}/IncidenceEditor/
%{_kf5_libdir}/libKF5IncidenceEditor.so
%{_kf5_mkspecsdir}/qt_IncidenceEditor.pri

%files -n libKF5IncidenceEditor5
%license LICENSES/*
%{_libdir}/libKF5IncidenceEditor.so.*

%files
%{_kf5_debugdir}/incidenceeditor.categories
%{_kf5_debugdir}/incidenceeditor.renamecategories

%files lang -f %{name}.lang

%changelog
