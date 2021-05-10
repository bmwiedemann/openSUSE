#
# spec file for package qt6-3d
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


%define real_version 6.1.0
%define short_version 6.1
%define tar_name qt3d-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-3d%{?pkg_suffix}
Version:        6.1.0
Release:        0
Summary:        Qt 6 3D Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-3d-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-opengl-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-shadertools-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
# Doesn't build yet
# BuildRequires: cmake(Qt6Gamepad)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(assimp) >= 5
BuildRequires:  pkgconfig(zlib)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 3D provides functionality for near-realtime simulation
systems with support for 2D and 3D rendering in both Qt C++ and Qt Quick applications.

%if !%{qt6_docs_flavor}

%package devel
Summary:        Qt 6 3D development meta package
Requires:       cmake(Qt63DAnimation) = %{real_version}
Requires:       cmake(Qt63DCore) = %{real_version}
Requires:       cmake(Qt63DExtras) = %{real_version}
Requires:       cmake(Qt63DInput) = %{real_version}
Requires:       cmake(Qt63DLogic) = %{real_version}
Requires:       cmake(Qt63DQuick) = %{real_version}
Requires:       cmake(Qt63DQuickAnimation) = %{real_version}
Requires:       cmake(Qt63DQuickExtras) = %{real_version}
Requires:       cmake(Qt63DQuickInput) = %{real_version}
Requires:       cmake(Qt63DQuickRender) = %{real_version}
Requires:       cmake(Qt63DQuickScene2D) = %{real_version}
Requires:       cmake(Qt63DRender) = %{real_version}
BuildArch:      noarch

%description devel
This meta-package requires all the qt6-3d development packages.

