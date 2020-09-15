#
# spec file for package libqt5-qt3d
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


%define qt5_snapshot 0
%define libname libQt53DCore5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qt3d-everywhere-src-5.15.1
Name:           libqt5-qt3d
Version:        5.15.1
Release:        0
Summary:        Qt 5 3D Addon
# Legal: some files are GPL-3.0-only WITH Qt-GPL-exception-1.0
# The exception allows using these files under the license of the larger project
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libQt5Bootstrap-devel-static >= %{version}
BuildRequires:  libQt5Concurrent-devel >= %{version}
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libQt5OpenGLExtensions-devel-static >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(zlib)

%description
Qt is a set of libraries for developing applications.

Qt 3D provides functionality for near-realtime simulation
systems with support for 2D and 3D rendering in both Qt C++ and Qt Quick applications.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5
# Removed in Qt3D 5.6
Provides:       libQt53dCollision5 = %{version}
Obsoletes:      libQt53dCollision5 < %{version}

%description -n %{libname}
Qt is a set of libraries for developing applications.

Qt 3D provides functionality for near-realtime simulation
systems with support for 2D and 3D rendering in both Qt C++ and Qt Quick applications.

%package -n libQt53DInput5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DInput5
Qt is a set of libraries for developing applications.

The Qt 3D Input module provides classes for handling user input in
applications using Qt3D.

%package -n libQt53DQuick5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DQuick5
Qt is a set of libraries for developing applications.

This package provides core Qt 3D QML types.

%package -n libQt53DQuickRender5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5
Provides:       libQt53DQuickRenderer5 = %{version}
Obsoletes:      libQt53DQuickRenderer5 < %{version}

%description -n libQt53DQuickRender5
Qt is a set of libraries for developing applications.

This package provides Qt 3D QML types for rendering.

%package -n libQt53DRender5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5
Provides:       libQt53DRenderer5 = %{version}
Obsoletes:      libQt53DRenderer5 < %{version}

%description -n libQt53DRender5
Qt is a set of libraries for developing applications.

The Qt 3D Render module contains functionality to support 2D and 3D
rendering using Qt 3D.

%package -n libQt53DQuickInput5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DQuickInput5
Qt is a set of libraries for developing applications.

Qt 3D provides functionality for near-realtime simulation
systems with support for 2D and 3D rendering in both Qt C++ and Qt Quick applications.

%package -n libQt53DLogic5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DLogic5
Qt is a set of libraries for developing applications.

Qt 3D Logic module enables synchronizing frames with the Qt 3D
backend.

%package -n libQt53DExtras5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DExtras5
Qt is a set of libraries for developing applications.

Qt 3D provides functionality for near-realtime simulation
systems with support for 2D and 3D rendering in both Qt C++ and Qt Quick applications.

%package -n libQt53DQuickExtras5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DQuickExtras5
Qt is a set of libraries for developing applications.

This Qt 3D module contains functionality to support near-realtime
simulation systems.

%package -n libQt53DAnimation5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DAnimation5
Qt is a set of libraries for developing applications.

This Qt 3D module contains functionality to support near-realtime
simulation systems.

%package -n libQt53DQuickAnimation5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DQuickAnimation5
Qt is a set of libraries for developing applications.

This Qt 3D module contains functionality to support near-realtime
simulation systems.

%package -n libQt53DQuickScene2D5
Summary:        Qt 5 3D Addon
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n libQt53DQuickScene2D5
Qt is a set of libraries for developing applications.

This Qt 3D module contains functionality to support near-realtime
simulation systems.

%package imports
Summary:        Qt 5 3D Library - QML imports
Group:          Development/Libraries/X11
%requires_ge    libQtQuick5
Supplements:    (%{libname} and libQtQuick5)

%description imports
Qt is a set of libraries for developing applications.

This Qt 3D module contains functionality to support near-realtime
simulation systems.

%package examples
Summary:        Qt5 3D examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qt3d module.

%package tools
Summary:        Qt5 3D tools
Group:          Development/Libraries/X11
Recommends:     %{name}-devel

%description tools
Tools for libqt5-qt3d module.

%package -n libQt53DCore-devel
Summary:        Development files for the Qt 5 Core 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DCore5 = %{version}

%description -n libQt53DCore-devel
Development files for the Qt 5 Core 3D library.

