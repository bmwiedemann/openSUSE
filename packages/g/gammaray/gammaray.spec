#
# spec file for package gammaray
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define qt_suffix 6
%define qt_min_version 6.3
%else
%define qt5 1
%define qt_suffix 5
%define qt_min_version 5.15
%endif
%define rname gammaray
%define short_version 3.1
%define soversion 3_1_0
Name:           gammaray%{?pkg_suffix}
Version:        3.1.0
Release:        0
Summary:        Introspection/Debugging Tool for Qt Applications
License:        GPL-2.0-or-later
URL:            https://www.kdab.com/gammaray
Source:         https://github.com/KDAB/GammaRay/releases/download/v%{version}/%{rname}-%{version}.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  cmake >= 3.16.0
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz-gnome
# include this so the icon folders don't need to be owned by the package
BuildRequires:  hicolor-icon-theme
BuildRequires:  libdw-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt%{qt_suffix}3DAnimation) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}3DExtras) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}3DInput) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}3DLogic) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}3DQuick) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}3DRender) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Bluetooth) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Concurrent) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Designer) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Help) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}LinguistTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Network) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}OpenGL) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Positioning) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Qml) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Quick) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}QuickWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Scxml) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Svg) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Test) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}WaylandCompositor) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Widgets) >= %{qt_min_version}
BuildRequires:  pkgconfig(wayland-server)
Requires:       %{name}-shared-plugins = %{version}
%if 0%{?qt5}
BuildRequires:  libQt5Core-private-headers-devel >= %{qt_min_version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt_min_version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qtscxml-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qttools-doc >= %{qt_min_version}
# No Qt6 support in current release
BuildRequires:  cmake(KDSME)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(Qt5AttributionsScannerTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Location) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Script) >= %{qt_min_version}
BuildRequires:  cmake(Qt5ScriptTools) >= %{qt_min_version}
Recommends:     gammaray-qt6-shared-plugins = %{version}
%ifnarch ppc64 ppc64le s390 s390x
BuildRequires:  cmake(Qt5WebEngineWidgets) >= %{qt_min_version}
%endif
%endif
%if 0%{?qt6}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150600
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6SyntaxHighlighting)
%endif
BuildRequires:  qt6-core-private-devel >= %{qt_min_version}
BuildRequires:  qt6-gui-private-devel >= %{qt_min_version}
BuildRequires:  qt6-qml-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick-private-devel >= %{qt_min_version}
# Needed to build the statemachine examples
BuildRequires:  qt6-scxml-imports >= %{qt_min_version}
BuildRequires:  qt6-scxml-private-devel >= %{qt_min_version}
BuildRequires:  qt6-statemachine-private-devel >= %{qt_min_version}
BuildRequires:  qt6-widgets-private-devel >= %{qt_min_version}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150500
BuildRequires:  cmake(Qt6Location) >= %{qt_min_version}
%endif
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt_min_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt_min_version}
Recommends:     gammaray-shared-plugins = %{version}
Conflicts:      gammaray
%ifnarch %{ix86} %{arm} ppc64 ppc64le s390 s390x
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt_min_version}
%endif
%endif
# Pull in the correct set of shared libraries (Qt5/Qt6)
Requires:       libgammaray%{?pkg_suffix}-%{soversion} >= %{version}

%description
Gamma Ray is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt.

%package shared-plugins
Summary:        Shared plugins and libraries
Requires:       (gammaray = %{version} or gammaray-qt6 = %{version})

%description shared-plugins
This package ships libraries and plugins built with a different Qt version.
There are required in order to inspect executables built with different
Qt versions.

%package -n libgammaray%{?pkg_suffix}-%{soversion}
Summary:        Gammaray libraries
%if 0%{?qt6}
Conflicts:      libgammaray-%{soversion}
%endif

%description -n libgammaray%{?pkg_suffix}-%{soversion}
Gammaray libraries.

%package -n libgammaray-shared%{?pkg_suffix}-%{soversion}
Summary:        Shared Gammaray libraries used by either gammaray or gammaray-qt6

%description -n libgammaray-shared%{?pkg_suffix}-%{soversion}
This package provides libraries required by %{name}-shared-plugins

%package devel
Summary:        Introspection/Debugging Tool for Qt Applications
Requires:       libgammaray%{?pkg_suffix}-%{soversion}
Requires:       libgammaray-shared%{?pkg_suffix}-%{soversion}
%if 0%{?qt6}
Conflicts:      gammaray-devel
%endif

%description devel
Gamma Ray is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%define _lto_cflags %{nil}
%if 0%{?qt5}
%cmake \
  -DQT_VERSION_MAJOR=5 \
  -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
  -DQCH_INSTALL_DIR=%{_datadir}/gammaray
%cmake_build
%endif

%if 0%{?qt6}
%cmake_qt6 \
  -DQT_VERSION_MAJOR=6 \
  -DECM_MKSPECS_INSTALL_DIR=%{_qt6_mkspecsdir}/modules \
  -DQCH_INSTALL_DIR=%{_datadir}/gammaray \
  -DQDOC_INDEX_DIR=%{_qt6_docdir}
%qt6_build
%endif

%install
%if 0%{?qt5}
%cmake_install
%endif

%if 0%{?qt6}
%qt6_install
%endif

# Already packaged with %%doc and %%license tags
rm -r %{buildroot}%{_datadir}/doc

%fdupes %{buildroot}

%ldconfig_scriptlets -n libgammaray%{?pkg_suffix}-%{soversion}
%ldconfig_scriptlets -n libgammaray-shared%{?pkg_suffix}-%{soversion}

%files
%doc CHANGES README.md
%{_bindir}/gammaray
%{_datadir}/applications/GammaRay.desktop
# Scaled directories are not owned by hicolor
%dir %{_datadir}/icons/hicolor/*@*/
%dir %{_datadir}/icons/hicolor/*@*/apps/
%{_datadir}/icons/hicolor/*/apps/GammaRay.png
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_gammaray
%dir %{_libdir}/gammaray
%{_libdir}/gammaray/libexec/
%{_mandir}/man1/gammaray.1%{?ext_man}
%{_datadir}/metainfo/com.kdab.GammaRay.metainfo.xml
%{_datadir}/gammaray/

%files -n libgammaray%{?pkg_suffix}-%{soversion}
%license LICENSES/*
%{_libdir}/libgammaray_client.so.*
%{_libdir}/libgammaray_kuserfeedback.so.*
%{_libdir}/libgammaray_launcher.so.*
%{_libdir}/libgammaray_launcher_ui.so.*

%files -n libgammaray-shared%{?pkg_suffix}-%{soversion}
%{_libdir}/libgammaray_*-qt*.so.*

# Shared libraries and plugins to load e.g. Qt 5 executables if gammaray was
# built with Qt 6
%files shared-plugins
%dir %{_libdir}/gammaray
%{_libdir}/gammaray/%{short_version}/

%files devel
%{_includedir}/gammaray/
%{_libdir}/cmake/GammaRay/
%{_libdir}/libgammaray_*-qt*.so
%{_libdir}/libgammaray_client.so
%{_libdir}/libgammaray_kuserfeedback.so
%{_libdir}/libgammaray_launcher.so
%{_libdir}/libgammaray_launcher_ui.so
%{_libdir}/qt*/mkspecs/modules/qt_GammaRay*.pri

%changelog
