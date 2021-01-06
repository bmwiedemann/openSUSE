#
# spec file for package qt6-declarative
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


%define real_version 6.0.0
%define short_version 6.0
%define tar_name qtdeclarative-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-declarative%{?pkg_suffix}
Version:        6.0.0
Release:        0
Summary:        Qt 6 Declarative Libraries and tools
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-declarative-rpmlintrc
BuildRequires:  python3-base
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-opengl-private-devel
BuildRequires:  qt6-test-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 6 Declarative Libraries and tools

%if !%{qt6_docs_flavor}

%package devel
Summary:        Qt 6 Declarative meta package
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
Requires:       cmake(Qt6QmlWorkerScript) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickParticles) = %{real_version}
Requires:       cmake(Qt6QuickShapes) = %{real_version}
Requires:       cmake(Qt6QuickTest) = %{real_version}
Requires:       cmake(Qt6QuickWidgets) = %{real_version}
BuildArch:      noarch

%description devel
This meta-package requires all the qt6-declarative development packages.

%package private-devel
Summary:        Qt 6 Declarative unstable ABI meta package
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-qmlmodels-private-devel = %{version}
Requires:       qt6-qmlworkerscript-private-devel = %{version}
Requires:       qt6-quick-private-devel = %{version}
Requires:       qt6-quickparticles-private-devel = %{version}
Requires:       qt6-quickshapes-private-devel = %{version}
Requires:       qt6-quicktest-private-devel = %{version}
Requires:       qt6-quickwidgets-private-devel = %{version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-declarative development packages that do
not have any ABI or API guarantees.

%package imports
Summary:        Qt 6 Declarative QML files and plugins

%description imports
QML files and plugins from the Qt 6 Declarative module

%package tools
Summary:        Qt 6 Declarative Tools
License:        GPL-3.0-only
Requires:       qt6-declarative-imports

%description tools
Additional tools for inspecting, testing, viewing QML imports and files.

%package -n libQt6Qml6
Summary:        Qt 6 Qml library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-declarative-imports

%description -n libQt6Qml6
The Qt 6 Qml library.

%package -n qt6-qml-devel
Summary:        Qt 6 Qml library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6Qml6 = %{version}
# Executables are required
Requires:       qt6-declarative-tools
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Network)

%description -n qt6-qml-devel
Development files for the Qt 6 Qml library.

%package -n qt6-qml-private-devel
Summary:        Non-ABI stable API for the Qt 6 Qml library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6Qml) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-qml-private-devel
This package provides private headers of libQt6Qml that do not have any
ABI or API guarantees.

%package -n libQt6QmlModels6
Summary:        Qt 6 QmlModels library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QmlModels6
The Qt 6 QmlModels library.

%package -n qt6-qmlmodels-devel
Summary:        Qt 6 QmlModels library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QmlModels6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Qml)

%description -n qt6-qmlmodels-devel
Development files for the Qt 6 QmlModels library.

%package -n qt6-qmlmodels-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlModels library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-qmlmodels-private-devel
This package provides private headers of libQt6QmlModels that do not have any
ABI or API guarantees.

%package -n libQt6QmlWorkerScript6
Summary:        Qt 6 QmlWorkScript library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QmlWorkerScript6
The Qt 6 QmlModels library.

%package -n qt6-qmlworkerscript-devel
Summary:        Qt 6 QmlModels library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QmlWorkerScript6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Qml)

%description -n qt6-qmlworkerscript-devel
Development files for the Qt 6 QmlModels library.

%package -n qt6-qmlworkerscript-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlWorkerScript library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6QmlWorkerScript) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-qmlworkerscript-private-devel
This package provides private headers of libQt6QmlWorkerScript that do not have
any ABI or API guarantees.

%package -n libQt6Quick6
Summary:        Qt 6 Quick library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6Quick6
The Qt 6 Quick library.

%package -n qt6-quick-devel
Summary:        Qt 6 Quick library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6Quick6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6OpenGL)
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6QmlModels)

%description -n qt6-quick-devel
Development files for the Qt 6 Quick library.

