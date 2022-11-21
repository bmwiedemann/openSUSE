#
# spec file for package qt6-quick3dphysics
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
%define tar_name qtquick3dphysics-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-quick3dphysics%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 Quick3D Physics Extensions
License:        GPL-3.0-only
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-quick3d-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Quick3D)
#
# Only arm and x86_64 are supported
ExclusiveArch:  %{arm} aarch64 x86_64
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
This module adds physical simulation capabilities on top of Qt Quick 3D.
In particular, it enables rigid body simulation using simple primitives as well
as convex- and triangle meshes and heightmaps. Physical properties such as mass,
density, gravity and friction are customizable. This makes it possible to create
physically correct behavior in 3D scenes without having to handcraft animations.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Quick3DPhysics QML files and plugins

%description imports
QML files and plugins from the Qt 6 Quick3DPhysics module.

%package -n libQt6Quick3DPhysics6
Summary:        Qt 6 Quick3DPhysics library

%description -n libQt6Quick3DPhysics6
The Qt 6 Quick3DPhysics library.

%package -n qt6-quick3dphysics-devel
Summary:        Qt 6 Quick3DPhysics library - Development files
Requires:       libQt6Quick3DPhysics6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6Quick3D)

%description -n qt6-quick3dphysics-devel
Development files for the Qt 6 Quick3DPhysics library.

%package -n qt6-quick3dphysics-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick3DPhysics library
Requires:       cmake(Qt6Quick3DPhysics) = %{real_version}
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-qml-private-devel
%requires_eq    qt6-quick-private-devel

%description -n qt6-quick3dphysics-private-devel
This package provides private headers of libQt6Quick3DPhysics that do not have
any ABI or API guarantees.

### Private only library ###

%package -n libQt6Quick3DPhysicsHelpers6
Summary:        Qt 6 Quick3DPhysicsHelpers library

%description -n libQt6Quick3DPhysicsHelpers6
The Qt 6 Quick3DPhysicsHelpers library.
This library does not have any ABI or API guarantees.

%package -n qt6-quick3dphysicshelpers-private-devel
Summary:        Qt 6 Quick3DPhysicsHelpers library - Development files
Requires:       libQt6Quick3DPhysicsHelpers6 = %{version}
Requires:       qt6-quick3dphysics-private-devel = %{version}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6Quick3D)

%description -n qt6-quick3dphysicshelpers-private-devel
Development files for the Qt 6 Quick3DPhysics private library.
This library does not have any ABI or API guarantees.

### Static libraries ###

%package -n qt6-bundledphysx-devel-static
Summary:        Qt6 BundledPhysX static library
%requires_eq    qt6-core-private-devel

%description -n qt6-bundledphysx-devel-static
The Qt6 BundledPhysX static library.
This library does not have any ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%define _lto_cflags %{nil}
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%{qt6_link_executables}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%post -n libQt6Quick3DPhysicsHelpers6 -p /sbin/ldconfig
%post -n libQt6Quick3DPhysics6 -p /sbin/ldconfig
%postun -n libQt6Quick3DPhysicsHelpers6 -p /sbin/ldconfig
%postun -n libQt6Quick3DPhysics6 -p /sbin/ldconfig

%files
%{_bindir}/cooker6
%{_qt6_bindir}/cooker

%files imports
%dir %{_qt6_qmldir}/QtQuick3D
%{_qt6_qmldir}/QtQuick3D/Physics/

%files -n libQt6Quick3DPhysics6
%license LICENSES/*
%{_qt6_libdir}/libQt6Quick3DPhysics.so.*

%files -n qt6-quick3dphysics-devel
%{_qt6_cmakedir}/Qt6/FindWrapBundledPhysXConfigExtra.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtQuick3DPhysicsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Quick3DPhysics/
%{_qt6_descriptionsdir}/Quick3DPhysics.json
%{_qt6_includedir}/QtQuick3DPhysics/
%{_qt6_libdir}/libQt6Quick3DPhysics.prl
%{_qt6_libdir}/libQt6Quick3DPhysics.so
%{_qt6_metatypesdir}/qt6quick3dphysics_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dphysics.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DPhysics.pc
%exclude %{_qt6_includedir}/QtQuick3DPhysics/%{real_version}

%files -n qt6-quick3dphysics-private-devel
%{_qt6_includedir}/QtQuick3DPhysics/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dphysics_private.pri

### Private only library ###

%files -n libQt6Quick3DPhysicsHelpers6
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.so.*

%files -n qt6-quick3dphysicshelpers-private-devel
%{_qt6_cmakedir}/Qt6Quick3DPhysicsHelpers/
%{_qt6_descriptionsdir}/Quick3DPhysicsHelpers.json
%{_qt6_includedir}/QtQuick3DPhysicsHelpers/
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.prl
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.so
%{_qt6_metatypesdir}/qt6quick3dphysicshelpers_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dphysicshelpers.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dphysicshelpers_private.pri
%{_qt6_pkgconfigdir}/Qt6Quick3DPhysicsHelpers.pc

### Static libraries ###

%files -n qt6-bundledphysx-devel-static
%{_qt6_cmakedir}/Qt6BundledPhysX/
%{_qt6_libdir}/libQt6BundledPhysX.a

%endif

%changelog
