#
# spec file for package qt6-location
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
%define tar_name qtlocation-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-location%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 Location plugins and libraries
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-location-rpmlintrc
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-positioning-private-devel
BuildRequires:  qt6-positioningquick-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6QuickShapesPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Positioning) = %{real_version}
BuildRequires:  cmake(Qt6PositioningQuick) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}
BuildRequires:  cmake(Qt6Test) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt Location API helps creating mapping solutions using the data available
from some of the popular location services.

%if !%{qt6_docs_flavor}

%package -n libQt6Location6
Summary:        Qt 6 Location library

%description -n libQt6Location6
The Qt 6 Location library.

%package -n qt6-location-devel
Summary:        Qt 6 Location library - Development files
Requires:       libQt6Location6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Positioning) = %{real_version}
Requires:       cmake(Qt6PositioningQuick) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickShapesPrivate) = %{real_version}

%description -n qt6-location-devel
Development files for the Qt 6 Location library.

%package -n qt6-location-private-devel
Summary:        Non-ABI stable API for the Qt 6 Location Library
Requires:       cmake(Qt6Location) = %{real_version}

%description -n qt6-location-private-devel
This package provides private headers of libQt6Location that do not have any
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
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/Qt6Location/*Plugin*.cmake

%ldconfig_scriptlets -n libQt6Location6

%files
%dir %{_qt6_pluginsdir}/geoservices
%{_qt6_pluginsdir}/geoservices/libqtgeoservices_itemsoverlay.so
%{_qt6_pluginsdir}/geoservices/libqtgeoservices_osm.so
%{_qt6_qmldir}/QtLocation/

%files -n libQt6Location6
%license LICENSE.*
%{_qt6_libdir}/libQt6Location.so.*

%files -n qt6-location-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLocationTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Location/
%{_qt6_descriptionsdir}/Location.json
%{_qt6_includedir}/QtLocation/
%{_qt6_libdir}/libQt6Location.prl
%{_qt6_libdir}/libQt6Location.so
%{_qt6_metatypesdir}/qt6location_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_location.pri
%{_qt6_pkgconfigdir}/Qt6Location.pc
%exclude %{_qt6_includedir}/QtLocation/%{real_version}

%files -n qt6-location-private-devel
%{_qt6_includedir}/QtLocation/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_location_private.pri

%endif

%changelog
