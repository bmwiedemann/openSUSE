#
# spec file for package qt6-declarative
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


%define real_version 6.9.1
%define short_version 6.9
%define tar_name qtdeclarative-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-declarative%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        Qt 6 Declarative Libraries and tools
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-declarative-rpmlintrc
# PATCH-FIX-OPENSUSE
Patch0:         0001-qmlimportscanner-Include-module-versions-again.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-qmlcachegen-fix-crash-on-unresolved-type-with-requir.patch
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  cmake(Qt6Concurrent) = %{real_version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6GuiPrivate) = %{real_version}
BuildRequires:  cmake(Qt6LanguageServerPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6OpenGL) = %{real_version}
BuildRequires:  cmake(Qt6OpenGLPrivate) = %{real_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}
BuildRequires:  cmake(Qt6Sql) = %{real_version}
BuildRequires:  cmake(Qt6Svg) = %{real_version}
BuildRequires:  cmake(Qt6SvgPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Test) = %{real_version}
BuildRequires:  cmake(Qt6TestPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  cmake(Qt6WidgetsPrivate) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%endif

%description
Qt 6 Declarative Libraries and tools

%if %{qt6_docs_flavor}
# qtdeclarative and qtquickcontrols2 were merged before the 6.2 release.
# Provides/Obsoletes are needed, we can't use the %%qt6_doc_packages and
# %%qt6_examples_package macros.
%package -n qt6-declarative-docs-html
Summary:        Documentation for qt6-declarative in HTML format
License:        GFDL-1.3-or-later
Provides:       qt6-quickcontrols2-docs-html = 6.2.0
Obsoletes:      qt6-quickcontrols2-docs-html < 6.2.0

%description -n qt6-declarative-docs-html
This package contains documentation for qt6-declarative in HTML format.

%package -n qt6-declarative-docs-qch
Summary:        Documentation for qt6-declarative in QCH format
License:        GFDL-1.3-or-later
Provides:       qt6-quickcontrols2-docs-qch = 6.2.0
Obsoletes:      qt6-quickcontrols2-docs-qch < 6.2.0

%description -n qt6-declarative-docs-qch
This package contains documentation for qt6-declarative in QCH format.

%else

%package devel
Summary:        Qt 6 Declarative meta package
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlCompiler) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickControls2) = %{real_version}
Requires:       cmake(Qt6QuickControls2Impl) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2QuickImpl) = %{real_version}
Requires:       cmake(Qt6QuickTest) = %{real_version}
Requires:       cmake(Qt6QuickWidgets) = %{real_version}
BuildArch:      noarch

%description devel
This meta-package requires all the qt6-declarative development packages.

%package private-devel
Summary:        Qt 6 Declarative unstable ABI meta package
Requires:       cmake(Qt6QmlCompilerPrivate) = %{real_version}
Requires:       cmake(Qt6QmlCorePrivate) = %{real_version}
Requires:       cmake(Qt6QmlLocalStoragePrivate) = %{real_version}
Requires:       cmake(Qt6QmlMetaPrivate) = %{real_version}
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Requires:       cmake(Qt6QmlNetworkPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QmlWorkerScriptPrivate) = %{real_version}
Requires:       cmake(Qt6QmlXmlListModelPrivate) = %{real_version}
Requires:       cmake(Qt6QuickControls2ImplPrivate) = %{real_version}
Requires:       cmake(Qt6QuickControls2Private) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2Private) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2QuickImplPrivate) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2UtilsPrivate) = %{real_version}
Requires:       cmake(Qt6QuickEffectsPrivate) = %{real_version}
Requires:       cmake(Qt6QuickLayoutsPrivate) = %{real_version}
Requires:       cmake(Qt6QuickParticlesPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6QuickShapesPrivate) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2Private) = %{real_version}
Requires:       cmake(Qt6QuickTestPrivate) = %{real_version}
Requires:       cmake(Qt6QuickVectorImagePrivate) = %{real_version}
Requires:       cmake(Qt6QuickWidgetsPrivate) = %{real_version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-declarative development packages that do
not have any ABI or API guarantees.

%package examples
Summary:        Examples for the qt6-declarative module
Provides:       qt6-quickcontrols2-examples = 6.2.0
Obsoletes:      qt6-quickcontrols2-examples < 6.2.0

%description examples
Examples for the qt6-declarative module.

%package imports
Summary:        Qt 6 Declarative QML files and plugins
Provides:       qt6-quickcontrols2-imports = 6.2.0
Obsoletes:      qt6-quickcontrols2-imports < 6.2.0

%description imports
QML files and plugins from the Qt 6 Declarative module.

%package tools
Summary:        Qt 6 Declarative Tools
License:        GPL-3.0-only
Requires:       qt6-declarative-imports = %{version}
Requires:       (qml-autoreqprov if rpm-build)

%description tools
Additional tools for inspecting, testing, viewing QML imports and files.

%package -n libQt6Qml6
Summary:        Qt 6 Qml library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       qt6-declarative-imports
Requires:       (qml-autoreqprov if rpm-build)

%description -n libQt6Qml6
The Qt 6 Qml library.

%package -n qt6-qml-devel
Summary:        Qt 6 Qml library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6Qml6 = %{version}
# Executables are required
Requires:       qt6-declarative-tools = %{version}
Requires:       cmake(Qt6Network) = %{real_version}
# Required by Qt6QmlMacros.cmake
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
# qmldevtools is gone since 6.3
Provides:       qt6-qmldevtools-devel-static = 6.3
Obsoletes:      qt6-qmldevtools-devel-static < 6.3

%description -n qt6-qml-devel
Development files for the Qt 6 Qml library.

%package -n qt6-qml-private-devel
Summary:        Non-ABI stable API for the Qt 6 Qml library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}

%description -n qt6-qml-private-devel
This package provides private headers of libQt6Qml that do not have any
ABI or API guarantees.

%package -n libQt6QmlCompiler6
Summary:        Qt6 QmlCompiler library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QmlCompiler6
The Qt 6 QmlCompiler library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmlcompiler-devel
Summary:        Qt 6 QmlCompiler library - Development files
Requires:       libQt6QmlCompiler6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
# The qmlcompiler library became a shared library (again) in 6.4.0
Provides:       qt6-qmlcompiler-devel-static = 6.4.0
Obsoletes:      qt6-qmlcompiler-devel-static < 6.4.0

%description -n qt6-qmlcompiler-devel
Development files for the Qt 6 QmlCompiler library.

%package -n qt6-qmlcompiler-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlCompiler library
Requires:       qt6-qmlcompiler-devel = %{version}

%description -n qt6-qmlcompiler-private-devel
This package provides private headers of libQt6QmlCompiler that do not have any
ABI or API guarantees.

%package -n libQt6Quick6
Summary:        Qt 6 Quick library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6Quick6
The Qt 6 Quick library.

%package -n qt6-quick-devel
Summary:        Qt 6 Quick library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6Quick6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}

%description -n qt6-quick-devel
Development files for the Qt 6 Quick library.

%package -n qt6-quick-private-devel
Summary:        Non-ABI stable API for the Qt 6 Quick library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}

%description -n qt6-quick-private-devel
This package provides private headers of libQt6Quick that do not have any
ABI or API guarantees.

%package -n libQt6QuickControls2-6
Summary:        Qt 6 QuickControls2 library

%description -n libQt6QuickControls2-6
The Qt 6 QuickControls2 library.

%package -n qt6-quickcontrols2-devel
Summary:        Qt 6 QuickControls2 library - Development files
Requires:       libQt6QuickControls2-6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}

%description -n qt6-quickcontrols2-devel
Development files for the Qt 6 QuickControls2 library.

%package -n qt6-quickcontrols2-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickControls2 library
Requires:       cmake(Qt6QuickControls2) = %{real_version}

%description -n qt6-quickcontrols2-private-devel
This package provides private headers of libQt6QuickControls2 that do not have
any ABI or API guarantees.

%package -n libQt6QuickControls2Impl6
Summary:        Qt 6 QuickControls2Impl library

%description -n libQt6QuickControls2Impl6
The Qt 6 QuickControls2Impl library.

%package -n qt6-quickcontrols2impl-devel
Summary:        Qt6 QuickControls2Impl library - Development files
Requires:       libQt6QuickControls2Impl6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}

%description -n qt6-quickcontrols2impl-devel
Development files for the Qt 6 QuickControls2Impl library.

%package -n qt6-quickcontrols2impl-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickControls2Impl library
Requires:       cmake(Qt6QuickControls2Impl) = %{real_version}

