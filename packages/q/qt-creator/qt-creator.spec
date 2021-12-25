#
# spec file for package qt-creator
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


%define real_version 6.0.1
%define short_version 6.0
%define tar_name qt-creator-opensource-src
%define tar_suffix %{nil}
#
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define pkgname_prefix qt
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt5"
  %define qt5 1
  %define pkgname_prefix qt5
  %define qt_min_version 5.14
  %define qtc_docdir %{_docdir}/qt5
%endif
%if "%{flavor}" == "qt6"
  %define qt6 1
  %define pkgname_prefix qt6
  %define qt_min_version 6.2
  %define qtc_docdir %{_qt6_docdir}
%endif
#
# Enable the clangcodemodel plugin on openSUSE TW and Leap 15.3+, which have LLVM >= 10
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%global build_clang_backend 1
%endif

%global libexecdirname libexec
%if "%{_libexecdir}" == "%{_prefix}/lib"
%global libexecdirname lib
%endif

# Private QML imports
%global __requires_exclude qmlimport\\((CameraGeometry|GridGeometry|HelperWidgets|LightUtils|LineGeometry|MouseArea3D|QtQuickDesignerColorPalette|QtQuickDesignerTheme|SelectionBoxGeometry|StudioControls|StudioTheme).*

# Has mocks for quite a few components, which are only pulled in when actually used
%global __requires_exclude_from %{_datadir}/qtcreator/qml/qmlpuppet/

Name:           %{pkgname_prefix}-creator
Version:        6.0.1
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
%if 0%{?build_clang_backend}
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
%if 0%{?qt5}
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qtquick3d-private-headers-devel >= %{qt_min_version}
BuildRequires:  libqt5-qttools-private-headers-devel >= %{qt_min_version}
# the DefinitionDownloader header is required
BuildRequires:  cmake(KF5SyntaxHighlighting) >= 5.56
BuildRequires:  cmake(Qt5Concurrent) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Designer) >= %{qt_min_version}
BuildRequires:  cmake(Qt5DocTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Help) >= %{qt_min_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Network) >= %{qt_min_version}
BuildRequires:  cmake(Qt5PrintSupport) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Quick3D) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Quick3DAssetImport) >= %{qt_min_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt5SerialPort) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt_min_version}
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquicktimeline
# Make sure to rebuild against latest Qt5 (using the last package in chain - libQt5Designer5)
%requires_eq    libQt5Designer5
%requires_eq    libQt5DesignerComponents5
# Explicitly require libQt5Script5 (needed by plugins). Qt Creator crashes with old versions on project load.
%requires_eq    libQt5Script5
Recommends:     libqt5-qtbase-common-devel
Recommends:     libqt5-qtbase-devel
Recommends:     libqt5-qtdeclarative-devel
Recommends:     libqt5-qtdoc-qch
Recommends:     libqt5-qttranslations
Provides:       qt-creator = %{version}
Obsoletes:      qt-creator < %{version}
Provides:       libqt5-creator = %{version}
Obsoletes:      libqt5-creator < %{version}
%endif
%if 0%{?qt6}
BuildRequires:  qt6-core-private-devel >= %{qt_min_version}
# Temporary
BuildRequires:  qt6-designer-private-devel >= %{qt_min_version}
BuildRequires:  qt6-gui-private-devel >= %{qt_min_version}
BuildRequires:  qt6-qml-private-devel >= %{qt_min_version}
BuildRequires:  qt6-quick-private-devel >= %{qt_min_version}
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
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6SerialPort) >= %{qt_min_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt_min_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Tools) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt_min_version}
Recommends:     qt6-base-devel
Recommends:     qt6-base-docs-qch
Recommends:     qt6-declarative-devel
Recommends:     qt6-declarative-docs-qch
Recommends:     qt6-translations
Conflicts:      libqt5-creator
Conflicts:      qt5-qtcreator
%endif
Requires:       hicolor-icon-theme
# clangcodemodel hardcodes clang include paths: QTCREATORBUG-21972
%requires_eq    libclang%{_llvm_sonum}
%endif

%description
Qt Creator is an integrated development environment (IDE) designed to
facilitate development with the Qt application framework.

