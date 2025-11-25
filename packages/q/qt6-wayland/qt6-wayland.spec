#
# spec file for package qt6-wayland
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define real_version 6.10.1
%define short_version 6.10
%define tar_name qtwayland-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
# Private QML imports
%global __requires_exclude qt6qmlimport\\(io\\.qt\\.examples.*
#
%ifnarch %{arm} aarch64
%global with_opengl 1
%endif
Name:           qt6-wayland%{?pkg_suffix}
Version:        6.10.1
Release:        0
Summary:        Qt 6 Wayland libraries and tools
# The wayland compositor files are GPL-3.0-or-later
License:        (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-or-later) AND GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-wayland-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-platformsupport-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6GuiPrivate) = %{real_version}
BuildRequires:  cmake(Qt6OpenGL) = %{real_version}
BuildRequires:  cmake(Qt6OpenGLPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6QmlPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Svg) = %{real_version}
BuildRequires:  cmake(Qt6WaylandClientPrivate) = %{real_version}
BuildRequires:  cmake(Qt6WaylandGlobalPrivate) = %{real_version}
BuildRequires:  cmake(Qt6WaylandScannerTools) = %{real_version}
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

%package integration
Summary:        Qt 6 Wayland integration
# Some plugins and libraries were moved from qt6-wayland to qt6-base
Conflicts:      qt6-wayland < 6.10.0

%description integration
Qt 6 Wayland integration plugins.

%package decoration-client-adwaita
Summary:        GNOME-like client-side decoration plugin
# Split from qt6-wayland-integration immediately after 6.10.0 release
# TODO: drop after 6.11 release
Conflicts: qt6-wayland-integration < %{version}-%{release}

%description  decoration-client-adwaita
This package provides a client-side decoration plugin implementing GNOME's
Adwaita style.

%package devel
Summary:        Qt6 Wayland development meta package
Requires:       cmake(Qt6WaylandCompositor) = %{real_version}

%description devel
This meta-package requires all the qt6-wayland development packages.

%package private-devel
Summary:        Qt6 wayland unstable ABI meta package
Requires:       cmake(Qt6WaylandCompositorPrivate) = %{real_version}
Requires:       cmake(Qt6WaylandEglCompositorHwIntegrationPrivate) = %{real_version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-wayland development packages that do not
have any ABI or API guarantees.

%package imports
Summary:        Qt 6 Wayland QML files and plugins

%description imports
QML files and plugins from the Qt 6 Wayland module

%package -n libQt6WaylandCompositor6
Summary:        Qt 6 WaylandCompositor library

%description -n libQt6WaylandCompositor6
The Qt 6 WaylandCompositor library.

%package -n qt6-waylandcompositor-devel
Summary:        Development files for the Qt6 WaylandCompositor library
Requires:       libQt6WaylandCompositor6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6WaylandGlobalPrivate) = %{real_version}

%description -n qt6-waylandcompositor-devel
Development files for the Qt6 WaylandCompositor library.

%package -n qt6-waylandcompositor-private-devel
Summary:        Non-ABI stable API for the Qt6 WaylandCompositor library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6WaylandCompositor) = %{real_version}

%description -n qt6-waylandcompositor-private-devel
This package provides private headers of libQt6WaylandCompositor that do not
have any ABI or API guarantees.

### Private only libraries ###

%package -n libQt6WaylandEglCompositorHwIntegration6
Summary:        Qt 6 WaylandEglCompositorHwIntegration library

%description -n libQt6WaylandEglCompositorHwIntegration6
The Qt 6 WaylandEglCompositorHwIntegration library.
This library does not have any ABI or API guarantees.

%package -n qt6-waylandeglcompositorhwintegration-private-devel
Summary:        Qt 6 WaylandEglCompositorHwIntegration library - Development files
Requires:       libQt6WaylandEglCompositorHwIntegration6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6WaylandCompositorPrivate) = %{real_version}

%description -n qt6-waylandeglcompositorhwintegration-private-devel
Development files for the Qt 6 WaylandEglCompositorHwIntegration library.
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
%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# .CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin{AdditionalTargetInfo,Config,Targets}*.cmake

# Shouldn't be needed by anything but qtwayland itself
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6WaylandClientFeaturesPrivate
rm %{buildroot}%{_qt6_descriptionsdir}/WaylandClientFeaturesPrivate.json
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_waylandclientfeatures_private.pri

# W: hidden-file-or-dir
find %{buildroot}%{_qt6_examplesdir} -name ".gitignore" -delete

%ldconfig_scriptlets -n libQt6WaylandCompositor6
%ldconfig_scriptlets -n libQt6WaylandEglCompositorHwIntegration6

%files integration
%{_qt6_pluginsdir}/wayland-graphics-integration-server/
%{_qt6_pluginsdir}/wayland-shell-integration

%files decoration-client-adwaita
%dir %{_qt6_pluginsdir}/wayland-decoration-client/
%{_qt6_pluginsdir}/wayland-decoration-client/libadwaita.so

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files imports
%{_qt6_qmldir}/QtWayland/

