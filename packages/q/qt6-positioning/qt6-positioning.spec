#
# spec file for package qt6-positioning
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


%define real_version 6.7.2
%define short_version 6.7
%define tar_name qtpositioning-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-positioning%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 Positioning plugins and libraries
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-positioning-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6DBus) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6SerialPort) = %{real_version}
BuildRequires:  cmake(Qt6Svg) = %{real_version}
BuildRequires:  cmake(Qt6Test) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%else
# These plugins were in qt6-location before
Provides:       qt6-location = 6.2.2
Obsoletes:      qt6-location < 6.2.2
%endif

%description
The Qt Positioning API provides positioning information via QML and C++ interfaces.

%if %{qt6_docs_flavor}
# qtpositioning and qtlocation were split in 6.2.2.
# 'Conflicts' are needed, we can't use the %%qt6_doc_packages and
# %%qt6_examples_package macros.
%package -n qt6-positioning-docs-html
Summary:        Documentation for qt6-positioning in HTML format
License:        GFDL-1.3-or-later
Provides:       qt6-location-docs-html = 6.2.2
Obsoletes:      qt6-location-docs-html < 6.2.2

%description -n qt6-positioning-docs-html
This package contains documentation for qt6-positioning in HTML format.

%package -n qt6-positioning-docs-qch
Summary:        Documentation for qt6-positioning in QCH format
License:        GFDL-1.3-or-later
Provides:       qt6-location-docs-qch = 6.2.2
Obsoletes:      qt6-location-docs-qch < 6.2.2

%description -n qt6-positioning-docs-qch
This package contains documentation for qt6-positioning in QCH format.

%else

%package examples
Summary:        Examples for the qt6-positioning module
Provides:       qt6-location-examples = 6.2.2
Obsoletes:      qt6-location-examples < 6.2.2

%description examples
Examples for the qt6-positioning module.

%package imports
Summary:        Qt 6 Positioning QML files and plugins
Provides:       qt6-location-imports = 6.2.2
Obsoletes:      qt6-location-imports < 6.2.2

%description imports
QML files and plugins from the Qt 6 Positioning module.

%package -n libQt6Positioning6
Summary:        Qt 6 Positioning library

%description -n libQt6Positioning6
The Qt 6 Positioning library.

%package -n qt6-positioning-devel
Summary:        Qt 6 Positioning library - Development files
Requires:       libQt6Positioning6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

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
Requires:       cmake(Qt6Positioning) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}

%description -n qt6-positioningquick-devel
Development files for the Qt 6 PositioningQuick library.

%package -n qt6-positioningquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 PositioningQuick Library
Requires:       qt6-positioning-private-devel = %{version}
Requires:       cmake(Qt6PositioningQuick) = %{real_version}
%requires_eq    qt6-quick-private-devel

%description -n qt6-positioningquick-private-devel
This package provides private headers of libQt6PositioningQuick that do not have any
ABI or API guarantees.

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

%ldconfig_scriptlets -n libQt6Positioning6
%ldconfig_scriptlets -n libQt6PositioningQuick6

%files
%dir %{_qt6_pluginsdir}/position
%{_qt6_pluginsdir}/position/libqtposition_geoclue2.so
%{_qt6_pluginsdir}/position/libqtposition_positionpoll.so
%{_qt6_pluginsdir}/position/libqtposition_nmea.so

%files examples
%{_qt6_examplesdir}/*

%files imports
%{_qt6_qmldir}/QtPositioning/

%files -n libQt6Positioning6
%license LICENSES/*
%{_qt6_libdir}/libQt6Positioning.so.*

%files -n qt6-positioning-devel
%dir %{_qt6_cmakedir}/Qt6
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Positioning/
%{_qt6_cmakedir}/Qt6/FindGconf.cmake
%{_qt6_cmakedir}/Qt6/FindGypsy.cmake
%{_qt6_descriptionsdir}/Positioning.json
%{_qt6_includedir}/QtPositioning/
%{_qt6_libdir}/libQt6Positioning.prl
%{_qt6_libdir}/libQt6Positioning.so
%{_qt6_metatypesdir}/qt6positioning_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_positioning.pri
%{_qt6_pkgconfigdir}/Qt6Positioning.pc
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
%{_qt6_pkgconfigdir}/Qt6PositioningQuick.pc
%exclude %{_qt6_includedir}/QtPositioningQuick/%{real_version}

%files -n qt6-positioningquick-private-devel
%{_qt6_includedir}/QtPositioningQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_positioningquick_private.pri

%else

%pre -n qt6-positioning-docs-qch -f qch.pre

%files -n qt6-positioning-docs-html
%dir %{_qt6_docdir}
%{_qt6_docdir}/*
%exclude %{_qt6_docdir}/*.qch

%files -n qt6-positioning-docs-qch
%dir %{_qt6_docdir}
%{_qt6_docdir}/*.qch

%endif

%changelog
