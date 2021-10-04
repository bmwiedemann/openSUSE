#
# spec file for package qt6-location
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


%define real_version 6.2.0
%define short_version 6.2
%define tar_name qtlocation-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-location%{?pkg_suffix}
Version:        6.2.0
Release:        0
Summary:        Qt 6 Location plugins and libraries
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-location-rpmlintrc
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt Location API helps creating mapping solutions using the data available
from some of the popular location services.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Location QML files and plugins

%description imports
QML files and plugins from the Qt 6 Location module.

%package -n libQt6Positioning6
Summary:        Qt 6 Positioning library

%description -n libQt6Positioning6
The Qt 6 Positioning library.

%package -n qt6-positioning-devel
Summary:        Qt 6 Positioning library - Development files
Requires:       libQt6Positioning6 = %{version}

%description -n qt6-positioning-devel
Development files for the Qt 6 Positioning library.

%package -n qt6-positioning-private-devel
Summary:        Non-ABI stable API for the Qt 6 Positioning Library
Requires:       cmake(Qt6Positioning) = %{real_version}

%description -n qt6-positioning-private-devel
This package provides private headers of libQt6Positioning that do not have any
ABI or API guarantees.

%package -n libQt6PositioningQuick6
Summary:        Qt 6 PositioningQuick library

%description -n libQt6PositioningQuick6
The Qt 6 PositioningQuick library.

%package -n qt6-positioningquick-devel
Summary:        Qt 6 PositioningQuick library - Development files
Requires:       libQt6PositioningQuick6 = %{version}

%description -n qt6-positioningquick-devel
Development files for the Qt 6 PositioningQuick library.

%package -n qt6-positioningquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 PositioningQuick Library
Requires:       cmake(Qt6PositioningQuick) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-qml-private-devel
%requires_eq    qt6-quick-private-devel

%description -n qt6-positioningquick-private-devel
This package provides private headers of libQt6PositioningQuick that do not have any
ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# CMake files are not needed for plugins
rm %{buildroot}%{_qt6_cmakedir}/Qt6Positioning/Qt6QGeoPositionInfoSourceFactory*.cmake
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

# and also not for static plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Bundled_Clip2Tri

%post -n libQt6Positioning6 -p /sbin/ldconfig
%post -n libQt6PositioningQuick6 -p /sbin/ldconfig
%postun -n libQt6Positioning6 -p /sbin/ldconfig
%postun -n libQt6PositioningQuick6 -p /sbin/ldconfig

%files
%dir %{_qt6_pluginsdir}/position
%{_qt6_pluginsdir}/position/libqtposition_geoclue2.so
%{_qt6_pluginsdir}/position/libqtposition_positionpoll.so
%{_qt6_pluginsdir}/position/libqtposition_nmea.so

%files imports
%{_qt6_qmldir}/QtPositioning/

%files -n libQt6Positioning6
%license LICENSE.*
%{_qt6_libdir}/libQt6Positioning.so.*

%files -n qt6-positioning-devel
%dir %{_qt6_cmakedir}/Qt6
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLocationTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Positioning/
%{_qt6_cmakedir}/Qt6/FindGconf.cmake
%{_qt6_cmakedir}/Qt6/FindGypsy.cmake
%{_qt6_descriptionsdir}/Positioning.json
%{_qt6_includedir}/QtPositioning/
%{_qt6_libdir}/libQt6Positioning.prl
%{_qt6_libdir}/libQt6Positioning.so
%{_qt6_metatypesdir}/qt6positioning_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_positioning.pri
%exclude %{_qt6_includedir}/QtPositioning/%{real_version}

%files -n qt6-positioning-private-devel
%{_qt6_includedir}/QtPositioning/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_positioning_private.pri

%files -n libQt6PositioningQuick6
%{_qt6_libdir}/libQt6PositioningQuick.so.*

%files -n qt6-positioningquick-devel
%{_qt6_cmakedir}/Qt6PositioningQuick/
%{_qt6_descriptionsdir}/PositioningQuick.json
%{_qt6_includedir}/QtPositioningQuick/
%{_qt6_libdir}/libQt6PositioningQuick.prl
%{_qt6_libdir}/libQt6PositioningQuick.so
%{_qt6_metatypesdir}/qt6positioningquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_positioningquick.pri
%exclude %{_qt6_includedir}/QtPositioningQuick/%{real_version}

%files -n qt6-positioningquick-private-devel
%{_qt6_includedir}/QtPositioningQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_positioningquick_private.pri

%endif

%changelog
