#
# spec file for package qt6-quick3d
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
%define tar_name qtquick3d-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
# Private QML imports
%global __requires_exclude qt6qmlimport\\((Quick3DAssets|VirtualAssistant\\.Constants|robotassistant|.*Example|xr_shared).*
#
Name:           qt6-quick3d%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        API for creating 3D content and 3D user interfaces based on Qt Quick
License:        GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-quick3d-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-quicktimeline-private-devel
BuildRequires:  cmake(Qt6Concurrent) = %{real_version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6GuiPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6QmlPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickPrivate) = %{real_version}
# Only needed if QT_FEATURE_qml_debug is enabled
# BuildRequires:  cmake(Qt6PacketProtocolPrivate)
BuildRequires:  cmake(Qt6QuickTimeline) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}
BuildRequires:  cmake(Qt6ShaderToolsPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  cmake(assimp) >= 5.1.0
BuildRequires:  pkgconfig(zlib)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Quick 3D provides a high-level API for creating 3D content and 3D user
interfaces based on Qt Quick.

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
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}

%description devel
Development files for the Qt 6 Quick3D library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3D library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3D) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRenderPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}

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
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick3DUtils) = %{real_version}

%description -n qt6-quick3dassetimport-devel
Development files for the Qt 6 Quick3DAssetImport library.

%package -n qt6-quick3dassetimport-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DAssetImport library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetImport) = %{real_version}
Requires:       cmake(Qt6Quick3DUtilsPrivate) = %{real_version}

%description -n qt6-quick3dassetimport-private-devel
This package provides private headers of libQt6Quick3DAssetImport that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DAssetUtils6
Summary:        Qt 6 Quick3DAssetUtils library

%description -n libQt6Quick3DAssetUtils6
The Qt 6 Quick3DAssetUtils library.

%package -n qt6-quick3dassetutils-devel
Summary:        Qt6 Quick3DAssetUtils library - Development files
Requires:       libQt6Quick3DAssetUtils6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3D) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetImport) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetImportPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRenderPrivate) = %{real_version}
Requires:       cmake(Qt6QuickTimeline) = %{real_version}

%description -n qt6-quick3dassetutils-devel
Development files for the Qt 6 Quick3DAssetUtils library.

%package -n qt6-quick3dassetutils-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DAssetUtils library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetImportPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetUtils) = %{real_version}
Requires:       cmake(Qt6Quick3DPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRenderPrivate) = %{real_version}
Requires:       cmake(Qt6QuickTimelinePrivate) = %{real_version}

%description -n qt6-quick3dassetutils-private-devel
This package provides private headers of libQt6Quick3DAssetUtils that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DEffects6
Summary:        Qt 6 Quick3DEffects library

%description -n libQt6Quick3DEffects6
The Qt 6 Quick3DEffects library.

%package -n qt6-quick3deffects-devel
Summary:        Qt6 Quick3DEffects library - Development files
Requires:       libQt6Quick3DEffects6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3DPrivate) = %{real_version}

%description -n qt6-quick3deffects-devel
Development files for the Qt 6 Quick3DEffects library.

%package -n libQt6Quick3DHelpers6
Summary:        Qt 6 Quick3DHelpers library

%description -n libQt6Quick3DHelpers6
The Qt 6 Quick3DHelpers library.

%package -n qt6-quick3dhelpers-devel
Summary:        Qt6 Quick3DHelpers library - Development files
Requires:       libQt6Quick3DHelpers6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3DPrivate) = %{real_version}

%description -n qt6-quick3dhelpers-devel
Development files for the Qt 6 Quick3DHelpers library.

%package -n qt6-quick3dhelpers-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DHelpers library
Requires:       cmake(Qt6Quick3DHelpers) = %{real_version}

%description -n qt6-quick3dhelpers-private-devel
This package provides private headers of libQt6Quick3DHelpers that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DHelpersImpl6
Summary:        Qt 6 Quick3DHelpersImpl library

%description -n libQt6Quick3DHelpersImpl6
The Qt 6 Quick3DHelpersImpl library.

%package -n qt6-quick3dhelpersimpl-devel
Summary:        Qt6 Quick3DHelpersImpl library - Development files
Requires:       libQt6Quick3DHelpersImpl6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3DPrivate) = %{real_version}

%description -n qt6-quick3dhelpersimpl-devel
Development files for the Qt 6 Quick3DHelpersImpl library.

%package -n qt6-quick3dhelpersimpl-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DHelpersImpl library
Requires:       cmake(Qt6Quick3DHelpersImpl) = %{real_version}

