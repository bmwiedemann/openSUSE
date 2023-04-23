#
# spec file for package kpublictransport
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


%global sover   1
%global lname   libKPublicTransport%{sover}
%bcond_without released
Name:           kpublictransport
Version:        23.04.0
Release:        0
Summary:        QML imports for querying public transport data
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(zlib)
Requires:       %{lname} = %{version}
Requires:       libKPublicTransportOnboard%{sover} = %{version}

%description
A library for access realtime public transport data and for performing public
ransport journey queries. QML imports.

%package -n %{lname}
Summary:        Library for querying public transport data

%description -n %{lname}
A library for access realtime public transport data and for performing public
ransport journey queries.

%package -n libKPublicTransportOnboard%{sover}
Summary:        Library for querying public transport data onboard trains
Requires:       %{lname} = %{version}

%description -n libKPublicTransportOnboard%{sover}
A library for access realtime public transport data and for performing public
transport journey queries. This package contains a library to determine 
the presence onboard of a train using WiFi SSIDs and provide journey 
details.

%package devel
Summary:        Library for querying public transport data
Requires:       %{lname} = %{version}
Requires:       libKPublicTransportOnboard%{sover} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Gui)
Requires:       pkgconfig(zlib)

%description devel
A library for access realtime public transport data and for performing public
ransport journey queries.Development files.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%check
%ctest

%ldconfig_scriptlets -n %{lname}
%ldconfig_scriptlets -n libKPublicTransportOnboard%{sover}

%files
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kpublictransport/

%files -n %{lname}
%license LICENSES/*
%{_kf5_debugdir}/org_kde_kpublictransport.categories
%{_kf5_libdir}/libKPublicTransport.so.*

%files -n libKPublicTransportOnboard%{sover}
%{_kf5_libdir}/libKPublicTransportOnboard.so.*
%{_kf5_debugdir}/org_kde_kpublictransport_onboard.categories

%files devel
%{_includedir}/KPublicTransport/
%{_kf5_cmakedir}/KPublicTransport/
%{_kf5_libdir}/libKPublicTransport.so
%{_kf5_libdir}/libKPublicTransportOnboard.so

%changelog
