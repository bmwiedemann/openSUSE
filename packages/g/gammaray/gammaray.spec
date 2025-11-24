#
# spec file for package gammaray
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


%define qt6_version 6.5
%define rname gammaray
%define short_version 3.3
%define soversion 3_3_1
Name:           gammaray
Version:        3.3.1
Release:        0
Summary:        Introspection/Debugging Tool for Qt Applications
License:        GPL-2.0-or-later
URL:            https://www.kdab.com/gammaray
Source0:        https://github.com/KDAB/GammaRay/releases/download/v%{version}/%{rname}-%{version}.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz-gnome
# include this so the icon folders don't need to be owned by the package
BuildRequires:  hicolor-icon-theme
BuildRequires:  libdw-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  qt6-qml-private-devel >= %{qt6_version}
BuildRequires:  qt6-quick-private-devel >= %{qt6_version}
# # Needed to build the statemachine examples
BuildRequires:  qt6-scxml-imports >= %{qt6_version}
BuildRequires:  qt6-scxml-private-devel >= %{qt6_version}
BuildRequires:  qt6-statemachine-private-devel >= %{qt6_version}
BuildRequires:  qt6-widgets-private-devel >= %{qt6_version}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150600
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6SyntaxHighlighting)
%endif
BuildRequires:  cmake(Qt63DAnimation) >= %{qt6_version}
BuildRequires:  cmake(Qt63DExtras) >= %{qt6_version}
BuildRequires:  cmake(Qt63DInput) >= %{qt6_version}
BuildRequires:  cmake(Qt63DLogic) >= %{qt6_version}
BuildRequires:  cmake(Qt63DQuick) >= %{qt6_version}
BuildRequires:  cmake(Qt63DRender) >= %{qt6_version}
BuildRequires:  cmake(Qt6Bluetooth) >= %{qt6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Help) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Location) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Scxml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandCompositor) >= %{qt6_version}
%ifarch x86_64 aarch64 riscv64
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-server)

%description
GammaRay is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt.

%package -n gammaray-qt6
Summary:        Introspection/Debugging Tool for Qt Applications
Requires:       libgammaray-qt6-%{soversion} >= %{version}
# No longer present after Qt 5 support removal
Obsoletes:      gammaray < 3.3.0
Obsoletes:      gammaray-qt6-shared-plugins < 3.3.0
Obsoletes:      gammaray-shared-plugins < 3.3.0

%description -n gammaray-qt6
GammaRay is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt.

%package -n libgammaray-qt6-%{soversion}
Summary:        Gammaray libraries
Conflicts:      libgammaray-%{soversion}

%description -n libgammaray-qt6-%{soversion}
Gammaray libraries.

%package -n gammaray-qt6-devel
Summary:        Introspection/Debugging Tool for Qt Applications
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      gammaray-devel <= 3.3.0

%description -n gammaray-qt6-devel
Gamma Ray is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt. Development files.

%prep
%autosetup -p1 -n GammaRay-%{version}

%build
%define _lto_cflags %{nil}

%cmake_qt6 \
  -DECM_MKSPECS_INSTALL_DIR:STRING=%{_qt6_mkspecsdir}/modules \
  -DQCH_INSTALL_DIR:STRING=%{_datadir}/gammaray \
  -DQDOC_INDEX_DIR:STRING=%{_qt6_docdir}

%qt6_build

%install
%qt6_install

# Already packaged with %%doc and %%license tags
rm -r %{buildroot}%{_datadir}/doc

%fdupes %{buildroot}

%ldconfig_scriptlets -n libgammaray-qt6-%{soversion}

%files -n gammaray-qt6
%doc CHANGES README.md
%{_bindir}/gammaray
%{_datadir}/applications/GammaRay.desktop
%{_datadir}/gammaray/
# Scaled directories are not owned by hicolor
%dir %{_datadir}/icons/hicolor/*@*/
%dir %{_datadir}/icons/hicolor/*@*/apps/
%{_datadir}/icons/hicolor/*/apps/GammaRay.png
%{_datadir}/metainfo/com.kdab.GammaRay.metainfo.xml
%{_datadir}/zsh/site-functions/_gammaray
%{_libdir}/gammaray/
%{_mandir}/man1/gammaray.1%{?ext_man}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

%files -n libgammaray-qt6-%{soversion}
%license LICENSES/*
%{_libdir}/libgammaray_*-qt*.so.*
%{_libdir}/libgammaray_client.so.*
%{_libdir}/libgammaray_kuserfeedback.so.*
%{_libdir}/libgammaray_launcher_ui.so.*
%{_libdir}/libgammaray_launcher.so.*

%files -n gammaray-qt6-devel
%{_includedir}/gammaray/
%{_libdir}/cmake/GammaRay/
%{_libdir}/libgammaray_*-qt*.so
%{_libdir}/libgammaray_client.so
%{_libdir}/libgammaray_kuserfeedback.so
%{_libdir}/libgammaray_launcher_ui.so
%{_libdir}/libgammaray_launcher.so
%{_qt6_mkspecsdir}/modules/qt_GammaRay*.pri

%changelog