%description -n qt6-quick3dhelpersimpl-private-devel
This package provides private headers of libQt6Quick3DHelpersImpl that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DIblBaker6
Summary:        Qt 6 Quick3DIblBaker library

%description -n libQt6Quick3DIblBaker6
The Qt 6 Quick3DIblBaker library.

%package -n qt6-quick3diblbaker-devel
Summary:        Qt6 Quick3DIblBaker library - Development files
Requires:       libQt6Quick3DIblBaker6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}

%description -n qt6-quick3diblbaker-devel
Development files for the Qt 6 Quick3DIblBaker library.

%package -n qt6-quick3diblbaker-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DIblBaker library
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DIblBaker) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRenderPrivate) = %{real_version}

%description -n qt6-quick3diblbaker-private-devel
This package provides private headers of libQt6Quick3DIblBaker that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DParticles6
Summary:        Qt 6 Quick3DParticles library

%description -n libQt6Quick3DParticles6
The Qt 6 Quick3DParticles library.

%package -n qt6-quick3dparticles-devel
Summary:        Qt6 Quick3DParticles library - Development files
Requires:       libQt6Quick3DParticles6 = %{version}
Requires:       cmake(Qt6Quick3DAssetImport) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}

%description -n qt6-quick3dparticles-devel
Development files for the Qt 6 Quick3DParticles library.

%package -n qt6-quick3dparticles-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DParticles library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetImportPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DParticles) = %{real_version}
Requires:       cmake(Qt6Quick3DPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRenderPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}

%description -n qt6-quick3dparticles-private-devel
This package provides private headers of libQt6Quick3DParticles that do not
have any ABI or API guarantees.

%package -n libQt6Quick3DParticleEffects6
Summary:        Qt 6 Quick3DParticleEffects library

%description -n libQt6Quick3DParticleEffects6
The Qt 6 Quick3DParticleEffects library.

%package -n qt6-quick3dparticleeffects-devel
Summary:        Qt6 Quick3DParticleEffects library - Development files
Requires:       libQt6Quick3DParticleEffects6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3D) = %{real_version}
Requires:       cmake(Qt6Quick3DAssetImport) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}

%description -n qt6-quick3dparticleeffects-devel
Development files for the Qt 6 Quick3DParticleEffects library.

%package -n libQt6Quick3DRuntimeRender6
Summary:        Qt 6 Quick3DRuntimeRender library

%description -n libQt6Quick3DRuntimeRender6
The Qt 6 Quick3DRuntimeRender library.

%package -n qt6-quick3druntimerender-devel
Summary:        Qt6 Quick3DRuntimeRender library - Development files
Requires:       libQt6Quick3DRuntimeRender6 = %{version}
Requires:       cmake(Qt6Concurrent) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3DUtils) = %{real_version}
Requires:       cmake(Qt6ShaderTools) = %{real_version}

%description -n qt6-quick3druntimerender-devel
Development files for the Qt 6 Quick3DRuntimeRender library.

%package -n qt6-quick3druntimerender-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DRuntimeRender library
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}
Requires:       cmake(Qt6Quick3DUtilsPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6ShaderToolsPrivate) = %{real_version}

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
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}

%description -n qt6-quick3dutils-devel
Development files for the Qt 6 Quick3DUtils library.

%package -n qt6-quick3dutils-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DUtils library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Quick3DUtils) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}

%description -n qt6-quick3dutils-private-devel
This package provides private headers of libQt6Quick3DUtils that do not have any
ABI or API guarantees.

%package -n libQt6Quick3DXr6
Summary:        Qt 6 Quick3DXr library

%description -n libQt6Quick3DXr6
Adds OpenXR support for applications using QtQuick3D.

%package -n qt6-quick3dxr-private-devel
Summary:        Qt 6 Quick3DXr library - Development files
Requires:       libQt6Quick3DXr6 = %{version}

%description -n qt6-quick3dxr-private-devel
Development files for the Qt 6 Quick3DXr library.
This library does not have any ABI or API guarantees.


### Private only library ###

%package -n libQt6Quick3DGlslParser6
Summary:        Qt 6 Quick3DGlslParser library

%description -n libQt6Quick3DGlslParser6
The Qt 6 Quick3DGlslParser library.
This library does not have any ABI or API guarantees.

%package -n qt6-quick3dglslparser-private-devel
Summary:        Development files for the Qt 6 Quick3DGlslParser library
Requires:       libQt6Quick3DGlslParser6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description -n qt6-quick3dglslparser-private-devel
Development files for the Qt 6 Quick3DGlslParser library.
This library does not have any ABI or API guarantees.

