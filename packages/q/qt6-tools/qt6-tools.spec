#
# spec file for package qt6-tools
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


%define real_version 6.1.0
%define short_version 6.1
%define tar_name qttools-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-tools%{?pkg_suffix}
Version:        6.1.0
Release:        0
Summary:        Qt 6 Tools libraries and tools
# TODO Check if it's still valid
# Legal:
# most src/ subfolders are GPL-3.0-only WITH Qt-GPL-exception-1.0, except:
# qtpaths is BSD-3-Clause
# qdoc is GPL-3.0-only WITH Qt-GPL-exception-1.0 + (LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)) == GPL-3.0-only
# src/shared contains BSD-3-Clause and LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) files. The
# 'GPL-3.0-only WITH Qt-GPL-exception-1.0' files in this folder are only used on Windows.
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source10:       org.qt.designer6.desktop
Source11:       org.qt.linguist6.desktop
Source12:       org.qt.qdbusviewer6.desktop
Source13:       org.qt.assistant6.desktop
Source99:       qt6-tools-rpmlintrc
# clang-devel in Leap 15.3 points to clang7...
%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150300
BuildRequires:  clang11-devel
%else
BuildRequires:  clang-devel >= 8
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-dbus-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6QmlDevTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
# These packages are required to generate documentation for the Qt packages
Requires:       qt6-tools-helpgenerators
Requires:       qt6-tools-qdoc
Recommends:     qt6-tools-assistant
Recommends:     qt6-tools-designer
Recommends:     qt6-tools-linguist
Recommends:     qt6-tools-qdbus
Recommends:     qt6-tools-qtpaths
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

%package -n libQt6DesignerComponents6
Summary:        Qt 6 DesignerComponents library
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0

%description -n libQt6DesignerComponents6
This package contains the Qt 6 Designer Library.

%package -n qt6-designer-devel
Summary:        Qt 6 Designer libraries - Development files
Requires:       libQt6Designer6 = %{version}
Requires:       libQt6DesignerComponents6 = %{version}

%description -n qt6-designer-devel
Development files for the Qt6 Designer libraries.

%package -n qt6-designer-private-devel
Summary:        Non-ABI stable API for the Qt 6 Designer libraries
Requires:       cmake(Qt6Designer) = %{real_version}
Requires:       cmake(Qt6DesignerComponents) = %{real_version}
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
# Qt6UiToolsDependencies.cmake has explicit dependencies on these libraries
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6OpenGLWidgets)
Requires:       cmake(Qt6Widgets)

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

%package qtpaths
Summary:        Command line client to QStandardPaths
License:        BSD-3-Clause

%description qtpaths
Command line client to QStandardPaths.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# 475d609 creates a useless qtdiag6 hardlink (also see QTBUG-89170)
rm %{buildroot}%{_qt6_bindir}/qtdiag6

%{qt6_link_executables}

# Unused file. There is no private headers for this library
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_linguist_private.pri

# Desktop files for applications
%suse_update_desktop_file -i org.qt.assistant6
%suse_update_desktop_file -i org.qt.designer6
%suse_update_desktop_file -i org.qt.linguist6
%suse_update_desktop_file -i org.qt.qdbusviewer6

# Icons for the desktop files
install -D -m644 src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer6.png
install -D -m644 src/linguist/linguist/images/icons/linguist-48-32.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/linguist6.png
install -D -m644 src/linguist/linguist/images/icons/linguist-128-32.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/linguist6.png
install -D -m644 src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer6.png
install -D -m644 src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer6.png
install -D -m644 src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant6.png
install -D -m644 src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant6.png

%post -n libQt6Designer6 -p /sbin/ldconfig
%postun -n libQt6Designer6 -p /sbin/ldconfig
%post -n libQt6DesignerComponents6 -p /sbin/ldconfig
%postun -n libQt6DesignerComponents6 -p /sbin/ldconfig
%post -n libQt6Help6 -p /sbin/ldconfig
%postun -n libQt6Help6 -p /sbin/ldconfig
%post -n libQt6UiTools6 -p /sbin/ldconfig
%postun -n libQt6UiTools6 -p /sbin/ldconfig

%files
%license LICENSE.*
%{_bindir}/pixeltool6
%{_bindir}/qdistancefieldgenerator6
%{_bindir}/qtattributionsscanner6
%{_bindir}/qtdiag6
%{_bindir}/qtplugininfo6
%{_qt6_bindir}/pixeltool
%{_qt6_bindir}/qdistancefieldgenerator
%{_qt6_bindir}/qtattributionsscanner
%{_qt6_bindir}/qtdiag
%{_qt6_bindir}/qtplugininfo

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

%files -n libQt6DesignerComponents6
%{_qt6_libdir}/libQt6DesignerComponents.so.*

%files -n qt6-designer-devel
%{_qt6_cmakedir}/Qt6Designer/
%{_qt6_cmakedir}/Qt6DesignerComponents/
%{_qt6_cmakedir}/Qt6UiPlugin/
%{_qt6_descriptionsdir}/Designer.json
%{_qt6_descriptionsdir}/DesignerComponents.json
%{_qt6_descriptionsdir}/UiPlugin.json
%{_qt6_includedir}/QtDesigner/
%{_qt6_includedir}/QtDesignerComponents/
%{_qt6_includedir}/QtUiPlugin/
%{_qt6_libdir}/libQt6Designer.prl
%{_qt6_libdir}/libQt6Designer.so
%{_qt6_libdir}/libQt6DesignerComponents.prl
%{_qt6_libdir}/libQt6DesignerComponents.so
%{_qt6_mkspecsdir}/modules/qt_lib_designer.pri
%{_qt6_mkspecsdir}/modules/qt_lib_uiplugin.pri
%exclude %{_qt6_includedir}/QtDesigner/%{real_version}
%exclude %{_qt6_includedir}/QtDesignerComponents/%{real_version}

%files -n qt6-designer-private-devel
%{_qt6_includedir}/QtDesigner/%{real_version}/
%{_qt6_includedir}/QtDesignerComponents/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_designer_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_designercomponents_private.pri

%files -n libQt6Help6
%{_qt6_libdir}/libQt6Help.so.*

%files -n qt6-help-devel
%{_qt6_cmakedir}/Qt6Help/
%{_qt6_descriptionsdir}/Help.json
%{_qt6_includedir}/QtHelp/
%{_qt6_libdir}/libQt6Help.prl
%{_qt6_libdir}/libQt6Help.so
%{_qt6_mkspecsdir}/modules/qt_lib_help.pri
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
%{_qt6_mkspecsdir}/modules/qt_lib_uitools.pri
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
%{_qt6_pluginsdir}/designer/libqquickwidget.so

%files helpgenerators
%{_bindir}/qhelpgenerator6
%{_qt6_bindir}/qhelpgenerator

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

%files qtpaths
%{_bindir}/qtpaths6
%{_qt6_bindir}/qtpaths

%endif

%changelog
