#
# spec file for package incidenceeditor
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
%define libname libKPim5IncidenceEditor5
Name:           incidenceeditor
Version:        23.04.0
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
BuildRequires:  cmake(KGantt)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5EventViews)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransportAkonadi)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
This package contains the incidenceeditor library.

%package -n %{libname}
Summary:        Incidenceeditor Library
License:        LGPL-2.1-or-later
Requires:       incidenceeditor >= %{version}
# Renamed
Obsoletes:      incidenceeditor-lang <= 23.04.0

%description -n %{libname}
The IncidenceEditor library for KDE PIM applications.

%package devel
Summary:        Development package for incidenceeditor
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}
Requires:       cmake(KChart)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KPim5CalendarSupport)
Requires:       cmake(KPim5CalendarUtils)
Requires:       cmake(KPim5EventViews)
Requires:       cmake(KPim5MailTransportAkonadi)
Requires:       cmake(KPim5Mime)

%description devel
The development package for the incidenceeditor libraries.

%lang_package -n %{libname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%{_kf5_debugdir}/incidenceeditor.categories
%{_kf5_debugdir}/incidenceeditor.renamecategories

%files -n %{libname}
%license LICENSES/*
%{_libdir}/libKPim5IncidenceEditor.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/IncidenceEditor/
%{_kf5_cmakedir}/KF5IncidenceEditor/
%{_kf5_cmakedir}/KPim5IncidenceEditor/
%{_kf5_libdir}/libKPim5IncidenceEditor.so
%{_kf5_mkspecsdir}/qt_IncidenceEditor.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
