#
# spec file for package qt6-quickcontrols2
#
# Copyright (c) 2020 SUSE LLC
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


%define real_version 6.1.0
%define short_version 6.1
%define tar_name qtquickcontrols2-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-quickcontrols2%{?pkg_suffix}
Version:        6.1.0
Release:        0
Summary:        Set of controls to build interfaces in Qt Quick
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-quickcontrols2-rpmlintrc
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-qmlmodels-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt 6 QuickControls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 QuickControls2 QML files and plugins

%description imports
QML files and plugins from the Qt 6 QuickControls2 module

%package -n libQt6QuickControls2-6
Summary:        Qt 6 QuickControls2 library

%description -n libQt6QuickControls2-6
The Qt 6 QuickControls2 library.

%package devel
Summary:        Qt 6 QuickControls2 library - Development files
Requires:       libQt6QuickControls2-6 = %{version}

%description devel
Development files for the Qt 6 QuickControls2 library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickControls2 library
Requires:       cmake(Qt6QuickControls2) = %{real_version}

%description private-devel
This package provides private headers of libQt6QuickControls2 that do not have
any ABI or API guarantees.

%package -n libQt6QuickControls2Impl6
Summary:        Qt 6 QuickControls2Impl library

%description -n libQt6QuickControls2Impl6
The Qt 6 QuickControls2Impl library.

%package -n qt6-quickcontrols2impl-devel
Summary:        Qt6 QuickControls2Impl library - Development files
Requires:       libQt6QuickControls2Impl6 = %{version}

%description -n qt6-quickcontrols2impl-devel
Development files for the Qt 6 QuickControls2Impl library.

%package -n qt6-quickcontrols2impl-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickControls2Impl library
Requires:       cmake(Qt6QuickControls2Impl) = %{real_version}

%description -n qt6-quickcontrols2impl-private-devel
This package provides private headers of libQt6QuickControls2Impl that do not
have any ABI or API guarantees.

%package -n libQt6QuickTemplates2-6
Summary:        Qt 6 QuickTemplates2 library

%description -n libQt6QuickTemplates2-6
The Qt 6 QuickTemplates2 library.

%package -n qt6-quicktemplates2-devel
Summary:        Qt6 QuickTemplates2 library - Development files
Requires:       libQt6QuickTemplates2-6 = %{version}

%description -n qt6-quicktemplates2-devel
Development files for the Qt 6 QuickTemplates2 library.

%package -n qt6-quicktemplates2-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickTemplates2 library
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}
%requires_eq    qt6-qmlmodels-private-devel

%description -n qt6-quicktemplates2-private-devel
This package provides private headers of libQt6QuickTemplates2 that do not have
any ABI or API guarantees.

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

# metatype files are not needed for plugins
rm %{buildroot}%{_qt6_metatypesdir}/*plugin_*.json

%post -n libQt6QuickControls2-6 -p /sbin/ldconfig
%postun -n libQt6QuickControls2-6 -p /sbin/ldconfig
%post -n libQt6QuickControls2Impl6 -p /sbin/ldconfig
%postun -n libQt6QuickControls2Impl6 -p /sbin/ldconfig
%post -n libQt6QuickTemplates2-6 -p /sbin/ldconfig
%postun -n libQt6QuickTemplates2-6 -p /sbin/ldconfig

%files imports
%dir %{_qt6_qmldir}/Qt
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_qmldir}/Qt/labs/
%{_qt6_qmldir}/QtQuick/Controls/
%{_qt6_qmldir}/QtQuick/NativeStyle/
%{_qt6_qmldir}/QtQuick/Templates/

%files -n libQt6QuickControls2-6
%license LICENSE.*
%{_qt6_libdir}/libQt6QuickControls2.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtQuickControls2TestsConfig.cmake
%{_qt6_cmakedir}/Qt6QuickControls2/
%{_qt6_descriptionsdir}/QuickControls2.json
%{_qt6_includedir}/QtQuickControls2/
%{_qt6_libdir}/libQt6QuickControls2.prl
%{_qt6_libdir}/libQt6QuickControls2.so
%{_qt6_metatypesdir}/qt6quickcontrols2_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2.pri
%exclude %{_qt6_includedir}/QtQuickControls2/%{real_version}

%files private-devel
%{_qt6_includedir}/QtQuickControls2/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2_private.pri

%files -n libQt6QuickControls2Impl6
%{_qt6_libdir}/libQt6QuickControls2Impl.so.*

%files -n qt6-quickcontrols2impl-devel
%{_qt6_cmakedir}/Qt6QuickControls2Impl/
%{_qt6_descriptionsdir}/QuickControls2Impl.json
%{_qt6_includedir}/QtQuickControls2Impl/
%{_qt6_libdir}/libQt6QuickControls2Impl.prl
%{_qt6_libdir}/libQt6QuickControls2Impl.so
%{_qt6_metatypesdir}/qt6quickcontrols2impl_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2impl.pri
%exclude %{_qt6_includedir}/QtQuickControls2Impl/%{real_version}

%files -n qt6-quickcontrols2impl-private-devel
%{_qt6_includedir}/QtQuickControls2Impl/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2impl_private.pri

%files -n libQt6QuickTemplates2-6
%{_qt6_libdir}/libQt6QuickTemplates2.so.*

%files -n qt6-quicktemplates2-devel
%{_qt6_cmakedir}/Qt6QuickTemplates2/
%{_qt6_descriptionsdir}/QuickTemplates2.json
%{_qt6_includedir}/QtQuickTemplates2/
%{_qt6_libdir}/libQt6QuickTemplates2.prl
%{_qt6_libdir}/libQt6QuickTemplates2.so
%{_qt6_metatypesdir}/qt6quicktemplates2_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicktemplates2.pri
%exclude %{_qt6_includedir}/QtQuickTemplates2/%{real_version}

%files -n qt6-quicktemplates2-private-devel
%{_qt6_includedir}/QtQuickTemplates2/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quicktemplates2_private.pri

%endif

%changelog
