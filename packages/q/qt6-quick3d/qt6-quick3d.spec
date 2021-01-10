#
# spec file for package qt6-quick3d
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


%define real_version 6.0.0
%define short_version 6.0
%define tar_name qtquick3d
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-quick3d%{?pkg_suffix}
Version:        6.0.0
Release:        0
Summary:        Qt6 Quick3D Libraries and utilities
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         %{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-quick3d-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-shadertools-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(assimp) >= 5
BuildRequires:  pkgconfig(zlib)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt6 Quick3D Libraries and plugins.

%if !%{qt6_docs_flavor}

%package -n libQt6Quick3D6
Summary:        Qt 6 Quick3D library

%description -n libQt6Quick3D6
The Qt 6 Quick3D library.

%package devel
Summary:        Qt 6 Quick3D library - Development files
Requires:       libQt6Quick3D6 = %{version}
# Executables are required
Requires:       qt6-quick3d

%description devel
Development files for the Qt 6 Quick3D library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3D library
Requires:       qt6-quick3druntimerender-private-devel = %{version}
Requires:       cmake(Qt6Quick3D) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-qml-private-devel
%requires_eq    qt6-quick-private-devel

%description private-devel
This package provides private headers of libQt6Quick3D that do not have any
ABI or API guarantees.

%package imports
Summary:        Qt 6 Quick3D QML files and plugins

%description imports
QML files and plugins from the Qt 6 Quick3D module

%package -n libQt6Quick3DAssetImport6
Summary:        Qt 6 Quick3DAssetImport library

%description -n libQt6Quick3DAssetImport6
The Qt 6 Quick3DAssetImport library.

%package -n qt6-quick3dassetimport-devel
Summary:        Qt6 Quick3DAssetImport library - Development files
Requires:       libQt6Quick3DAssetImport6 = %{version}

%description -n qt6-quick3dassetimport-devel
Development files for the Qt 6 Quick3DAssetImport library.

%package -n qt6-quick3dassetimport-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DAssetImport library
Requires:       qt6-quick3dutils-private-devel = %{version}
Requires:       cmake(Qt6Quick3DAssetImport) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-quick3dassetimport-private-devel
This package provides private headers of libQt6Quick3DAssetImport that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DRuntimeRender6
Summary:        Qt 6 Quick3DRuntimeRender library

%description -n libQt6Quick3DRuntimeRender6
The Qt 6 Quick3DRuntimeRender library.

%package -n qt6-quick3druntimerender-devel
Summary:        Qt6 Quick3DRuntimeRender library - Development files
Requires:       libQt6Quick3DRuntimeRender6 = %{version}

%description -n qt6-quick3druntimerender-devel
Development files for the Qt 6 Quick3DRuntimeRender library.

%package -n qt6-quick3druntimerender-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DRuntimeRender library
Requires:       qt6-quick3dassetimport-private-devel = %{version}
Requires:       qt6-quick3dutils-private-devel = %{version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}
%requires_eq    qt6-quick-private-devel
%requires_eq    qt6-shadertools-private-devel

%description -n qt6-quick3druntimerender-private-devel
This package provides private headers of libQt6Quick3DRuntimeRender that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DUtils6
Summary:        Qt 6 Quick3DUtils library

%description -n libQt6Quick3DUtils6
The Qt 6 Quick3DUtils library.

%package -n qt6-quick3dutils-devel
Summary:        Qt6 Quick3DUtils library - Development files
Requires:       libQt6Quick3DUtils6 = %{version}

%description -n qt6-quick3dutils-devel
Development files for the Qt 6 Quick3DUtils library.

%package -n qt6-quick3dutils-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DUtils library
Requires:       cmake(Qt6Quick3DUtils) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description -n qt6-quick3dutils-private-devel
This package provides private headers of libQt6Quick3DUtils that do not have any
ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6 \
  -DQT_FEATURE_system_assimp=ON

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%{qt6_link_executables}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin*.cmake

# metatype files are not needed for plugins
rm %{buildroot}%{_qt6_metatypesdir}/*plugin_*.json

%fdupes %{buildroot}%{_qt6_qmldir}/QtQuick3D

%post -n libQt6Quick3D6 -p /sbin/ldconfig
%postun -n libQt6Quick3D6 -p /sbin/ldconfig
%post -n libQt6Quick3DAssetImport6 -p /sbin/ldconfig
%postun -n libQt6Quick3DAssetImport6 -p /sbin/ldconfig
%post -n libQt6Quick3DRuntimeRender6 -p /sbin/ldconfig
%postun -n libQt6Quick3DRuntimeRender6 -p /sbin/ldconfig
%post -n libQt6Quick3DUtils6 -p /sbin/ldconfig
%postun -n libQt6Quick3DUtils6 -p /sbin/ldconfig

%files
# No better place to install these quick3d plugins
%dir %{_qt6_pluginsdir}/assetimporters
%{_bindir}/balsam6
%{_bindir}/meshdebug6
%{_bindir}/shadergen6
%{_qt6_bindir}/balsam
%{_qt6_bindir}/meshdebug
%{_qt6_bindir}/shadergen
%{_qt6_pluginsdir}/assetimporters/libassimp.so
%{_qt6_pluginsdir}/assetimporters/libuip.so

%files imports
%{_qt6_qmldir}/QtQuick3D/

%files -n libQt6Quick3D6
%license LICENSE.*
%{_qt6_libdir}/libQt6Quick3D.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindWrapQuick3DAssimp.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtQuick3DTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Quick3D/
# Only required by Qt6Quick3DDependencies.cmake
%{_qt6_cmakedir}/Qt6Quick3DTools/
%{_qt6_descriptionsdir}/Quick3D.json
%{_qt6_includedir}/QtQuick3D/
%{_qt6_libdir}/libQt6Quick3D.prl
%{_qt6_libdir}/libQt6Quick3D.so
%{_qt6_metatypesdir}/qt6quick3d_relwithdebinfo_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3d.pri
%exclude %{_qt6_includedir}/QtQuick3D/%{real_version}

%files private-devel
%{_qt6_includedir}/QtQuick3D/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3d_private.pri

%files -n libQt6Quick3DAssetImport6
%{_qt6_libdir}/libQt6Quick3DAssetImport.so.*

%files -n qt6-quick3dassetimport-devel
%{_qt6_cmakedir}/Qt6Quick3DAssetImport/
%{_qt6_descriptionsdir}/Quick3DAssetImport.json
%{_qt6_includedir}/QtQuick3DAssetImport/
%{_qt6_libdir}/libQt6Quick3DAssetImport.prl
%{_qt6_libdir}/libQt6Quick3DAssetImport.so
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dassetimport.pri
%exclude %{_qt6_includedir}/QtQuick3DAssetImport/%{real_version}

%files -n qt6-quick3dassetimport-private-devel
%{_qt6_includedir}/QtQuick3DAssetImport/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dassetimport_private.pri

%files -n libQt6Quick3DRuntimeRender6
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so.*

%files -n qt6-quick3druntimerender-devel
%{_qt6_cmakedir}/Qt6Quick3DRuntimeRender/
%{_qt6_descriptionsdir}/Quick3DRuntimeRender.json
%{_qt6_includedir}/QtQuick3DRuntimeRender/
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.prl
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so
%{_qt6_mkspecsdir}/modules/qt_lib_quick3druntimerender.pri
%exclude %{_qt6_includedir}/QtQuick3DRuntimeRender/%{real_version}

%files -n qt6-quick3druntimerender-private-devel
%{_qt6_includedir}/QtQuick3DRuntimeRender/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3druntimerender_private.pri

%files -n libQt6Quick3DUtils6
%{_qt6_libdir}/libQt6Quick3DUtils.so.*

%files -n qt6-quick3dutils-devel
%{_qt6_cmakedir}/Qt6Quick3DUtils/
%{_qt6_descriptionsdir}/Quick3DUtils.json
%{_qt6_includedir}/QtQuick3DUtils/
%{_qt6_libdir}/libQt6Quick3DUtils.prl
%{_qt6_libdir}/libQt6Quick3DUtils.so
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dutils.pri
%exclude %{_qt6_includedir}/QtQuick3DUtils/%{real_version}

%files -n qt6-quick3dutils-private-devel
%{_qt6_includedir}/QtQuick3DUtils/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dutils_private.pri

%endif

%changelog
