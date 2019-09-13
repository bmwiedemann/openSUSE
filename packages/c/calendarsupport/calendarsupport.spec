#
# spec file for package calendarsupport
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


%define lname libKF5CalendarSupport5
%define kf5_version 5.58.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           calendarsupport
Version:        19.08.1
Release:        0
Summary:        KDE PIM calendaring support library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-calendar-devel
BuildRequires:  akonadi-mime-devel >= %{_kapp_version}
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kguiaddons-devel
BuildRequires:  kholidays-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kidentitymanagement-devel
BuildRequires:  kio-devel
BuildRequires:  kmime-devel
BuildRequires:  pimcommon-devel
BuildRequires:  cmake(Qt5PrintSupport) >= 5.10.0
BuildRequires:  cmake(Qt5Test) >= 5.10.0
BuildRequires:  cmake(Qt5UiTools) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
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
Requires:       akonadi-calendar-devel >= %{_kapp_version}
Requires:       kidentitymanagement-devel >= %{_kapp_version}
Requires:       kmime-devel >= %{_kapp_version}
Requires:       cmake(Qt5PrintSupport) >= 5.10.0

%description devel
The development package for the calendarsupport libraries

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build

%make_jobs

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
