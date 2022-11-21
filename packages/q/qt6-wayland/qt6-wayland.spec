#
# spec file for package qt6-wayland
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
%define tar_name qtwayland-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
%ifnarch %{arm} aarch64
%global with_opengl 1
%endif
Name:           qt6-wayland%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 Wayland libraries and tools
# The wayland compositor files are GPL-3.0-or-later
License:        GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-wayland-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-opengl-private-devel
BuildRequires:  qt6-platformsupport-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt6 Wayland libraries and tools.

%if !%{qt6_docs_flavor}

%package devel
Summary:        Qt6 Wayland development meta package
Requires:       cmake(Qt6WaylandClient) = %{real_version}
Requires:       cmake(Qt6WaylandCompositor) = %{real_version}
# This package contains information on features enabled at build time
Requires:       cmake(Qt6WaylandGlobalPrivate) = %{real_version}

%description devel
This meta-package requires all the qt6-wayland development packages.

%package private-devel
Summary:        Qt6 wayland unstable ABI meta package
Requires:       qt6-waylandclient-private-devel = %{version}
Requires:       qt6-waylandcompositor-private-devel = %{version}
Requires:       cmake(Qt6WaylandEglClientHwIntegrationPrivate) = %{real_version}
Requires:       cmake(Qt6WaylandEglCompositorHwIntegrationPrivate) = %{real_version}
Requires:       cmake(Qt6WlShellIntegrationPrivate) = %{real_version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-wayland development packages that do not
have any ABI or API guarantees.

%package imports
Summary:        Qt 6 Wayland QML files and plugins

%description imports
QML files and plugins from the Qt 6 Wayland module

%package -n libQt6WaylandClient6
Summary:        Qt 6 WaylandClient library

%description -n libQt6WaylandClient6
The Qt 6 WaylandClient library.

%package -n qt6-waylandclient-devel
Summary:        Development files for the Qt 6 WaylandClient library
Requires:       libQt6WaylandClient6 = %{version}
# qtwaylandscanner is required
Requires:       qt6-wayland = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6WaylandGlobalPrivate) = %{real_version}

%description -n qt6-waylandclient-devel
Development files for the Qt6 WaylandClient library.

%package -n qt6-waylandclient-private-devel
Summary:        Non-ABI stable API for the Qt 6 WaylandClient library
Requires:       cmake(Qt6WaylandClient) = %{real_version}

%description -n qt6-waylandclient-private-devel
This package provides private headers of libQt6WaylandClient that do not have
any ABI or API guarantees.

%package -n libQt6WaylandCompositor6
Summary:        Qt 6 WaylandCompositor library

%description -n libQt6WaylandCompositor6
The Qt 6 WaylandCompositor library.

%package -n qt6-waylandcompositor-devel
Summary:        Development files for the Qt6 WaylandCompositor library
Requires:       libQt6WaylandCompositor6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6OpenGL)
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6WaylandGlobalPrivate) = %{real_version}

%description -n qt6-waylandcompositor-devel
Development files for the Qt6 WaylandCompositor library.

%package -n qt6-waylandcompositor-private-devel
Summary:        Non-ABI stable API for the Qt6 WaylandCompositor library
Requires:       cmake(Qt6WaylandCompositor) = %{real_version}

%description -n qt6-waylandcompositor-private-devel
This package provides private headers of libQt6WaylandCompositor that do not
have any ABI or API guarantees.

%package -n qt6-waylandglobal-private-devel
Summary:        Collection of build features used by qt6-wayland libraries

%description -n qt6-waylandglobal-private-devel
This package contains enabled features information shared by all the
qt6-wayland libraries.

### Private only libraries ###

%package -n libQt6WaylandEglClientHwIntegration6
Summary:        Qt 6 WaylandEglClientHwIntegration library

%description -n libQt6WaylandEglClientHwIntegration6
The Qt 6 WaylandEglClientHwIntegration  library.
This library does not have any ABI or API guarantees.