### Static libraries ###

# Embree only supports x86_64 %%x86_64 and arm64
%ifarch x86_64 %{x86_64} aarch64
%package -n qt6-bundledembree-devel-static
Summary:        Qt6 BundledEmbree static library
Requires:       cmake(Qt6CorePrivate) = %{real_version}

%description -n qt6-bundledembree-devel-static
The Qt6 BundledEmbree static library.
This library does not have any ABI or API guarantees.
%endif

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
# Package provides static libraries, -ffat-lto-objects is not enough for libQt6BundledEmbree.a
%global _lto_cflags %{nil}

%if %{qt6_docs_flavor}
# Work around https://bugreports.qt.io/browse/QTBUG-129807
%define extra_args -DFEATURE_quick3dxr_openxr:BOOL=FALSE -DFEATURE_system_openxr:BOOL=FALSE
%endif

%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE \
  -DFEATURE_system_assimp:BOOL=TRUE %{?extra_args}

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%{qt6_link_executables}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin*.cmake

# There's no private api
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_quick3deffects_private.pri
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_quick3dparticleeffects_private.pri
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Quick3DEffectsPrivate
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Quick3DParticleEffectsPrivate

# Probably unneeded
rm %{buildroot}%{_qt6_cmakedir}/Qt6/FindWrapBundledOpenXRConfigExtra.cmake
rm %{buildroot}%{_qt6_libdir}/libQt6BundledOpenXR.a
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6BundledOpenXR

%fdupes %{buildroot}%{_qt6_qmldir}/QtQuick3D

%ldconfig_scriptlets -n libQt6Quick3D6
%ldconfig_scriptlets -n libQt6Quick3DAssetImport6
%ldconfig_scriptlets -n libQt6Quick3DAssetUtils6
%ldconfig_scriptlets -n libQt6Quick3DEffects6
%ldconfig_scriptlets -n libQt6Quick3DGlslParser6
%ldconfig_scriptlets -n libQt6Quick3DHelpers6
%ldconfig_scriptlets -n libQt6Quick3DHelpersImpl6
%ldconfig_scriptlets -n libQt6Quick3DIblBaker6
%ldconfig_scriptlets -n libQt6Quick3DParticleEffects6
%ldconfig_scriptlets -n libQt6Quick3DParticles6
%ldconfig_scriptlets -n libQt6Quick3DRuntimeRender6
%ldconfig_scriptlets -n libQt6Quick3DUtils6
%ldconfig_scriptlets -n libQt6Quick3DXr6

%files
# No better place to install these quick3d plugins
%dir %{_qt6_pluginsdir}/assetimporters
%{_bindir}/balsam6
%{_bindir}/balsamui6
%{_bindir}/instancer6
%{_bindir}/materialeditor6
%{_bindir}/meshdebug6
%{_bindir}/shadergen6
%{_bindir}/shapegen6
%{_qt6_bindir}/balsam
%{_qt6_bindir}/balsamui
%{_qt6_bindir}/instancer
%{_qt6_bindir}/materialeditor
%{_qt6_bindir}/meshdebug
%{_qt6_bindir}/shadergen
%{_qt6_bindir}/shapegen
%{_qt6_pluginsdir}/assetimporters/libassimp.so

%files imports
%{_qt6_qmldir}/QtQuick3D/

