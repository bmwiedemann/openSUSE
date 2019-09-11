#
# spec file for package incidenceeditor
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
Name:           incidenceeditor
Version:        19.08.0
Release:        0
Summary:        Incidenceeditor library
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
BuildRequires:  calendarsupport-devel
BuildRequires:  eventviews-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kdiagram-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kidentitymanagement-devel
BuildRequires:  kldap-devel
BuildRequires:  kmailtransport-devel
BuildRequires:  kmime-devel
BuildRequires:  libkdepim-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This package contains the incidenceeditor library.

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
Requires:       calendarsupport-devel
Requires:       eventviews-devel
Requires:       kcalcore-devel
Requires:       kcalutils-devel
Requires:       kdiagram-devel
Requires:       kmailtransport-devel
Requires:       kmime-devel
Requires:       libKF5IncidenceEditor5 = %{version}

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
