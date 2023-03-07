#
# spec file for package kddockwidgets
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define qt5 1
%define pkg_suffix %{nil}
%endif
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%endif
%define soversion 1_6
%define rname kddockwidgets
Name:           kddockwidgets%{pkg_suffix}
Version:        1.6.0
Release:        0
Summary:        Qt dock widget library, suitable for replacing QDockWidget
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.kdab.com/development-resources/qt-tools/kddockwidgets
Source:         https://github.com/KDAB/KDDockWidgets/releases/download/v%{version}/%{rname}-%{version}.tar.gz
Source1:        https://github.com/KDAB/KDDockWidgets/releases/download/v%{version}/%{rname}-%{version}.tar.gz.asc
Source2:        kddockwidgets.keyring
%if 0%{?qt5}
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
%if 0%{?qt6}
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Core) >= 6.2
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%endif
%if 0%{?suse_version} == 1500
# Full c++-17 support needed
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif

%description
KDDockWidgets is a Qt dock widget library written by KDAB, suitable for
replacing QDockWidget and implementing advanced functionalities missing in Qt.

Although KDDockWidgets is ready to be used out of the box, it can also be seen
as a framework to allow building very tailored custom docking systems. It tries
to expose every internal widget and every knob for the app developer to tune.

%package -n libkddockwidgets%{pkg_suffix}%{?qt6:-}%{soversion}
Summary:        Qt dock widget library, suitable for replacing QDockWidget

%description -n libkddockwidgets%{pkg_suffix}%{?qt6:-}%{soversion}
KDDockWidgets is a Qt dock widget library written by KDAB, suitable for
replacing QDockWidget and implementing advanced functionalities missing in Qt.

Although KDDockWidgets is ready to be used out of the box, it can also be seen
as a framework to allow building very tailored custom docking systems. It tries
to expose every internal widget and every knob for the app developer to tune.

%package devel
Summary:        Development files for libkddockwidgets
Requires:       libkddockwidgets%{pkg_suffix}%{?qt6:-}%{soversion} = %{version}
%if 0%{?qt5}
Requires:       cmake(Qt5X11Extras)
%endif

%description devel
Development files for libkddockwidgets

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?suse_version} == 1500
export CXX=g++-10
%endif

%if 0%{?qt5}
%cmake
%cmake_build
%endif

%if 0%{?qt6}
%cmake_qt6 -DKDDockWidgets_QT6:BOOL=ON
%{qt6_build}
%endif

%install
%if 0%{?qt5}
%cmake_install
%endif

%if 0%{?qt6}
%{qt6_install}
%endif

# Installed using %%doc and %%license instead
rm -r %{buildroot}%{_datadir}/doc

%ldconfig_scriptlets -n libkddockwidgets%{pkg_suffix}%{?qt6:-}%{soversion}

%files -n libkddockwidgets%{pkg_suffix}%{?qt6:-}%{soversion}
%license LICENSES/*
%doc README.md
%{_libdir}/libkddockwidgets%{pkg_suffix}.so.*

%files devel
%{_includedir}/kddockwidgets%{pkg_suffix}
%{_libdir}/cmake/KDDockWidgets%{pkg_suffix}/
%{_libdir}/libkddockwidgets%{pkg_suffix}.so
%if 0%{?qt5}
%{_libqt5_archdatadir}/mkspecs/modules/qt_KDDockWidgets.pri
%endif
%if 0%{?qt6}
%{_qt6_mkspecsdir}/modules/qt_KDDockWidgets.pri
%endif

%changelog
