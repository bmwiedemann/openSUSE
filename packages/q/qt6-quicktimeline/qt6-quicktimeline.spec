#
# spec file for package qt6-quicktimeline
#
# Copyright (c) 2022 SUSE LLC
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


%define real_version 6.4.1
%define short_version 6.4
%define tar_name qtquicktimeline-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-quicktimeline%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 module for creating keyframe-based animations
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-quicktimeline-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt Quick Timeline module enables keyframe-based animations and
parameterization. This module is directly supported by Qt Design Studio and
Qt Quick Designer, with a timeline editor to create keyframe-based animations.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 QuickTimeline QML files and plugins

%description imports
QML files and plugins from the Qt 6 QuickTimeline module

%package -n libQt6QuickTimeline6
Summary:        Qt 6 QuickTimeline library

%description -n libQt6QuickTimeline6
The Qt 6 QuickTimeline library.

%package devel
Summary:        Qt 6 QuickTimeline library - Development files
Requires:       libQt6QuickTimeline6 = %{version}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Quick)

%description devel
Development files for the Qt 6 QuickTimeline library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickTimeline Library
Requires:       cmake(Qt6QuickTimeline) = %{real_version}

%description private-devel
This package provides private headers of libQt6QuickTimeline that do not have
any ABI or API guarantees.

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

%post -n libQt6QuickTimeline6 -p /sbin/ldconfig
%postun -n libQt6QuickTimeline6 -p /sbin/ldconfig

%files imports
%license LICENSES/*
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_qmldir}/QtQuick/Timeline/

%files -n libQt6QuickTimeline6
%{_qt6_libdir}/libQt6QuickTimeline.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtQuickTimelineTestsConfig.cmake
%{_qt6_cmakedir}/Qt6QuickTimeline/
%{_qt6_descriptionsdir}/QuickTimeline.json
%{_qt6_includedir}/QtQuickTimeline/
%{_qt6_libdir}/libQt6QuickTimeline.prl
%{_qt6_libdir}/libQt6QuickTimeline.so
%{_qt6_metatypesdir}/qt6quicktimeline_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicktimeline.pri
%{_qt6_pkgconfigdir}/Qt6QuickTimeline.pc
%exclude %{_qt6_includedir}/QtQuickTimeline/%{real_version}

%files private-devel
%{_qt6_includedir}/QtQuickTimeline/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_quicktimeline_private.pri

%endif

%changelog
