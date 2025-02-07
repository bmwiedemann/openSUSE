#
# spec file for package kdstatemachineeditor
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define qt_suffix 6
%define qt_min_version 6.1
%else
%define qt5 1
%define qt_suffix 5
%define qt_min_version 5.15
%endif
#
%global sover 2
%define libnamecore libkdstatemachineeditor_core%{?qt6:%{pkg_suffix}-}%{sover}
%define libnamedebuginterfaceclient libkdstatemachineeditor_debuginterfaceclient%{?qt6:%{pkg_suffix}-}%{sover}
%define libnamedebuginterfacesource libkdstatemachineeditor_debuginterfacesource%{?qt6:%{pkg_suffix}}-static
%define libnameview libkdstatemachineeditor_view%{?qt6:%{pkg_suffix}-}%{sover}
#
Name:           kdstatemachineeditor%{?pkg_suffix}
Version:        2.0.0
Release:        0
Summary:        A framework for creating Qt State Machine metacode using a GUI
# Legal: NOTE the EULA mentioned in LICENSE.txt only applies to "Licensed Product" users.
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://kdab.github.io/KDStateMachineEditor/
Source:         https://github.com/KDAB/KDStateMachineEditor/releases/download/v%{version}/KDStateMachineEditor-v%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- work around build issue caused by graphviz packaging decisions
Patch0:         0001-CMake-Find-gvplugin_dot_layout-on-openSUSE.patch
BuildRequires:  cmake >= 3.16.0
BuildRequires:  doxygen
BuildRequires:  graphviz-devel >= 2.30.1
BuildRequires:  graphviz-gnome
BuildRequires:  cmake(Qt%{qt_suffix}Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Quick) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}QuickWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}RemoteObjects) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Scxml) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Test) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{qt_suffix}Widgets) >= %{qt_min_version}
%if 0%{?qt5}
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qtscxml-private-headers-devel >= %{qt_min_version}
BuildRequires:  cmake(Qt5XmlPatterns) >= %{qt_min_version}
%endif
%if 0%{?qt6}
BuildRequires:  qt6-gui-private-devel >= %{qt_min_version}
BuildRequires:  qt6-scxml-private-devel >= %{qt_min_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt_min_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt_min_version}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt_min_version}
%endif
Requires:       graphviz-plugins-core

%description
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package -n %{libnamecore}
Summary:        KDAB State Machine Editor core library
Group:          System/Libraries

%description -n %{libnamecore}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package -n %{libnamedebuginterfaceclient}
Summary:        KDAB State Machine Editor core library
Group:          System/Libraries

%description -n %{libnamedebuginterfaceclient}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package -n %{libnamedebuginterfacesource}
Summary:        KDAB State Machine Editor core library
Group:          System/Libraries

%description -n %{libnamedebuginterfacesource}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

This package provides a static library that can be injected into a
process running on the target in order to get information about the
internal state machines.

%package -n %{libnameview}
Summary:        KDAB State Machine Editor view library
Group:          System/Libraries

%description -n %{libnameview}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package devel
Summary:        Introspection/Debugging Tool for Qt Applications
Group:          Development/Libraries/C and C++
Requires:       %{libnamecore} = %{version}
Requires:       %{libnamedebuginterfaceclient} = %{version}
Requires:       %{libnamedebuginterfacesource} = %{version}
Requires:       %{libnameview} = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description devel
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%prep
%autosetup -p1 -n KDStateMachineEditor-%{version}

%build
# libkdstatemachineeditor_debuginterfacesource is a static library
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

%define build_options -DKDSME_INTERNAL_GRAPHVIZ:BOOL=FALSE

%if 0%{?qt5}
%cmake \
  -DECM_MKSPECS_INSTALL_DIR:STRING=%{_libdir}/qt5/mkspecs/modules \
  %{build_options}
%{nil}

%cmake_build
%endif

%if 0%{?qt6}
%cmake_qt6 \
  -DKDSME_QT6:BOOL=TRUE \
  %{build_options}
%{nil}

%qt6_build
%endif

%install
%if 0%{?qt5}
%cmake_install
%endif

%if 0%{?qt6}
%qt6_install
%endif

%ldconfig_scriptlets -n %{libnamecore}
%ldconfig_scriptlets -n %{libnamedebuginterfaceclient}
%ldconfig_scriptlets -n %{libnameview}

%files -n %{libnamecore}
%license LICENSES/*
%doc CHANGES README.md
%{_libdir}/libkdstatemachineeditor_core%{?pkg_suffix}.so.%{sover}

%files -n %{libnamedebuginterfaceclient}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient%{?pkg_suffix}.so.%{sover}

%files -n %{libnamedebuginterfacesource}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_debuginterfacesource%{?pkg_suffix}.a

%files -n %{libnameview}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_view%{?pkg_suffix}.so.%{sover}

%files devel
%license LICENSES/*
%{_includedir}/kdstatemachineeditor%{?pkg_suffix}/
%{_libdir}/cmake/KDSME%{?pkg_suffix}/
%{_libdir}/libkdstatemachineeditor_core%{?pkg_suffix}.so
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient%{?pkg_suffix}.so
%{_libdir}/libkdstatemachineeditor_view%{?pkg_suffix}.so
%if 0%{?qt5}
%{_libdir}/qt5/mkspecs/modules/qt_KDSMECore.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSMEDebugInterfaceClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSMEDebugInterfaceSource.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSMEView.pri
%endif

%changelog