%files -n libQt6Quick3D6
%license LICENSES/*
%{_qt6_libdir}/libQt6Quick3D.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindWrapQuick3DAssimp.cmake
%{_qt6_cmakedir}/Qt6/FindWrapOpenXR.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtQuick3DTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Quick3D/
# Only required by Qt6Quick3DDependencies.cmake
%{_qt6_cmakedir}/Qt6Quick3DTools/
%{_qt6_descriptionsdir}/Quick3D.json
%{_qt6_includedir}/QtQuick3D/
%{_qt6_libdir}/libQt6Quick3D.prl
%{_qt6_libdir}/libQt6Quick3D.so
%{_qt6_metatypesdir}/qt6quick3d_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3d.pri
%{_qt6_pkgconfigdir}/Qt6Quick3D.pc
%exclude %{_qt6_includedir}/QtQuick3D/%{real_version}

%files private-devel
%{_qt6_cmakedir}/Qt6Quick3DPrivate/
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
%{_qt6_metatypesdir}/qt6quick3dassetimport_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dassetimport.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DAssetImport.pc
%exclude %{_qt6_includedir}/QtQuick3DAssetImport/%{real_version}

%files -n qt6-quick3dassetimport-private-devel
%{_qt6_cmakedir}/Qt6Quick3DAssetImportPrivate/
%{_qt6_includedir}/QtQuick3DAssetImport/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dassetimport_private.pri

%files -n libQt6Quick3DAssetUtils6
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so.*

%files -n qt6-quick3dassetutils-devel
%{_qt6_cmakedir}/Qt6Quick3DAssetUtils/
%{_qt6_descriptionsdir}/Quick3DAssetUtils.json
%{_qt6_includedir}/QtQuick3DAssetUtils/
%{_qt6_libdir}/libQt6Quick3DAssetUtils.prl
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so
%{_qt6_metatypesdir}/qt6quick3dassetutils_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dassetutils.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DAssetUtils.pc
%exclude %{_qt6_includedir}/QtQuick3DAssetUtils/%{real_version}

%files -n qt6-quick3dassetutils-private-devel
%{_qt6_cmakedir}/Qt6Quick3DAssetUtilsPrivate/
%{_qt6_includedir}/QtQuick3DAssetUtils/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dassetutils_private.pri

%files -n libQt6Quick3DEffects6
%{_qt6_libdir}/libQt6Quick3DEffects.so.*

%files -n qt6-quick3deffects-devel
%{_qt6_cmakedir}/Qt6Quick3DEffects/
%{_qt6_descriptionsdir}/Quick3DEffects.json
%{_qt6_libdir}/libQt6Quick3DEffects.prl
%{_qt6_libdir}/libQt6Quick3DEffects.so
%{_qt6_metatypesdir}/qt6quick3deffects_*_metatypes.json
%{_qt6_pkgconfigdir}/Qt6Quick3DEffects.pc
%{_qt6_mkspecsdir}/modules/qt_lib_quick3deffects.pri

%files -n libQt6Quick3DHelpers6
%{_qt6_libdir}/libQt6Quick3DHelpers.so.*

%files -n qt6-quick3dhelpers-devel
%{_qt6_cmakedir}/Qt6Quick3DHelpers/
%{_qt6_descriptionsdir}/Quick3DHelpers.json
%{_qt6_includedir}/QtQuick3DHelpers/
%{_qt6_libdir}/libQt6Quick3DHelpers.prl
%{_qt6_libdir}/libQt6Quick3DHelpers.so
%{_qt6_metatypesdir}/qt6quick3dhelpers_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dhelpers.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DHelpers.pc
%exclude %{_qt6_includedir}/QtQuick3DHelpers/%{real_version}

%files -n qt6-quick3dhelpers-private-devel
%{_qt6_cmakedir}/Qt6Quick3DHelpersPrivate/
%{_qt6_includedir}/QtQuick3DHelpers/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dhelpers_private.pri

%files -n libQt6Quick3DHelpersImpl6
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so.*

%files -n qt6-quick3dhelpersimpl-devel
%{_qt6_cmakedir}/Qt6Quick3DHelpersImpl/
%{_qt6_descriptionsdir}/Quick3DHelpersImpl.json
%{_qt6_includedir}/QtQuick3DHelpersImpl/
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.prl
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so
%{_qt6_metatypesdir}/qt6quick3dhelpersimpl_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dhelpersimpl.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DHelpersImpl.pc
%exclude %{_qt6_includedir}/QtQuick3DHelpersImpl/%{real_version}

%files -n qt6-quick3dhelpersimpl-private-devel
%{_qt6_cmakedir}/Qt6Quick3DHelpersImplPrivate/
%{_qt6_includedir}/QtQuick3DHelpersImpl/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dhelpersimpl_private.pri

%files -n libQt6Quick3DIblBaker6
%{_qt6_libdir}/libQt6Quick3DIblBaker.so.*

%files -n qt6-quick3diblbaker-devel
%{_qt6_cmakedir}/Qt6Quick3DIblBaker/
%{_qt6_descriptionsdir}/Quick3DIblBaker.json
%{_qt6_includedir}/QtQuick3DIblBaker/
%{_qt6_libdir}/libQt6Quick3DIblBaker.prl
%{_qt6_libdir}/libQt6Quick3DIblBaker.so
%{_qt6_metatypesdir}/qt6quick3diblbaker_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3diblbaker.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DIblBaker.pc
%exclude %{_qt6_includedir}/QtQuick3DIblBaker/%{real_version}

%files -n qt6-quick3diblbaker-private-devel
%{_qt6_cmakedir}/Qt6Quick3DIblBakerPrivate/
%{_qt6_includedir}/QtQuick3DIblBaker/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3diblbaker_private.pri

%files -n libQt6Quick3DParticles6
%{_qt6_libdir}/libQt6Quick3DParticles.so.*

%files -n qt6-quick3dparticles-devel
%{_qt6_cmakedir}/Qt6Quick3DParticles/
%{_qt6_descriptionsdir}/Quick3DParticles.json
%{_qt6_includedir}/QtQuick3DParticles/
%{_qt6_libdir}/libQt6Quick3DParticles.prl
%{_qt6_libdir}/libQt6Quick3DParticles.so
%{_qt6_metatypesdir}/qt6quick3dparticles_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dparticles.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DParticles.pc
%exclude %{_qt6_includedir}/QtQuick3DParticles/%{real_version}

%files -n qt6-quick3dparticles-private-devel
%{_qt6_cmakedir}/Qt6Quick3DParticlesPrivate/
%{_qt6_includedir}/QtQuick3DParticles/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dparticles_private.pri

%files -n libQt6Quick3DParticleEffects6
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so.*

%files -n qt6-quick3dparticleeffects-devel
%{_qt6_cmakedir}/Qt6Quick3DParticleEffects/
%{_qt6_descriptionsdir}/Quick3DParticleEffects.json
%{_qt6_libdir}/libQt6Quick3DParticleEffects.prl
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so
%{_qt6_metatypesdir}/qt6quick3dparticleeffects_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dparticleeffects.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DParticleEffects.pc

%files -n libQt6Quick3DRuntimeRender6
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so.*

%files -n qt6-quick3druntimerender-devel
%{_qt6_cmakedir}/Qt6Quick3DRuntimeRender/
%{_qt6_descriptionsdir}/Quick3DRuntimeRender.json
%{_qt6_includedir}/QtQuick3DRuntimeRender/
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.prl
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so
%{_qt6_metatypesdir}/qt6quick3druntimerender_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3druntimerender.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DRuntimeRender.pc
%exclude %{_qt6_includedir}/QtQuick3DRuntimeRender/%{real_version}

%files -n qt6-quick3druntimerender-private-devel
%{_qt6_cmakedir}/Qt6Quick3DRuntimeRenderPrivate/
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
%{_qt6_metatypesdir}/qt6quick3dutils_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dutils.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DUtils.pc
%exclude %{_qt6_includedir}/QtQuick3DUtils/%{real_version}

%files -n qt6-quick3dutils-private-devel
%{_qt6_cmakedir}/Qt6Quick3DUtilsPrivate/
%{_qt6_includedir}/QtQuick3DUtils/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dutils_private.pri

%files -n libQt6Quick3DXr6
%{_qt6_libdir}/libQt6Quick3DXr.so.*

%files -n qt6-quick3dxr-private-devel
%{_qt6_cmakedir}/Qt6/FindWrapSystemOpenXR.cmake
%{_qt6_cmakedir}/Qt6Quick3DXr/
%{_qt6_cmakedir}/Qt6Quick3DXrPrivate/
%{_qt6_descriptionsdir}/Quick3DXr.json
%{_qt6_includedir}/QtQuick3DXr/
%{_qt6_libdir}/libQt6Quick3DXr.prl
%{_qt6_libdir}/libQt6Quick3DXr.so
%{_qt6_metatypesdir}/qt6quick3dxr_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_ext_openxr_loader.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dxr.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dxr_private.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DXr.pc

### Private only library ###

%files -n libQt6Quick3DGlslParser6
%{_qt6_libdir}/libQt6Quick3DGlslParser.so.*

%files -n qt6-quick3dglslparser-private-devel
%{_qt6_cmakedir}/Qt6Quick3DGlslParserPrivate/
%{_qt6_descriptionsdir}/Quick3DGlslParserPrivate.json
%{_qt6_includedir}/QtQuick3DGlslParser/
%{_qt6_libdir}/libQt6Quick3DGlslParser.prl
%{_qt6_libdir}/libQt6Quick3DGlslParser.so
%{_qt6_metatypesdir}/qt6quick3dglslparserprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dglslparser_private.pri

### Static libraries ###

%ifarch x86_64 %{x86_64} aarch64
%files -n qt6-bundledembree-devel-static
%{_qt6_cmakedir}/Qt6/FindWrapBundledEmbreeConfigExtra.cmake
%{_qt6_cmakedir}/Qt6BundledEmbree/
%{_qt6_libdir}/libQt6BundledEmbree.a
%endif

%endif

%changelog
