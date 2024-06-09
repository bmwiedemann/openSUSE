#
# spec file for package kf6-prison
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


%define qt6_version 6.6.0

%define rname prison
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-prison
Version:        6.3.0
Release:        0
Summary:        Barcode abstraction layer library
License:        MIT
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(ZXing) >= 1.2.0
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)

%description
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%package imports
Summary:        Barcode abstraction layer library - QML files
Requires:       libKF6Prison6 = %{version}

%description imports
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data. This package contains
files that allow use of libprison with QtQuick based applications.

%package -n libKF6Prison6
Summary:        Barcode abstraction layer library
Requires:       kf6-prison >= %{version}
Recommends:     kf6-prison-imports

%description -n libKF6Prison6
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%package devel
Summary:        Development files Prison, a barcode abstraction library
Requires:       libKF6Prison6 = %{version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
Development files for prison, a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Prison6

%files
%{_kf6_debugdir}/prison.categories
%{_kf6_debugdir}/prison.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/prison/

%files -n libKF6Prison6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Prison.so.*
%{_kf6_libdir}/libKF6PrisonScanner.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Prison.*
%doc %{_kf6_qchdir}/KF6PrisonScanner.*
%{_kf6_cmakedir}/KF6Prison/
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so

%changelog