%package -n libQt53DInput-devel
Summary:        Development files for the Qt 5 Input 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DInput5 = %{version}

%description -n libQt53DInput-devel
Development files for the Qt 5 Input 3D library.

%package -n libQt53DQuick-devel
Summary:        Development files for the Qt 5 Quick 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DQuick5 = %{version}

%description -n libQt53DQuick-devel
Development files for the Qt 5 Quick 3D library.

%package -n libQt53DQuickRender-devel
Summary:        Development files for the Qt 5 QuickRenderer 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DQuickRender5 = %{version}
Provides:       libQt53DQuickRenderer-devel = %{version}
Obsoletes:      libQt53DQuickRenderer-devel < %{version}

%description -n libQt53DQuickRender-devel
Development files for the Qt 5 QuickRenderer 3D library.

%package -n libQt53DRender-devel
Summary:        Development files for the Qt 5 Renderer 3D library
Group:          Development/Libraries/X11
# Qt53DRenderConfig.cmake requires libscene2d.so
Requires:       libQt53DQuickScene2D5 = %{version}
Requires:       libQt53DRender5 = %{version}
Provides:       libQt53DRenderer-devel = %{version}
Obsoletes:      libQt53DRenderer-devel < %{version}

%description -n libQt53DRender-devel
Development files for the Qt 5 Renderer 3D library.

%package -n libQt53DQuickInput-devel
Summary:        Development files for the Qt 5 QuickInput 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DQuickInput5 = %{version}

%description -n libQt53DQuickInput-devel
Development files for the Qt 5 Quick Input 3D library.

%package -n libQt53DLogic-devel
Summary:        Development files for the Qt 5 Logic 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DLogic5 = %{version}

%description -n libQt53DLogic-devel
Development files for the Qt 5 Logic 3D library.

%package -n libQt53DExtras-devel
Summary:        Development files for the Qt 5 3D Extras libary
Group:          Development/Libraries/X11
Requires:       libQt53DExtras5 = %{version}

%description -n libQt53DExtras-devel
Development files for the Qt 5 3D Extras library.

%package -n libQt53DAnimation-devel
Summary:        Development files for the Qt 5 3D Animation library
Group:          Development/Libraries/X11
Requires:       libQt53DAnimation5 = %{version}

%description -n libQt53DAnimation-devel
Development files for the Qt 5 3D Animation library.

%package -n libQt53DQuickAnimation-devel
Summary:        Development files for the Qt 5 3D Quick Animation library
Group:          Development/Libraries/X11
Requires:       libQt53DQuickAnimation5 = %{version}

%description -n libQt53DQuickAnimation-devel
Development files for the Qt 5 3D Quick Animation library.

%package -n libQt53DQuickScene2D-devel
Summary:        Development files for the Qt 5 3D Quick Scene 2D library
Group:          Development/Libraries/X11
Requires:       libQt53DQuickScene2D5 = %{version}

%description -n libQt53DQuickScene2D-devel
Development files for the Qt 5 3D Quick Scene 2D library.

%package -n libQt53DQuickExtras-devel
Summary:        Development files for the Qt 5 3D QuickExtras library
Group:          Development/Libraries/X11
Requires:       libQt53DQuickExtras5 = %{version}

%description -n libQt53DQuickExtras-devel
Development files for the Qt 5 Logic 3D library.

%package devel
Summary:        Development files for the Qt5 3D library
Group:          Development/Libraries/X11
Requires:       libQt53DAnimation-devel = %{version}
Requires:       libQt53DCore-devel = %{version}
Requires:       libQt53DExtras-devel = %{version}
Requires:       libQt53DInput-devel = %{version}
Requires:       libQt53DLogic-devel = %{version}
Requires:       libQt53DQuick-devel = %{version}
Requires:       libQt53DQuickAnimation-devel = %{version}
Requires:       libQt53DQuickExtras-devel = %{version}
Requires:       libQt53DQuickInput-devel = %{version}
Requires:       libQt53DQuickRender-devel = %{version}
Requires:       libQt53DQuickScene2D-devel = %{version}
Requires:       libQt53DRender-devel = %{version}
# Removed in Qt3D 5.6
Provides:       libQt53dCollision-devel = %{version}
Obsoletes:      libQt53dCollision-devel < %{version}

