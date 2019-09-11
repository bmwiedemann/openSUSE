#
# spec file for package eventviews
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
Name:           eventviews
Version:        19.08.0
Release:        0
Summary:        Eventviews Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-calendar-devel >= %{_kapp_version}
BuildRequires:  akonadi-server-devel
BuildRequires:  calendarsupport-devel
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kdiagram-devel
BuildRequires:  kholidays-devel
BuildRequires:  ki18n-devel
BuildRequires:  kmime-devel
BuildRequires:  libkdepim-devel >= %{_kapp_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This internal library implements a GUI framework for viewing various
calendar events in agenda, list, month view or timeline fashion.

%if %{with lang}
%lang_package
%endif

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

%package -n libKF5EventViews5
Summary:        Eventviews Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}

%description -n libKF5EventViews5
This internal library implements a GUI framework for viewing various
calendar events in agenda, list, month view or timeline fashion.

%post  -n libKF5EventViews5 -p /sbin/ldconfig
%postun -n libKF5EventViews5 -p /sbin/ldconfig

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       akonadi-calendar-devel
Requires:       akonadi-server-devel
Requires:       calendarsupport-devel
Requires:       kcalcore-devel
Requires:       kcalutils-devel
Requires:       libKF5EventViews5 = %{version}

%description devel
The development package for the eventviews libraries

%files
%license COPYING*
%{_kf5_debugdir}/eventviews.categories
%{_kf5_debugdir}/eventviews.renamecategories
%{_kf5_servicetypesdir}/calendardecoration.desktop

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5EventViews/
%{_kf5_includedir}/EventViews/
%{_kf5_includedir}/eventviews/
%{_kf5_includedir}/eventviews_version.h
%{_kf5_libdir}/libKF5EventViews.so
%{_kf5_mkspecsdir}/qt_EventViews.pri

%files -n libKF5EventViews5
%{_kf5_libdir}/libKF5EventViews.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
