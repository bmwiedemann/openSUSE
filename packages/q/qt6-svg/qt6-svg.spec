#
# spec file for package qt6-svg
#
# Copyright (c) 2025 SUSE LLC
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


%define real_version 6.9.1
%define short_version 6.9
%define tar_name qtsvg-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-svg%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        Classes for rendering and displaying SVG drawings
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-svg-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6GuiPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  cmake(Qt6WidgetsPrivate) = %{real_version}
BuildRequires:  pkgconfig(zlib)
# Ignored: only used for building tests
# BuildRequires:  cmake(Qt6Xml)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt SVG module provides classes for rendering and displaying SVG drawings
in widgets and on other paint devices.

%if !%{qt6_docs_flavor}

%package -n libQt6Svg6
Summary:        Qt 6 Svg library

%description -n libQt6Svg6
The Qt 6 Svg library.

%package -n libQt6SvgWidgets6
Summary:        Qt 6 SVGWidgets library

%description -n libQt6SvgWidgets6
The Qt 6 SvgWidgets library.

%package devel
Summary:        Qt 6 SVG libraries - Development files
Requires:       libQt6Svg6 = %{version}
Requires:       libQt6SvgWidgets6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description devel
Development files for the Qt 6 SVG libraries.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 SVG libraries
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Svg) = %{real_version}
Requires:       cmake(Qt6SvgWidgets) = %{real_version}
Requires:       cmake(Qt6WidgetsPrivate) = %{real_version}

%description private-devel
This package provides private headers of libQt6Svg that do not have any
ABI or API guarantees.

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# No private headers for Qt6SvgWidgets
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_svgwidgets_private.pri

%ldconfig_scriptlets -n libQt6Svg6
%ldconfig_scriptlets -n libQt6SvgWidgets6

%files -n libQt6Svg6
%license LICENSES/*
%dir %{_qt6_pluginsdir}/iconengines
%dir %{_qt6_pluginsdir}/imageformats
%{_qt6_pluginsdir}/iconengines/libqsvgicon.so
%{_qt6_pluginsdir}/imageformats/libqsvg.so
%{_qt6_libdir}/libQt6Svg.so.*

%files -n libQt6SvgWidgets6
%{_qt6_libdir}/libQt6SvgWidgets.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Gui/*
%{_qt6_cmakedir}/Qt6Svg/
%{_qt6_cmakedir}/Qt6SvgWidgets/
%{_qt6_descriptionsdir}/Svg.json
%{_qt6_descriptionsdir}/SvgWidgets.json
%{_qt6_includedir}/QtSvg/
%{_qt6_includedir}/QtSvgWidgets/
%{_qt6_libdir}/libQt6Svg.prl
%{_qt6_libdir}/libQt6Svg.so
%{_qt6_libdir}/libQt6SvgWidgets.prl
%{_qt6_libdir}/libQt6SvgWidgets.so
%{_qt6_metatypesdir}/qt6svg_*_metatypes.json
%{_qt6_metatypesdir}/qt6svgwidgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_svg.pri
%{_qt6_mkspecsdir}/modules/qt_lib_svgwidgets.pri
%{_qt6_pkgconfigdir}/Qt6Svg.pc
%{_qt6_pkgconfigdir}/Qt6SvgWidgets.pc
%exclude %{_qt6_includedir}/QtSvg/%{real_version}/

%files private-devel
%{_qt6_cmakedir}/Qt6SvgPrivate/
%{_qt6_cmakedir}/Qt6SvgWidgetsPrivate/
%dir %{_qt6_includedir}/QtSvg/
%{_qt6_includedir}/QtSvg/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_svg_private.pri

%endif

%changelog