%description -n qt6-quickcontrols2impl-private-devel
This package provides private headers of libQt6QuickControls2Impl that do not
have any ABI or API guarantees.

%package -n libQt6QuickDialogs2-6
Summary:        Qt 6 QuickDialogs2 library

%description -n libQt6QuickDialogs2-6
The Qt 6 QuickDialogs2 library.

%package -n qt6-quickdialogs2-devel
Summary:        Qt6 QuickDialogs2 library - Development files
Requires:       libQt6QuickDialogs2-6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickControls2Impl) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2QuickImpl) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2Utils) = %{real_version}

%description -n qt6-quickdialogs2-devel
Development files for the Qt 6 QuickDialogs2 library.

%package -n qt6-quickdialogs2-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickDialogs2 library
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2) = %{real_version}

%description -n qt6-quickdialogs2-private-devel
This package provides private headers of libQt6QuickDialogs2 that do not have
any ABI or API guarantees.

%package -n libQt6QuickDialogs2QuickImpl6
Summary:        Qt 6 QuickDialogs2Impl library

%description -n libQt6QuickDialogs2QuickImpl6
The Qt 6 QuickDialogs2Impl library.

%package -n qt6-quickdialogs2quickimpl-devel
Summary:        Qt6 QuickDialogs2Impl library - Development files
Requires:       libQt6QuickDialogs2QuickImpl6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickControls2Impl) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2Utils) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}

%description -n qt6-quickdialogs2quickimpl-devel
Development files for the Qt 6 QuickDialogs2Impl library.

%package -n qt6-quickdialogs2quickimpl-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickDialogs2Impl library
Requires:       cmake(Qt6QuickDialogs2QuickImpl) = %{real_version}

%description -n qt6-quickdialogs2quickimpl-private-devel
This package provides private headers of libQt6QuickDialogs2Impl that do not
have any ABI or API guarantees.

%package -n libQt6QuickTest6
Summary:        Qt 6 QuickTest library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickTest6
The Qt 6 QuickTest library.

%package -n qt6-quicktest-devel
Summary:        Qt 6 QuickTest library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickTest6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Test) = %{real_version}

%description -n qt6-quicktest-devel
Development files for the Qt 6 QuickTest library.

%package -n qt6-quicktest-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickTest library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6QuickTest) = %{real_version}
Requires:       cmake(Qt6TestPrivate) = %{real_version}

%description -n qt6-quicktest-private-devel
This package provides private headers of libQt6QuickTest that do not have any
ABI or API guarantees.

%package -n libQt6QuickWidgets6
Summary:        Qt 6 QuickWidgets library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickWidgets6
The Qt 6 QuickWidgets library.

%package -n qt6-quickwidgets-devel
Summary:        Qt 6 QuickWidgets library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickWidgets6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description -n qt6-quickwidgets-devel
Development files for the Qt 6 QuickWidgets library.

%package -n qt6-quickwidgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickWidgets library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6QuickWidgets) = %{real_version}
Requires:       cmake(Qt6WidgetsPrivate) = %{real_version}

%description -n qt6-quickwidgets-private-devel
This package provides private headers of libQt6QuickWidgets that do not have any
ABI or API guarantees.


### Private only libraries ###

%package -n libQt6LabsPlatform6
Summary:        Qt 6 LabsPlatform library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsPlatform6
The Qt 6 LabsPlatform library.
This library does not have any ABI or API guarantees.

%package -n qt6-labsplatform-private-devel
Summary:        Qt 6 LabsPlatform library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2Private) = %{real_version}

%description -n qt6-labsplatform-private-devel
Development files for the Qt 6 LabsPlatform library.
This library does not have any ABI or API guarantees.

%package -n libQt6LabsAnimation6
Summary:        Qt 6 LabsAnimation library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsAnimation6
The Qt 6 LabsAnimation library.
This library does not have any ABI or API guarantees.

%package -n qt6-labsanimation-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsAnimation library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6LabsAnimation6 = %{version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Provides:       qt6-labsanimation-devel = %{version}
Obsoletes:      qt6-labsanimation-devel < %{version}

%description -n qt6-labsanimation-private-devel
Development files for the Qt 6 LabsAnimation library.
This library does not have any ABI or API guarantees.

%package -n libQt6LabsFolderListModel6
Summary:        Qt 6 LabsFolderListModel library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsFolderListModel6
The Qt 6 LabsFolderListModel library.
This library does not have any ABI or API guarantees.

%package -n qt6-labsfolderlistmodel-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsFolderListModel library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6LabsFolderListModel6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Provides:       qt6-labsfolderlistmodel-devel = %{version}
Obsoletes:      qt6-labsfolderlistmodel-devel < %{version}

%description -n qt6-labsfolderlistmodel-private-devel
Development files for the Qt 6 LabsFolderListModel library.
This library does not have any ABI or API guarantees.

%package -n libQt6LabsQmlModels6
Summary:        Qt 6 LabsQmlModels library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsQmlModels6
The Qt 6 LabsQmlModels library.
This library does not have any ABI or API guarantees.

%package -n qt6-labsqmlmodels-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsQmlModels library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6LabsQmlModels6 = %{version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Provides:       qt6-labsqmlmodels-devel = %{version}
Obsoletes:      qt6-labsqmlmodels-devel < %{version}

%description -n qt6-labsqmlmodels-private-devel
Development files for the Qt 6 LabsQmlModels library.
This library does not have any ABI or API guarantees.

%package -n libQt6LabsSettings6
Summary:        Qt 6 LabsSettings library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsSettings6
The Qt 6 LabsSettings library.
This library does not have any ABI or API guarantees.

%package -n qt6-labssettings-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsSettings library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6LabsSettings6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Provides:       qt6-labssettings-devel = %{version}
Obsoletes:      qt6-labssettings-devel < %{version}

%description -n qt6-labssettings-private-devel
Development files for the Qt 6 LabsSettings library.
This library does not have any ABI or API guarantees.

%package -n libQt6LabsSharedImage6
Summary:        Qt 6 LabsSharedImage library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsSharedImage6
The Qt 6 LabsSharedImage library.
This library does not have any ABI or API guarantees.

%package -n qt6-labssharedimage-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsSharedImage library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6LabsSharedImage6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Provides:       qt6-labssharedimage-devel = %{version}
Obsoletes:      qt6-labssharedimage-devel < %{version}

%description -n qt6-labssharedimage-private-devel
Development files for the Qt 6 LabsSharedImage library.
This library does not have any ABI or API guarantees.

%package -n libQt6LabsWavefrontMesh6
Summary:        Qt 6 LabsWavefrontMesh library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6LabsWavefrontMesh6
The Qt 6 LabsWavefrontMesh library.
This library does not have any ABI or API guarantees.

%package -n qt6-labswavefrontmesh-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsWavefrontMesh library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6LabsWavefrontMesh6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Provides:       qt6-labswavefrontmesh-devel = %{version}
Obsoletes:      qt6-labswavefrontmesh-devel < %{version}

%description -n qt6-labswavefrontmesh-private-devel
Development files for the Qt 6 LabsWavefrontMesh library.
This library does not have any ABI or API guarantees.

%package -n libQt6QmlCore6
Summary:        Qt 6 QmlCore library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       qt6-declarative-imports

%description -n libQt6QmlCore6
The Qt 6 QmlCore library.

%package -n qt6-qmlcore-private-devel
Summary:        Qt 6 QmlCore library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlCore6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Provides:       qt6-qmlcore-devel = %{version}
Obsoletes:      qt6-qmlcore-devel < %{version}

%description -n qt6-qmlcore-private-devel
Development files for the Qt 6 QmlCore library.
This library does not have any ABI or API guarantees.

%package -n libQt6QmlLocalStorage6
Summary:        Qt 6 QmlLocalStorage library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QmlLocalStorage6
The Qt 6 QmlLocalStorage library.

%package -n qt6-qmllocalstorage-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlLocalStorage library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlLocalStorage6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6Sql) = %{real_version}
Provides:       qt6-qmllocalstorage-devel = %{version}
Obsoletes:      qt6-qmllocalstorage-devel < %{version}

%description -n qt6-qmllocalstorage-private-devel
Development files for the Qt 6 QmlLocalStorage library.
This library does not have any ABI or API guarantees.

%package -n libQt6QmlMeta6
Summary:        Qt 6 QmlMeta library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QmlMeta6
The Qt 6 QmlMeta library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmlmeta-private-devel
Summary:        Qt 6 QmlMeta library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlMeta6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
Requires:       cmake(Qt6QmlWorkerScript) = %{real_version}

%description -n qt6-qmlmeta-private-devel
Development files for the Qt 6 QmlMeta library.
This library does not have any ABI or API guarantees.

%package -n libQt6QmlModels6
Summary:        Qt 6 QmlModels library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QmlModels6
The Qt 6 QmlModels library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmlmodels-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlModels library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlModels6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Provides:       qt6-qmlmodels-devel = %{version}
Obsoletes:      qt6-qmlmodels-devel < %{version}

%description -n qt6-qmlmodels-private-devel
This package provides private headers of libQt6QmlModels that do not have any
ABI or API guarantees.

%package -n libQt6QmlNetwork6
Summary:        Qt 6 QmlNetwork library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QmlNetwork6
QML Binding for the QNetworkInformation C++ class.
This library does not have any ABI or API guarantees.

%package -n qt6-qmlnetwork-private-devel
Summary:        Qt 6 QmlNetwork library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlNetwork6 = %{version}
Requires:       qt6-network-devel = %{version}
Requires:       qt6-qml-devel = %{version}

%description -n qt6-qmlnetwork-private-devel
Development files for the Qt 6 QmlNetwork library.
This library does not have any ABI or API guarantees.

%package -n libQt6QmlWorkerScript6
Summary:        Qt 6 QmlWorkScript library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QmlWorkerScript6
The Qt 6 QmlModels library.

%package -n qt6-qmlworkerscript-private-devel
Summary:        Qt 6 QmlWorkerScript library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlWorkerScript6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Provides:       qt6-qmlworkerscript-devel = %{version}
Obsoletes:      qt6-qmlworkerscript-devel < %{version}

%description -n qt6-qmlworkerscript-private-devel
Development files for the Qt 6 QmlWorkerScript library.
This library does not have any ABI or API guarantees.

%package -n libQt6QmlXmlListModel6
Summary:        Qt 6 QmlXmlListModel library

%description -n libQt6QmlXmlListModel6
The Qt 6 QmlXmlListModel library.

%package -n qt6-qmlxmllistmodel-private-devel
Summary:        Qt 6 QmlXmlListModel library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QmlXmlListModel6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
Provides:       qt6-qmlxmllistmodel-devel = %{version}
Obsoletes:      qt6-qmlxmllistmodel-devel < %{version}

%description -n qt6-qmlxmllistmodel-private-devel
Development files for the Qt 6 QmlXmlListModel library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickDialogs2Utils6
Summary:        Qt 6 QuickDialogs2Utils library

%description -n libQt6QuickDialogs2Utils6
The Qt 6 QuickDialogs2Utils library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickdialogs2utils-private-devel
Summary:        Qt6 QuickDialogs2Utils library - Development files
Requires:       libQt6QuickDialogs2Utils6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Provides:       qt6-quickdialogs2utils-devel = %{version}
Obsoletes:      qt6-quickdialogs2utils-devel < %{version}

%description -n qt6-quickdialogs2utils-private-devel
The Qt 6 QuickDialogs2Utils library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickEffects6
Summary:        Qt 6 QuickEffects library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickEffects6
The Qt 6 QuickEffects library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickeffects-private-devel
Summary:        Qt 6 QuickEffects library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickEffects6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}

