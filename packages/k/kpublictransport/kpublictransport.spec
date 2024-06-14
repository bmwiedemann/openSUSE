#
# spec file for package kpublictransport
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

%bcond_without released
Name:           kpublictransport
Version:        24.05.1
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
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)

%description
A library for access realtime public transport data and for performing public
ransport journey queries.

%package imports
Summary:        QML Imports for using kpublictransport

%description imports
A library for access realtime public transport data and for performing public
ransport journey queries. QML imports.

%package -n libKPublicTransport1
Summary:        Library for querying public transport data
Requires:       kpublictransport >= %{version}

%description -n libKPublicTransport1
A library for access realtime public transport data and for performing public
ransport journey queries.

%package -n libKPublicTransportOnboard1
Summary:        Library for querying public transport data onboard trains
Requires:       libKPublicTransport1 = %{version}

%description -n libKPublicTransportOnboard1
A library for access realtime public transport data and for performing public
transport journey queries. This package contains a library to determine 
the presence onboard of a train using WiFi SSIDs and provide journey 
details.

%package devel
Summary:        Library for querying public transport data
Requires:       libKPublicTransport1 = %{version}
Requires:       libKPublicTransportOnboard1 = %{version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       pkgconfig(zlib)

%description devel
A library for access realtime public transport data and for performing public
ransport journey queries.Development files.

%prep
%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_TESTING:BOOL=TRUE \
  -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%check
%ctest

%ldconfig_scriptlets -n libKPublicTransport1
%ldconfig_scriptlets -n libKPublicTransportOnboard1

%files
%{_kf6_debugdir}/org_kde_kpublictransport.categories
%{_kf6_debugdir}/org_kde_kpublictransport_onboard.categories

%files imports
%{_kf6_qmldir}/org/kde/kpublictransport/

%files -n libKPublicTransport1
%license LICENSES/*
%{_kf6_libdir}/libKPublicTransport.so.*

%files -n libKPublicTransportOnboard1
%{_kf6_libdir}/libKPublicTransportOnboard.so.*

%files devel
%doc %{_kf6_qchdir}/KPublicTransport.*
%{_includedir}/KPublicTransport/
%{_kf6_cmakedir}/KPublicTransport/
%{_kf6_libdir}/libKPublicTransport.so
%{_kf6_libdir}/libKPublicTransportOnboard.so

%changelog