%package plugin-devel
Summary:        Qt Creator Plugin Development Files
Group:          Development/Tools/IDE
Requires:       %{pkgname_prefix}-creator = %{version}
%if 0%{?qt5}
Provides:       libqt5-creator-plugin-devel = %{version}
Obsoletes:      libqt5-creator-plugin-devel < %{version}
Requires:       libqt5-qtbase-devel >= %{qt_min_version}
%endif
%if 0%{?qt6}
Requires:       qt6-base-devel >= %{qt_min_version}
Conflicts:      libqt5-creator-plugin-devel
Conflicts:      qt5-creator-plugin-devel
%endif

%description plugin-devel
This package contains all files from the Qt Creator source directory
(aka QTC_SOURCE) necessary to compile plugins.

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# E: spurious-executable-perm
chmod -x doc/qtcreator/images/qtcreator-cmakeexecutable.png

# Don't build qbs, we already have a package
rm -r src/shared/qbs

%build
%define _lto_cflags %{nil}

# - qtc wants relative paths for CMAKE_INSTALL_LIB{,EXEC}DIR
# - https://bugreports.qt.io/browse/QTCREATORBUG-24357 suggests disabling
#   the clangpchmanagerbackend and clangrefactoringbackend builds
%if 0%{?qt5}
%cmake \
%else
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

%if 0%{?qt5}
%cmake_build
cmake --build . -t docs
%else
%qt6_build
%qt6_build_docs
%endif

%install
%if 0%{?qt5}
%cmake_install
%else
%qt6_install
%endif

%if 0%{?build_clang_backend}
if [ ! -f %{buildroot}%{_libexecdir}/qtcreator/clangbackend ]; then
  echo 'ERROR: The Clang backend was not built. Check the build requirements' ; exit 1
fi
%endif

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

# plugin development files
mkdir %{buildroot}%{_datadir}/qtcreator-devel
cp *.pri %{buildroot}%{_datadir}/qtcreator-devel
find src \( \
   -name '*.h' -o -name '*.hpp' -o -name '*.pri' -o -iname 'license*.txt' -o \
   -name 'QtConcurrentTools' \
\) \
   -exec cp --parents {} %{buildroot}%{_datadir}/qtcreator-devel \;

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat >%{buildroot}%{_sysconfdir}/profile.d/qtcreator-devel.sh <<EOF
export QTC_SOURCE=%{_datadir}/qtcreator-devel
export QTC_BUILD=%{_exec_prefix}
EOF
cat >%{buildroot}%{_sysconfdir}/profile.d/qtcreator-devel.csh <<EOF
setenv QTC_SOURCE %{_datadir}/qtcreator-devel
setenv QTC_BUILD %{_exec_prefix}
EOF

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license *GPL*
%dir %{qtc_docdir}
%dir %{_libexecdir}/qtcreator
%{_bindir}/qtcreator
%{_datadir}/applications/org.qt-project.qtcreator.desktop
%{_datadir}/icons/hicolor/*/apps/QtProject-qtcreator.png
%{_datadir}/metainfo/org.qt-project.qtcreator.appdata.xml
%{_datadir}/qtcreator/
%{qtc_docdir}/qtcreator.qch
%{qtc_docdir}/qtcreator/
%{_libdir}/qtcreator/
%{_libexecdir}/qtcreator/buildoutputparser
%if 0%{?build_clang_backend}
%{_libexecdir}/qtcreator/clangbackend
%endif
%{_libexecdir}/qtcreator/cpaster
%{_libexecdir}/qtcreator/perf2text
%{_libexecdir}/qtcreator/perfparser
%{_libexecdir}/qtcreator/qml2puppet
%{_libexecdir}/qtcreator/qtc-askpass
%{_libexecdir}/qtcreator/qtcreator_processlauncher
%{_libexecdir}/qtcreator/qtcreator_process_stub
%{_libexecdir}/qtcreator/qtpromaker
%{_libexecdir}/qtcreator/sdktool

%files plugin-devel
%license *GPL*
%{_datadir}/qtcreator-devel/
%{_sysconfdir}/profile.d/qtcreator-devel.*

%changelog
