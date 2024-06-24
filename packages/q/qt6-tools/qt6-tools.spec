#
# spec file for package qt6-tools
#
# Copyright (c) 2024 SUSE LLC
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


%define real_version 6.7.2
%define short_version 6.7
%define tar_name qttools-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-tools%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 Tools libraries and tools
# TODO Check if it's still valid
# Legal:
# most src/ subfolders are GPL-3.0-only WITH Qt-GPL-exception-1.0, except:
# qdoc is GPL-3.0-only WITH Qt-GPL-exception-1.0 + (LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)) == GPL-3.0-only
# src/shared contains BSD-3-Clause and LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) files. The
# 'GPL-3.0-only WITH Qt-GPL-exception-1.0' files in this folder are only used on Windows.
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source10:       org.qt.designer6.desktop
Source11:       org.qt.linguist6.desktop
Source12:       org.qt.qdbusviewer6.desktop
Source13:       org.qt.assistant6.desktop
# The 48x48 icon was removed from qttools
Source14:       linguist6.png
Source99:       qt6-tools-rpmlintrc
# clang-devel in Leap 15 points to clang7...
%if 0%{?suse_version} == 1500 && 0%{?sle_version} >= 150600
BuildRequires:  clang17-devel
%else
%if 0%{?suse_version} == 1500 && 0%{?sle_version} >= 150400
BuildRequires:  clang15-devel
%else
BuildRequires:  clang-devel >= 8
%endif
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-dbus-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6DBus) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6OpenGL) = %{real_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) = %{real_version}
BuildRequires:  cmake(Qt6PrintSupport) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickWidgets) = %{real_version}
BuildRequires:  cmake(Qt6Sql) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  cmake(Qt6Xml) = %{real_version}
BuildRequires:  pkgconfig(libzstd) >= 1.3
# These packages are required to generate documentation for the Qt packages
Requires:       qt6-tools-helpgenerators
Requires:       qt6-tools-qdoc
Recommends:     qt6-tools-assistant
Recommends:     qt6-tools-designer
Recommends:     qt6-tools-linguist
Recommends:     qt6-tools-qdbus
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The QtTools modules contains some tools mostly useful for application
development.

Included are Qt Designer (GUI design), QDbusViewer and more.

%if !%{qt6_docs_flavor}

%package devel
Summary:        Qt 6 Tools libraries - Development files
Requires:       qt6-tools = %{version}
Requires:       qt6-tools-helpgenerators = %{version}
Requires:       qt6-tools-qdoc = %{version}

%description devel
Development files for the Qt6 tools libraries.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 tools libraries

%description private-devel
This package provides private headers of qt6-tools that do not have any
ABI or API guarantees.

%package -n libQt6Designer6
Summary:        Qt 6 Designer library
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0

%description -n libQt6Designer6
This package contains the Qt 6 Designer Library.

%package -n qt6-designer-devel
Summary:        Qt 6 Designer libraries - Development files
Requires:       libQt6Designer6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6OpenGLWidgets) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}
Requires:       cmake(Qt6Xml) = %{real_version}

%description -n qt6-designer-devel
Development files for the Qt6 Designer libraries.

%package -n qt6-designer-private-devel
Summary:        Non-ABI stable API for the Qt 6 Designer libraries
Requires:       cmake(Qt6Designer) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-widgets-private-devel

%description -n qt6-designer-private-devel
This package provides private headers of libQt6Designer that do not have any
ABI or API guarantees.

%package -n libQt6Help6
Summary:        Qt 6 Help library

%description -n libQt6Help6
This package contains the Qt 6 Help library.

%package -n qt6-help-devel
Summary:        Qt 6 Help library - Development files
Requires:       libQt6Help6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6Sql) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description -n qt6-help-devel
Development files for the Qt6 Help library.

%package -n qt6-help-private-devel
Summary:        Non-ABI stable API for the Qt 6 Help library
Requires:       cmake(Qt6Help) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-help-private-devel
This package provides private headers of libQt6Help that do not have any
ABI or API guarantees.

%package -n libQt6UiTools6
Summary:        Qt 6 UiTools library

%description -n libQt6UiTools6
This package contains the Qt 6 UiTools library.

%package -n qt6-uitools-devel
Summary:        Qt 6 UiTools library - Development files
Requires:       libQt6UiTools6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6OpenGLWidgets) = %{real_version}
Requires:       cmake(Qt6UiPlugin) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}
# qt6uitools_*_metatypes.json location fixed
Conflicts:      qt6-designer-devel < 6.2.2

%description -n qt6-uitools-devel
Development files for the Qt6 UiTools library.

%package -n qt6-uitools-private-devel
Summary:        Non-ABI stable API for the Qt 6 UiTools library
Requires:       cmake(Qt6UiTools) = %{real_version}

%description -n qt6-uitools-private-devel
This package provides private headers of libQt6UiTools that do not have any
ABI or API guarantees.

%package assistant
Summary:        Documentation browser

%description assistant
Qt Assistant is a tool for viewing documentation in Qt help file format.

