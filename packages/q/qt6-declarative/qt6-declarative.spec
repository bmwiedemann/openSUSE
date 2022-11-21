#
# spec file for package qt6-declarative
#
# Copyright (c) 2022 SUSE LLC
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


%define real_version 6.4.1
%define short_version 6.4
%define tar_name qtdeclarative-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-declarative%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 Declarative Libraries and tools
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-declarative-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-opengl-private-devel
BuildRequires:  qt6-test-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LanguageServerPrivate)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
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

# Note: The qt 'labs' libraries are not part of the meta packages
%package devel
Summary:        Qt 6 Declarative meta package
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlCore) = %{real_version}
Requires:       cmake(Qt6QmlLocalStorage) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
Requires:       cmake(Qt6QmlWorkerScript) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickControls2) = %{real_version}
Requires:       cmake(Qt6QuickControls2Impl) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2QuickImpl) = %{real_version}
Requires:       cmake(Qt6QuickDialogs2Utils) = %{real_version}
Requires:       cmake(Qt6QuickLayouts) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}
Requires:       cmake(Qt6QuickTest) = %{real_version}
Requires:       cmake(Qt6QuickWidgets) = %{real_version}
BuildArch:      noarch

%description devel
This meta-package requires all the qt6-declarative development packages.

%package private-devel
Summary:        Qt 6 Declarative unstable ABI meta package
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-qmlcore-private-devel = %{version}
Requires:       qt6-qmllocalstorage-private-devel = %{version}
Requires:       qt6-qmlmodels-private-devel = %{version}
Requires:       qt6-qmlworkerscript-private-devel = %{version}
Requires:       qt6-quick-private-devel = %{version}
Requires:       qt6-quickcontrols2-private-devel = %{version}
Requires:       qt6-quickcontrols2impl-private-devel = %{version}
Requires:       qt6-quickdialogs2-private-devel = %{version}
Requires:       qt6-quickdialogs2quickimpl-private-devel = %{version}
Requires:       qt6-quickdialogs2utils-private-devel = %{version}
Requires:       qt6-quicklayouts-private-devel = %{version}
Requires:       qt6-quickparticles-private-devel = %{version}
Requires:       qt6-quickshapes-private-devel = %{version}
Requires:       qt6-quicktemplates2-private-devel = %{version}
Requires:       qt6-quicktest-private-devel = %{version}
Requires:       qt6-quickwidgets-private-devel = %{version}
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
Requires:       qt6-declarative-imports

%description tools
Additional tools for inspecting, testing, viewing QML imports and files.

%package -n libQt6LabsAnimation6
Summary:        Qt 6 LabsAnimation library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6LabsAnimation6
The Qt 6 LabsAnimation library.

%package -n qt6-labsanimation-devel
Summary:        Qt 6 LabsAnimation library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6LabsAnimation6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quick-private-devel = %{version}

%description -n qt6-labsanimation-devel
Development files for the Qt 6 LabsAnimation library.

%package -n qt6-labsanimation-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsAnimation library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6LabsAnimation) = %{real_version}

%description -n qt6-labsanimation-private-devel
This package provides private headers of libQt6LabsAnimation that do not have any
ABI or API guarantees.

%package -n libQt6LabsFolderListModel6
Summary:        Qt 6 LabsFolderListModel library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6LabsFolderListModel6
The Qt 6 LabsFolderListModel library.

%package -n qt6-labsfolderlistmodel-devel
Summary:        Qt 6 LabsFolderListModel library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6LabsFolderListModel6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
%requires_eq    qt6-core-private-devel

%description -n qt6-labsfolderlistmodel-devel
Development files for the Qt 6 LabsFolderListModel library.

%package -n qt6-labsfolderlistmodel-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsFolderListModel library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6LabsFolderListModel) = %{real_version}

%description -n qt6-labsfolderlistmodel-private-devel
This package provides private headers of libQt6LabsFolderListModel that do not have any
ABI or API guarantees.

%package -n libQt6LabsQmlModels6
Summary:        Qt 6 LabsQmlModels library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6LabsQmlModels6
The Qt 6 LabsQmlModels library.

%package -n qt6-labsqmlmodels-devel
Summary:        Qt 6 LabsQmlModels library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6LabsQmlModels6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-qmlmodels-private-devel = %{version}

%description -n qt6-labsqmlmodels-devel
Development files for the Qt 6 LabsQmlModels library.

%package -n qt6-labsqmlmodels-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsQmlModels library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6LabsQmlModels) = %{real_version}

%description -n qt6-labsqmlmodels-private-devel
This package provides private headers of libQt6LabsQmlModels that do not have any
ABI or API guarantees.