%description devel
You need this package if you want to compile programs with qt3d.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 3D library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
Requires:       libQt5Gui-private-headers-devel >= %{version}
Requires:       libQt5OpenGLExtensions-devel-static >= %{version}
Requires:       libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qt3d that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n libQt53DInput5 -p /sbin/ldconfig
%postun -n libQt53DInput5 -p /sbin/ldconfig
%post -n libQt53DQuick5 -p /sbin/ldconfig
%postun -n libQt53DQuick5 -p /sbin/ldconfig
%post -n libQt53DQuickRender5 -p /sbin/ldconfig
%postun -n libQt53DQuickRender5 -p /sbin/ldconfig
%post -n libQt53DRender5 -p /sbin/ldconfig
%postun -n libQt53DRender5 -p /sbin/ldconfig
%post -n libQt53DQuickInput5 -p /sbin/ldconfig
%postun -n libQt53DQuickInput5 -p /sbin/ldconfig
%post -n libQt53DLogic5 -p /sbin/ldconfig
%postun -n libQt53DLogic5 -p /sbin/ldconfig
%post -n libQt53DExtras5 -p /sbin/ldconfig
%postun -n libQt53DExtras5 -p /sbin/ldconfig
%post -n libQt53DAnimation5 -p /sbin/ldconfig
%postun -n libQt53DAnimation5 -p /sbin/ldconfig
%post -n libQt53DQuickAnimation5 -p /sbin/ldconfig
%postun -n libQt53DQuickAnimation5 -p /sbin/ldconfig
%post -n libQt53DQuickScene2D5 -p /sbin/ldconfig
%postun -n libQt53DQuickScene2D5 -p /sbin/ldconfig
%post -n libQt53DQuickExtras5 -p /sbin/ldconfig
%postun -n libQt53DQuickExtras5 -p /sbin/ldconfig

%build
# -flto breaks CONFIG += resources_big (QTBUG-73834), but resources_big is needed to prevent excessive memory use
%define _lto_cflags %{nil}
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%fdupes %{buildroot}
# put all the binaries to %%_bindir and symlink them back to %%_qt5_bindir
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
      mv $i ../../../bin/
      ln -s ../../../bin/$i .
done
popd

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DCore.so.*

%files -n libQt53DInput5
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DInput.so.*

%files -n libQt53DQuick5
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuick.so.*

%files -n libQt53DQuickRender5
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickRender.so.*

%files -n libQt53DRender5
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DRender.so.*
%dir %{_libqt5_libdir}/qt5/plugins/sceneparsers
%{_libqt5_libdir}/qt5/plugins/sceneparsers/libgltfsceneimport.so
%{_libqt5_libdir}/qt5/plugins/sceneparsers/libgltfsceneexport.so
%if 0%{?suse_version} >= 1500
%{_libqt5_libdir}/qt5/plugins/sceneparsers/libassimpsceneimport.so
%endif
%dir %{_libqt5_libdir}/qt5/plugins/geometryloaders
%{_libqt5_libdir}/qt5/plugins/geometryloaders/libdefaultgeometryloader.so
%{_libqt5_libdir}/qt5/plugins/geometryloaders/libgltfgeometryloader.so
%dir %{_libqt5_libdir}/qt5/plugins/renderers
%{_libqt5_libdir}/qt5/plugins/renderers/libopenglrenderer.so

%files -n libQt53DQuickInput5
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickInput.so.*

%files -n libQt53DLogic5
%defattr(-,root,root,755)
%{_libqt5_libdir}/libQt53DLogic.so.*
%license LICENSE.*

%files -n libQt53DExtras5
%license LICENSE.*
%{_libqt5_libdir}/libQt53DExtras.so.*

%files -n libQt53DAnimation5
%license LICENSE.*
%{_libqt5_libdir}/libQt53DAnimation.so.*

%files -n libQt53DQuickAnimation5
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickAnimation.so.*

%files -n libQt53DQuickScene2D5
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickScene2D.so.*
%dir %{_libqt5_libdir}/qt5/plugins/renderplugins
%{_libqt5_libdir}/qt5/plugins/renderplugins/libscene2d.so

%files -n libQt53DQuickExtras5
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickExtras.so.*

