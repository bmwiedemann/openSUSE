#
# spec file for package calendarsupport
#
# Copyright (c) 2020 SUSE LLC
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


%define lname libKF5CalendarSupport5
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           calendarsupport
Version:        20.08.2
Release:        0
Summary:        KDE PIM calendaring support library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(Qt5PrintSupport) >= 5.10.0
BuildRequires:  cmake(Qt5Test) >= 5.10.0
BuildRequires:  cmake(Qt5UiTools) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains the calendarsupport library, used by KDE PIM applications to handle calendaring.

%package -n %{lname}
Summary:        Library for handling calendaring in PIM applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}

%description -n %{lname}
This package contains the calendarsupport library, used by KDE PIM applications to handle calendaring.

%package devel
Summary:        Development package for the KDEPIM Calendarsupport library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       cmake(KF5AkonadiCalendar)
Requires:       cmake(KF5IdentityManagement)
Requires:       cmake(KF5Mime)
Requires:       cmake(Qt5PrintSupport) >= 5.10.0

%description devel
The development package for the calendarsupport libraries

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post -n %{lname}  -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%{_kf5_debugdir}/calendarsupport.categories
%{_kf5_debugdir}/calendarsupport.renamecategories
%{_kf5_servicetypesdir}/calendarplugin.desktop

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5CalendarSupport/
%{_kf5_includedir}/CalendarSupport/
%{_kf5_includedir}/calendarsupport/
%{_kf5_includedir}/calendarsupport_version.h
%{_kf5_libdir}/libKF5CalendarSupport.so
%{_kf5_mkspecsdir}/qt_CalendarSupport.pri

%files -n %{lname}
%{_libdir}/libKF5CalendarSupport.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