%package private-devel
Summary:        Qt 6 3D unstable ABI meta package
Requires:       qt6-3d-devel = %{version}
Requires:       qt6-3danimation-private-devel = %{version}
Requires:       qt6-3dcore-private-devel = %{version}
Requires:       qt6-3dextras-private-devel = %{version}
Requires:       qt6-3dinput-private-devel = %{version}
Requires:       qt6-3dlogic-private-devel = %{version}
Requires:       qt6-3dquick-private-devel = %{version}
Requires:       qt6-3dquickanimation-private-devel = %{version}
Requires:       qt6-3dquickextras-private-devel = %{version}
Requires:       qt6-3dquickinput-private-devel = %{version}
Requires:       qt6-3dquickrender-private-devel = %{version}
Requires:       qt6-3dquickscene2d-private-devel = %{version}
Requires:       qt6-3drender-private-devel = %{version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-3d development packages that do not
have any ABI or API guarantees.

%package -n libQt63DAnimation6
Summary:        Qt 6 3DAnimation library

%description -n libQt63DAnimation6
The Qt 6 3DAnimation library.

%package -n qt6-3danimation-devel
Summary:        Development files for the Qt 6 3DAnimation library
Requires:       libQt63DAnimation6 = %{version}

%description -n qt6-3danimation-devel
Development files for the Qt 6 3DAnimation library.

%package -n qt6-3danimation-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DAnimation library
Requires:       cmake(Qt63DAnimation) = %{real_version}

%description -n qt6-3danimation-private-devel
This package provides private headers of libQt63DAnimation that do not have any
ABI or API guarantees.

%package -n libQt63DCore6
Summary:        Qt 6 3DCore library

%description -n libQt63DCore6
The Qt 6 3DCore library.

%package -n qt6-3dcore-devel
Summary:        Development files for the Qt 6 3DCore library
Requires:       libQt63DCore6 = %{version}

%description -n qt6-3dcore-devel
Development files for the Qt 6 3DCore library.

%package -n qt6-3dcore-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DCore library
Requires:       cmake(Qt63DCore) = %{real_version}

%description -n qt6-3dcore-private-devel
This package provides private headers of libQt63DCore that do not have any
ABI or API guarantees.

%package -n libQt63DExtras6
Summary:        Qt 6 3DExtras library

%description -n libQt63DExtras6
The Qt 6 3DExtras library.

%package -n qt6-3dextras-devel
Summary:        Development files for the Qt 6 3DExtras library
Requires:       libQt63DExtras6 = %{version}
Requires:       qt6-3dcore-private-devel = %{version}
Requires:       qt6-3drender-private-devel = %{version}
%requires_eq    qt6-gui-private-devel

%description -n qt6-3dextras-devel
Development files for the Qt 6 3DExtras library.

%package -n qt6-3dextras-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DExtras library
Requires:       cmake(Qt63DExtras) = %{real_version}

%description -n qt6-3dextras-private-devel
This package provides private headers of libQt63DExtras that do not have any
ABI or API guarantees.

%package -n libQt63DInput6
Summary:        Qt 6 3DInput library

%description -n libQt63DInput6
The Qt 6 3DInput library.

%package -n qt6-3dinput-devel
Summary:        Development files for the Qt 6 3DInput library
Requires:       libQt63DInput6 = %{version}

%description -n qt6-3dinput-devel
Development files for the Qt 6 3DInput library.

%package -n qt6-3dinput-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DInput library
Requires:       cmake(Qt63DInput) = %{real_version}

%description -n qt6-3dinput-private-devel
This package provides private headers of libQt63DInput that do not have any
ABI or API guarantees.

%package -n libQt63DLogic6
Summary:        Qt 6 3DLogic library

%description -n libQt63DLogic6
The Qt 6 3DLogic library.

%package -n qt6-3dlogic-devel
Summary:        Development files for the Qt 6 3DLogic library
Requires:       libQt63DLogic6 = %{version}

%description -n qt6-3dlogic-devel
Development files for the Qt 6 3DLogic library.

%package -n qt6-3dlogic-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DLogic library
Requires:       cmake(Qt63DLogic) = %{real_version}

%description -n qt6-3dlogic-private-devel
This package provides private headers of libQt63DLogic that do not have any
ABI or API guarantees.

%package -n libQt63DQuick6
Summary:        Qt 6 3DQuick library

%description -n libQt63DQuick6
The Qt 6 3DQuick library.

%package -n qt6-3dquick-devel
Summary:        Development files for the Qt 6 3DQuick library
Requires:       libQt63DQuick6 = %{version}

%description -n qt6-3dquick-devel
Development files for the Qt 6 3DQuick library.

%package -n qt6-3dquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DQuick library
Requires:       cmake(Qt63DQuick) = %{real_version}

%description -n qt6-3dquick-private-devel
This package provides private headers of libQt63DQuick that do not have any
ABI or API guarantees.

%package -n libQt63DQuickAnimation6
Summary:        Qt 6 3DQuickAnimation library

%description -n libQt63DQuickAnimation6
The Qt 6 3DQuickAnimation library.

%package -n qt6-3dquickanimation-devel
Summary:        Development files for the Qt 6 3DQuickAnimation library
Requires:       libQt63DQuickAnimation6 = %{version}

%description -n qt6-3dquickanimation-devel
Development files for the Qt 6 3DQuickAnimation library.

%package -n qt6-3dquickanimation-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DQuickAnimation library
Requires:       cmake(Qt63DQuickAnimation) = %{real_version}

%description -n qt6-3dquickanimation-private-devel
This package provides private headers of libQt63DQuickAnimation that do not
have any ABI or API guarantees.

%package -n libQt63DQuickExtras6
Summary:        Qt 6 3DQuickExtras library

%description -n libQt63DQuickExtras6
The Qt 6 3DQuickExtras library.

%package -n qt6-3dquickextras-devel
Summary:        Development files for the Qt 6 3DQuickExtras library
Requires:       libQt63DQuickExtras6 = %{version}

%description -n qt6-3dquickextras-devel
Development files for the Qt 6 3DQuickExtras library.

%package -n qt6-3dquickextras-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DQuickExtras library
Requires:       cmake(Qt63DQuickExtras) = %{real_version}

%description -n qt6-3dquickextras-private-devel
This package provides private headers of libQt63DQuickExtras that do not have
any ABI or API guarantees.

%package -n libQt63DQuickInput6
Summary:        Qt 6 3DQuickInput library

%description -n libQt63DQuickInput6
The Qt 6 3DQuickInput library.

%package -n qt6-3dquickinput-devel
Summary:        Development files for the Qt 6 3DQuickInput library
Requires:       libQt63DQuickInput6 = %{version}

%description -n qt6-3dquickinput-devel
Development files for the Qt 6 3DQuickInput library.

%package -n qt6-3dquickinput-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DQuickInput library
Requires:       cmake(Qt63DQuickInput) = %{real_version}

%description -n qt6-3dquickinput-private-devel
This package provides private headers of libQt63DQuickInput that do not have any
ABI or API guarantees.

%package -n libQt63DQuickRender6
Summary:        Qt 6 3DQuickRender library

%description -n libQt63DQuickRender6
The Qt 6 3DQuickRender library.

%package -n qt6-3dquickrender-devel
Summary:        Development files for the Qt 6 3DQuickRender library
Requires:       libQt63DQuickRender6 = %{version}

%description -n qt6-3dquickrender-devel
Development files for the Qt 6 3DQuickRender library.

%package -n qt6-3dquickrender-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DQuickRender library
Requires:       cmake(Qt63DQuickRender) = %{real_version}

%description -n qt6-3dquickrender-private-devel
This package provides private headers of libQt63DQuickRender that do not have
any ABI or API guarantees.

%package -n libQt63DQuickScene2D6
Summary:        Qt 6 3DQuickScene2D library

%description -n libQt63DQuickScene2D6
The Qt 6 3DQuickScene2D library.

%package -n qt6-3dquickscene2d-devel
Summary:        Development files for the Qt 6 3DQuickScene2D library
Requires:       libQt63DQuickScene2D6 = %{version}

%description -n qt6-3dquickscene2d-devel
Development files for the Qt 6 3DQuickScene2D library.

%package -n qt6-3dquickscene2d-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DQuickScene2D library
Requires:       cmake(Qt63DQuickScene2D) = %{real_version}

%description -n qt6-3dquickscene2d-private-devel
This package provides private headers of libQt63DQuickScene2D that do not have
any ABI or API guarantees.

%package -n libQt63DRender6
Summary:        Qt 6 3DRender library

%description -n libQt63DRender6
The Qt 6 3DRender library.

%package -n qt6-3drender-devel
Summary:        Development files for the Qt 6 3DRender library
Requires:       libQt63DRender6 = %{version}

%description -n qt6-3drender-devel
Development files for the Qt 6 3DRender library.

%package -n qt6-3drender-private-devel
Summary:        Non-ABI stable API for the Qt 6 3DRender library
Requires:       cmake(Qt63DRender) = %{real_version}

%description -n qt6-3drender-private-devel
This package provides private headers of libQt63DRender that do not have any
ABI or API guarantees.

%package imports
Summary:        Qt 6 3D Library - QML imports
%requires_ge    libQt6Quick6
Supplements:    (libQt63DCore6 and libQt6Quick6)

%description imports
Qt 6 3D QML imports.

%{qt6_examples_package}
%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# Empty file used for the meta packages
touch meta_package

%build
# -flto breaks CONFIG += resources_big (QTBUG-73834), but resources_big is
# needed to prevent excessive memory use.
# The error is visible when building the 'planets-qml' example.
%define _lto_cflags %{nil}

%cmake_qt6 \
  -DQT_FEATURE_qt3d_system_assimp=ON

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# Unneeded files related to plugins
rm -fr %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%post -n libQt63DAnimation6 -p /sbin/ldconfig
%postun -n libQt63DAnimation6 -p /sbin/ldconfig
%post -n libQt63DCore6 -p /sbin/ldconfig
%postun -n libQt63DCore6 -p /sbin/ldconfig
%post -n libQt63DExtras6 -p /sbin/ldconfig
%postun -n libQt63DExtras6 -p /sbin/ldconfig
%post -n libQt63DInput6 -p /sbin/ldconfig
%postun -n libQt63DInput6 -p /sbin/ldconfig
%post -n libQt63DLogic6 -p /sbin/ldconfig
%postun -n libQt63DLogic6 -p /sbin/ldconfig
%post -n libQt63DQuick6 -p /sbin/ldconfig
%postun -n libQt63DQuick6 -p /sbin/ldconfig
%post -n libQt63DQuickAnimation6 -p /sbin/ldconfig
%postun -n libQt63DQuickAnimation6 -p /sbin/ldconfig
%post -n libQt63DQuickExtras6 -p /sbin/ldconfig
%postun -n libQt63DQuickExtras6 -p /sbin/ldconfig
%post -n libQt63DQuickInput6 -p /sbin/ldconfig
%postun -n libQt63DQuickInput6 -p /sbin/ldconfig
%post -n libQt63DQuickRender6 -p /sbin/ldconfig
%postun -n libQt63DQuickRender6 -p /sbin/ldconfig
%post -n libQt63DQuickScene2D6 -p /sbin/ldconfig
%postun -n libQt63DQuickScene2D6 -p /sbin/ldconfig
%post -n libQt63DRender6 -p /sbin/ldconfig
%postun -n libQt63DRender6 -p /sbin/ldconfig

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files -n libQt63DAnimation6
%{_qt6_libdir}/libQt63DAnimation.so.*

%files -n qt6-3danimation-devel
%{_qt6_cmakedir}/Qt63DAnimation/
%{_qt6_descriptionsdir}/3DAnimation.json
%{_qt6_includedir}/Qt3DAnimation/
%{_qt6_libdir}/libQt63DAnimation.prl
%{_qt6_libdir}/libQt63DAnimation.so
%{_qt6_mkspecsdir}/modules/qt_lib_3danimation.pri
%exclude %{_qt6_includedir}/Qt3DAnimation/%{real_version}

%files -n qt6-3danimation-private-devel
%{_qt6_includedir}/Qt3DAnimation/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3danimation_private.pri

%files -n libQt63DCore6
%license LICENSE.*
%{_qt6_libdir}/libQt63DCore.so.*

%files -n qt6-3dcore-devel
%dir %{_qt6_cmakedir}/Qt6
%{_qt6_cmakedir}/Qt6/FindWrapAssimp.cmake
%{_qt6_cmakedir}/Qt63DCore/
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/Qt3DTestsConfig.cmake
%{_qt6_descriptionsdir}/3DCore.json
%{_qt6_includedir}/Qt3DCore/
%{_qt6_libdir}/libQt63DCore.prl
%{_qt6_libdir}/libQt63DCore.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dcore.pri
%exclude %{_qt6_includedir}/Qt3DCore/%{real_version}

%files -n qt6-3dcore-private-devel
%{_qt6_includedir}/Qt3DCore/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dcore_private.pri

%files -n libQt63DExtras6
%{_qt6_libdir}/libQt63DExtras.so.*

%files -n qt6-3dextras-devel
%{_qt6_cmakedir}/Qt63DExtras/
%{_qt6_descriptionsdir}/3DExtras.json
%{_qt6_includedir}/Qt3DExtras/
%{_qt6_libdir}/libQt63DExtras.prl
%{_qt6_libdir}/libQt63DExtras.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dextras.pri
%exclude %{_qt6_includedir}/Qt3DExtras/%{real_version}

%files -n qt6-3dextras-private-devel
%{_qt6_includedir}/Qt3DExtras/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dextras_private.pri

%files -n libQt63DInput6
%{_qt6_libdir}/libQt63DInput.so.*

%files -n qt6-3dinput-devel
%{_qt6_cmakedir}/Qt63DInput/
%{_qt6_descriptionsdir}/3DInput.json
%{_qt6_includedir}/Qt3DInput/
%{_qt6_libdir}/libQt63DInput.prl
%{_qt6_libdir}/libQt63DInput.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dinput.pri
%exclude %{_qt6_includedir}/Qt3DInput/%{real_version}

%files -n qt6-3dinput-private-devel
%{_qt6_includedir}/Qt3DInput/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dinput_private.pri

%files -n libQt63DLogic6
%{_qt6_libdir}/libQt63DLogic.so.*

%files -n qt6-3dlogic-devel
%{_qt6_cmakedir}/Qt63DLogic/
%{_qt6_descriptionsdir}/3DLogic.json
%{_qt6_includedir}/Qt3DLogic/
%{_qt6_libdir}/libQt63DLogic.prl
%{_qt6_libdir}/libQt63DLogic.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dlogic.pri
%exclude %{_qt6_includedir}/Qt3DLogic/%{real_version}

%files -n qt6-3dlogic-private-devel
%{_qt6_includedir}/Qt3DLogic/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dlogic_private.pri

%files -n libQt63DQuick6
%{_qt6_libdir}/libQt63DQuick.so.*

%files -n qt6-3dquick-devel
%{_qt6_cmakedir}/Qt63DQuick/
%{_qt6_descriptionsdir}/3DQuick.json
%{_qt6_includedir}/Qt3DQuick/
%{_qt6_libdir}/libQt63DQuick.prl
%{_qt6_libdir}/libQt63DQuick.so
%{_qt6_metatypesdir}/qt63dquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_3dquick.pri
%exclude %{_qt6_includedir}/Qt3DQuick/%{real_version}

%files -n qt6-3dquick-private-devel
%{_qt6_includedir}/Qt3DQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dquick_private.pri

%files -n libQt63DQuickAnimation6
%{_qt6_libdir}/libQt63DQuickAnimation.so.*

%files -n qt6-3dquickanimation-devel
%{_qt6_cmakedir}/Qt63DQuickAnimation/
%{_qt6_descriptionsdir}/3DQuickAnimation.json
%{_qt6_includedir}/Qt3DQuickAnimation/
%{_qt6_libdir}/libQt63DQuickAnimation.prl
%{_qt6_libdir}/libQt63DQuickAnimation.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickanimation.pri
%exclude %{_qt6_includedir}/Qt3DQuickAnimation/%{real_version}

%files -n qt6-3dquickanimation-private-devel
%{_qt6_includedir}/Qt3DQuickAnimation/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickanimation_private.pri

%files -n libQt63DQuickExtras6
%{_qt6_libdir}/libQt63DQuickExtras.so.*

%files -n qt6-3dquickextras-devel
%{_qt6_cmakedir}/Qt63DQuickExtras/
%{_qt6_descriptionsdir}/3DQuickExtras.json
%{_qt6_includedir}/Qt3DQuickExtras/
%{_qt6_libdir}/libQt63DQuickExtras.prl
%{_qt6_libdir}/libQt63DQuickExtras.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickextras.pri
%exclude %{_qt6_includedir}/Qt3DQuickExtras/%{real_version}

%files -n qt6-3dquickextras-private-devel
%{_qt6_includedir}/Qt3DQuickExtras/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickextras_private.pri

%files -n libQt63DQuickInput6
%{_qt6_libdir}/libQt63DQuickInput.so.*

%files -n qt6-3dquickinput-devel
%{_qt6_cmakedir}/Qt63DQuickInput/
%{_qt6_descriptionsdir}/3DQuickInput.json
%{_qt6_includedir}/Qt3DQuickInput/
%{_qt6_libdir}/libQt63DQuickInput.prl
%{_qt6_libdir}/libQt63DQuickInput.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickinput.pri
%exclude %{_qt6_includedir}/Qt3DQuickInput/%{real_version}

%files -n qt6-3dquickinput-private-devel
%{_qt6_includedir}/Qt3DQuickInput/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickinput_private.pri

%files -n libQt63DQuickRender6
%{_qt6_libdir}/libQt63DQuickRender.so.*

%files -n qt6-3dquickrender-devel
%{_qt6_cmakedir}/Qt63DQuickRender/
%{_qt6_descriptionsdir}/3DQuickRender.json
%{_qt6_includedir}/Qt3DQuickRender/
%{_qt6_libdir}/libQt63DQuickRender.prl
%{_qt6_libdir}/libQt63DQuickRender.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickrender.pri
%exclude %{_qt6_includedir}/Qt3DQuickRender/%{real_version}

%files -n qt6-3dquickrender-private-devel
%{_qt6_includedir}/Qt3DQuickRender/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickrender_private.pri

%files -n libQt63DQuickScene2D6
%{_qt6_libdir}/libQt63DQuickScene2D.so.*
# TODO move plugins elsewhere?
%{_qt6_pluginsdir}/renderplugins/

%files -n qt6-3dquickscene2d-devel
%{_qt6_cmakedir}/Qt63DQuickScene2D/
%{_qt6_descriptionsdir}/3DQuickScene2D.json
%{_qt6_includedir}/Qt3DQuickScene2D/
%{_qt6_libdir}/libQt63DQuickScene2D.prl
%{_qt6_libdir}/libQt63DQuickScene2D.so
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickscene2d.pri
%exclude %{_qt6_includedir}/Qt3DQuickScene2D/%{real_version}

%files -n qt6-3dquickscene2d-private-devel
%{_qt6_includedir}/Qt3DQuickScene2D/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3dquickscene2d_private.pri

%files -n libQt63DRender6
%{_qt6_libdir}/libQt63DRender.so.*
# TODO move plugins elsewhere?
%{_qt6_pluginsdir}/geometryloaders/
%{_qt6_pluginsdir}/sceneparsers/
%{_qt6_pluginsdir}/renderers/

%files -n qt6-3drender-devel
%{_qt6_cmakedir}/Qt63DRender/
%{_qt6_descriptionsdir}/3DRender.json
%{_qt6_includedir}/Qt3DRender/
%{_qt6_libdir}/libQt63DRender.prl
%{_qt6_libdir}/libQt63DRender.so
%{_qt6_mkspecsdir}/modules/qt_lib_3drender.pri
%exclude %{_qt6_includedir}/Qt3DRender/%{real_version}

%files -n qt6-3drender-private-devel
%{_qt6_includedir}/Qt3DRender/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_3drender_private.pri

%files imports
%{_qt6_qmldir}/Qt3D/
%{_qt6_qmldir}/QtQuick/

%endif

%changelog
