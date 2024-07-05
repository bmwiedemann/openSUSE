#
# spec file for package calendarsupport
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           calendarsupport
Version:        24.05.2
Release:        0
Summary:        KDE PIM calendaring support library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiNotes) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This package contains the calendarsupport library, used by KDE PIM applications
to handle calendaring.

%package -n libKPim6CalendarSupport6
Summary:        Library for handling calendaring in PIM applications
Requires:       calendarsupport >= %{version}
Obsoletes:      calendarsupport-lang <= 23.04.0
Obsoletes:      libKF5CalendarSupport5 < %{version}
Obsoletes:      libKPim5CalendarSupport5 < %{version}
Obsoletes:      libKPim5CalendarSupport5-lang < %{version}

%description -n libKPim6CalendarSupport6
This package contains the calendarsupport library, used by KDE PIM applications
to handle calendaring.

%package devel
Summary:        Development package for the KDEPIM Calendarsupport library
Requires:       libKPim6CalendarSupport6 = %{version}
Requires:       cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
Requires:       cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}
Requires:       cmake(Qt6PrintSupport) >= %{qt6_version}

%description devel
The development package for the calendarsupport libraries

%lang_package -n libKPim6CalendarSupport6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6CalendarSupport6 --all-name

%ldconfig_scriptlets -n libKPim6CalendarSupport6

%files
%{_kf6_debugdir}/calendarsupport.categories
%{_kf6_debugdir}/calendarsupport.renamecategories

%files -n libKPim6CalendarSupport6
%license LICENSES/*
%{_libdir}/libKPim6CalendarSupport.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6CalendarSupport.*
%{_includedir}/KPim6/CalendarSupport/
%{_kf6_cmakedir}/KPim6CalendarSupport/
%{_kf6_libdir}/libKPim6CalendarSupport.so

%files -n libKPim6CalendarSupport6-lang -f libKPim6CalendarSupport6.lang

%changelog