%files -n libQt6WaylandCompositor6
%license LICENSES/*
%{_qt6_libdir}/libQt6WaylandCompositor.so.*
%{_qt6_libdir}/libQt6WaylandCompositorIviapplication.so.*
%{_qt6_libdir}/libQt6WaylandCompositorPresentationTime.so.*
%{_qt6_libdir}/libQt6WaylandCompositorWLShell.so.*
%{_qt6_libdir}/libQt6WaylandCompositorXdgShell.so.*

%files -n qt6-waylandcompositor-devel
%{_qt6_cmakedir}/Qt6/FindWaylandkms.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtWaylandTestsConfig.cmake
%{_qt6_cmakedir}/Qt6WaylandCompositor/
%{_qt6_cmakedir}/Qt6WaylandCompositorIviapplication/
%{_qt6_cmakedir}/Qt6WaylandCompositorPresentationTime/
%{_qt6_cmakedir}/Qt6WaylandCompositorWLShell/
%{_qt6_cmakedir}/Qt6WaylandCompositorXdgShell/
%{_qt6_descriptionsdir}/WaylandCompositor.json
%{_qt6_descriptionsdir}/WaylandCompositorIviapplication.json
%{_qt6_descriptionsdir}/WaylandCompositorPresentationTime.json
%{_qt6_descriptionsdir}/WaylandCompositorWLShell.json
%{_qt6_descriptionsdir}/WaylandCompositorXdgShell.json
%{_qt6_includedir}/QtWaylandCompositor/
# TODO private?
%{_qt6_includedir}/QtWaylandCompositorIviapplication/
# TODO private?
%{_qt6_includedir}/QtWaylandCompositorPresentationTime/
# TODO private?
%{_qt6_includedir}/QtWaylandCompositorWLShell/
# TODO private?
%{_qt6_includedir}/QtWaylandCompositorXdgShell/
%{_qt6_libdir}/libQt6WaylandCompositor.prl
%{_qt6_libdir}/libQt6WaylandCompositor.so
%{_qt6_libdir}/libQt6WaylandCompositorIviapplication.prl
%{_qt6_libdir}/libQt6WaylandCompositorIviapplication.so
%{_qt6_libdir}/libQt6WaylandCompositorPresentationTime.prl
%{_qt6_libdir}/libQt6WaylandCompositorPresentationTime.so
%{_qt6_libdir}/libQt6WaylandCompositorWLShell.prl
%{_qt6_libdir}/libQt6WaylandCompositorWLShell.so
%{_qt6_libdir}/libQt6WaylandCompositorXdgShell.prl
%{_qt6_libdir}/libQt6WaylandCompositorXdgShell.so
%{_qt6_metatypesdir}/qt6waylandcompositor_metatypes.json
%{_qt6_metatypesdir}/qt6waylandcompositoriviapplication_metatypes.json
%{_qt6_metatypesdir}/qt6waylandcompositorpresentationtime_metatypes.json
%{_qt6_metatypesdir}/qt6waylandcompositorwlshell_metatypes.json
%{_qt6_metatypesdir}/qt6waylandcompositorxdgshell_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositor.pri
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositoriviapplication*.pri
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositorpresentationtime*.pri
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositorwlshell*.pri
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositorxdgshell*.pri
%{_qt6_pkgconfigdir}/Qt6WaylandCompositor.pc
%{_qt6_pkgconfigdir}/Qt6WaylandCompositorIviapplication.pc
%{_qt6_pkgconfigdir}/Qt6WaylandCompositorPresentationTime.pc
%{_qt6_pkgconfigdir}/Qt6WaylandCompositorWLShell.pc
%{_qt6_pkgconfigdir}/Qt6WaylandCompositorXdgShell.pc
%exclude %{_qt6_includedir}/QtWaylandCompositor/%{real_version}

%files -n qt6-waylandcompositor-private-devel
%{_qt6_cmakedir}/Qt6WaylandCompositorPrivate/
%{_qt6_cmakedir}/Qt6WaylandCompositorIviapplicationPrivate/
%{_qt6_cmakedir}/Qt6WaylandCompositorPresentationTimePrivate/
%{_qt6_cmakedir}/Qt6WaylandCompositorWLShellPrivate/
%{_qt6_cmakedir}/Qt6WaylandCompositorXdgShellPrivate/
%{_qt6_includedir}/QtWaylandCompositor/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositor_private.pri

# ### Private only libraries ###

%files -n libQt6WaylandEglCompositorHwIntegration6
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so.*

%files -n qt6-waylandeglcompositorhwintegration-private-devel
%{_qt6_cmakedir}/Qt6WaylandEglCompositorHwIntegrationPrivate/
%{_qt6_descriptionsdir}/WaylandEglCompositorHwIntegrationPrivate.json
%{_qt6_includedir}/QtWaylandEglCompositorHwIntegration/
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.prl
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so
%{_qt6_metatypesdir}/qt6waylandeglcompositorhwintegrationprivate_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_wayland_egl_compositor_hw_integration_private.pri

%endif

%changelog