%package -n libQt6LabsSettings6
Summary:        Qt 6 LabsSettings library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6LabsSettings6
The Qt 6 LabsSettings library.

%package -n qt6-labssettings-devel
Summary:        Qt 6 LabsSettings library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6LabsSettings6 = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Qml)

%description -n qt6-labssettings-devel
Development files for the Qt 6 LabsSettings library.

%package -n qt6-labssettings-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsSettings library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6LabsSettings) = %{real_version}

%description -n qt6-labssettings-private-devel
This package provides private headers of libQt6LabsSettings that do not have any
ABI or API guarantees.

%package -n libQt6LabsSharedImage6
Summary:        Qt 6 LabsSharedImage library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6LabsSharedImage6
The Qt 6 LabsSharedImage library.

%package -n qt6-labssharedimage-devel
Summary:        Qt 6 LabsSharedImage library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6LabsSharedImage6 = %{version}
Requires:       qt6-quick-private-devel = %{version}
%requires_eq    qt6-gui-private-devel

%description -n qt6-labssharedimage-devel
Development files for the Qt 6 LabsSharedImage library.

%package -n qt6-labssharedimage-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsSharedImage library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6LabsSharedImage) = %{real_version}

%description -n qt6-labssharedimage-private-devel
This package provides private headers of libQt6LabsSharedImage that do not have any
ABI or API guarantees.

%package -n libQt6LabsWavefrontMesh6
Summary:        Qt 6 LabsWavefrontMesh library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6LabsWavefrontMesh6
The Qt 6 LabsWavefrontMesh library.

%package -n qt6-labswavefrontmesh-devel
Summary:        Qt 6 LabsWavefrontMesh library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6LabsWavefrontMesh6 = %{version}
Requires:       qt6-quick-private-devel = %{version}
%requires_eq    qt6-gui-private-devel

%description -n qt6-labswavefrontmesh-devel
Development files for the Qt 6 LabsWavefrontMesh library.

%package -n qt6-labswavefrontmesh-private-devel
Summary:        Non-ABI stable API for the Qt 6 LabsWavefrontMesh library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6LabsWavefrontMesh) = %{real_version}

%description -n qt6-labswavefrontmesh-private-devel
This package provides private headers of libQt6LabsWavefrontMesh that do not have any
ABI or API guarantees.

%package -n libQt6Qml6
Summary:        Qt 6 Qml library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       (qml-autoreqprov if rpm-build)
Requires:       qt6-declarative-imports

%description -n libQt6Qml6
The Qt 6 Qml library.

%package -n qt6-qml-devel
Summary:        Qt 6 Qml library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6Qml6 = %{version}
# Executables are required
Requires:       qt6-declarative-tools
Requires:       cmake(Qt6Network)
# qmldevtools is gone in 6.3
Provides:       qt6-qmldevtools-devel-static = 6.3
Obsoletes:      qt6-qmldevtools-devel-static < 6.3

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

%package -n libQt6QmlCore6
Summary:        Qt 6 QmlCore library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-declarative-imports

%description -n libQt6QmlCore6
The Qt 6 QmlCore library.

%package -n qt6-qmlcore-devel
Summary:        Qt 6 QmlCore library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QmlCore6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}

%description -n qt6-qmlcore-devel
Development files for the Qt 6 QmlCore library.

%package -n qt6-qmlcore-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlCore library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QmlCore) = %{real_version}

%description -n qt6-qmlcore-private-devel
This package provides private headers of libQt6QmlCore that do not have any
ABI or API guarantees.

%package -n libQt6QmlLocalStorage6
Summary:        Qt 6 QmlLocalStorage library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QmlLocalStorage6
The Qt 6 QmlLocalStorage library.

%package -n qt6-qmllocalstorage-devel
Summary:        Qt 6 QmlLocalStorage library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QmlLocalStorage6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6Sql)
%requires_eq    qt6-core-private-devel

%description -n qt6-qmllocalstorage-devel
Development files for the Qt 6 QmlLocalStorage library.

%package -n qt6-qmllocalstorage-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlLocalStorage library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6QmlLocalStorage) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-qmllocalstorage-private-devel
This package provides private headers of libQt6QmlLocalStorage that do not have any
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
Requires:       cmake(Qt6Qml) = %{real_version}

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
Requires:       cmake(Qt6Qml) = %{real_version}

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

%package -n libQt6QmlXmlListModel6
Summary:        Qt 6 QmlXmlListModel library

%description -n libQt6QmlXmlListModel6
The Qt 6 QmlXmlListModel library.

%package -n qt6-qmlxmllistmodel-devel
Summary:        Qt 6 QmlXmlListModel library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QmlXmlListModel6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}