%description -n qt6-quickeffects-private-devel
Development files for the Qt 6 QuickEffects library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickLayouts6
Summary:        Qt 6 QuickLayouts library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickLayouts6
The Qt 6 QuickLayouts library.

%package -n qt6-quicklayouts-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickLayouts library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickLayouts6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Provides:       qt6-quicklayouts-devel = %{version}
Obsoletes:      qt6-quicklayouts-devel < %{version}

%description -n qt6-quicklayouts-private-devel
Development files for the Qt 6 QuickLayouts library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickParticles6
Summary:        Qt 6 QuickParticles library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickParticles6
The Qt 6 QuickParticles library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickparticles-private-devel
Summary:        Qt 6 QuickParticles library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickParticles6 = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-quickparticles-devel = 6.2.0
Obsoletes:      qt6-quickparticles-devel < 6.2.0

%description -n qt6-quickparticles-private-devel
Development files for the Qt 6 QuickParticles library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickShapes6
Summary:        Qt 6 QuickShapes library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickShapes6
The Qt 6 QuickShapes library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickshapes-private-devel
Summary:        Qt 6 QuickShapes library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickShapes6 = %{version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-quickshapes-devel = 6.2.0
Obsoletes:      qt6-quickshapes-devel < 6.2.0

%description -n qt6-quickshapes-private-devel
Development files for the Qt 6 QuickShapes library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickTemplates2-6
Summary:        Qt 6 QuickTemplates2 library

%description -n libQt6QuickTemplates2-6
The Qt 6 QuickTemplates2 library.
This library does not have any ABI or API guarantees.

%package -n qt6-quicktemplates2-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickTemplates2 library
Requires:       libQt6QuickTemplates2-6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
Requires:       cmake(Qt6QmlModelsPrivate) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Provides:       qt6-quicktemplates2-devel = %{version}
Obsoletes:      qt6-quicktemplates2-devel < %{version}

%description -n qt6-quicktemplates2-private-devel
Development files for the Qt 6 QuickTemplates2 library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickVectorImage6
Summary:        Qt 6 QuickVectorImage library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only

%description -n libQt6QuickVectorImage6
The Qt 6 QuickVectorImage library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickvectorimage-private-devel
Summary:        Qt 6 QuickVectorImage library - Development files
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       libQt6QuickVectorImage6 = %{version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6QuickShapesPrivate) = %{real_version}
Requires:       cmake(Qt6SvgPrivate) = %{real_version}

%description -n qt6-quickvectorimage-private-devel
Development files for the Qt 6 QuickVectorImage library.
This library does not have any ABI or API guarantees.


### Static libraries ###

%package -n qt6-packetprotocol-devel-static
Summary:        Qt6 PacketProtocol static library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6CorePrivate) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-packetprotocol-private-devel = 6.2.0
Obsoletes:      qt6-packetprotocol-private-devel < 6.2.0

%description -n qt6-packetprotocol-devel-static
The Qt6 PacketProtocol static library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmldebug-devel-static
Summary:        Qt6 QmlDebug static library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       qt6-packetprotocol-devel-static = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-qmldebug-private-devel = 6.2.0
Obsoletes:      qt6-qmldebug-private-devel < 6.2.0

%description -n qt6-qmldebug-devel-static
The Qt6 QmlDebug static library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmldom-devel-static
Summary:        Qt6 QmlDom static library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-qmldom-private-devel = 6.2.0
Obsoletes:      qt6-qmldom-private-devel < 6.2.0

%description -n qt6-qmldom-devel-static
The Qt6 QmlDom static library.
The goal of the Dom library is to provide a nicer to use basis for the
Qml Code model, to be used by the various QML tools, the designer and
the new compiler.

%package -n qt6-qmlformat-devel-static
Summary:        Qt6 QmlFormat static library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6QmlPrivate) = %{real_version}

%description -n qt6-qmlformat-devel-static
The Qt6 QmlFormat static library.
This code parses .qmlformat.ini files and is required by the QmlLS static library

%package -n qt6-qmlls-devel-static
Summary:        Qt6 QmlLS static library
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6LanguageServerPrivate) = %{real_version}
Requires:       cmake(Qt6QmlCompiler) = %{real_version}
Requires:       cmake(Qt6QmlCompilerPrivate) = %{real_version}
Requires:       cmake(Qt6QmlDomPrivate) = %{real_version}
Requires:       cmake(Qt6QmlFormatPrivate) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6QmlToolingSettingsPrivate) = %{real_version}

%description -n qt6-qmlls-devel-static
The Qt6 QmlLS static library.

%package -n qt6-qmltoolingsettings-devel-static
Summary:        Qt6 QmlToolingSettings static library
Requires:       cmake(Qt6CorePrivate) = %{real_version}

%description -n qt6-qmltoolingsettings-devel-static
The Qt6 QmlToolingSettings static library.

%package -n qt6-qmltyperegistrar-devel-static
Summary:        Qt6 QmlTypeRegistrar static library

%description -n qt6-qmltyperegistrar-devel-static
The Qt6 QmlTypeRegistrar static library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickcontrolstestutils-devel-static
Summary:        Qt6 QuickControlsTestUtils static library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6QuickControls2) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2QuickImpl) = %{real_version}
Requires:       cmake(Qt6QuickPrivate) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}
Requires:       cmake(Qt6Test) = %{real_version}
Requires:       qt6-quicktestutils-devel-static = %{version}

