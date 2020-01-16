#
# spec file for package kdstatemachineeditor
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


%define sover 1_2_7
%define libnamecore libkdstatemachineeditor_core%{sover}
%define libnamedebuginterfaceclient libkdstatemachineeditor_debuginterfaceclient%{sover}
%define libnamedebuginterfacesource libkdstatemachineeditor_debuginterfacesource-static
%define libnameview libkdstatemachineeditor_view%{sover}
Name:           kdstatemachineeditor
Version:        1.2.7
Release:        0
Summary:        A framework for creating Qt State Machine metacode using a GUI
# Legal: NOTE the EULA mentioned in LICENSE.txt only applies to "Licensed Product" users.
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://kdab.github.io/KDStateMachineEditor/
Source:         https://github.com/KDAB/KDStateMachineEditor/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.11
BuildRequires:  doxygen
BuildRequires:  graphviz-devel
BuildRequires:  graphviz-gnome
BuildRequires:  libQt5Core-private-headers-devel >= 5.3
BuildRequires:  libQt5Gui-private-headers-devel >= 5.3
BuildRequires:  libQt5Network-private-headers-devel >= 5.3
BuildRequires:  libqt5-qtscxml-private-headers-devel >= 5.8
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core) >= 5.3
BuildRequires:  cmake(Qt5Gui) >= 5.3
BuildRequires:  cmake(Qt5Network) >= 5.3
BuildRequires:  cmake(Qt5Qml) >= 5.3
BuildRequires:  cmake(Qt5RemoteObjects) >= 5.4
BuildRequires:  cmake(Qt5Scxml) >= 5.8
BuildRequires:  cmake(Qt5Test) >= 5.3
BuildRequires:  cmake(Qt5Widgets) >= 5.3
BuildRequires:  cmake(Qt5XmlPatterns) >= 5.3

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
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
        -DLIB_INSTALL_DIR="%{_lib}"
make VERBOSE=1 %{?_smp_mflags}

%install
%make_install

%post   -n %{libnamecore} -p /sbin/ldconfig
%postun -n %{libnamecore} -p /sbin/ldconfig
%post   -n %{libnamedebuginterfaceclient} -p /sbin/ldconfig
%postun -n %{libnamedebuginterfaceclient} -p /sbin/ldconfig
%post   -n %{libnameview} -p /sbin/ldconfig
%postun -n %{libnameview} -p /sbin/ldconfig

%files -n %{libnamecore}
%license LICENSE.*
%doc CHANGES ReadMe.txt
%{_libdir}/libkdstatemachineeditor_core.so.%{version}

%files -n %{libnamedebuginterfaceclient}
%license LICENSE.*
%doc CHANGES ReadMe.txt
%{_libdir}/libkdstatemachineeditor_debuginterfaceclient.so.%{version}

%files -n %{libnamedebuginterfacesource}
%license LICENSE.*
%doc CHANGES ReadMe.txt
%{_libdir}/libkdstatemachineeditor_debuginterfacesource.a

%files -n %{libnameview}
%license LICENSE.*
%doc CHANGES ReadMe.txt
%{_libdir}/libkdstatemachineeditor_view.so.%{version}

%files devel
%license LICENSE.*
%doc CHANGES ReadMe.txt
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
