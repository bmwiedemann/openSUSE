#
# spec file for package qt6-wayland
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
Version:        6.1.0
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

%description devel
This meta-package requires all the qt6-wayland development packages.

%package private-devel
Summary:        Qt6 wayland unstable ABI meta package
Requires:       qt6-waylandclient-private-devel = %{version}
Requires:       qt6-waylandcompositor-private-devel = %{version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-wayland development packages that do not
have any ABI or API guarantees.

%package imports
Summary:        Qt 6 Wayland QML files and plugins

%description imports
QML files and plugins from the Qt 6 Wayland module

%package -n libQt6WaylandClient6
Summary:        Qt6 WaylandClient library

%description -n libQt6WaylandClient6
The Qt6 WaylandClient library.

%package -n qt6-waylandclient-devel
Summary:        Development files for the Qt6 WaylandClient library
Requires:       libQt6WaylandClient6 = %{version}
# qtwaylandscanner is required
Requires:       qt6-wayland = %{version}

%description -n qt6-waylandclient-devel
Development files for the Qt6 WaylandClient library.

%package -n qt6-waylandclient-private-devel
Summary:        Non-ABI stable API for the Qt6 WaylandClient library
Requires:       cmake(Qt6WaylandClient) = %{real_version}

%description -n qt6-waylandclient-private-devel
This package provides private headers of libQt6WaylandClient that do not have
any ABI or API guarantees.

%package -n libQt6WaylandCompositor6
Summary:        Qt6 WaylandCompositor library

%description -n libQt6WaylandCompositor6
The Qt6 WaylandCompositor library.

%package -n qt6-waylandcompositor-devel
Summary:        Development files for the Qt6 WaylandCompositor library
Requires:       libQt6WaylandCompositor6 = %{version}

%description -n qt6-waylandcompositor-devel
Development files for the Qt6 WaylandCompositor library.

%package -n qt6-waylandcompositor-private-devel
Summary:        Non-ABI stable API for the Qt6 WaylandCompositor library
Requires:       cmake(Qt6WaylandCompositor) = %{real_version}

%description -n qt6-waylandcompositor-private-devel
This package provides private headers of libQt6WaylandCompositor that do not
have any ABI or API guarantees.

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

%{qt6_link_executables}

# .CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Gui
rm -r %{buildroot}%{_qt6_cmakedir}/*/Qt6*PluginConfig*.cmake
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%post -n libQt6WaylandClient6 -p /sbin/ldconfig
%postun -n libQt6WaylandClient6 -p /sbin/ldconfig
%post -n libQt6WaylandCompositor6 -p /sbin/ldconfig
%postun -n libQt6WaylandCompositor6 -p /sbin/ldconfig

%files
%license LICENSE.*
%dir %{_qt6_pluginsdir}/platforms
%{_bindir}/qtwaylandscanner6
%{_qt6_bindir}/qtwaylandscanner
%{_qt6_pluginsdir}/platforms/libqwayland-*.so
%{_qt6_pluginsdir}/wayland-decoration-client
%{_qt6_pluginsdir}/wayland-graphics-integration-client
%{_qt6_pluginsdir}/wayland-graphics-integration-server
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
%{_qt6_cmakedir}/Qt6/FindXComposite.cmake
%{_qt6_cmakedir}/Qt6WaylandClient/
%{_qt6_cmakedir}/Qt6WaylandScannerTools/
%{_qt6_descriptionsdir}/WaylandClient.json
%{_qt6_includedir}/QtWaylandClient
%{_qt6_libdir}/libQt6WaylandClient.prl
%{_qt6_libdir}/libQt6WaylandClient.so
%{_qt6_mkspecsdir}/modules/qt_lib_waylandclient.pri
%exclude %{_qt6_includedir}/QtWaylandClient/%{real_version}

%files -n qt6-waylandclient-private-devel
%{_qt6_includedir}/QtWaylandClient/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_waylandclient_private.pri

%files -n libQt6WaylandCompositor6
%{_qt6_libdir}/libQt6WaylandCompositor.so.*

%files -n qt6-waylandcompositor-devel
%{_qt6_cmakedir}/Qt6WaylandCompositor/
%{_qt6_descriptionsdir}/WaylandCompositor.json
%{_qt6_includedir}/QtWaylandCompositor
%{_qt6_libdir}/libQt6WaylandCompositor.prl
%{_qt6_libdir}/libQt6WaylandCompositor.so
%{_qt6_metatypesdir}/qt6waylandcompositor_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositor.pri
%exclude %{_qt6_includedir}/QtWaylandCompositor/%{real_version}

%files -n qt6-waylandcompositor-private-devel
%{_qt6_includedir}/QtWaylandCompositor/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_waylandcompositor_private.pri

%endif

%changelog
