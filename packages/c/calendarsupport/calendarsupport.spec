#
# spec file for package calendarsupport
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


%define lname libKPim5CalendarSupport5
%define kf5_version 5.99.0
%bcond_without released
Name:           calendarsupport
Version:        23.04.0
Release:        0
Summary:        KDE PIM calendaring support library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5AkonadiNotes)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5TextEdit)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
This package contains the calendarsupport library, used by KDE PIM applications
to handle calendaring.

%package -n %{lname}
Summary:        Library for handling calendaring in PIM applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       %{name}
# Renamed
Obsoletes:      calendarsupport-lang <= 23.04.0

%description -n %{lname}
This package contains the calendarsupport library, used by KDE PIM applications
to handle calendaring.

%package devel
Summary:        Development package for the KDEPIM Calendarsupport library
License:        LGPL-2.1-or-later
Requires:       %{lname} = %{version}
Requires:       cmake(KPim5AkonadiCalendar)
Requires:       cmake(KPim5IdentityManagement)
Requires:       cmake(KPim5Mime)
Requires:       cmake(Qt5PrintSupport)

%description devel
The development package for the calendarsupport libraries

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{lname} --with-man --all-name

%ldconfig_scriptlets -n %{lname}

%files
%{_kf5_debugdir}/calendarsupport.categories
%{_kf5_debugdir}/calendarsupport.renamecategories

%files -n %{lname}
%license LICENSES/*
%{_libdir}/libKPim5CalendarSupport.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/CalendarSupport/
%{_kf5_cmakedir}/KF5CalendarSupport/
%{_kf5_cmakedir}/KPim5CalendarSupport/
%{_kf5_libdir}/libKPim5CalendarSupport.so
%{_kf5_mkspecsdir}/qt_CalendarSupport.pri

%files -n %{lname}-lang -f %{lname}.lang

%changelog