%files imports
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/*/

%files tools
%defattr(-,root,root,755)
%license LICENSE.*
%{_bindir}/qgltf
%{_libqt5_bindir}/qgltf

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%files -n libQt53DCore-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DCore.so
%{_libqt5_libdir}/libQt53DCore.prl
%{_libqt5_libdir}/cmake/Qt53DCore/
%{_libqt5_libdir}/pkgconfig/Qt53DCore.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dcore.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dcore_private.pri
%{_libqt5_includedir}/Qt3DCore/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DInput-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DInput.so
%{_libqt5_libdir}/libQt53DInput.prl
%{_libqt5_libdir}/cmake/Qt53DInput/
%{_libqt5_libdir}/pkgconfig/Qt53DInput.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dinput.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dinput_private.pri
%{_libqt5_includedir}/Qt3DInput/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DQuick-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuick.so
%{_libqt5_libdir}/libQt53DQuick.prl
%{_libqt5_libdir}/cmake/Qt53DQuick/
%{_libqt5_libdir}/pkgconfig/Qt53DQuick.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquick.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquick_private.pri
%{_libqt5_includedir}/Qt3DQuick/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DQuickRender-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt3DQuickRender/
%{_libqt5_libdir}/cmake/Qt53DQuickRender/
%{_libqt5_libdir}/libQt53DQuickRender.so
%{_libqt5_libdir}/libQt53DQuickRender.prl
%{_libqt5_libdir}/pkgconfig/Qt53DQuickRender.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickrender.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickrender_private.pri
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DQuickInput-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt3DQuickInput/
%{_libqt5_libdir}/libQt53DQuickInput.so
%{_libqt5_libdir}/libQt53DQuickInput.prl
%{_libqt5_libdir}/cmake/Qt53DQuickInput/
%{_libqt5_libdir}/pkgconfig/Qt53DQuickInput.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickinput.pri
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DRender-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt3DRender/
%{_libqt5_libdir}/cmake/Qt53DRender/
%{_libqt5_libdir}/libQt53DRender.so
%{_libqt5_libdir}/libQt53DRender.prl
%{_libqt5_libdir}/pkgconfig/Qt53DRender.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3drender_private.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3drender.pri
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DLogic-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DLogic.so
%{_libqt5_libdir}/libQt53DLogic.prl
%{_libqt5_libdir}/cmake/Qt53DLogic/
%{_libqt5_libdir}/pkgconfig/Qt53DLogic.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dlogic.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dlogic_private.pri
%{_libqt5_includedir}/Qt3DLogic/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DExtras-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DExtras.so
%{_libqt5_libdir}/libQt53DExtras.prl
%{_libqt5_libdir}/cmake/Qt53DExtras/
%{_libqt5_libdir}/pkgconfig/Qt53DExtras.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dextras.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dextras_private.pri
%{_libqt5_includedir}/Qt3DExtras/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DAnimation-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DAnimation.so
%{_libqt5_libdir}/libQt53DAnimation.prl
%{_libqt5_libdir}/cmake/Qt53DAnimation/
%{_libqt5_libdir}/pkgconfig/Qt53DAnimation.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3danimation.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3danimation_private.pri
%{_libqt5_includedir}/Qt3DAnimation/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DQuickAnimation-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickAnimation.so
%{_libqt5_libdir}/libQt53DQuickAnimation.prl
%{_libqt5_libdir}/cmake/Qt53DQuickAnimation/
%{_libqt5_libdir}/pkgconfig/Qt53DQuickAnimation.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickanimation.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{_libqt5_includedir}/Qt3DQuickAnimation/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DQuickScene2D-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickScene2D.so
%{_libqt5_libdir}/libQt53DQuickScene2D.prl
%{_libqt5_libdir}/cmake/Qt53DQuickScene2D/
%{_libqt5_libdir}/pkgconfig/Qt53DQuickScene2D.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{_libqt5_includedir}/Qt3DQuickScene2D/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files -n libQt53DQuickExtras-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt53DQuickExtras.so
%{_libqt5_libdir}/libQt53DQuickExtras.prl
%{_libqt5_libdir}/cmake/Qt53DQuickExtras/
%{_libqt5_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickextras.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{_libqt5_includedir}/Qt3DQuickExtras/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}/

%files devel
%defattr(-,root,root,755)
%license LICENSE.*

%changelog
