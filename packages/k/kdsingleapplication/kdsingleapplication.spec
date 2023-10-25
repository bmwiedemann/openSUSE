#
# spec file for package kdsingleapplication
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


%global rname  kdsingleapplication
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%endif
Name:           kdsingleapplication%{?pkg_suffix}
Version:        1.0.0
Release:        0
Summary:        Helper class for single-instance policy applications
License:        MIT
URL:            https://github.com/KDAB/KDSingleApplication
Source0:        https://github.com/KDAB/KDSingleApplication/releases/download/v%{version}/%{rname}-%{version}.tar.gz
Source1:        https://github.com/KDAB/KDSingleApplication/releases/download/v%{version}/%{rname}-%{version}.tar.gz.asc
Source2:        kdab.keyring
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
%endif

%description
KDSingleApplication is a helper class for single-instance policy applications.

%package -n libkdsingleapplication%{?pkg_suffix}
Summary:        Helper class for single-instance policy applications

%description -n libkdsingleapplication%{?pkg_suffix}
KDSingleApplication is a helper class for single-instance policy applications.

%package devel
Summary:        Development files for libkdsingleapplication%{?pkg_suffix}
Requires:       libkdsingleapplication%{?pkg_suffix} = %{version}
%if 0%{?qt6}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)
%else
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Widgets)
%endif

%description devel
Development files for libkdsingleapplication%{?pkg_suffix}.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_qt6 \
  -DKDSingleApplication_QT6:BOOL=TRUE \
  -DKDSingleApplication_TESTS:BOOL=TRUE

%qt6_build
%else
%cmake -DKDSingleApplication_TESTS:BOOL=TRUE

%cmake_build
%endif

%install
%if 0%{?qt6}
%qt6_install
%else
%cmake_install
%endif

# Packaged using %%license and %%doc
rm -r %{buildroot}%{_datadir}/doc

%check
%ctest

%ldconfig_scriptlets -n libkdsingleapplication%{?pkg_suffix}

%files -n libkdsingleapplication%{?pkg_suffix}
%license LICENSES/*
%doc README.md
%{_libdir}/libkdsingleapplication%{?pkg_suffix}.so

%files devel
%{_includedir}/kdsingleapplication%{?pkg_suffix}/
%{_libdir}/cmake/KDSingleApplication%{?pkg_suffix}/
%if 0%{?qt6}
%{_qt6_mkspecsdir}/modules/qt_KDSingleApplication.pri
%else
%{_libqt5_archdatadir}/mkspecs/modules/qt_KDSingleApplication.pri
%endif

%changelog