%description -n qt6-qmlxmllistmodel-devel
Development files for the Qt 6 QmlXmlListModel library.

%package -n qt6-qmlxmllistmodel-private-devel
Summary:        Non-ABI stable API for the Qt 6 QmlXmlListModel library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QmlXmlListModel) = %{real_version}
%requires_eq    qt6-core-private-devel

%description -n qt6-qmlxmllistmodel-private-devel
This package provides private headers of libQt6QmlXmlListModel that do not have
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
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6OpenGL)
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}

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

%package -n libQt6QuickControls2-6
Summary:        Qt 6 QuickControls2 library

%description -n libQt6QuickControls2-6
The Qt 6 QuickControls2 library.

%package -n qt6-quickcontrols2-devel
Summary:        Qt 6 QuickControls2 library - Development files
Requires:       libQt6QuickControls2-6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quicktemplates2-private-devel = %{version}
Requires:       cmake(Qt6Quick) = %{real_version}

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
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quicktemplates2-private-devel = %{version}
Requires:       cmake(Qt6Gui)

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
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quickcontrols2impl-devel = %{version}
Requires:       qt6-quickdialogs2quickimpl-private-devel = %{version}
Requires:       qt6-quickdialogs2utils-private-devel = %{version}
Requires:       cmake(Qt6Gui)

%description -n qt6-quickdialogs2-devel
Development files for the Qt 6 QuickDialogs2 library.

%package -n qt6-quickdialogs2-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickDialogs2 library
Requires:       cmake(Qt6QuickDialogs2) = %{real_version}
%requires_eq    qt6-qmlmodels-private-devel

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
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quickcontrols2impl-private-devel = %{version}
Requires:       qt6-quickdialogs2utils-private-devel = %{version}
Requires:       qt6-quicktemplates2-private-devel = %{version}
Requires:       cmake(Qt6Gui)

%description -n qt6-quickdialogs2quickimpl-devel
Development files for the Qt 6 QuickDialogs2Impl library.

%package -n qt6-quickdialogs2quickimpl-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickDialogs2Impl library
Requires:       cmake(Qt6QuickDialogs2QuickImpl) = %{real_version}

%description -n qt6-quickdialogs2quickimpl-private-devel
This package provides private headers of libQt6QuickDialogs2Impl that do not
have any ABI or API guarantees.

%package -n libQt6QuickDialogs2Utils6
Summary:        Qt 6 QuickDialogs2Utils library

%description -n libQt6QuickDialogs2Utils6
The Qt 6 QuickDialogs2Utils library.

%package -n qt6-quickdialogs2utils-devel
Summary:        Qt6 QuickDialogs2Utils library - Development files
Requires:       libQt6QuickDialogs2Utils6 = %{version}
%requires_eq    qt6-gui-private-devel

%description -n qt6-quickdialogs2utils-devel
Development files for the Qt 6 QuickDialogs2Utils library.

%package -n qt6-quickdialogs2utils-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickDialogs2Utils library
Requires:       cmake(Qt6QuickDialogs2Utils) = %{real_version}
%requires_eq    qt6-qmlmodels-private-devel

%description -n qt6-quickdialogs2utils-private-devel
This package provides private headers of libQt6QuickDialogs2Utils that do not have
any ABI or API guarantees.

%package -n libQt6QuickLayouts6
Summary:        Qt 6 QuickLayouts library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickLayouts6
The Qt 6 QuickLayouts library.

%package -n qt6-quicklayouts-devel
Summary:        Qt 6 QuickLayouts library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickLayouts6 = %{version}
Requires:       qt6-quick-private-devel = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
%requires_eq    qt6-gui-private-devel

%description -n qt6-quicklayouts-devel
Development files for the Qt 6 QuickLayouts library.

%package -n qt6-quicklayouts-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickLayouts library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       cmake(Qt6QuickLayouts) = %{real_version}

%description -n qt6-quicklayouts-private-devel
This package provides private headers of libQt6QuickLayouts that do not have
any ABI or API guarantees.

%package -n libQt6QuickTemplates2-6
Summary:        Qt 6 QuickTemplates2 library

%description -n libQt6QuickTemplates2-6
The Qt 6 QuickTemplates2 library.

%package -n qt6-quicktemplates2-devel
Summary:        Qt6 QuickTemplates2 library - Development files
Requires:       libQt6QuickTemplates2-6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6QmlModels) = %{real_version}

%description -n qt6-quicktemplates2-devel
Development files for the Qt 6 QuickTemplates2 library.

