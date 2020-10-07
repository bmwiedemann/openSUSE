#
# spec file for package libqt5-creator
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

# Enable the clangcodemodel plugin on openSUSE TW and Leap 15.2+, which have LLVM >= 8.0.
%ifarch %{arm} aarch64 %{ix86} x86_64
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%global build_clang_backend 1
%endif
%endif
%define major_ver 4.13
%define qt5_version 5.12.0
%define tar_version 4.13.2
Name:           libqt5-creator
Version:        4.13.2
Release:        0
Summary:        Integrated Development Environment targeting Qt apps
# src/plugins/cmakeprojectmanager/configmodelitemdelegate.* -> LGPL-2.1-only OR LGPL-3.0-only
# src/shared/qbs is not built
# src/plugins/help/qlitehtml/litehtml and src/plugins/help/qlitehtml/litehtml/src/gumbo are not built
# src/plugins/imageviewer/imageview.cpp, src/plugins/vcsbase/wizard/vcsconfigurationpage.cpp -> BSD-3-Clause
# src/plugins/emacskeys/* -> GPL-3.0-only
# src/libs/3rdparty/syntax-highlighting -> MIT
# many files are dual licensed 'LGPL-3.0-only or (GPL-2.0-or-later OR GPL-3.0-or-later + KDE Free Qt Foundation option)', we'll use LGPL-3.0-only for these files
License:        GPL-3.0-with-Qt-Company-Qt-exception-1.1 AND (LGPL-2.1-only OR LGPL-3.0-only) AND GPL-3.0-only AND LGPL-3.0-only AND MIT AND BSD-3-Clause
Group:          Development/Tools/IDE
URL:            https://www.qt.io/ide/
Source:         https://download.qt.io/official_releases/qtcreator/%{major_ver}/%{tar_version}/qt-creator-opensource-src-%{tar_version}.tar.xz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE
Patch0:         0001-Fix-build-with-openSUSE-clang9-package.patch
# PATCH-FIX-OPENSUSE
Patch1:         fix-application-output.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Disable-some-plugins.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Don-t-rely-on-clang-include-and-binary-copies.patch
BuildRequires:  cmake
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{qt5_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{qt5_version}
BuildRequires:  libqt5-qtquick3d-private-headers-devel >= %{qt5_version}
BuildRequires:  libqt5-qttools-private-headers-devel >= %{qt5_version}
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.5
# Needs an internal patched version :-/
# BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Designer) >= %{qt5_version}
BuildRequires:  cmake(Qt5DocTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Help) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5PrintSupport) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick3D) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick3DAssetImport) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Script) >= %{qt5_version}
BuildRequires:  cmake(Qt5SerialPort) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
BuildRequires:  cmake(yaml-cpp)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libdw)
Requires:       libqt5-qtquickcontrols
# Make sure to rebuild against latest Qt5 (using the last package in chain - libQt5Designer5)
# Explicitly require libQt5Script5 (needed by plugins). Qt Creator crashes with old versions on project load.
%requires_eq    libQt5Designer5
%requires_eq    libQt5DesignerComponents5
%requires_eq    libQt5Script5
Recommends:     libqt5-qtbase-common-devel
Recommends:     libqt5-qtbase-devel
Recommends:     libqt5-qtdeclarative-devel
Recommends:     libqt5-qtdoc-qch
Recommends:     libqt5-qtquick1-devel
Recommends:     libqt5-qttranslations
Provides:       qt-creator = %{version}
Obsoletes:      qt-creator < %{version}
%if 0%{?build_clang_backend}
BuildRequires:  clang-devel >= 8.0
BuildRequires:  llvm-devel
# clangcodemodel hardcodes clang include paths: QTCREATORBUG-21972
%requires_eq    libclang%(rpm -q --qf '%''{version}' clang-devel | cut -d. -f1)
%endif
%ifnarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  cmake(Qt5WebEngine) >= %{qt5_version}
BuildRequires:  cmake(Qt5WebEngineWidgets) >= %{qt5_version}
%endif

%description
Qt Creator is an integrated development environment (IDE) designed to
facilitate development with the Qt application framework.

%package plugin-devel
Summary:        Qt Creator Plugin Development Files
Group:          Development/Tools/IDE
Requires:       libqt5-creator = %{version}
Requires:       libqt5-qtbase-devel >= %{qt5_version}

%description plugin-devel
This package contains all files from the Qt Creator source directory
(aka QTC_SOURCE) necessary to compile plugins.

%prep
%autosetup -p1 -n qt-creator-opensource-src-%{tar_version}

# E: spurious-executable-perm
chmod -x doc/qtcreator/images/qtcreator-cmakeexecutable.png

%build
%define _lto_cflags %{nil}

# https://bugzilla.opensuse.org/962650
sed -i 's#libexec/\${IDE_ID}#lib/\${IDE_ID}/libexec#' cmake/QtCreatorAPIInternal.cmake

%if "%{_lib}" == "lib64"
sed -i 's#lib/#lib64/#g' cmake/QtCreatorAPIInternal.cmake
%endif

# https://bugreports.qt.io/browse/QTCREATORBUG-24357 suggests disabling
# the clangpchmanagerbackend and clangrefactoringbackend builds
%cmake \
  -DBUILD_WITH_PCH=OFF \
  -DWITH_DOCS=ON \
  -DBUILD_EXECUTABLE_CLANGPCHMANAGERBACKEND=OFF \
  -DBUILD_EXECUTABLE_CLANGREFACTORINGBACKEND=OFF

%cmake_build

make docs

%install
%cmake_install

%if 0%{?build_clang_backend}
if [ ! -f %{buildroot}%{_libdir}/qtcreator/libexec/clangbackend ]; then
  echo 'ERROR: The Clang backend was not built. Check the build requirements' ; exit 1
fi
%endif

# Install the doc files
mkdir -p %{buildroot}%{_docdir}/qt5
pushd build
cp share/doc/qtcreator/qtcreator.qch %{buildroot}%{_docdir}/qt5/
popd

mkdir -p %{buildroot}%{_docdir}/qt5/qtcreator
cp -a doc/qtcreator/* %{buildroot}%{_docdir}/qt5/qtcreator/

# Install icons for the desktop file
# https://bugreports.qt.io/browse/QTCREATORBUG-24355
for i in 16 24 32 48 64 128 256 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  install -D -m644 src/plugins/coreplugin/images/logo/${i}/QtProject-qtcreator.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/QtProject-qtcreator.png
done

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
%dir %{_docdir}/qt5
%{_bindir}/qtcreator
%{_bindir}/qtcreator.sh
%{_datadir}/applications/org.qt-project.qtcreator.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/org.qt-project.qtcreator.appdata.xml
%{_datadir}/qtcreator/
%{_docdir}/qt5/qtcreator.qch
%{_docdir}/qt5/qtcreator/
%{_libdir}/qtcreator/

%files plugin-devel
%license *GPL*
%{_datadir}/qtcreator-devel/
%{_sysconfdir}/profile.d/qtcreator-devel.*

%changelog
