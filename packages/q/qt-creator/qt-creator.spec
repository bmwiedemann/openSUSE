#
# spec file for package qt-creator
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


%define real_version 9.0.1
%define short_version 9.0
%define tar_name qt-creator-opensource-src
%define tar_suffix %{nil}
#
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define pkgname_prefix qt
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt6"
  %define qt6 1
  %define pkgname_prefix qt6
  %define qt_min_version 6.2
  %define qtc_docdir %{_qt6_docdir}
%endif
#
%global libexecdirname libexec
%if "%{_libexecdir}" == "%{_prefix}/lib"
%global libexecdirname lib
%endif

# Private QML imports
%global __requires_exclude qmlimport\\((CameraGeometry|GridGeometry|HelperWidgets|LightUtils|LineGeometry|MouseArea3D|QtQuickDesignerColorPalette|QtQuickDesignerTheme|SelectionBoxGeometry|StudioControls|StudioTheme).*

# Has mocks for quite a few components, which are only pulled in when actually used
%global __requires_exclude_from %{_datadir}/qtcreator/qml/qmlpuppet/

Name:           %{pkgname_prefix}-creator
Version:        9.0.1
Release:        0
Summary:        Integrated Development Environment targeting Qt apps
# src/plugins/cmakeprojectmanager/configmodelitemdelegate.* -> LGPL-2.1-only OR LGPL-3.0-only
# src/shared/qbs is not built
# src/plugins/imageviewer/imageview.cpp, src/plugins/vcsbase/wizard/vcsconfigurationpage.cpp -> BSD-3-Clause
# src/plugins/emacskeys/* -> GPL-3.0-only
# many files are dual licensed 'LGPL-3.0-only or (GPL-2.0-or-later OR GPL-3.0-or-later + KDE Free Qt Foundation option)', we'll use LGPL-3.0-only for these files
License:        GPL-3.0-with-Qt-Company-Qt-exception-1.1 AND (LGPL-2.1-only OR LGPL-3.0-only) AND GPL-3.0-only AND LGPL-3.0-only AND BSD-3-Clause
URL:            https://www.qt.io/product/development-tools
Source:         https://download.qt.io/official_releases/qtcreator/%{short_version}/%{real_version}%{tar_suffix}/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source1:        qt-creator-rpmlintrc
# Patches 0-10 are upstream changes
# Patches 11-20 are openSUSE changes
Patch11:        fix-application-output.patch
Patch12:        0001-Disable-some-plugins.patch
##
BuildRequires:  cmake
# clang-devel in Leap 15.3 points to clang7...
%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150300
BuildRequires:  clang11-devel
BuildRequires:  llvm11-devel
%else
BuildRequires:  clang-devel >= 10.0
BuildRequires:  llvm-devel
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.5
BuildRequires:  cmake(yaml-cpp)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libzstd)
%if 0%{?qt6}
BuildRequires:  qt6-core-private-devel >= %{qt_min_version}
BuildRequires:  qt6-gui-private-devel >= %{qt_min_version}
BuildRequires:  qt6-qml-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick3d-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick3dassetimport-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick3dassetutils-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick3dparticles-private-devel >= %{qt_min_version}
BuildRequires:  qt6-tools-qdoc >= %{qt_min_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt_min_version}
BuildRequires:  cmake(Qt6DesignerComponentsPrivate) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Help) >= %{qt_min_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Network) >= %{qt_min_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Quick3D) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Quick3DAssetImport) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Quick3DAssetUtils) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Quick3DParticles) >= %{qt_min_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6SerialPort) >= %{qt_min_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt_min_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Tools) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt_min_version}
# Explicitly require qt6-sql-sqlite (needed by help system).
Requires:       qt6-sql-sqlite
Recommends:     qt6-base-devel
Recommends:     qt6-base-docs-qch
Recommends:     qt6-declarative-devel
Recommends:     qt6-declarative-docs-qch
Recommends:     qt6-translations
Provides:       libqt5-creator = %{version}
Provides:       qt5-creator = %{version}
Obsoletes:      libqt5-creator < %{version}
Obsoletes:      qt5-creator < %{version}
%endif
Requires:       hicolor-icon-theme

%description
Qt Creator is an integrated development environment (IDE) designed to
facilitate development with the Qt application framework.

%package plugin-devel
Summary:        Qt Creator Plugin Development Files
Group:          Development/Tools/IDE
Requires:       %{pkgname_prefix}-creator = %{version}
%if 0%{?qt6}
Requires:       qt6-base-devel >= %{qt_min_version}
Provides:      libqt5-creator-plugin-devel = %{version}
Provides:      qt5-creator-plugin-devel = %{version}
Obsoletes:     libqt5-creator-plugin-devel < %{version}
Obsoletes:     qt5-creator-plugin-devel < %{version}
%endif