%package -n qt6-waylandeglclienthwintegration-private-devel
Summary:        Qt 6 WaylandEglClientHwIntegration library - Development files
Requires:       libQt6WaylandEglClientHwIntegration6 = %{version}
Requires:       qt6-waylandclient-private-devel = %{version}
Requires:       cmake(Qt6Gui)
%requires_eq    qt6-opengl-private-devel

%description -n qt6-waylandeglclienthwintegration-private-devel
Development files for the Qt 6 WaylandEglClientHwIntegration library.
This library does not have any ABI or API guarantees.

%package -n libQt6WaylandEglCompositorHwIntegration6
Summary:        Qt 6 WaylandEglCompositorHwIntegration library

%description -n libQt6WaylandEglCompositorHwIntegration6
The Qt 6 WaylandEglCompositorHwIntegration library.
This library does not have any ABI or API guarantees.

%package -n qt6-waylandeglcompositorhwintegration-private-devel
Summary:        Qt 6 WaylandEglCompositorHwIntegration library - Development files
Requires:       libQt6WaylandEglCompositorHwIntegration6 = %{version}
Requires:       qt6-waylandcompositor-private-devel = %{version}
Requires:       cmake(Qt6Gui)

%description -n qt6-waylandeglcompositorhwintegration-private-devel
Development files for the Qt 6 WaylandEglCompositorHwIntegration library.
This library does not have any ABI or API guarantees.

%package -n libQt6WlShellIntegration6
Summary:        Qt 6 WlShellIntegration library

%description -n libQt6WlShellIntegration6
The Qt 6 WlShellIntegration library.
This library does not have any ABI or API guarantees.

%package -n qt6-wlshellintegration-private-devel
Summary:        Qt 6 WlShellIntegration library - Development files
Requires:       libQt6WlShellIntegration6 = %{version}
Requires:       qt6-waylandclient-private-devel = %{version}
%requires_eq    qt6-gui-private-devel

%description -n qt6-wlshellintegration-private-devel
Development files for the Qt 6 WlShellIntegration library.
This library does not have any ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# Empty file used for the meta packages
cat >> meta_package << EOF
This is a meta package, it does not contain any file
EOF

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# .CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Gui
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%post -n libQt6WaylandClient6 -p /sbin/ldconfig
%post -n libQt6WaylandCompositor6 -p /sbin/ldconfig
%post -n libQt6WaylandEglClientHwIntegration6 -p /sbin/ldconfig
%post -n libQt6WaylandEglCompositorHwIntegration6 -p /sbin/ldconfig
%post -n libQt6WlShellIntegration6 -p /sbin/ldconfig
%postun -n libQt6WaylandClient6 -p /sbin/ldconfig
%postun -n libQt6WaylandCompositor6 -p /sbin/ldconfig
%postun -n libQt6WaylandEglClientHwIntegration6 -p /sbin/ldconfig
%postun -n libQt6WaylandEglCompositorHwIntegration6 -p /sbin/ldconfig
%postun -n libQt6WlShellIntegration6 -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_qt6_pluginsdir}/platforms
%{_qt6_libexecdir}/qtwaylandscanner
%{_qt6_pluginsdir}/platforms/libqwayland-*.so
%{_qt6_pluginsdir}/wayland-decoration-client/
%{_qt6_pluginsdir}/wayland-graphics-integration-client/
%{_qt6_pluginsdir}/wayland-graphics-integration-server/
%{_qt6_pluginsdir}/wayland-shell-integration

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files imports
%{_qt6_qmldir}/QtWayland/

%files -n libQt6WaylandClient6
%{_qt6_libdir}/libQt6WaylandClient.so.*