%package -n qt6-quick-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-qmlmodels-private-devel = %{version}
Requires:       cmake(Qt6Quick) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description -n qt6-quick-private-devel
This package provides private headers of libQt6Quick that do not have any
ABI or API guarantees.

%package -n libQt6QuickParticles6
Summary:        Qt 6 QuickParticles library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickParticles6
The Qt 6 QuickParticles library.

%package -n qt6-quickparticles-devel
Summary:        Qt 6 QuickParticles library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickParticles6 = %{version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-qml-private-devel
%requires_eq    qt6-quick-private-devel

%description -n qt6-quickparticles-devel
Development files for the Qt 6 QuickParticles library.

%package -n qt6-quickparticles-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickParticles library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QuickParticles) = %{real_version}

%description -n qt6-quickparticles-private-devel
This package provides private headers of libQt6QuickParticles that do not have
any ABI or API guarantees.

%package -n libQt6QuickShapes6
Summary:        Qt 6 QuickShapes library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickShapes6
The Qt 6 QuickShapes library.

%package -n qt6-quickshapes-devel
Summary:        Qt 6 QuickShapes library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickShapes6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Qml)
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-quick-private-devel

%description -n qt6-quickshapes-devel
Development files for the Qt 6 QuickShapes library.

%package -n qt6-quickshapes-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickShapes library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QuickShapes) = %{real_version}

%description -n qt6-quickshapes-private-devel
This package provides private headers of libQt6QuickShapes that do not have any
ABI or API guarantees.

%package -n libQt6QuickTest6
Summary:        Qt 6 QuickTest library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickTest6
The Qt 6 QuickTest library.

%package -n qt6-quicktest-devel
Summary:        Qt 6 QuickTest library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickTest6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Test)
Requires:       cmake(Qt6Widgets)

%description -n qt6-quicktest-devel
Development files for the Qt 6 QuickTest library.

%package -n qt6-quicktest-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickTest library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QuickTest) = %{real_version}
%requires_eq    qt6-test-private-devel

%description -n qt6-quicktest-private-devel
This package provides private headers of libQt6QuickTest that do not have any
ABI or API guarantees.

%package -n libQt6QuickWidgets6
Summary:        Qt 6 QuickWidgets library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickWidgets6
The Qt 6 QuickWidgets library.

%package -n qt6-quickwidgets-devel
Summary:        Qt 6 QuickWidgets library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickWidgets6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6Widgets)

%description -n qt6-quickwidgets-devel
Development files for the Qt 6 QuickWidgets library.

%package -n qt6-quickwidgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickWidgets library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quick-private-devel = %{version}
Requires:       cmake(Qt6QuickWidgets) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-widgets-private-devel

%description -n qt6-quickwidgets-private-devel
This package provides private headers of libQt6QuickWidgets that do not have any
ABI or API guarantees.

### Static libraries ###
%package -n qt6-packetprotocol-devel-static
Summary:        Qt6 PacketProtocol static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
%requires_eq    qt6-core-private-devel

%description -n qt6-packetprotocol-devel-static
The Qt6 PacketProtocol static library.

%package -n qt6-packetprotocol-private-devel
Summary:        Non-ABI stable API for the Qt 6 PacketProtocol library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6PacketProtocol) = %{real_version}

%description -n qt6-packetprotocol-private-devel
This package provides private headers of libQt6PacketProtocol that do not have
any ABI or API guarantees.

%package -n qt6-qmlcompiler-devel-static
Summary:        Qt6 QmlCompiler static library

%description -n qt6-qmlcompiler-devel-static
The Qt6 QmlCompiler static library.

%package -n qt6-qmlcompiler-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlCompiler library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QmlCompiler) = %{real_version}

%description -n qt6-qmlcompiler-private-devel
This package provides private headers of libQt6QmlCompiler that do not have any
ABI or API guarantees.

%package -n qt6-qmldebug-devel-static
Summary:        Qt6 QmlDebug static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-packetprotocol-private-devel = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6Network)
%requires_eq    qt6-core-private-devel

%description -n qt6-qmldebug-devel-static
The Qt6 QmlDebug static library.

%package -n qt6-qmldebug-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlDebug library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QmlDebug) = %{real_version}