%description plugin-devel
This package contains all files from the Qt Creator source directory
(aka QTC_SOURCE) necessary to compile plugins.

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# Don't build qbs, we already have a package
rm -r src/shared/qbs

%build
%define _lto_cflags %{nil}

# - qtc wants relative paths for CMAKE_INSTALL_LIB{,EXEC}DIR
# - https://bugreports.qt.io/browse/QTCREATORBUG-24357 suggests disabling
#   the clangpchmanagerbackend and clangrefactoringbackend builds
%if 0%{?qt6}
%cmake_qt6 \
%endif
  -DCMAKE_INSTALL_LIBDIR:STRING=%{_lib} \
  -DCMAKE_INSTALL_LIBEXECDIR:STRING=%{libexecdirname} \
  -DCLANGTOOLING_LINK_CLANG_DYLIB:BOOL=ON \
  -DBUILD_WITH_PCH:BOOL=OFF \
  -DWITH_DOCS:BOOL=ON \
  -DBUILD_TESTING:BOOL=OFF \
  -DQTC_SEPARATE_DEBUG_INFO:BOOL=OFF \
  -DBUILD_LIBRARY_QLITEHTML:BOOL=ON \
  -DBUILD_HELPVIEWERBACKEND_QTWEBENGINE:BOOL=OFF

%if 0%{?qt6}
%{qt6_build}
%{qt6_build_docs}
%endif

%install
%if 0%{?qt6}
%{qt6_install}
%endif

# Install files needed to develop qtcreator plugins.
DESTDIR=%{buildroot} cmake --install build --component Devel

# The upstream scripts should not be needed for plugins development
rm -r %{buildroot}%{_datadir}/qtcreator/scripts

# Already packaged
rm %{buildroot}%{_datadir}/qtcreator/{HACKING,LICENSE.GPL3-EXCEPT,README.md}

# Broken and useless for most users
rm %{buildroot}%{_bindir}/qtcreator.sh

# Install the doc files
mkdir -p %{buildroot}%{qtc_docdir}
pushd build
cp share/doc/qtcreator/qtcreator.qch %{buildroot}%{qtc_docdir}/
popd

mkdir -p %{buildroot}%{qtc_docdir}/qtcreator
cp -a doc/qtcreator/* %{buildroot}%{qtc_docdir}/qtcreator/

# Source Code Pro is packaged independently
rm -r %{buildroot}%{_datadir}/qtcreator/fonts

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license *GPL*
%doc README.md HACKING
%dir %{qtc_docdir}
%dir %{_datadir}/qtcreator
%dir %{_libdir}/qtcreator
%dir %{_libexecdir}/qtcreator
%{_bindir}/qtcreator
%{_datadir}/applications/org.qt-project.qtcreator.desktop
%{_datadir}/icons/hicolor/*/apps/QtProject-qtcreator.png
%{_datadir}/metainfo/org.qt-project.qtcreator.appdata.xml
%{_datadir}/qtcreator/android/
%{_datadir}/qtcreator/changelog/
%{_datadir}/qtcreator/cplusplus/
%{_datadir}/qtcreator/debugger/
%{_datadir}/qtcreator/externaltools/
# This won't be needed when syntax-highlighting has a KF6 release
%{_datadir}/qtcreator/generic-highlighter/
%{_datadir}/qtcreator/glsl/
%{_datadir}/qtcreator/indexer_preincludes/
%{_datadir}/qtcreator/modeleditor/
%{_datadir}/qtcreator/package-manager/
%{_datadir}/qtcreator/qml-type-descriptions/
%{_datadir}/qtcreator/qml/
%{_datadir}/qtcreator/qmldesigner/
%{_datadir}/qtcreator/qmlicons/
%{_datadir}/qtcreator/schemes/
%{_datadir}/qtcreator/snippets/
%{_datadir}/qtcreator/styles/
%{_datadir}/qtcreator/templates/
%{_datadir}/qtcreator/themes/
%{_datadir}/qtcreator/translations/
%{_libdir}/qtcreator/*.so.*
%{_libdir}/qtcreator/plugins/
%{_libexecdir}/qtcreator/buildoutputparser
%{_libexecdir}/qtcreator/cpaster
%{_libexecdir}/qtcreator/perf2text
%{_libexecdir}/qtcreator/perfparser
%{_libexecdir}/qtcreator/qml2puppet
%{_libexecdir}/qtcreator/qtc-askpass
%{_libexecdir}/qtcreator/qtcreator_process_stub
%{_libexecdir}/qtcreator/qtcreator_processlauncher
%{_libexecdir}/qtcreator/qtpromaker
%{_libexecdir}/qtcreator/sdktool
%{qtc_docdir}/qtcreator.qch
%{qtc_docdir}/qtcreator/

%files plugin-devel
%{_includedir}/qtcreator/
%{_libdir}/cmake/QtCreator/
%{_libdir}/qtcreator/*.a
%{_libdir}/qtcreator/*.so
%{_libdir}/qtcreator/objects-*/

%changelog
