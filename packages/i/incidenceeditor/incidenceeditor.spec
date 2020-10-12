#
# spec file for package incidenceeditor
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           incidenceeditor
Version:        20.08.2
Release:        0
Summary:        Incidenceeditor library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kdepim-apps-libs-devel
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
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains the incidenceeditor library.

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

%package -n libKF5IncidenceEditor5
Summary:        Incidenceeditor Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}
Obsoletes:      libKF5IncidenceEditorsng5 < %{version}
Provides:       libKF5IncidenceEditorsng5 = %{version}

%description -n libKF5IncidenceEditor5
The IncidenceEditor library for kdepim

%post -n libKF5IncidenceEditor5  -p /sbin/ldconfig
%postun -n libKF5IncidenceEditor5 -p /sbin/ldconfig

%package devel
Summary:        Development package for incidenceeditor
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5IncidenceEditor5 = %{version}
Requires:       cmake(KChart)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5CalendarSupport)
Requires:       cmake(KF5CalendarUtils)
Requires:       cmake(KF5EventViews)
Requires:       cmake(KF5MailTransport)
Requires:       cmake(KF5Mime)

%description devel
The development package for the incidenceeditor libraries

%files devel
%license COPYING*
%{_kf5_includedir}/IncidenceEditor/
%{_kf5_includedir}/incidenceeditor/
%{_kf5_includedir}/incidenceeditor_version.h
%{_kf5_cmakedir}/KF5IncidenceEditor/
%{_kf5_libdir}/libKF5IncidenceEditor.so
%{_kf5_mkspecsdir}/qt_IncidenceEditor.pri

%files -n libKF5IncidenceEditor5
%license COPYING*
%{_libdir}/libKF5IncidenceEditor.so.*

%files
%license COPYING*
%{_kf5_debugdir}/incidenceeditor.categories
%{_kf5_debugdir}/incidenceeditor.renamecategories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
