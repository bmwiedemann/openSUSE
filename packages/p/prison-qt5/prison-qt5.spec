#
# spec file for package prison-qt5
#
# Copyright (c) 2021 SUSE LLC
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


%define sonum   5
%define rname prison
%define _libname KF5Prison
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           prison-qt5
Version:        5.101.0
Release:        0
Summary:        Barcode abstraction layer library
License:        MIT
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(ZXing) >= 1.2.0
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)

%description
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%package imports
Summary:        Barcode abstraction layer library - QML files
Requires:       lib%{_libname}%{sonum} = %{version}

%description imports
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data. This package contains
files that allow use of libprison with QtQuick based applications.

%package -n lib%{_libname}%{sonum}
Summary:        Barcode abstraction layer library
Recommends:     %{name}-imports

%description -n lib%{_libname}%{sonum}
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%package -n prison-qt5-devel
Summary:        Development files for prison-qt5, a barcode abstraction library
Requires:       lib%{_libname}%{sonum} = %{version}
Requires:       cmake(Qt5Gui) >= 5.15.0

%description -n prison-qt5-devel
Development files for prison, a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%post -n lib%{_libname}%{sonum} -p /sbin/ldconfig
%postun -n lib%{_libname}%{sonum} -p /sbin/ldconfig

%files -n lib%{_libname}%{sonum}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_libqt5_libdir}/lib%{_libname}*.so.*

%files imports
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/prison/
%{_kf5_qmldir}/org/kde/prison/libprisonquickplugin.so
%{_kf5_qmldir}/org/kde/prison/qmldir

%files -n prison-qt5-devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Prison/
%{_kf5_mkspecsdir}/qt_Prison.pri
%{_libqt5_libdir}/lib%{_libname}*.so

%changelog