%description -n qt6-quickcontrolstestutils-devel-static
The Qt6 QuickControlsTestUtils static library.

%package -n qt6-quicktestutils-devel-static
Summary:        Qt6 QuickTestUtils static library
License:        GPL-2.0-only OR GPL-3.0-or-later OR LGPL-3.0-only
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6QmlPrivate) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickTest) = %{real_version}
Requires:       cmake(Qt6Test) = %{real_version}

%description -n qt6-quicktestutils-devel-static
The Qt6 QuickTestUtils static library.

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# Empty file used for the meta packages
cat >> meta_package << EOF
This is a meta package, it does not contain any file
EOF

%build
%ifarch s390x
%if "%{qt6_flavor}" == ""
# Determine the right number of parallel processes based on the available memory
%limit_build -m 1700
%endif
%endif
# Package provides static libraries
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# Empty folder provided by libQt6Qml6
mkdir -p %{buildroot}%{_qt6_importsdir}

%{qt6_link_executables}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin{Config,Targets}*.cmake

# There are no private headers
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_qmlintegration_private.pri

%ldconfig_scriptlets -n libQt6LabsAnimation6
%ldconfig_scriptlets -n libQt6LabsFolderListModel6
%ldconfig_scriptlets -n libQt6LabsPlatform6
%ldconfig_scriptlets -n libQt6LabsQmlModels6
%ldconfig_scriptlets -n libQt6LabsSettings6
%ldconfig_scriptlets -n libQt6LabsSharedImage6
%ldconfig_scriptlets -n libQt6LabsWavefrontMesh6
%ldconfig_scriptlets -n libQt6Qml6
%ldconfig_scriptlets -n libQt6QmlCompiler6
%ldconfig_scriptlets -n libQt6QmlCore6
%ldconfig_scriptlets -n libQt6QmlLocalStorage6
%ldconfig_scriptlets -n libQt6QmlMeta6
%ldconfig_scriptlets -n libQt6QmlModels6
%ldconfig_scriptlets -n libQt6QmlNetwork6
%ldconfig_scriptlets -n libQt6QmlWorkerScript6
%ldconfig_scriptlets -n libQt6QmlXmlListModel6
%ldconfig_scriptlets -n libQt6Quick6
%ldconfig_scriptlets -n libQt6QuickControls2-6
%ldconfig_scriptlets -n libQt6QuickControls2Impl6
%ldconfig_scriptlets -n libQt6QuickDialogs2-6
%ldconfig_scriptlets -n libQt6QuickDialogs2QuickImpl6
%ldconfig_scriptlets -n libQt6QuickDialogs2Utils6
%ldconfig_scriptlets -n libQt6QuickEffects6
%ldconfig_scriptlets -n libQt6QuickLayouts6
%ldconfig_scriptlets -n libQt6QuickParticles6
%ldconfig_scriptlets -n libQt6QuickShapes6
%ldconfig_scriptlets -n libQt6QuickTemplates2-6
%ldconfig_scriptlets -n libQt6QuickTest6
%ldconfig_scriptlets -n libQt6QuickVectorImage6
%ldconfig_scriptlets -n libQt6QuickWidgets6

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files examples
%{_qt6_examplesdir}/*

%files imports
%{_qt6_qmldir}/QML/
%{_qt6_qmldir}/QmlTime/
%{_qt6_qmldir}/Qt/
%{_qt6_qmldir}/QtCore/
%{_qt6_qmldir}/QtNetwork/
%{_qt6_qmldir}/QtQml/
%{_qt6_qmldir}/QtQuick/
%{_qt6_qmldir}/QtTest/
%{_qt6_qmldir}/builtins.qmltypes
%{_qt6_qmldir}/jsroot.qmltypes

%files tools
%{_bindir}/qml6
%{_bindir}/qmldom6
%{_bindir}/qmleasing6
%{_bindir}/qmlformat6
%{_bindir}/qmllint6
%{_bindir}/qmlls6
%{_bindir}/qmlplugindump6
%{_bindir}/qmlpreview6
%{_bindir}/qmlprofiler6
%{_bindir}/qmlscene6
%{_bindir}/qmltc6
%{_bindir}/qmltestrunner6
%{_bindir}/qmltime6
%{_bindir}/svgtoqml6
%{_qt6_bindir}/qml
%{_qt6_bindir}/qmldom
%{_qt6_bindir}/qmleasing
%{_qt6_bindir}/qmlformat
%{_qt6_bindir}/qmllint
%{_qt6_bindir}/qmlls
%{_qt6_bindir}/qmlplugindump
%{_qt6_bindir}/qmlpreview
%{_qt6_bindir}/qmlprofiler
%{_qt6_bindir}/qmlscene
%{_qt6_bindir}/qmltc
%{_qt6_bindir}/qmltestrunner
%{_qt6_bindir}/qmltime
%{_qt6_bindir}/svgtoqml
%{_qt6_libexecdir}/qmlaotstats
%{_qt6_libexecdir}/qmlcachegen
%{_qt6_libexecdir}/qmlimportscanner
%{_qt6_libexecdir}/qmljsrootgen
%{_qt6_libexecdir}/qmltyperegistrar
%{_qt6_pluginsdir}/qmllint/
%{_qt6_pluginsdir}/qmlls/
%{_qt6_pluginsdir}/qmltooling/

%files -n libQt6Qml6
%license LICENSES/*
# libQt6Qml6 'provides' %%_qt6_importsdir and %%_qt6_qmldir
%dir %{_qt6_importsdir}
%dir %{_qt6_qmldir}
%{_qt6_libdir}/libQt6Qml.so.*

%files -n qt6-qml-devel
%dir %{_qt6_mkspecsdir}/features
%{_qt6_cmakedir}/Qt6Qml/
%{_qt6_cmakedir}/Qt6QmlIntegration/
# Files from the two directories above are only used by Qt6QmlMacros.cmake
%{_qt6_cmakedir}/Qt6QmlImportScanner/
%{_qt6_cmakedir}/Qt6QmlTools/
%{_qt6_descriptionsdir}/Qml.json
%{_qt6_descriptionsdir}/QmlIntegration.json
%{_qt6_includedir}/QtQml/
%{_qt6_includedir}/QtQmlIntegration/
%{_qt6_libdir}/libQt6Qml.prl
%{_qt6_libdir}/libQt6Qml.so
%{_qt6_metatypesdir}/qt6qml_*_metatypes.json
%{_qt6_mkspecsdir}/features/qmlcache.prf
%{_qt6_mkspecsdir}/features/qmltypes.prf
%{_qt6_mkspecsdir}/features/qtquickcompiler.prf
%{_qt6_mkspecsdir}/modules/qt_lib_qml.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlintegration.pri
%{_qt6_pkgconfigdir}/Qt6Qml.pc
%{_qt6_pkgconfigdir}/Qt6QmlIntegration.pc
%exclude %{_qt6_includedir}/QtQml/%{real_version}

%files -n qt6-qml-private-devel
%{_qt6_cmakedir}/Qt6QmlIntegrationPrivate/
%{_qt6_cmakedir}/Qt6QmlPrivate/
%{_qt6_includedir}/QtQml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qml_private.pri

%files -n libQt6QmlCompiler6
%{_qt6_libdir}/libQt6QmlCompiler.so.*

%files -n qt6-qmlcompiler-devel
%{_qt6_cmakedir}/Qt6QmlCompiler/
%{_qt6_descriptionsdir}/QmlCompiler.json
%{_qt6_includedir}/QtQmlCompiler/
%{_qt6_libdir}/libQt6QmlCompiler.prl
%{_qt6_libdir}/libQt6QmlCompiler.so
%{_qt6_metatypesdir}/qt6qmlcompiler_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcompiler.pri
%{_qt6_pkgconfigdir}/Qt6QmlCompiler.pc
%exclude %{_qt6_includedir}/QtQmlCompiler/%{real_version}

%files -n qt6-qmlcompiler-private-devel
%{_qt6_cmakedir}/Qt6QmlCompilerPrivate/
%{_qt6_includedir}/QtQmlCompiler/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcompiler_private.pri

%files -n libQt6Quick6
%{_qt6_libdir}/libQt6Quick.so.*

%files -n qt6-quick-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtDeclarativeTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Quick/
%{_qt6_cmakedir}/Qt6QuickTools/
%{_qt6_descriptionsdir}/Quick.json
%{_qt6_includedir}/QtQuick/
%{_qt6_libdir}/libQt6Quick.prl
%{_qt6_libdir}/libQt6Quick.so
%{_qt6_metatypesdir}/qt6quick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick.pri
%{_qt6_pkgconfigdir}/Qt6Quick.pc
%exclude %{_qt6_includedir}/QtQuick/%{real_version}

%files -n qt6-quick-private-devel
%{_qt6_cmakedir}/Qt6QuickPrivate/
%{_qt6_includedir}/QtQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick_private.pri

%files -n libQt6QuickControls2-6
%{_qt6_libdir}/libQt6QuickControls2.so.*
%{_qt6_libdir}/libQt6QuickControls2Basic.so.*
%{_qt6_libdir}/libQt6QuickControls2Fusion.so.*
%{_qt6_libdir}/libQt6QuickControls2Imagine.so.*
%{_qt6_libdir}/libQt6QuickControls2Material.so.*
%{_qt6_libdir}/libQt6QuickControls2Universal.so.*

%files -n qt6-quickcontrols2-devel
%{_qt6_cmakedir}/Qt6QuickControls2/
%{_qt6_descriptionsdir}/QuickControls2.json
%{_qt6_includedir}/QtQuickControls2/
%{_qt6_libdir}/libQt6QuickControls2.prl
%{_qt6_libdir}/libQt6QuickControls2.so
%{_qt6_metatypesdir}/qt6quickcontrols2_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2.pri
%{_qt6_pkgconfigdir}/Qt6QuickControls2.pc
%exclude %{_qt6_includedir}/QtQuickControls2/%{real_version}

%files -n qt6-quickcontrols2-private-devel
%{_qt6_cmakedir}/Qt6QuickControls2Basic/
%{_qt6_cmakedir}/Qt6QuickControls2BasicPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2Fusion/
%{_qt6_cmakedir}/Qt6QuickControls2FusionPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2Imagine/
%{_qt6_cmakedir}/Qt6QuickControls2ImaginePrivate/
%{_qt6_cmakedir}/Qt6QuickControls2Material/
%{_qt6_cmakedir}/Qt6QuickControls2MaterialPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2Private/
%{_qt6_cmakedir}/Qt6QuickControls2Universal/
%{_qt6_cmakedir}/Qt6QuickControls2UniversalPrivate/
%{_qt6_descriptionsdir}/QuickControls2Basic.json
%{_qt6_descriptionsdir}/QuickControls2Fusion.json
%{_qt6_descriptionsdir}/QuickControls2Imagine.json
%{_qt6_descriptionsdir}/QuickControls2Material.json
%{_qt6_descriptionsdir}/QuickControls2Universal.json
%{_qt6_includedir}/QtQuickControls2/%{real_version}/
%{_qt6_includedir}/QtQuickControls2Basic/
%{_qt6_includedir}/QtQuickControls2Fusion/
%{_qt6_includedir}/QtQuickControls2Imagine/
%{_qt6_includedir}/QtQuickControls2Material/
%{_qt6_includedir}/QtQuickControls2Universal/
%{_qt6_libdir}/libQt6QuickControls2Basic.prl
%{_qt6_libdir}/libQt6QuickControls2Basic.so
%{_qt6_libdir}/libQt6QuickControls2Fusion.prl
%{_qt6_libdir}/libQt6QuickControls2Fusion.so
%{_qt6_libdir}/libQt6QuickControls2Imagine.prl
%{_qt6_libdir}/libQt6QuickControls2Imagine.so
%{_qt6_libdir}/libQt6QuickControls2Material.prl
%{_qt6_libdir}/libQt6QuickControls2Material.so
%{_qt6_libdir}/libQt6QuickControls2Universal.prl
%{_qt6_libdir}/libQt6QuickControls2Universal.so
%{_qt6_metatypesdir}/qt6quickcontrols2basic_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2fusion_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2imagine_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2material_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2universal_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2basic.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2basic_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2fusion.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2fusion_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2imagine.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2imagine_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2material.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2material_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2universal.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2universal_private.pri
%{_qt6_pkgconfigdir}/Qt6QuickControls2Basic.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2Fusion.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2Imagine.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2Material.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2Universal.pc

%files -n libQt6QuickControls2Impl6
%{_qt6_libdir}/libQt6QuickControls2BasicStyleImpl.so.*
%{_qt6_libdir}/libQt6QuickControls2FluentWinUI3StyleImpl.so.*
%{_qt6_libdir}/libQt6QuickControls2FusionStyleImpl.so.*
%{_qt6_libdir}/libQt6QuickControls2ImagineStyleImpl.so.*
%{_qt6_libdir}/libQt6QuickControls2Impl.so.*
%{_qt6_libdir}/libQt6QuickControls2MaterialStyleImpl.so.*
%{_qt6_libdir}/libQt6QuickControls2UniversalStyleImpl.so.*

%files -n qt6-quickcontrols2impl-devel
%{_qt6_cmakedir}/Qt6QuickControls2BasicStyleImpl/
%{_qt6_cmakedir}/Qt6QuickControls2FluentWinUI3StyleImpl/
%{_qt6_cmakedir}/Qt6QuickControls2FusionStyleImpl/
%{_qt6_cmakedir}/Qt6QuickControls2ImagineStyleImpl/
%{_qt6_cmakedir}/Qt6QuickControls2Impl/
%{_qt6_cmakedir}/Qt6QuickControls2MaterialStyleImpl/
%{_qt6_cmakedir}/Qt6QuickControls2UniversalStyleImpl/
%{_qt6_descriptionsdir}/QuickControls2BasicStyleImpl.json
%{_qt6_descriptionsdir}/QuickControls2FluentWinUI3StyleImpl.json
%{_qt6_descriptionsdir}/QuickControls2FusionStyleImpl.json
%{_qt6_descriptionsdir}/QuickControls2ImagineStyleImpl.json
%{_qt6_descriptionsdir}/QuickControls2Impl.json
%{_qt6_descriptionsdir}/QuickControls2MaterialStyleImpl.json
%{_qt6_descriptionsdir}/QuickControls2UniversalStyleImpl.json
%{_qt6_includedir}/QtQuickControls2BasicStyleImpl/
%{_qt6_includedir}/QtQuickControls2FluentWinUI3StyleImpl/
%{_qt6_includedir}/QtQuickControls2FusionStyleImpl/
%{_qt6_includedir}/QtQuickControls2ImagineStyleImpl/
%{_qt6_includedir}/QtQuickControls2Impl/
%{_qt6_includedir}/QtQuickControls2MaterialStyleImpl/
%{_qt6_includedir}/QtQuickControls2UniversalStyleImpl/
%{_qt6_libdir}/libQt6QuickControls2BasicStyleImpl.prl
%{_qt6_libdir}/libQt6QuickControls2BasicStyleImpl.so
%{_qt6_libdir}/libQt6QuickControls2FluentWinUI3StyleImpl.prl
%{_qt6_libdir}/libQt6QuickControls2FluentWinUI3StyleImpl.so
%{_qt6_libdir}/libQt6QuickControls2FusionStyleImpl.prl
%{_qt6_libdir}/libQt6QuickControls2FusionStyleImpl.so
%{_qt6_libdir}/libQt6QuickControls2ImagineStyleImpl.prl
%{_qt6_libdir}/libQt6QuickControls2ImagineStyleImpl.so
%{_qt6_libdir}/libQt6QuickControls2Impl.prl
%{_qt6_libdir}/libQt6QuickControls2Impl.so
%{_qt6_libdir}/libQt6QuickControls2MaterialStyleImpl.prl
%{_qt6_libdir}/libQt6QuickControls2MaterialStyleImpl.so
%{_qt6_libdir}/libQt6QuickControls2UniversalStyleImpl.prl
%{_qt6_libdir}/libQt6QuickControls2UniversalStyleImpl.so
%{_qt6_metatypesdir}/qt6quickcontrols2basicstyleimpl_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2fluentwinui3styleimpl_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2fusionstyleimpl_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2imaginestyleimpl_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2impl_*.json
%{_qt6_metatypesdir}/qt6quickcontrols2materialstyleimpl_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickcontrols2universalstyleimpl_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2basicstyleimpl.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2fluentwinui3styleimpl.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2fusionstyleimpl.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2imaginestyleimpl.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2impl.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2materialstyleimpl.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2universalstyleimpl.pri
%{_qt6_pkgconfigdir}/Qt6QuickControls2BasicStyleImpl.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2FluentWinUI3StyleImpl.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2FusionStyleImpl.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2ImagineStyleImpl.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2Impl.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2MaterialStyleImpl.pc
%{_qt6_pkgconfigdir}/Qt6QuickControls2UniversalStyleImpl.pc
%exclude %{_qt6_includedir}/QtQuickControls2BasicStyleImpl/%{real_version}
%exclude %{_qt6_includedir}/QtQuickControls2FluentWinUI3StyleImpl/%{real_version}
%exclude %{_qt6_includedir}/QtQuickControls2FusionStyleImpl/%{real_version}
%exclude %{_qt6_includedir}/QtQuickControls2Impl/%{real_version}
%exclude %{_qt6_includedir}/QtQuickControls2MaterialStyleImpl/%{real_version}
%exclude %{_qt6_includedir}/QtQuickControls2UniversalStyleImpl/%{real_version}

%files -n qt6-quickcontrols2impl-private-devel
%{_qt6_cmakedir}/Qt6QuickControls2BasicStyleImplPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2FluentWinUI3StyleImplPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2FusionStyleImplPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2ImagineStyleImplPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2ImplPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2MaterialStyleImplPrivate/
%{_qt6_cmakedir}/Qt6QuickControls2UniversalStyleImplPrivate/
%{_qt6_includedir}/QtQuickControls2BasicStyleImpl/%{real_version}/
%{_qt6_includedir}/QtQuickControls2FluentWinUI3StyleImpl/%{real_version}/
%{_qt6_includedir}/QtQuickControls2FusionStyleImpl/%{real_version}/
%{_qt6_includedir}/QtQuickControls2Impl/%{real_version}/
%{_qt6_includedir}/QtQuickControls2MaterialStyleImpl/%{real_version}/
%{_qt6_includedir}/QtQuickControls2UniversalStyleImpl/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2basicstyleimpl_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2fluentwinui3styleimpl_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2fusionstyleimpl_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2imaginestyleimpl_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2impl_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2materialstyleimpl_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2universalstyleimpl_private.pri

%files -n libQt6QuickDialogs2-6
%{_qt6_libdir}/libQt6QuickDialogs2.so.*

%files -n qt6-quickdialogs2-devel
%{_qt6_cmakedir}/Qt6QuickDialogs2/
%{_qt6_descriptionsdir}/QuickDialogs2.json
%{_qt6_includedir}/QtQuickDialogs2/
%{_qt6_libdir}/libQt6QuickDialogs2.prl
%{_qt6_libdir}/libQt6QuickDialogs2.so
%{_qt6_metatypesdir}/qt6quickdialogs2_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2.pri
%{_qt6_pkgconfigdir}/Qt6QuickDialogs2.pc
%exclude %{_qt6_includedir}/QtQuickDialogs2/%{real_version}

%files -n qt6-quickdialogs2-private-devel
%{_qt6_cmakedir}/Qt6QuickDialogs2Private/
%{_qt6_includedir}/QtQuickDialogs2/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2_private.pri

%files -n libQt6QuickDialogs2QuickImpl6
%{_qt6_libdir}/libQt6QuickDialogs2QuickImpl.so.*

%files -n qt6-quickdialogs2quickimpl-devel
%{_qt6_cmakedir}/Qt6QuickDialogs2QuickImpl/
%{_qt6_descriptionsdir}/QuickDialogs2QuickImpl.json
%{_qt6_includedir}/QtQuickDialogs2QuickImpl/
%{_qt6_libdir}/libQt6QuickDialogs2QuickImpl.prl
%{_qt6_libdir}/libQt6QuickDialogs2QuickImpl.so
%{_qt6_metatypesdir}/qt6quickdialogs2quickimpl_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2quickimpl.pri
%{_qt6_pkgconfigdir}/Qt6QuickDialogs2QuickImpl.pc
%exclude %{_qt6_includedir}/QtQuickDialogs2QuickImpl/%{real_version}

%files -n qt6-quickdialogs2quickimpl-private-devel
%{_qt6_cmakedir}/Qt6QuickDialogs2QuickImplPrivate/
%{_qt6_includedir}/QtQuickDialogs2QuickImpl/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2quickimpl_private.pri

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
%{_qt6_pkgconfigdir}/Qt6QuickTest.pc
%exclude %{_qt6_includedir}/QtQuickTest/%{real_version}

%files -n qt6-quicktest-private-devel
%{_qt6_cmakedir}/Qt6QuickTestPrivate/
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
%{_qt6_metatypesdir}/qt6quickwidgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickwidgets.pri
%{_qt6_pkgconfigdir}/Qt6QuickWidgets.pc
%exclude %{_qt6_includedir}/QtQuickWidgets/%{real_version}

%files -n qt6-quickwidgets-private-devel
%{_qt6_cmakedir}/Qt6QuickWidgetsPrivate/
%{_qt6_includedir}/QtQuickWidgets/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_quickwidgets_private.pri

### Private only libraries ###

%files -n libQt6LabsPlatform6
%{_qt6_libdir}/libQt6LabsPlatform.so.*

%files -n qt6-labsplatform-private-devel
%{_qt6_cmakedir}/Qt6LabsPlatform/
%{_qt6_cmakedir}/Qt6LabsPlatformPrivate/
%{_qt6_descriptionsdir}/LabsPlatform.json
%{_qt6_includedir}/QtLabsPlatform/
%{_qt6_libdir}/libQt6LabsPlatform.prl
%{_qt6_libdir}/libQt6LabsPlatform.so
%{_qt6_metatypesdir}/qt6labsplatform_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsplatform.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labsplatform_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsPlatform.pc

%files -n libQt6LabsAnimation6
%{_qt6_libdir}/libQt6LabsAnimation.so.*

%files -n qt6-labsanimation-private-devel
%{_qt6_cmakedir}/Qt6LabsAnimation/
%{_qt6_cmakedir}/Qt6LabsAnimationPrivate/
%{_qt6_descriptionsdir}/LabsAnimation.json
%{_qt6_includedir}/QtLabsAnimation/
%{_qt6_libdir}/libQt6LabsAnimation.prl
%{_qt6_libdir}/libQt6LabsAnimation.so
%{_qt6_metatypesdir}/qt6labsanimation_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsanimation.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labsanimation_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsAnimation.pc

%files -n libQt6LabsFolderListModel6
%{_qt6_libdir}/libQt6LabsFolderListModel.so.*

%files -n qt6-labsfolderlistmodel-private-devel
%{_qt6_cmakedir}/Qt6LabsFolderListModel/
%{_qt6_cmakedir}/Qt6LabsFolderListModelPrivate/
%{_qt6_descriptionsdir}/LabsFolderListModel.json
%{_qt6_includedir}/QtLabsFolderListModel/
%{_qt6_libdir}/libQt6LabsFolderListModel.prl
%{_qt6_libdir}/libQt6LabsFolderListModel.so
%{_qt6_metatypesdir}/qt6labsfolderlistmodel_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsfolderlistmodel.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labsfolderlistmodel_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsFolderListModel.pc

%files -n libQt6LabsQmlModels6
%{_qt6_libdir}/libQt6LabsQmlModels.so.*

%files -n qt6-labsqmlmodels-private-devel
%{_qt6_cmakedir}/Qt6LabsQmlModels/
%{_qt6_cmakedir}/Qt6LabsQmlModelsPrivate/
%{_qt6_descriptionsdir}/LabsQmlModels.json
%{_qt6_includedir}/QtLabsQmlModels/
%{_qt6_libdir}/libQt6LabsQmlModels.prl
%{_qt6_libdir}/libQt6LabsQmlModels.so
%{_qt6_metatypesdir}/qt6labsqmlmodels_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsqmlmodels.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labsqmlmodels_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsQmlModels.pc

%files -n libQt6LabsSettings6
%{_qt6_libdir}/libQt6LabsSettings.so.*

%files -n qt6-labssettings-private-devel
%{_qt6_cmakedir}/Qt6LabsSettings/
%{_qt6_cmakedir}/Qt6LabsSettingsPrivate/
%{_qt6_descriptionsdir}/LabsSettings.json
%{_qt6_includedir}/QtLabsSettings/
%{_qt6_libdir}/libQt6LabsSettings.prl
%{_qt6_libdir}/libQt6LabsSettings.so
%{_qt6_metatypesdir}/qt6labssettings_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labssettings.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labssettings_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsSettings.pc

%files -n libQt6LabsSharedImage6
%{_qt6_libdir}/libQt6LabsSharedImage.so.*

%files -n qt6-labssharedimage-private-devel
%{_qt6_cmakedir}/Qt6LabsSharedImage/
%{_qt6_cmakedir}/Qt6LabsSharedImagePrivate/
%{_qt6_descriptionsdir}/LabsSharedImage.json
%{_qt6_includedir}/QtLabsSharedImage/
%{_qt6_libdir}/libQt6LabsSharedImage.prl
%{_qt6_libdir}/libQt6LabsSharedImage.so
%{_qt6_metatypesdir}/qt6labssharedimage_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labssharedimage.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labssharedimage_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsSharedImage.pc

%files -n libQt6LabsWavefrontMesh6
%{_qt6_libdir}/libQt6LabsWavefrontMesh.so.*

%files -n qt6-labswavefrontmesh-private-devel
%{_qt6_cmakedir}/Qt6LabsWavefrontMesh/
%{_qt6_cmakedir}/Qt6LabsWavefrontMeshPrivate/
%{_qt6_descriptionsdir}/LabsWavefrontMesh.json
%{_qt6_includedir}/QtLabsWavefrontMesh/
%{_qt6_libdir}/libQt6LabsWavefrontMesh.prl
%{_qt6_libdir}/libQt6LabsWavefrontMesh.so
%{_qt6_metatypesdir}/qt6labswavefrontmesh_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labswavefrontmesh.pri
%{_qt6_mkspecsdir}/modules/qt_lib_labswavefrontmesh_private.pri
%{_qt6_pkgconfigdir}/Qt6LabsWavefrontMesh.pc

%files -n libQt6QmlLocalStorage6
%{_qt6_libdir}/libQt6QmlLocalStorage.so.*

%files -n qt6-qmllocalstorage-private-devel
%{_qt6_cmakedir}/Qt6QmlLocalStorage/
%{_qt6_cmakedir}/Qt6QmlLocalStoragePrivate/
%{_qt6_descriptionsdir}/QmlLocalStorage.json
%{_qt6_includedir}/QtQmlLocalStorage/
%{_qt6_libdir}/libQt6QmlLocalStorage.prl
%{_qt6_libdir}/libQt6QmlLocalStorage.so
%{_qt6_metatypesdir}/qt6qmllocalstorage_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmllocalstorage.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmllocalstorage_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlLocalStorage.pc

%files -n libQt6QmlMeta6
%{_qt6_libdir}/libQt6QmlMeta.so.*

%files -n qt6-qmlmeta-private-devel
%{_qt6_cmakedir}/Qt6QmlMeta/
%{_qt6_cmakedir}/Qt6QmlMetaPrivate/
%{_qt6_descriptionsdir}/QmlMeta.json
%{_qt6_includedir}/QtQmlMeta
%{_qt6_libdir}/libQt6QmlMeta.prl
%{_qt6_libdir}/libQt6QmlMeta.so
%{_qt6_metatypesdir}/qt6qmlmeta_relwithdebinfo_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlmeta.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlmeta_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlMeta.pc

%files -n libQt6QmlModels6
%{_qt6_libdir}/libQt6QmlModels.so.*

%files -n qt6-qmlmodels-private-devel
%{_qt6_cmakedir}/Qt6QmlModels/
%{_qt6_cmakedir}/Qt6QmlModelsPrivate/
%{_qt6_descriptionsdir}/QmlModels.json
%{_qt6_includedir}/QtQmlModels/
%{_qt6_libdir}/libQt6QmlModels.prl
%{_qt6_libdir}/libQt6QmlModels.so
%{_qt6_metatypesdir}/qt6qmlmodels_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlmodels.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlmodels_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlModels.pc

%files -n libQt6QmlNetwork6
%{_qt6_libdir}/libQt6QmlNetwork.so.*

%files -n qt6-qmlnetwork-private-devel
%{_qt6_cmakedir}/Qt6QmlNetwork/
%{_qt6_cmakedir}/Qt6QmlNetworkPrivate/
%{_qt6_descriptionsdir}/QmlNetwork.json
%{_qt6_includedir}/QtQmlNetwork/
%{_qt6_libdir}/libQt6QmlNetwork.prl
%{_qt6_libdir}/libQt6QmlNetwork.so
%{_qt6_metatypesdir}/qt6qmlnetwork_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlnetwork.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlnetwork_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlNetwork.pc

%files -n libQt6QmlCore6
%{_qt6_libdir}/libQt6QmlCore.so.*

%files -n qt6-qmlcore-private-devel
%{_qt6_cmakedir}/Qt6QmlCore/
%{_qt6_cmakedir}/Qt6QmlCorePrivate/
%{_qt6_descriptionsdir}/QmlCore.json
%{_qt6_includedir}/QtQmlCore/
%{_qt6_libdir}/libQt6QmlCore.prl
%{_qt6_libdir}/libQt6QmlCore.so
%{_qt6_metatypesdir}/qt6qmlcore_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcore.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcore_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlCore.pc

%files -n libQt6QmlWorkerScript6
%{_qt6_libdir}/libQt6QmlWorkerScript.so.*

%files -n qt6-qmlworkerscript-private-devel
%{_qt6_cmakedir}/Qt6QmlWorkerScript/
%{_qt6_cmakedir}/Qt6QmlWorkerScriptPrivate/
%{_qt6_descriptionsdir}/QmlWorkerScript.json
%{_qt6_includedir}/QtQmlWorkerScript/
%{_qt6_libdir}/libQt6QmlWorkerScript.prl
%{_qt6_libdir}/libQt6QmlWorkerScript.so
%{_qt6_metatypesdir}/qt6qmlworkerscript_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlworkerscript.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlworkerscript_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlWorkerScript.pc

%files -n libQt6QmlXmlListModel6
%{_qt6_libdir}/libQt6QmlXmlListModel.so.*

%files -n qt6-qmlxmllistmodel-private-devel
%{_qt6_cmakedir}/Qt6QmlXmlListModel/
%{_qt6_cmakedir}/Qt6QmlXmlListModelPrivate/
%{_qt6_descriptionsdir}/QmlXmlListModel.json
%{_qt6_includedir}/QtQmlXmlListModel/
%{_qt6_libdir}/libQt6QmlXmlListModel.prl
%{_qt6_libdir}/libQt6QmlXmlListModel.so
%{_qt6_metatypesdir}/qt6qmlxmllistmodel_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlxmllistmodel.pri
%{_qt6_mkspecsdir}/modules/qt_lib_qmlxmllistmodel_private.pri
%{_qt6_pkgconfigdir}/Qt6QmlXmlListModel.pc

%files -n libQt6QuickDialogs2Utils6
%{_qt6_libdir}/libQt6QuickDialogs2Utils.so.*

%files -n qt6-quickdialogs2utils-private-devel
%{_qt6_cmakedir}/Qt6QuickDialogs2Utils/
%{_qt6_cmakedir}/Qt6QuickDialogs2UtilsPrivate/
%{_qt6_descriptionsdir}/QuickDialogs2Utils.json
%{_qt6_includedir}/QtQuickDialogs2Utils/
%{_qt6_libdir}/libQt6QuickDialogs2Utils.prl
%{_qt6_libdir}/libQt6QuickDialogs2Utils.so
%{_qt6_metatypesdir}/qt6quickdialogs2utils_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2utils.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2utils_private.pri
%{_qt6_pkgconfigdir}/Qt6QuickDialogs2Utils.pc

%files -n libQt6QuickEffects6
%{_qt6_libdir}/libQt6QuickEffects.so.*

%files -n qt6-quickeffects-private-devel
%{_qt6_cmakedir}/Qt6QuickEffects/
%{_qt6_cmakedir}/Qt6QuickEffectsPrivate/
%{_qt6_descriptionsdir}/QuickEffects.json
%{_qt6_includedir}/QtQuickEffects/
%{_qt6_libdir}/libQt6QuickEffects.prl
%{_qt6_libdir}/libQt6QuickEffects.so
%{_qt6_metatypesdir}/qt6quickeffects_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickeffects.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickeffects_private.pri
%{_qt6_pkgconfigdir}/Qt6QuickEffects.pc

%files -n libQt6QuickLayouts6
%{_qt6_libdir}/libQt6QuickLayouts.so.*

%files -n qt6-quicklayouts-private-devel
%{_qt6_cmakedir}/Qt6QuickLayouts/
%{_qt6_cmakedir}/Qt6QuickLayoutsPrivate/
%{_qt6_descriptionsdir}/QuickLayouts.json
%{_qt6_includedir}/QtQuickLayouts/
%{_qt6_libdir}/libQt6QuickLayouts.prl
%{_qt6_libdir}/libQt6QuickLayouts.so
%{_qt6_metatypesdir}/qt6quicklayouts_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicklayouts.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quicklayouts_private.pri
%{_qt6_pkgconfigdir}/Qt6QuickLayouts.pc

%files -n libQt6QuickParticles6
%{_qt6_libdir}/libQt6QuickParticles.so.*

%files -n qt6-quickparticles-private-devel
%{_qt6_cmakedir}/Qt6QuickParticlesPrivate/
%{_qt6_descriptionsdir}/QuickParticlesPrivate.json
%{_qt6_includedir}/QtQuickParticles/
%{_qt6_libdir}/libQt6QuickParticles.prl
%{_qt6_libdir}/libQt6QuickParticles.so
%{_qt6_metatypesdir}/qt6quickparticlesprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickparticles_private.pri

%files -n libQt6QuickShapes6
%{_qt6_libdir}/libQt6QuickShapes.so.*

%files -n qt6-quickshapes-private-devel
%{_qt6_cmakedir}/Qt6QuickShapesPrivate/
%{_qt6_descriptionsdir}/QuickShapesPrivate.json
%{_qt6_includedir}/QtQuickShapes/
%{_qt6_libdir}/libQt6QuickShapes.prl
%{_qt6_libdir}/libQt6QuickShapes.so
%{_qt6_metatypesdir}/qt6quickshapesprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickshapes_private.pri

%files -n libQt6QuickTemplates2-6
%{_qt6_libdir}/libQt6QuickTemplates2.so.*

%files -n qt6-quicktemplates2-private-devel
%{_qt6_cmakedir}/Qt6QuickTemplates2/
%{_qt6_cmakedir}/Qt6QuickTemplates2Private/
%{_qt6_descriptionsdir}/QuickTemplates2.json
%{_qt6_includedir}/QtQuickTemplates2/
%{_qt6_libdir}/libQt6QuickTemplates2.prl
%{_qt6_libdir}/libQt6QuickTemplates2.so
%{_qt6_metatypesdir}/qt6quicktemplates2_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicktemplates2.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quicktemplates2_private.pri
%{_qt6_pkgconfigdir}/Qt6QuickTemplates2.pc

%files -n libQt6QuickVectorImage6
%{_qt6_libdir}/libQt6QuickVectorImage.so.*
%{_qt6_libdir}/libQt6QuickVectorImageGenerator.so.*

%files -n qt6-quickvectorimage-private-devel
%{_qt6_cmakedir}/Qt6QuickVectorImage/
%{_qt6_cmakedir}/Qt6QuickVectorImagePrivate/
%{_qt6_cmakedir}/Qt6QuickVectorImageGeneratorPrivate/
%{_qt6_descriptionsdir}/QuickVectorImage.json
%{_qt6_descriptionsdir}/QuickVectorImageGeneratorPrivate.json
%{_qt6_includedir}/QtQuickVectorImage/
%{_qt6_includedir}/QtQuickVectorImageGenerator/
%{_qt6_libdir}/libQt6QuickVectorImage.prl
%{_qt6_libdir}/libQt6QuickVectorImage.so
%{_qt6_libdir}/libQt6QuickVectorImageGenerator.prl
%{_qt6_libdir}/libQt6QuickVectorImageGenerator.so
%{_qt6_metatypesdir}/qt6quickvectorimage_*_metatypes.json
%{_qt6_metatypesdir}/qt6quickvectorimagegeneratorprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickvectorimage.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickvectorimage_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_quickvectorimagegenerator_private.pri
%{_qt6_pkgconfigdir}/Qt6QuickVectorImage.pc

### Static libraries ###

%files -n qt6-packetprotocol-devel-static
%{_qt6_cmakedir}/Qt6PacketProtocolPrivate/
%{_qt6_descriptionsdir}/PacketProtocolPrivate.json
%{_qt6_includedir}/QtPacketProtocol/
%{_qt6_libdir}/libQt6PacketProtocol.a
%{_qt6_libdir}/libQt6PacketProtocol.prl
%{_qt6_metatypesdir}/qt6packetprotocolprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_packetprotocol_private.pri

%files -n qt6-qmldebug-devel-static
%{_qt6_cmakedir}/Qt6QmlDebugPrivate/
%{_qt6_descriptionsdir}/QmlDebugPrivate.json
%{_qt6_includedir}/QtQmlDebug/
%{_qt6_libdir}/libQt6QmlDebug.a
%{_qt6_libdir}/libQt6QmlDebug.prl
%{_qt6_metatypesdir}/qt6qmldebugprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmldebug_private.pri

%files -n qt6-qmldom-devel-static
%{_qt6_cmakedir}/Qt6QmlDomPrivate/
%{_qt6_descriptionsdir}/QmlDomPrivate.json
%{_qt6_includedir}/QtQmlDom/
%{_qt6_libdir}/libQt6QmlDom.a
%{_qt6_libdir}/libQt6QmlDom.prl
%{_qt6_metatypesdir}/qt6qmldomprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmldom_private.pri

%files -n qt6-qmlformat-devel-static
%{_qt6_cmakedir}/Qt6QmlFormatPrivate/
%{_qt6_descriptionsdir}/QmlFormatPrivate.json
%{_qt6_includedir}/QtQmlFormat/
%{_qt6_libdir}/libQt6QmlFormat.a
%{_qt6_libdir}/libQt6QmlFormat.prl
%{_qt6_metatypesdir}/qt6qmlformatprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlformat_private.pri

%files -n qt6-qmlls-devel-static
%{_qt6_cmakedir}/Qt6QmlLSPrivate/
%{_qt6_descriptionsdir}/QmlLSPrivate.json
%{_qt6_includedir}/QtQmlLS/
%{_qt6_libdir}/libQt6QmlLS.a
%{_qt6_libdir}/libQt6QmlLS.prl
%{_qt6_metatypesdir}/qt6qmllsprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlls_private.pri

%files -n qt6-qmltoolingsettings-devel-static
%{_qt6_cmakedir}/Qt6QmlToolingSettingsPrivate/
%{_qt6_descriptionsdir}/QmlToolingSettingsPrivate.json
%{_qt6_includedir}/QtQmlToolingSettings/
%{_qt6_libdir}/libQt6QmlToolingSettings.a
%{_qt6_libdir}/libQt6QmlToolingSettings.prl
%{_qt6_metatypesdir}/qt6qmltoolingsettingsprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmltoolingsettings_private.pri

%files -n qt6-qmltyperegistrar-devel-static
# Expected development files
%dir %{_qt6_archdatadir}/objects-*
%{_qt6_archdatadir}/objects-*/QmlTypeRegistrarPrivate_resources_1/
%{_qt6_cmakedir}/Qt6QmlTypeRegistrarPrivate/
%{_qt6_descriptionsdir}/QmlTypeRegistrarPrivate.json
%{_qt6_includedir}/QtQmlTypeRegistrar/
%{_qt6_libdir}/libQt6QmlTypeRegistrar.a
%{_qt6_libdir}/libQt6QmlTypeRegistrar.prl
%{_qt6_metatypesdir}/qt6qmltyperegistrarprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmltyperegistrar_private.pri