%package designer
Summary:        Qt graphical interface creation tool

%description designer
Qt Designer is a tool for designing and building graphical user interface
with Qt Widgets.

%package helpgenerators
Summary:        Qt Help files generator
Requires:       qt6-docs-common
# help files are SQLite databases, so qhelpgenerator needs the SQLite plugin
Requires:       qt6-sql-sqlite

%description helpgenerators
Qt 6 tool for generating .qch help catalogs.

%package linguist
Summary:        Translation tool for Qt applications

%description linguist
Qt Linguist can be used by translator to translate text in Qt applications.

%package -n qt6-linguist-devel
Summary:        Qt 6 linguist tools - Development files
# Executables are required
Requires:       qt6-tools-linguist = %{version}

%description -n qt6-linguist-devel
Development files for the Qt 6 linguist tools.

%package qdbus
Summary:        Command line client for communication over D-Bus
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0

%description qdbus
Command line client for communication over D-Bus.

%package qdoc
Summary:        Qt 6 Tool used by Qt to generate documentation
License:        GPL-3.0-only
# qdoc hardcodes clang include paths: boo#1109367, QTBUG-70687
%requires_eq    libclang%{_llvm_sonum}

%description qdoc
Qt 6 Tool used by Qt to generate documentation.

### Private only library ###

%package -n libQt6DesignerComponents6
Summary:        Qt 6 DesignerComponents library
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0

%description -n libQt6DesignerComponents6
The Qt 6 DesignerComponents library.
This library does not have any ABI or API guarantees.

%package -n qt6-designercomponents-private-devel
Summary:        Development files for the Qt 6 DesignerComponents library
Requires:       libQt6DesignerComponents6 = %{version}
Requires:       qt6-designer-private-devel = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Xml) = %{real_version}
%requires_eq    qt6-gui-private-devel
%requires_eq    qt6-widgets-private-devel

%description -n qt6-designercomponents-private-devel
Development files for the Qt 6 DesignerComponents library.
This library does not have any ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6 -DBUILD_TESTING:BOOL=OFF

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%{qt6_link_executables}

