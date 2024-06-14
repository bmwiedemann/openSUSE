#
# spec file for package kpkpass
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
Name:           kpkpass
Version:        24.05.1
Release:        0
Summary:        Library to parse Passbook files
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
kpkpass is a library to read and parse Apple Passbook files, such as the ones
commonly used for hotel and flight reservations.

%package -n libKPim6PkPass6
Summary:        Library to parse Passbook files
Requires:       kpkpass >= %{version}

%description -n libKPim6PkPass6
kpkpass is a library to read and parse Apple Passbook files, such as the ones
commonly used for hotel and flight reservations. This package contains the
library itself.

%package devel
Summary:        Development files for kpkpass
Requires:       libKPim6PkPass6 = %{version}
Requires:       cmake(KF6Archive) >= %{kf6_version}

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the kpkpass library.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKPim6PkPass6

%files
%if %{pkg_vcmp shared-mime-info < 2.2}
%{_datadir}/mime/packages/application-vnd-apple-pkpass.xml
%endif
%{_kf6_debugdir}/org_kde_kpkpass.categories

%files -n libKPim6PkPass6
%license LICENSES/*
%{_kf6_libdir}/libKPim6PkPass.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6PkPass.*
%{_includedir}/KPim6/KPkPass/
%{_kf6_cmakedir}/KPim6PkPass/
%{_kf6_libdir}/libKPim6PkPass.so

%changelog
