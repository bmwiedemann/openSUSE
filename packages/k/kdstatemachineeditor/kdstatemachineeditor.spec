#
# spec file for package kdstatemachineeditor
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


%define sover 1
%define libnamecore libkdstatemachineeditor_core%{sover}
%define libnamedebuginterfaceclient libkdstatemachineeditor_debuginterfaceclient%{sover}
%define libnamedebuginterfacesource libkdstatemachineeditor_debuginterfacesource-static
%define libnameview libkdstatemachineeditor_view%{sover}
Name:           kdstatemachineeditor
Version:        1.2.8
Release:        0
Summary:        A framework for creating Qt State Machine metacode using a GUI
# Legal: NOTE the EULA mentioned in LICENSE.txt only applies to "Licensed Product" users.
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://kdab.github.io/KDStateMachineEditor/
Source:         https://github.com/KDAB/KDStateMachineEditor/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz-devel
BuildRequires:  graphviz-gnome
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Network-private-headers-devel
BuildRequires:  libqt5-qtscxml-private-headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5RemoteObjects)
BuildRequires:  cmake(Qt5Scxml)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XmlPatterns)

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
%autosetup -p1

%build
# libkdstatemachineeditor_debuginterfacesource is a static library
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

%cmake \
  -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
  -DLIB_INSTALL_DIR="%{_lib}"

%cmake_build

%install
%cmake_install

%post   -n %{libnamecore} -p /sbin/ldconfig
%postun -n %{libnamecore} -p /sbin/ldconfig
%post   -n %{libnamedebuginterfaceclient} -p /sbin/ldconfig
%postun -n %{libnamedebuginterfaceclient} -p /sbin/ldconfig
%post   -n %{libnameview} -p /sbin/ldconfig
%postun -n %{libnameview} -p /sbin/ldconfig

%files -n %{libnamecore}
%license LICENSES/*
%doc CHANGES ReadMe.md
%{_libdir}/libkdstatemachineeditor_core.so.%{sover}

%files -n %{libnamedebuginterfaceclient}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient.so.%{sover}

%files -n %{libnamedebuginterfacesource}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_debuginterfacesource.a

%files -n %{libnameview}
%license LICENSES/*
%{_libdir}/libkdstatemachineeditor_view.so.%{sover}

%files devel
%license LICENSES/*
%{_includedir}/kdstatemachineeditor/
%{_libdir}/cmake/KDSME/
%{_libdir}/libkdstatemachineeditor_core.so
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient.so
%{_libdir}/libkdstatemachineeditor_view.so
%{_libdir}/qt5/mkspecs/modules/qt_KDSMECore.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSMEDebugInterfaceClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSMEDebugInterfaceSource.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSMEView.pri

%changelog