%description -n qt6-qmldebug-private-devel
This package provides private headers of libQt6QmlDebug that do not have any
ABI or API guarantees.

%package -n qt6-qmldevtools-devel-static
Summary:        Qt6 QmlDevTools static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
%requires_eq    qt6-core-private-devel

%description -n qt6-qmldevtools-devel-static
The Qt6 QmlDevTools static library.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# Empty file used for the meta packages
cat >> meta_package << EOF
This is a meta package, it does not contain any file
EOF

%build
# Package provides static libraries
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# Empty folder provided by libQt6Qml6
mkdir -p %{buildroot}%{_qt6_importsdir}

%{qt6_link_executables}

# metatypes files are not needed for plugins
rm %{buildroot}%{_qt6_metatypesdir}/*plugin_*.json
rm %{buildroot}%{_qt6_metatypesdir}/qt6quick{tooling,window}_*_metatypes.json

# No private headers
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_qmldevtools_private.pri

%post -n libQt6Qml6 -p /sbin/ldconfig
%post -n libQt6QmlModels6 -p /sbin/ldconfig
%post -n libQt6QmlWorkerScript6 -p /sbin/ldconfig
%post -n libQt6Quick6 -p /sbin/ldconfig
%post -n libQt6QuickParticles6 -p /sbin/ldconfig
%post -n libQt6QuickShapes6 -p /sbin/ldconfig
%post -n libQt6QuickTest6 -p /sbin/ldconfig
%post -n libQt6QuickWidgets6 -p /sbin/ldconfig
%postun -n libQt6Qml6 -p /sbin/ldconfig
%postun -n libQt6QmlModels6 -p /sbin/ldconfig
%postun -n libQt6QmlWorkerScript6 -p /sbin/ldconfig
%postun -n libQt6Quick6 -p /sbin/ldconfig
%postun -n libQt6QuickParticles6 -p /sbin/ldconfig
%postun -n libQt6QuickShapes6 -p /sbin/ldconfig
%postun -n libQt6QuickTest6 -p /sbin/ldconfig
%postun -n libQt6QuickWidgets6 -p /sbin/ldconfig

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files imports
%{_qt6_qmldir}/Qt/
%{_qt6_qmldir}/QtQml/
%{_qt6_qmldir}/QtQuick/
%{_qt6_qmldir}/QtTest/
%{_qt6_qmldir}/builtins.qmltypes

%files tools
%{_bindir}/qml6
%{_bindir}/qmlcachegen6
%{_bindir}/qmleasing6
%{_bindir}/qmlformat6
%{_bindir}/qmlimportscanner6
%{_bindir}/qmllint6
%{_bindir}/qmlplugindump6
%{_bindir}/qmlpreview6
%{_bindir}/qmlprofiler6
%{_bindir}/qmlscene6
%{_bindir}/qmltestrunner6
%{_bindir}/qmltime6
%{_bindir}/qmltyperegistrar6
%{_qt6_bindir}/qml
%{_qt6_bindir}/qmlcachegen
%{_qt6_bindir}/qmleasing
%{_qt6_bindir}/qmlformat
%{_qt6_bindir}/qmlimportscanner
%{_qt6_bindir}/qmllint
%{_qt6_bindir}/qmlplugindump
%{_qt6_bindir}/qmlpreview
%{_qt6_bindir}/qmlprofiler
%{_qt6_bindir}/qmlscene
%{_qt6_bindir}/qmltestrunner
%{_qt6_bindir}/qmltime
%{_qt6_bindir}/qmltyperegistrar
%{_qt6_pluginsdir}/qmltooling/

%files -n libQt6Qml6
%license LICENSE.*
# libQt6Qml6 'provides' %%_qt6_importsdir and %%_qt6_qmldir
%dir %{_qt6_importsdir}
%dir %{_qt6_qmldir}
%{_qt6_libdir}/libQt6Qml.so.*

%files -n qt6-qml-devel
%dir %{_qt6_mkspecsdir}/features
%{_qt6_cmakedir}/Qt6Qml/
# Files from the two directories above are only used by Qt6QmlMacros.cmake
%{_qt6_cmakedir}/Qt6QmlImportScanner/
%{_qt6_cmakedir}/Qt6QmlTools/
%{_qt6_descriptionsdir}/Qml.json
%{_qt6_includedir}/QtQml/
%{_qt6_libdir}/libQt6Qml.prl
%{_qt6_libdir}/libQt6Qml.so
%{_qt6_metatypesdir}/qt6qml_*_metatypes.json
%{_qt6_mkspecsdir}/features/qmlcache.prf
%{_qt6_mkspecsdir}/features/qmltypes.prf
%{_qt6_mkspecsdir}/features/qtquickcompiler.prf
%{_qt6_mkspecsdir}/modules/qt_lib_qml.pri
%exclude %{_qt6_includedir}/QtQml/%{real_version}

%files -n qt6-qml-private-devel
%{_qt6_includedir}/QtQml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qml_private.pri

%files -n libQt6QmlModels6
%{_qt6_libdir}/libQt6QmlModels.so.*

%files -n qt6-qmlmodels-devel
%{_qt6_cmakedir}/Qt6QmlModels/
%{_qt6_descriptionsdir}/QmlModels.json
%{_qt6_includedir}/QtQmlModels/
%{_qt6_libdir}/libQt6QmlModels.prl
%{_qt6_libdir}/libQt6QmlModels.so
%{_qt6_metatypesdir}/qt6qmlmodels_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlmodels.pri
%exclude %{_qt6_includedir}/QtQmlModels/%{real_version}

%files -n qt6-qmlmodels-private-devel
%{_qt6_includedir}/QtQmlModels/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlmodels_private.pri

%files -n libQt6QmlWorkerScript6
%{_qt6_libdir}/libQt6QmlWorkerScript.so.*

%files -n qt6-qmlworkerscript-devel
%{_qt6_cmakedir}/Qt6QmlWorkerScript/
%{_qt6_descriptionsdir}/QmlWorkerScript.json
%{_qt6_includedir}/QtQmlWorkerScript/
%{_qt6_libdir}/libQt6QmlWorkerScript.prl
%{_qt6_libdir}/libQt6QmlWorkerScript.so
%{_qt6_metatypesdir}/qt6qmlworkerscript_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlworkerscript.pri
%exclude %{_qt6_includedir}/QtQmlWorkerScript/%{real_version}

%files -n qt6-qmlworkerscript-private-devel
%{_qt6_includedir}/QtQmlWorkerScript/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlworkerscript_private.pri

%files -n libQt6Quick6
%{_qt6_libdir}/libQt6Quick.so.*

%files -n qt6-quick-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtDeclarativeTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Quick/
%{_qt6_descriptionsdir}/Quick.json
%{_qt6_includedir}/QtQuick/
%{_qt6_libdir}/libQt6Quick.prl
%{_qt6_libdir}/libQt6Quick.so
%{_qt6_metatypesdir}/qt6quick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick.pri
%exclude %{_qt6_includedir}/QtQuick/%{real_version}

%files -n qt6-quick-private-devel
%{_qt6_includedir}/QtQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick_private.pri

%files -n libQt6QuickParticles6
%{_qt6_libdir}/libQt6QuickParticles.so.*

%files -n qt6-quickparticles-devel
%{_qt6_cmakedir}/Qt6QuickParticles/
%{_qt6_descriptionsdir}/QuickParticles.json
%{_qt6_includedir}/QtQuickParticles/
%{_qt6_libdir}/libQt6QuickParticles.prl
%{_qt6_libdir}/libQt6QuickParticles.so
%{_qt6_metatypesdir}/qt6quickparticles_*_metatypes.json
%exclude %{_qt6_includedir}/QtQuickParticles/%{real_version}

%files -n qt6-quickparticles-private-devel
%{_qt6_includedir}/QtQuickParticles/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickparticles_private.pri

%files -n libQt6QuickShapes6
%{_qt6_libdir}/libQt6QuickShapes.so.*

%files -n qt6-quickshapes-devel
%{_qt6_cmakedir}/Qt6QuickShapes/
%{_qt6_descriptionsdir}/QuickShapes.json
%{_qt6_includedir}/QtQuickShapes/
%{_qt6_libdir}/libQt6QuickShapes.prl
%{_qt6_libdir}/libQt6QuickShapes.so
%{_qt6_metatypesdir}/qt6quickshapes_*_metatypes.json
%exclude %{_qt6_includedir}/QtQuickShapes/%{real_version}

%files -n qt6-quickshapes-private-devel
%{_qt6_includedir}/QtQuickShapes/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickshapes_private.pri

%files -n libQt6QuickTest6
%{_qt6_libdir}/libQt6QuickTest.so.*

%files -n qt6-quicktest-devel
%{_qt6_cmakedir}/Qt6QuickTest/
%{_qt6_descriptionsdir}/QuickTest.json
%{_qt6_includedir}/QtQuickTest/
%{_qt6_libdir}/libQt6QuickTest.prl
%{_qt6_libdir}/libQt6QuickTest.so
%{_qt6_metatypesdir}/qt6quicktest_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmltest.pri
%exclude %{_qt6_includedir}/QtQuickTest/%{real_version}

%files -n qt6-quicktest-private-devel
%{_qt6_includedir}/QtQuickTest/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmltest_private.pri

%files -n libQt6QuickWidgets6
%{_qt6_libdir}/libQt6QuickWidgets.so.*

%files -n qt6-quickwidgets-devel
%{_qt6_cmakedir}/Qt6QuickWidgets/
%{_qt6_descriptionsdir}/QuickWidgets.json
%{_qt6_includedir}/QtQuickWidgets/
%{_qt6_libdir}/libQt6QuickWidgets.prl
%{_qt6_libdir}/libQt6QuickWidgets.so
%{_qt6_mkspecsdir}/modules/qt_lib_quickwidgets.pri
%exclude %{_qt6_includedir}/QtQuickWidgets/%{real_version}

%files -n qt6-quickwidgets-private-devel
%{_qt6_includedir}/QtQuickWidgets/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_quickwidgets_private.pri

### Static libraries ###

%files -n qt6-packetprotocol-devel-static
%{_qt6_cmakedir}/Qt6PacketProtocol/
%{_qt6_descriptionsdir}/PacketProtocol.json
%{_qt6_includedir}/QtPacketProtocol/
%{_qt6_libdir}/libQt6PacketProtocol.a
%{_qt6_libdir}/libQt6PacketProtocol.prl
%exclude %{_qt6_includedir}/QtPacketProtocol/%{real_version}

%files -n qt6-packetprotocol-private-devel
%{_qt6_includedir}/QtPacketProtocol/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_packetprotocol_private.pri

%files -n qt6-qmlcompiler-devel-static
%{_qt6_cmakedir}/Qt6QmlCompiler/
%{_qt6_descriptionsdir}/QmlCompiler.json
%{_qt6_includedir}/QtQmlCompiler/
%{_qt6_libdir}/libQt6QmlCompiler.a
%{_qt6_libdir}/libQt6QmlCompiler.prl
%exclude %{_qt6_includedir}/QtQmlCompiler/%{real_version}

%files -n qt6-qmlcompiler-private-devel
%{_qt6_includedir}/QtQmlCompiler/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcompiler_private.pri

%files -n qt6-qmldebug-devel-static
%{_qt6_cmakedir}/Qt6QmlDebug/
%{_qt6_descriptionsdir}/QmlDebug.json
%{_qt6_includedir}/QtQmlDebug/
%{_qt6_libdir}/libQt6QmlDebug.a
%{_qt6_libdir}/libQt6QmlDebug.prl
%exclude %{_qt6_includedir}/QtQmlDebug/%{real_version}

%files -n qt6-qmldebug-private-devel
%{_qt6_includedir}/QtQmlDebug/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmldebug_private.pri

%files -n qt6-qmldevtools-devel-static
%{_qt6_cmakedir}/Qt6QmlDevTools/
%{_qt6_descriptionsdir}/QmlDevTools.json
%{_qt6_libdir}/libQt6QmlDevTools.a
%{_qt6_libdir}/libQt6QmlDevTools.prl

%endif

%changelog
