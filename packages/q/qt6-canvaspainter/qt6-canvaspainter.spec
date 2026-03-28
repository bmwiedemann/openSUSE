#
# spec file for package qt6-canvaspainter
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define real_version 6.11.0
%define short_version 6.11
%define short_name qtcanvaspainter
%define tar_name qtcanvaspainter-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
# Private QML imports
%global __requires_exclude qt6qmlimport\\(GalleryExample\\)
#
Name:           qt6-canvaspainter%{?pkg_suffix}
Version:        6.11.0
Release:        0
Summary:        Accelerated 2D painting solution for Qt Quick and QRhi-based render targets
License:        GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6DBusPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6GuiPrivate) = %{real_version}
BuildRequires:  cmake(Qt6NetworkPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickPrivate) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}
BuildRequires:  cmake(Qt6ShaderToolsPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  cmake(Qt6WidgetsPrivate) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Accelerated 2D painting solution for Qt Quick and QRhi-based render targets.

%if !%{qt6_docs_flavor}

%package -n libQt6CanvasPainter6
Summary:        Qt 6 CanvasPainter library

%description -n libQt6CanvasPainter6
Accelerated 2D painting solution for Qt Quick and QRhi-based render targets.

%package devel
Summary:        Qt 6 CanvasPainter library - Development files
Requires:       libQt6CanvasPainter6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description devel
Development files for the Qt 6 CanvasPainter library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 CanvasPainter Library
Requires:       cmake(Qt6CanvasPainter) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}

%description private-devel
This package provides private headers of libQt6CanvasPainter that do not have
any ABI or API guarantees.

%{qt6_examples_package}

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

# FIXME ? Needed ?
# %%qt6_link_executables

%ldconfig_scriptlets -n libQt6CanvasPainter6

%files -n libQt6CanvasPainter6
%license LICENSES/*
%{_qt6_libdir}/libQt6CanvasPainter.so.*

%files devel
%{_qt6_bindir}/qcshadergen
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtCanvasPainterTestsConfig.cmake
%{_qt6_cmakedir}/Qt6CanvasPainter/
%{_qt6_cmakedir}/Qt6CanvasPainterTools/
%{_qt6_descriptionsdir}/CanvasPainter.json
%{_qt6_includedir}/QtCanvasPainter/
%{_qt6_libdir}/libQt6CanvasPainter.prl
%{_qt6_libdir}/libQt6CanvasPainter.so
%{_qt6_metatypesdir}/qt6canvaspainter_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_canvaspainter.pri
%{_qt6_pkgconfigdir}/Qt6CanvasPainter.pc
%exclude %{_qt6_includedir}/QtCanvasPainter/%{real_version}

%files private-devel
%{_qt6_cmakedir}/Qt6CanvasPainterPrivate/
%{_qt6_includedir}/QtCanvasPainter/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_canvaspainter_private.pri

%endif

%changelog
