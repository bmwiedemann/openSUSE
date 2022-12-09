#
# spec file for package kpublictransport
#
# Copyright (c) 2022 SUSE LLC
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
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kpublictransport
Version:        22.12.0
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
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(zlib)
Requires:       %{lname} = %{version}

%description
A library for access realtime public transport data and for performing public
ransport journey queries. QML imports.

%package -n %{lname}
Summary:        Library for querying public transport data

%description -n %{lname}
A library for access realtime public transport data and for performing public
ransport journey queries.

%package devel
Summary:        Library for querying public transport data
Requires:       %{lname} = %{version}
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

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kpublictransport/

%files -n %{lname}
%license LICENSES/*
%{_kf5_debugdir}/org_kde_kpublictransport.categories
%{_kf5_libdir}/libKPublicTransport.so.*

%files devel
%{_includedir}/KPublicTransport/
%{_kf5_libdir}/cmake/KPublicTransport/
%{_kf5_libdir}/libKPublicTransport.so

%changelog
