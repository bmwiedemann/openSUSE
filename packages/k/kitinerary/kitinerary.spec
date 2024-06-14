#
# spec file for package kitinerary
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           kitinerary
Version:        24.05.1
Release:        0
Summary:        Data model and extraction system for travel reservations
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libphonenumber-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PkPass) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(ZXing)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(zlib)
Requires:       libKPim6Itinerary6 = %{version}

%description
Kitinerary is a library which provides a data model and a system to extract
information from travel reservations. The model can then be reused in other
applications.

%package -n libKPim6Itinerary6
Summary:        Data model and extraction system for travel reservations
Requires:       kitinerary >= %{version}
Obsoletes:      libKPim5Itinerary5-lang < %{version}

%description -n libKPim6Itinerary6
Kitinerary is a library which provides a data model and a system to extract
information from travel reservations. The model can then be reused in other
applications.
This package contains the kitinerary library.

%package devel
Summary:        Development files for kitinerary
Requires:       libKPim6Itinerary6 = %{version}
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}
Requires:       cmake(KF6Contacts) >= %{kf6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}
Requires:       cmake(KPim6PkPass) >= %{kpim6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the kitinerary library.

%lang_package -n libKPim6Itinerary6

%prep
%autosetup -p1

%build

%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6Itinerary6

%files
%{_kf6_debugdir}/org_kde_kitinerary.categories
%{_kf6_libexecdir}/kitinerary-extractor
%{_kf6_sharedir}/mime/packages/application-vnd-kde-itinerary.xml

%files -n libKPim6Itinerary6
%license LICENSES/*
%{_kf6_libdir}/libKPim6Itinerary.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Itinerary.*
%{_includedir}/KPim6/KItinerary/
%{_includedir}/KPim6/kitinerary/
%{_includedir}/KPim6/kitinerary_version.h
%{_kf6_cmakedir}/KPim6Itinerary/
%{_kf6_libdir}/libKPim6Itinerary.so

%files -n libKPim6Itinerary6-lang -f %{name}.lang

%changelog