# CMake files are not needed for plugins (except for Qt6UiPlugin)
rm %{buildroot}%{_qt6_cmakedir}/Qt6Designer/*Plugin{Config,Targets}*.cmake

# This doesn't look useful
rm -r %{buildroot}%{_qt6_includedir}/QtQDocCatch*
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6QDocCatch*
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_qdoccatch*.pri
rm %{buildroot}%{_qt6_descriptionsdir}/QDocCatch*.json

# Desktop files for applications
%suse_update_desktop_file -i org.qt.assistant6
%suse_update_desktop_file -i org.qt.designer6
%suse_update_desktop_file -i org.qt.linguist6
rm %{buildroot}%{_datadir}/pixmaps/linguist6.png
%suse_update_desktop_file -i org.qt.qdbusviewer6

# Icons for the desktop files
install -D -m644 src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer6.png
install -D -m644 %{SOURCE14} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/linguist6.png
install -D -m644 src/linguist/linguist/images/icons/linguist-128-32.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/linguist6.png
install -D -m644 src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer6.png
install -D -m644 src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer6.png
install -D -m644 src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant6.png
install -D -m644 src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant6.png

%ldconfig_scriptlets -n libQt6Designer6
%ldconfig_scriptlets -n libQt6DesignerComponents6
%ldconfig_scriptlets -n libQt6Help6
%ldconfig_scriptlets -n libQt6UiTools6

%files
%license LICENSES/*
%{_bindir}/pixeltool6
%{_bindir}/qdistancefieldgenerator6
%{_bindir}/qtdiag6
%{_bindir}/qtplugininfo6
%{_qt6_bindir}/pixeltool
%{_qt6_bindir}/qdistancefieldgenerator
%{_qt6_bindir}/qtdiag
%{_qt6_bindir}/qtplugininfo
%{_qt6_libexecdir}/qtattributionsscanner

%files devel
%{_qt6_cmakedir}/Qt6/FindWrapLibClang.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtToolsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Tools/
%{_qt6_cmakedir}/Qt6ToolsTools/
%{_qt6_descriptionsdir}/Tools.json
%{_qt6_includedir}/QtTools/
%exclude %{_qt6_includedir}/QtTools/%{real_version}

%files private-devel
%{_qt6_includedir}/QtTools/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_tools_private.pri

%files -n libQt6Designer6
%{_qt6_libdir}/libQt6Designer.so.*

%files -n qt6-designer-devel
%{_qt6_cmakedir}/Qt6Designer/
%{_qt6_cmakedir}/Qt6UiPlugin/
%{_qt6_descriptionsdir}/Designer.json
%{_qt6_descriptionsdir}/UiPlugin.json
%{_qt6_includedir}/QtDesigner/
%{_qt6_includedir}/QtUiPlugin/
%{_qt6_libdir}/libQt6Designer.prl
%{_qt6_libdir}/libQt6Designer.so
%{_qt6_metatypesdir}/qt6designer_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_designer.pri
%{_qt6_mkspecsdir}/modules/qt_lib_uiplugin.pri
%{_qt6_pkgconfigdir}/Qt6Designer.pc
%{_qt6_pkgconfigdir}/Qt6UiPlugin.pc
%exclude %{_qt6_includedir}/QtDesigner/%{real_version}

%files -n qt6-designer-private-devel
%{_qt6_includedir}/QtDesigner/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_designer_private.pri

%files -n libQt6Help6
%{_qt6_libdir}/libQt6Help.so.*

%files -n qt6-help-devel
%{_qt6_cmakedir}/Qt6Help/
%{_qt6_descriptionsdir}/Help.json
%{_qt6_includedir}/QtHelp/
%{_qt6_libdir}/libQt6Help.prl
%{_qt6_libdir}/libQt6Help.so
%{_qt6_metatypesdir}/qt6help_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_help.pri
%{_qt6_pkgconfigdir}/Qt6Help.pc
%exclude %{_qt6_includedir}/QtHelp/%{real_version}

%files -n qt6-help-private-devel
%{_qt6_includedir}/QtHelp/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_help_private.pri

%files -n libQt6UiTools6
%{_qt6_libdir}/libQt6UiTools.so.*

%files -n qt6-uitools-devel
%{_qt6_cmakedir}/Qt6UiTools/
%{_qt6_descriptionsdir}/UiTools.json
%{_qt6_includedir}/QtUiTools/
%{_qt6_libdir}/libQt6UiTools.prl
%{_qt6_libdir}/libQt6UiTools.so
%{_qt6_metatypesdir}/qt6uitools_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_uitools.pri
%{_qt6_pkgconfigdir}/Qt6UiTools.pc
%exclude %{_qt6_includedir}/QtUiTools/%{real_version}

%files -n qt6-uitools-private-devel
%{_qt6_includedir}/QtUiTools/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_uitools_private.pri

%files assistant
%{_bindir}/assistant6
%{_datadir}/applications/org.qt.assistant6.desktop
%{_datadir}/icons/hicolor/128x128/apps/assistant6.png
%{_datadir}/icons/hicolor/32x32/apps/assistant6.png
%{_qt6_bindir}/assistant

%files designer
%dir %{_qt6_pluginsdir}/designer
%{_bindir}/designer6
%{_datadir}/applications/org.qt.designer6.desktop
%{_datadir}/icons/hicolor/128x128/apps/designer6.png
%{_qt6_bindir}/designer
%{_qt6_pluginsdir}/designer/libcontainerextension.so
%{_qt6_pluginsdir}/designer/libcustomwidgetplugin.so
%{_qt6_pluginsdir}/designer/libqquickwidget.so
%{_qt6_pluginsdir}/designer/libtaskmenuextension.so

%files helpgenerators
%{_qt6_libexecdir}/qhelpgenerator

%files linguist
%dir %{_qt6_datadir}/phrasebooks
%{_bindir}/lconvert6
%{_bindir}/linguist6
%{_bindir}/lrelease6
%{_bindir}/lupdate6
%{_datadir}/applications/org.qt.linguist6.desktop
%{_datadir}/icons/hicolor/48x48/apps/linguist6.png
%{_datadir}/icons/hicolor/128x128/apps/linguist6.png
%{_qt6_bindir}/lconvert
%{_qt6_bindir}/linguist
%{_qt6_bindir}/lrelease
%{_qt6_bindir}/lupdate
%{_qt6_datadir}/phrasebooks/*.qph
%{_qt6_libexecdir}/lprodump
%{_qt6_libexecdir}/lrelease-pro
%{_qt6_libexecdir}/lupdate-pro

%files -n qt6-linguist-devel
%{_qt6_descriptionsdir}/Linguist.json
%{_qt6_cmakedir}/Qt6Linguist/
%{_qt6_cmakedir}/Qt6LinguistTools/
%{_qt6_mkspecsdir}/modules/qt_lib_linguist.pri
%{_qt6_pkgconfigdir}/Qt6Linguist.pc

%files qdbus
%{_bindir}/qdbus6
%{_bindir}/qdbusviewer6
%{_datadir}/applications/org.qt.qdbusviewer6.desktop
%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer6.png
%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer6.png
%{_qt6_bindir}/qdbus
%{_qt6_bindir}/qdbusviewer

%files qdoc
%{_bindir}/qdoc6
%{_qt6_bindir}/qdoc

### Private only library ###
%files -n libQt6DesignerComponents6
%{_qt6_libdir}/libQt6DesignerComponents.so.*

%files -n qt6-designercomponents-private-devel
%{_qt6_cmakedir}/Qt6DesignerComponentsPrivate/
%{_qt6_descriptionsdir}/DesignerComponentsPrivate.json
%{_qt6_includedir}/QtDesignerComponents/
%{_qt6_libdir}/libQt6DesignerComponents.prl
%{_qt6_libdir}/libQt6DesignerComponents.so
%{_qt6_metatypesdir}/qt6designercomponentsprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_designercomponents_private.pri

%endif

%changelog
