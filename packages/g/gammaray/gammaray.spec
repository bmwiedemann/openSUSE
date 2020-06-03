#
# spec file for package gammaray
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


# Required for the "highly experimental" object visualizer plugin, only VTK 7.1 supported
%bcond_with     vtk

%define tarname GammaRay
Name:           gammaray
Version:        2.11.1
Release:        0
Summary:        Introspection/Debugging Tool for Qt Applications
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://www.kdab.com/gammaray
Source:         https://github.com/KDAB/GammaRay/releases/download/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Fix_icons_installation.patch -- Don't try to install multiple copies in exotic subdirs
Patch0:         Fix_icons_installation.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-Qt-5.15.patch
Patch3:         fix-build-with-qt-5.15-again.patch
BuildRequires:  binutils-devel
BuildRequires:  cmake >= 3.1
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz-gnome
# include this so the icon folders don't need to be owned by the package
BuildRequires:  hicolor-icon-theme
BuildRequires:  kdstatemachineeditor-devel
BuildRequires:  libQt5Core-private-headers-devel >= 5.5.0
BuildRequires:  libQt5Gui-private-headers-devel >= 5.5.0
BuildRequires:  libQt5Network-private-headers-devel >= 5.5.0
BuildRequires:  libdw-devel
BuildRequires:  libqt5-qt3d-devel >= 5.5.0
BuildRequires:  libqt5-qtbase-doc >= 5.5.0
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= 5.5.0
BuildRequires:  libqt5-qttools >= 5.5.0
BuildRequires:  update-desktop-files
BuildRequires:  wayland-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(Qt5Bluetooth) >= 5.5.0
BuildRequires:  cmake(Qt5Concurrent) >= 5.5.0
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Designer) >= 5.5.0
BuildRequires:  cmake(Qt5Gui) >= 5.5.0
BuildRequires:  cmake(Qt5Network) >= 5.5.0
BuildRequires:  cmake(Qt5Positioning) >= 5.5.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.5.0
BuildRequires:  cmake(Qt5Qml) >= 5.5.0
BuildRequires:  cmake(Qt5Quick) >= 5.5.0
BuildRequires:  cmake(Qt5Script) >= 5.5.0
BuildRequires:  cmake(Qt5ScriptTools) >= 5.5.0
BuildRequires:  cmake(Qt5Svg) >= 5.5.0
BuildRequires:  cmake(Qt5Test) >= 5.5.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0
%if %{with vtk}
BuildRequires:  cmake(VTK) = 7.1.0
%endif
# Needed to build the user manual
BuildRequires:  libqt5-qtdoc-devel
#
BuildRequires:  glslang-devel
BuildRequires:  libqt5-qtscxml-private-headers-devel >= 5.8.0
BuildRequires:  cmake(KF5SyntaxHighlighting) >= 5.28.0
BuildRequires:  cmake(Qt5Scxml) >= 5.8.0
BuildRequires:  cmake(Qt5WaylandCompositor) >= 5.5.0

%description
Gamma Ray is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt.

%package devel
Summary:        Introspection/Debugging Tool for Qt Applications
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Gamma Ray is a comprehensive collection of high level introspection
and debugging utilities specifically tailored for the various
frameworks in Qt. Development files.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%cmake \
  -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
  -DQCH_INSTALL_DIR=%{_datadir}/gammaray/ \
  -DQDOC_EXECUTABLE=%{_libqt5_bindir}/qdoc \
  -DQHELPGEN_EXECUTABLE=%{_libqt5_bindir}/qhelpgenerator

%cmake_build

%install
%cmake_install

install -d -m 755 %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}
%suse_update_desktop_file GammaRay Development Qt Debugger
%fdupes %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.*
%doc CHANGES ReadMe.txt
%dir %{_datadir}/icons/hicolor/512x512/
%dir %{_datadir}/icons/hicolor/512x512/apps/
%{_bindir}/gammaray
%{_datadir}/applications/GammaRay.desktop
%{_datadir}/icons/hicolor/*/apps/GammaRay.png
%{_docdir}/%{name}/
%{_libdir}/gammaray/
%{_libdir}/libgammaray_*-qt5*.so.*
%{_libdir}/libgammaray_client.so.*
%{_libdir}/libgammaray_kuserfeedback.so.*
%{_libdir}/libgammaray_launcher.so.*
%{_libdir}/libgammaray_launcher_ui.so.*
%{_mandir}/man1/gammaray.*
%if 0%{?suse_version} <= 1320
%dir %{_datadir}/appdata
%endif
%{_datadir}/appdata/GammaRay.appdata.xml
%{_datadir}/gammaray

%files devel
%license LICENSE.*
%{_includedir}/%{name}
%{_libdir}/cmake/GammaRay/
%{_libdir}/libgammaray_*-qt5*.so
%{_libdir}/libgammaray_client.so
%{_libdir}/libgammaray_kuserfeedback.so
%{_libdir}/libgammaray_launcher.so
%{_libdir}/libgammaray_launcher_ui.so
%{_libdir}/qt5/mkspecs/modules/qt_GammaRay*.pri

%changelog