%files -n qt6-waylandclient-devel
%dir %{_qt6_cmakedir}/Qt6
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtWaylandTestsConfig.cmake
%{_qt6_cmakedir}/Qt6/FindWaylandkms.cmake
%{_qt6_cmakedir}/Qt6WaylandClient/
%{_qt6_cmakedir}/Qt6WaylandScannerTools/
%{_qt6_descriptionsdir}/WaylandClient.json
%{_qt6_includedir}/QtWaylandClient
%{_qt6_libdir}/libQt6WaylandClient.prl
%{_qt6_libdir}/libQt6WaylandClient.so
%{_qt6_metatypesdir}/qt6waylandclient_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_waylandclient.pri
%{_qt6_pkgconfigdir}/Qt6WaylandClient.pc
%exclude %{_qt6_includedir}/QtWaylandClient/%{real_version}

%files -n qt6-waylandclient-private-devel
%{_qt6_includedir}/QtWaylandClient/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_waylandclient_private.pri

%files -n libQt6WaylandCompositor6
%{_qt6_libdir}/libQt6WaylandCompositor.so.*

%files -n qt6-waylandcompositor-devel
%{_qt6_cmakedir}/Qt6WaylandCompositor/
%{_qt6_descriptionsdir}/WaylandCompositor.json
%{_qt6_includedir}/QtWaylandCompositor/
%{_qt6_libdir}/libQt6WaylandCompositor.prl
%{_qt6_libdir}/libQt6WaylandCompositor.so
%{_qt6_metatypesdir}/qt6waylandcompositor_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositor.pri
%{_qt6_pkgconfigdir}/Qt6WaylandCompositor.pc
%exclude %{_qt6_includedir}/QtWaylandCompositor/%{real_version}

%files -n qt6-waylandcompositor-private-devel
%{_qt6_includedir}/QtWaylandCompositor/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositor_private.pri

%files -n qt6-waylandglobal-private-devel
%{_qt6_cmakedir}/Qt6WaylandGlobalPrivate/
%{_qt6_descriptionsdir}/WaylandGlobalPrivate.json
%{_qt6_includedir}/QtWaylandGlobal/
%{_qt6_mkspecsdir}/modules/qt_lib_waylandglobal_private.pri

### Private only libraries ###

%files -n libQt6WaylandEglClientHwIntegration6
%{_qt6_libdir}/libQt6WaylandEglClientHwIntegration.so.*

%files -n qt6-waylandeglclienthwintegration-private-devel
%{_qt6_cmakedir}/Qt6WaylandEglClientHwIntegrationPrivate/
%{_qt6_descriptionsdir}/WaylandEglClientHwIntegrationPrivate.json
%{_qt6_includedir}/QtWaylandEglClientHwIntegration/
%{_qt6_libdir}/libQt6WaylandEglClientHwIntegration.prl
%{_qt6_libdir}/libQt6WaylandEglClientHwIntegration.so
%{_qt6_metatypesdir}/qt6waylandeglclienthwintegrationprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_wayland_egl_client_hw_integration_private.pri

%files -n libQt6WaylandEglCompositorHwIntegration6
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so.*

%files -n qt6-waylandeglcompositorhwintegration-private-devel
%{_qt6_cmakedir}/Qt6WaylandEglCompositorHwIntegrationPrivate/
%{_qt6_descriptionsdir}/WaylandEglCompositorHwIntegrationPrivate.json
%{_qt6_includedir}/QtWaylandEglCompositorHwIntegration/
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.prl
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so
%{_qt6_metatypesdir}/qt6waylandeglcompositorhwintegrationprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_wayland_egl_compositor_hw_integration_private.pri

%files -n libQt6WlShellIntegration6
%{_qt6_libdir}/libQt6WlShellIntegration.so.*

%files -n qt6-wlshellintegration-private-devel
%{_qt6_cmakedir}/Qt6WlShellIntegrationPrivate/
%{_qt6_descriptionsdir}/WlShellIntegrationPrivate.json
%{_qt6_includedir}/QtWlShellIntegration/
%{_qt6_libdir}/libQt6WlShellIntegration.prl
%{_qt6_libdir}/libQt6WlShellIntegration.so
%{_qt6_metatypesdir}/qt6wlshellintegrationprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_wl_shell_integration_private.pri

%endif

%changelog