%files -n qt6-quickcontrolstestutils-devel-static
%{_qt6_cmakedir}/Qt6QuickControlsTestUtilsPrivate/
%{_qt6_descriptionsdir}/QuickControlsTestUtilsPrivate.json
%{_qt6_includedir}/QtQuickControlsTestUtils/
%{_qt6_libdir}/libQt6QuickControlsTestUtils.a
%{_qt6_libdir}/libQt6QuickControlsTestUtils.prl
%{_qt6_metatypesdir}/qt6quickcontrolstestutilsprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrolstestutilsprivate_private.pri

%files -n qt6-quicktestutils-devel-static
%{_qt6_cmakedir}/Qt6QuickTestUtilsPrivate/
%{_qt6_descriptionsdir}/QuickTestUtilsPrivate.json
%{_qt6_includedir}/QtQuickTestUtils/
%{_qt6_libdir}/libQt6QuickTestUtils.a
%{_qt6_libdir}/libQt6QuickTestUtils.prl
%{_qt6_metatypesdir}/qt6quicktestutilsprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicktestutilsprivate_private.pri

%else

%pre -n qt6-declarative-docs-qch -f qch.pre

%files -n qt6-declarative-docs-html
%dir %{_qt6_docdir}
%{_qt6_docdir}/*
%exclude %{_qt6_docdir}/*.qch

%files -n qt6-declarative-docs-qch
%dir %{_qt6_docdir}
%{_qt6_docdir}/*.qch

%endif

%changelog