%package -n qt6-quicktemplates2-private-devel
Summary:        Non-ABI stable API for the Qt 6 QuickTemplates2 library
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}
%requires_eq    qt6-qmlmodels-private-devel

%description -n qt6-quicktemplates2-private-devel
This package provides private headers of libQt6QuickTemplates2 that do not have
any ABI or API guarantees.

%package -n libQt6QuickTest6
Summary:        Qt 6 QuickTest library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickTest6
The Qt 6 QuickTest library.

%package -n qt6-quicktest-devel
Summary:        Qt 6 QuickTest library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickTest6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quick-private-devel = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Test)

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
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Widgets)
%requires_eq    qt6-opengl-private-devel

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

### Private only libraries ###

%package -n libQt6QmlCompiler6
Summary:        Qt6 QmlCompiler library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QmlCompiler6
The Qt 6 QmlCompiler library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmlcompiler-private-devel
Summary:        Qt 6 QmlCompiler library - Development files
Requires:       qt6-qml-private-devel = %{version}
Requires:       libQt6QmlCompiler6 = %{version}
%requires_eq    qt6-core-private-devel
# The qmlcompiler library became a shared library (again) in 6.4.0
Provides:       qt6-qmlcompiler-devel-static = 6.4.0
Obsoletes:      qt6-qmlcompiler-devel-static < 6.4.0

%description -n qt6-qmlcompiler-private-devel
Development files for the Qt 6 QmlCompiler library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickParticles6
Summary:        Qt 6 QuickParticles library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickParticles6
The Qt 6 QuickParticles library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickparticles-private-devel
Summary:        Qt 6 QuickParticles library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickParticles6 = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       qt6-quick-private-devel = %{version}
%requires_eq    qt6-gui-private-devel
# Renamed in 6.2.0
Provides:       qt6-quickparticles-devel = 6.2.0
Obsoletes:      qt6-quickparticles-devel < 6.2.0

%description -n qt6-quickparticles-private-devel
Development files for the Qt 6 QuickParticles library.
This library does not have any ABI or API guarantees.

%package -n libQt6QuickShapes6
Summary:        Qt 6 QuickShapes library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

%description -n libQt6QuickShapes6
The Qt 6 QuickShapes library.
This library does not have any ABI or API guarantees.

%package -n qt6-quickshapes-private-devel
Summary:        Qt 6 QuickShapes library - Development files
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       libQt6QuickShapes6 = %{version}
Requires:       qt6-quick-private-devel = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
%requires_eq    qt6-gui-private-devel
# Renamed in 6.2.0
Provides:       qt6-quickshapes-devel = 6.2.0
Obsoletes:      qt6-quickshapes-devel < 6.2.0

%description -n qt6-quickshapes-private-devel
Development files for the Qt 6 QuickShapes library.
This library does not have any ABI or API guarantees.

### Static libraries ###
%package -n qt6-packetprotocol-devel-static
Summary:        Qt6 PacketProtocol static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
%requires_eq    qt6-core-private-devel
# Renamed in 6.2.0
Provides:       qt6-packetprotocol-private-devel = 6.2.0
Obsoletes:      qt6-packetprotocol-private-devel < 6.2.0

%description -n qt6-packetprotocol-devel-static
The Qt6 PacketProtocol static library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmldebug-devel-static
Summary:        Qt6 QmlDebug static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-packetprotocol-devel-static = %{version}
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6Network)
%requires_eq    qt6-core-private-devel
# Renamed in 6.2.0
Provides:       qt6-qmldebug-private-devel = 6.2.0
Obsoletes:      qt6-qmldebug-private-devel < 6.2.0

%description -n qt6-qmldebug-devel-static
The Qt6 QmlDebug static library.
This library does not have any ABI or API guarantees.

%package -n qt6-qmldom-devel-static
Summary:        Qt6 QmlDom static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-qml-private-devel = %{version}
Requires:       cmake(Qt6QmlCompilerPrivate) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-qmldom-private-devel = 6.2.0
Obsoletes:      qt6-qmldom-private-devel < 6.2.0

%description -n qt6-qmldom-devel-static
The Qt6 QmlDom static library.
The goal of the Dom library is to provide a nicer to use basis for the
Qml Code model, to be used by the various QML tools, the designer and
the new compiler.

%package -n qt6-quickcontrolstestutils-devel-static
Summary:        Qt6 QuickControlsTestUtils static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-quickdialogs2quickimpl-private-devel = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6QuickControls2) = %{real_version}
Requires:       cmake(Qt6QuickTemplates2) = %{real_version}
Requires:       cmake(Qt6QuickTestUtilsPrivate) = %{real_version}
Requires:       cmake(Qt6Test)

