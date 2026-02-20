#
# spec file for package kdstatemachineeditor
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


%define qt6_version 6.1
#
%global sover 2
#
Name:           kdstatemachineeditor
Version:        2.3.0
Release:        0
Summary:        A framework for creating Qt State Machine metacode using a GUI
# Legal: NOTE the EULA mentioned in LICENSE.txt only applies to "Licensed Product" users.
License:        LGPL-2.1-only
URL:            https://kdab.github.io/KDStateMachineEditor/
Source0:        https://github.com/KDAB/KDStateMachineEditor/releases/download/v%{version}/kdstatemachineeditor-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- work around build issue caused by graphviz packaging decisions
Patch0:         0001-CMake-Find-gvplugin_dot_layout-on-openSUSE.patch
BuildRequires:  doxygen
BuildRequires:  graphviz-devel >= 2.30.1
BuildRequires:  graphviz-gnome
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  qt6-scxml-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6RemoteObjects) >= %{qt6_version}
BuildRequires:  cmake(Qt6Scxml) >= %{qt6_version}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       graphviz-plugins-core

%description
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package -n libkdstatemachineeditor_core-qt6-%{sover}
Summary:        KDAB State Machine Editor core library

%description -n libkdstatemachineeditor_core-qt6-%{sover}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package -n libkdstatemachineeditor_debuginterfaceclient-qt6-%{sover}
Summary:        KDAB State Machine Editor core library

%description -n libkdstatemachineeditor_debuginterfaceclient-qt6-%{sover}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package -n libkdstatemachineeditor_debuginterfacesource-qt6-static
Summary:        KDAB State Machine Editor core library

%description -n libkdstatemachineeditor_debuginterfacesource-qt6-static
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

This package provides a static library that can be injected into a
process running on the target in order to get information about the
internal state machines.

%package -n libkdstatemachineeditor_view-qt6-%{sover}
Summary:        KDAB State Machine Editor view library

%description -n libkdstatemachineeditor_view-qt6-%{sover}
The KDAB State Machine Editor Library is a framework that can be used
to help develop State Machine Editing graphical user
interfaces and tools. Output from such applications is in metacode
or QML that can then be used in Qt or QtQuick projects.

%package devel
Summary:        Introspection/Debugging Tool for Qt Applications
Requires:       libkdstatemachineeditor_core-qt6-%{sover} = %{version}
Requires:       libkdstatemachineeditor_debuginterfaceclient-qt6-%{sover} = %{version}
Requires:       libkdstatemachineeditor_debuginterfacesource-qt6-static = %{version}
Requires:       libkdstatemachineeditor_view-qt6-%{sover} = %{version}
Provides:       kdstatemachineeditor-qt6 = %{version}
Obsoletes:      kdstatemachineeditor-qt6 < %{version}

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

%cmake_qt6 \
  -DKDSME_INTERNAL_GRAPHVIZ:BOOL=FALSE

%qt6_build

%install
%qt6_install

%ldconfig_scriptlets -n libkdstatemachineeditor_core-qt6-%{sover}
%ldconfig_scriptlets -n libkdstatemachineeditor_debuginterfaceclient-qt6-%{sover}
%ldconfig_scriptlets -n libkdstatemachineeditor_view-qt6-%{sover}

%files -n libkdstatemachineeditor_core-qt6-%{sover}
%license LICENSES/*
%doc CHANGES README.md
%{_libdir}/libkdstatemachineeditor_core-qt6.so.%{sover}

%files -n libkdstatemachineeditor_debuginterfaceclient-qt6-%{sover}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient-qt6.so.%{sover}

%files -n libkdstatemachineeditor_debuginterfacesource-qt6-static
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_debuginterfacesource-qt6.a

%files -n libkdstatemachineeditor_view-qt6-%{sover}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_view-qt6.so.%{sover}

%files devel
%license LICENSES/*
%{_includedir}/kdstatemachineeditor-qt6/
%{_libdir}/cmake/KDSME-qt6/
%{_libdir}/libkdstatemachineeditor_core-qt6.so
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient-qt6.so
%{_libdir}/libkdstatemachineeditor_view-qt6.so

%changelog
