#
# spec file for package kpkpass
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


%bcond_without released
Name:           kpkpass
Version:        22.12.1
Release:        0
Summary:        Library to parse Passbook files
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)

%description
kpkpass is a library to read and parse Apple Passbook files, such as the ones
commonly used for hotel and flight reservations.

%package -n libKPimPkPass5
Summary:        Library to parse Passbook files
%if %{pkg_vcmp shared-mime-info < 2.2}
Requires:       %{name}
%endif

%description -n libKPimPkPass5
kpkpass is a library to read and parse Apple Passbook files, such as the ones
commonly used for hotel and flight reservations. This package contains the
library itself.

%package devel
Summary:        Development files for kpkpass
Requires:       libKPimPkPass5 = %{version}
Requires:       cmake(KF5Archive)

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the kpkpass library.

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%post -n libKPimPkPass5 -p /sbin/ldconfig
%postun -n libKPimPkPass5 -p /sbin/ldconfig

%if %{pkg_vcmp shared-mime-info < 2.2}
%files
%{_datadir}/mime/packages/application-vnd-apple-pkpass.xml
%endif

%files -n libKPimPkPass5
%license LICENSES/*
%{_kf5_libdir}/libKPimPkPass.so.*
%{_kf5_debugdir}/*.categories

%files devel
%dir %{_includedir}/KPim/
%{_includedir}/KPim/KPkPass/
%{_kf5_cmakedir}/KPimPkPass/
%{_kf5_libdir}/libKPimPkPass.so

%changelog