%description -n qt6-quickcontrolstestutils-devel-static
The Qt6 QuickControlsTestUtils static library.

%package -n qt6-quicktestutils-devel-static
Summary:        Qt6 QuickTestUtils static library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Requires:       qt6-quick-private-devel = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6QuickTest) = %{real_version}
Requires:       cmake(Qt6Test)

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

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin{Config,Targets}*.cmake

# There are no private headers
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_qmlintegration_private.pri

%post -n libQt6LabsAnimation6 -p /sbin/ldconfig
%post -n libQt6LabsFolderListModel6 -p /sbin/ldconfig
%post -n libQt6LabsQmlModels6 -p /sbin/ldconfig
%post -n libQt6LabsSettings6 -p /sbin/ldconfig
%post -n libQt6LabsSharedImage6 -p /sbin/ldconfig
%post -n libQt6LabsWavefrontMesh6 -p /sbin/ldconfig
%post -n libQt6Qml6 -p /sbin/ldconfig
%post -n libQt6QmlCompiler6 -p /sbin/ldconfig
%post -n libQt6QmlCore6 -p /sbin/ldconfig
%post -n libQt6QmlLocalStorage6 -p /sbin/ldconfig
%post -n libQt6QmlModels6 -p /sbin/ldconfig
%post -n libQt6QmlWorkerScript6 -p /sbin/ldconfig
%post -n libQt6QmlXmlListModel6 -p /sbin/ldconfig
%post -n libQt6Quick6 -p /sbin/ldconfig
%post -n libQt6QuickControls2-6 -p /sbin/ldconfig
%post -n libQt6QuickControls2Impl6 -p /sbin/ldconfig
%post -n libQt6QuickDialogs2-6 -p /sbin/ldconfig
%post -n libQt6QuickDialogs2QuickImpl6 -p /sbin/ldconfig
%post -n libQt6QuickDialogs2Utils6 -p /sbin/ldconfig
%post -n libQt6QuickLayouts6 -p /sbin/ldconfig
%post -n libQt6QuickParticles6 -p /sbin/ldconfig
%post -n libQt6QuickShapes6 -p /sbin/ldconfig
%post -n libQt6QuickTemplates2-6 -p /sbin/ldconfig
%post -n libQt6QuickTest6 -p /sbin/ldconfig
%post -n libQt6QuickWidgets6 -p /sbin/ldconfig
%postun -n libQt6LabsAnimation6 -p /sbin/ldconfig
%postun -n libQt6LabsFolderListModel6 -p /sbin/ldconfig
%postun -n libQt6LabsQmlModels6 -p /sbin/ldconfig
%postun -n libQt6LabsSettings6 -p /sbin/ldconfig
%postun -n libQt6LabsSharedImage6 -p /sbin/ldconfig
%postun -n libQt6LabsWavefrontMesh6 -p /sbin/ldconfig
%postun -n libQt6Qml6 -p /sbin/ldconfig
%postun -n libQt6QmlCompiler6 -p /sbin/ldconfig
%postun -n libQt6QmlCore6 -p /sbin/ldconfig
%postun -n libQt6QmlLocalStorage6 -p /sbin/ldconfig
%postun -n libQt6QmlModels6 -p /sbin/ldconfig
%postun -n libQt6QmlWorkerScript6 -p /sbin/ldconfig
%postun -n libQt6QmlXmlListModel6 -p /sbin/ldconfig
%postun -n libQt6Quick6 -p /sbin/ldconfig
%postun -n libQt6QuickControls2-6 -p /sbin/ldconfig
%postun -n libQt6QuickControls2Impl6 -p /sbin/ldconfig
%postun -n libQt6QuickDialogs2-6 -p /sbin/ldconfig
%postun -n libQt6QuickDialogs2QuickImpl6 -p /sbin/ldconfig
%postun -n libQt6QuickDialogs2Utils6 -p /sbin/ldconfig
%postun -n libQt6QuickLayouts6 -p /sbin/ldconfig
%postun -n libQt6QuickParticles6 -p /sbin/ldconfig
%postun -n libQt6QuickShapes6 -p /sbin/ldconfig
%postun -n libQt6QuickTemplates2-6 -p /sbin/ldconfig
%postun -n libQt6QuickTest6 -p /sbin/ldconfig
%postun -n libQt6QuickWidgets6 -p /sbin/ldconfig

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files examples
%{_qt6_examplesdir}/*

%files imports
%{_qt6_qmldir}/Qt/
%{_qt6_qmldir}/QtCore/
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
%{_qt6_libexecdir}/qmlcachegen
%{_qt6_libexecdir}/qmlimportscanner
%{_qt6_libexecdir}/qmltyperegistrar
%{_qt6_pluginsdir}/qmllint/
%{_qt6_pluginsdir}/qmltooling/

%files -n libQt6LabsAnimation6
%{_qt6_libdir}/libQt6LabsAnimation.so.*

%files -n qt6-labsanimation-devel
%{_qt6_cmakedir}/Qt6LabsAnimation/
%{_qt6_descriptionsdir}/LabsAnimation.json
%{_qt6_includedir}/QtLabsAnimation/
%{_qt6_libdir}/libQt6LabsAnimation.prl
%{_qt6_libdir}/libQt6LabsAnimation.so
%{_qt6_metatypesdir}/qt6labsanimation_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsanimation.pri
%{_qt6_pkgconfigdir}/Qt6LabsAnimation.pc
%exclude %{_qt6_includedir}/QtLabsAnimation/%{real_version}

%files -n qt6-labsanimation-private-devel
%{_qt6_includedir}/QtLabsAnimation/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_labsanimation_private.pri

%files -n libQt6LabsFolderListModel6
%{_qt6_libdir}/libQt6LabsFolderListModel.so.*

%files -n qt6-labsfolderlistmodel-devel
%{_qt6_cmakedir}/Qt6LabsFolderListModel/
%{_qt6_descriptionsdir}/LabsFolderListModel.json
%{_qt6_includedir}/QtLabsFolderListModel/
%{_qt6_libdir}/libQt6LabsFolderListModel.prl
%{_qt6_libdir}/libQt6LabsFolderListModel.so
%{_qt6_metatypesdir}/qt6labsfolderlistmodel_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsfolderlistmodel.pri
%{_qt6_pkgconfigdir}/Qt6LabsFolderListModel.pc
%exclude %{_qt6_includedir}/QtLabsFolderListModel/%{real_version}

%files -n qt6-labsfolderlistmodel-private-devel
%{_qt6_includedir}/QtLabsFolderListModel/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_labsfolderlistmodel_private.pri

%files -n libQt6LabsQmlModels6
%{_qt6_libdir}/libQt6LabsQmlModels.so.*

%files -n qt6-labsqmlmodels-devel
%{_qt6_cmakedir}/Qt6LabsQmlModels/
%{_qt6_descriptionsdir}/LabsQmlModels.json
%{_qt6_includedir}/QtLabsQmlModels/
%{_qt6_libdir}/libQt6LabsQmlModels.prl
%{_qt6_libdir}/libQt6LabsQmlModels.so
%{_qt6_metatypesdir}/qt6labsqmlmodels_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labsqmlmodels.pri
%{_qt6_pkgconfigdir}/Qt6LabsQmlModels.pc
%exclude %{_qt6_includedir}/QtLabsQmlModels/%{real_version}

%files -n qt6-labsqmlmodels-private-devel
%{_qt6_includedir}/QtLabsQmlModels/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_labsqmlmodels_private.pri

%files -n libQt6LabsSettings6
%{_qt6_libdir}/libQt6LabsSettings.so.*

%files -n qt6-labssettings-devel
%{_qt6_cmakedir}/Qt6LabsSettings/
%{_qt6_descriptionsdir}/LabsSettings.json
%{_qt6_includedir}/QtLabsSettings/
%{_qt6_libdir}/libQt6LabsSettings.prl
%{_qt6_libdir}/libQt6LabsSettings.so
%{_qt6_metatypesdir}/qt6labssettings_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labssettings.pri
%{_qt6_pkgconfigdir}/Qt6LabsSettings.pc
%exclude %{_qt6_includedir}/QtLabsSettings/%{real_version}

%files -n qt6-labssettings-private-devel
%{_qt6_includedir}/QtLabsSettings/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_labssettings_private.pri

%files -n libQt6LabsSharedImage6
%{_qt6_libdir}/libQt6LabsSharedImage.so.*

%files -n qt6-labssharedimage-devel
%{_qt6_cmakedir}/Qt6LabsSharedImage/
%{_qt6_descriptionsdir}/LabsSharedImage.json
%{_qt6_includedir}/QtLabsSharedImage/
%{_qt6_libdir}/libQt6LabsSharedImage.prl
%{_qt6_libdir}/libQt6LabsSharedImage.so
%{_qt6_metatypesdir}/qt6labssharedimage_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labssharedimage.pri
%{_qt6_pkgconfigdir}/Qt6LabsSharedImage.pc
%exclude %{_qt6_includedir}/QtLabsSharedImage/%{real_version}

%files -n qt6-labssharedimage-private-devel
%{_qt6_includedir}/QtLabsSharedImage/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_labssharedimage_private.pri

%files -n libQt6LabsWavefrontMesh6
%{_qt6_libdir}/libQt6LabsWavefrontMesh.so.*

%files -n qt6-labswavefrontmesh-devel
%{_qt6_cmakedir}/Qt6LabsWavefrontMesh/
%{_qt6_descriptionsdir}/LabsWavefrontMesh.json
%{_qt6_includedir}/QtLabsWavefrontMesh/
%{_qt6_libdir}/libQt6LabsWavefrontMesh.prl
%{_qt6_libdir}/libQt6LabsWavefrontMesh.so
%{_qt6_metatypesdir}/qt6labswavefrontmesh_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_labswavefrontmesh.pri
%{_qt6_pkgconfigdir}/Qt6LabsWavefrontMesh.pc
%exclude %{_qt6_includedir}/QtLabsWavefrontMesh/%{real_version}

%files -n qt6-labswavefrontmesh-private-devel
%{_qt6_includedir}/QtLabsWavefrontMesh/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_labswavefrontmesh_private.pri

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
%{_qt6_includedir}/QtQml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qml_private.pri

%files -n libQt6QmlCore6
%{_qt6_libdir}/libQt6QmlCore.so.*

%files -n qt6-qmlcore-devel
%{_qt6_cmakedir}/Qt6QmlCore/
%{_qt6_descriptionsdir}/QmlCore.json
%{_qt6_includedir}/QtQmlCore/
%{_qt6_libdir}/libQt6QmlCore.prl
%{_qt6_libdir}/libQt6QmlCore.so
%{_qt6_metatypesdir}/qt6qmlcore_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcore.pri
%{_qt6_pkgconfigdir}/Qt6QmlCore.pc
%exclude %{_qt6_includedir}/QtQmlCore/%{real_version}

%files -n qt6-qmlcore-private-devel
%{_qt6_includedir}/QtQmlCore/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcore_private.pri

%files -n libQt6QmlLocalStorage6
%{_qt6_libdir}/libQt6QmlLocalStorage.so.*

%files -n qt6-qmllocalstorage-devel
%{_qt6_cmakedir}/Qt6QmlLocalStorage/
%{_qt6_descriptionsdir}/QmlLocalStorage.json
%{_qt6_includedir}/QtQmlLocalStorage/
%{_qt6_libdir}/libQt6QmlLocalStorage.prl
%{_qt6_libdir}/libQt6QmlLocalStorage.so
%{_qt6_metatypesdir}/qt6qmllocalstorage_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmllocalstorage.pri
%{_qt6_pkgconfigdir}/Qt6QmlLocalStorage.pc
%exclude %{_qt6_includedir}/QtQmlLocalStorage/%{real_version}

%files -n qt6-qmllocalstorage-private-devel
%{_qt6_includedir}/QtQmlLocalStorage/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmllocalstorage_private.pri

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
%{_qt6_pkgconfigdir}/Qt6QmlModels.pc
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
%{_qt6_pkgconfigdir}/Qt6QmlWorkerScript.pc
%exclude %{_qt6_includedir}/QtQmlWorkerScript/%{real_version}

%files -n qt6-qmlworkerscript-private-devel
%{_qt6_includedir}/QtQmlWorkerScript/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlworkerscript_private.pri

%files -n libQt6QmlXmlListModel6
%{_qt6_libdir}/libQt6QmlXmlListModel.so.*

%files -n qt6-qmlxmllistmodel-devel
%{_qt6_cmakedir}/Qt6QmlXmlListModel/
%{_qt6_descriptionsdir}/QmlXmlListModel.json
%{_qt6_includedir}/QtQmlXmlListModel/
%{_qt6_libdir}/libQt6QmlXmlListModel.prl
%{_qt6_libdir}/libQt6QmlXmlListModel.so
%{_qt6_metatypesdir}/qt6qmlxmllistmodel_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlxmllistmodel.pri
%{_qt6_pkgconfigdir}/Qt6QmlXmlListModel.pc
%exclude %{_qt6_includedir}/QtQmlXmlListModel/%{real_version}

%files -n qt6-qmlxmllistmodel-private-devel
%{_qt6_includedir}/QtQmlXmlListModel/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_qmlxmllistmodel_private.pri

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
%{_qt6_pkgconfigdir}/Qt6Quick.pc
%exclude %{_qt6_includedir}/QtQuick/%{real_version}

%files -n qt6-quick-private-devel
%{_qt6_includedir}/QtQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quick_private.pri

%files -n libQt6QuickControls2-6
%{_qt6_libdir}/libQt6QuickControls2.so.*

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
%{_qt6_includedir}/QtQuickControls2/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2_private.pri

%files -n libQt6QuickControls2Impl6
%{_qt6_libdir}/libQt6QuickControls2Impl.so.*

%files -n qt6-quickcontrols2impl-devel
%{_qt6_cmakedir}/Qt6QuickControls2Impl/
%{_qt6_descriptionsdir}/QuickControls2Impl.json
%{_qt6_includedir}/QtQuickControls2Impl/
%{_qt6_libdir}/libQt6QuickControls2Impl.prl
%{_qt6_libdir}/libQt6QuickControls2Impl.so
%{_qt6_metatypesdir}/qt6quickcontrols2impl_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2impl.pri
%{_qt6_pkgconfigdir}/Qt6QuickControls2Impl.pc
%exclude %{_qt6_includedir}/QtQuickControls2Impl/%{real_version}

%files -n qt6-quickcontrols2impl-private-devel
%{_qt6_includedir}/QtQuickControls2Impl/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickcontrols2impl_private.pri

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
%{_qt6_includedir}/QtQuickDialogs2QuickImpl/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2quickimpl_private.pri

%files -n libQt6QuickDialogs2Utils6
%{_qt6_libdir}/libQt6QuickDialogs2Utils.so.*

%files -n qt6-quickdialogs2utils-devel
%{_qt6_cmakedir}/Qt6QuickDialogs2Utils/
%{_qt6_descriptionsdir}/QuickDialogs2Utils.json
%{_qt6_includedir}/QtQuickDialogs2Utils/
%{_qt6_libdir}/libQt6QuickDialogs2Utils.prl
%{_qt6_libdir}/libQt6QuickDialogs2Utils.so
%{_qt6_metatypesdir}/qt6quickdialogs2utils_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2utils.pri
%{_qt6_pkgconfigdir}/Qt6QuickDialogs2Utils.pc
%exclude %{_qt6_includedir}/QtQuickDialogs2Utils/%{real_version}

%files -n qt6-quickdialogs2utils-private-devel
%{_qt6_includedir}/QtQuickDialogs2Utils/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quickdialogs2utils_private.pri

%files -n libQt6QuickLayouts6
%{_qt6_libdir}/libQt6QuickLayouts.so.*

%files -n qt6-quicklayouts-devel
%{_qt6_cmakedir}/Qt6QuickLayouts/
%{_qt6_descriptionsdir}/QuickLayouts.json
%{_qt6_includedir}/QtQuickLayouts/
%{_qt6_libdir}/libQt6QuickLayouts.prl
%{_qt6_libdir}/libQt6QuickLayouts.so
%{_qt6_metatypesdir}/qt6quicklayouts_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicklayouts.pri
%{_qt6_pkgconfigdir}/Qt6QuickLayouts.pc
%exclude %{_qt6_includedir}/QtQuickLayouts/%{real_version}

%files -n qt6-quicklayouts-private-devel
%{_qt6_includedir}/QtQuickLayouts/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quicklayouts_private.pri

%files -n libQt6QuickTemplates2-6
%{_qt6_libdir}/libQt6QuickTemplates2.so.*

%files -n qt6-quicktemplates2-devel
%{_qt6_cmakedir}/Qt6QuickTemplates2/
%{_qt6_descriptionsdir}/QuickTemplates2.json
%{_qt6_includedir}/QtQuickTemplates2/
%{_qt6_libdir}/libQt6QuickTemplates2.prl
%{_qt6_libdir}/libQt6QuickTemplates2.so
%{_qt6_metatypesdir}/qt6quicktemplates2_*.json
%{_qt6_mkspecsdir}/modules/qt_lib_quicktemplates2.pri
%{_qt6_pkgconfigdir}/Qt6QuickTemplates2.pc
%exclude %{_qt6_includedir}/QtQuickTemplates2/%{real_version}

%files -n qt6-quicktemplates2-private-devel
%{_qt6_includedir}/QtQuickTemplates2/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_quicktemplates2_private.pri

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
%{_qt6_includedir}/QtQuickWidgets/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_quickwidgets_private.pri

### Private only libraries ###

%files -n libQt6QmlCompiler6
%{_qt6_libdir}/libQt6QmlCompiler.so.*

%files -n qt6-qmlcompiler-private-devel
%{_qt6_cmakedir}/Qt6QmlCompilerPrivate/
%{_qt6_descriptionsdir}/QmlCompilerPrivate.json
%{_qt6_includedir}/QtQmlCompiler/
%{_qt6_libdir}/libQt6QmlCompiler.prl
%{_qt6_libdir}/libQt6QmlCompiler.so
%{_qt6_metatypesdir}/qt6qmlcompilerprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_qmlcompiler_private.pri

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
