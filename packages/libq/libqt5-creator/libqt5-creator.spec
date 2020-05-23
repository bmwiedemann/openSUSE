#
# spec file for package libqt5-creator
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global build_clang_backend 0
%ifarch %arm aarch64 %ix86 x86_64
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%global build_clang_backend 1
%endif
%endif

Name:           libqt5-creator
Version:        4.12.1
Release:        0
Summary:        Integrated Development Environment targeting Qt apps
# src/plugins/cmakeprojectmanager/configmodelitemdelegate.* -> LGPL-2.1-only OR LGPL-3.0-only
# src/shared/qbs/src/plugins/generator/visualstudio -> LGPL-2.1-with-Qt-Company-Qt-exception-1.1 OR LGPL-3.0-only
# src/plugins/imageviewer/imageview.cpp, src/plugins/vcsbase/wizard/vcsconfigurationpage.cpp -> BSD-3-Clause
# src/plugins/emacskeys/* -> GPL-3.0-only
# src/libs/3rdparty/syntax-highlighting -> MIT
# many files are dual licensed 'LGPL-3.0-only or (GPL-2.0-or-later OR GPL-3.0-or-later + KDE Free Qt Foundation option)', we'll use LGPL-3.0-only for these files
License:        GPL-3.0-with-Qt-Company-Qt-exception-1.1 AND (LGPL-2.1-with-Qt-Company-Qt-exception-1.1 OR LGPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND GPL-3.0-only AND LGPL-3.0-only AND MIT AND BSD-3-Clause
Group:          Development/Tools/IDE
Url:            https://www.qt.io/ide/
%define major_ver 4.12
%define qt5_version 5.11.0
%define tar_version 4.12.1
Source:         https://download.qt.io/official_releases/qtcreator/%{major_ver}/%{tar_version}/qt-creator-opensource-src-%{tar_version}.tar.xz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE
Patch0:         0001-Fix-build-with-openSUSE-clang9-package.patch
# PATCH-FIX-OPENSUSE
Patch1:         fix-application-output.patch
BuildRequires:  gdb
BuildRequires:  libQt5Sql5-sqlite >= %{qt5_version}
BuildRequires:  libbotan-devel
BuildRequires:  libqt5-qtbase-devel >= %{qt5_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{qt5_version}
BuildRequires:  libqt5-qtquickcontrols >= %{qt5_version}
BuildRequires:  libqt5-qtscript-devel >= %{qt5_version}
BuildRequires:  libqt5-qttools-doc
BuildRequires:  libqt5-qttools-private-headers-devel >= %{qt5_version}
%ifnarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  libqt5-qtwebengine-devel >= %{qt5_version}
%endif
BuildRequires:  libqt5-qtx11extras-devel >= %{qt5_version}
# Needs an internal patched version :-/
# BuildRequires:  cmake(KF5SyntaxHighlighting)
%if %{build_clang_backend}
BuildRequires:  llvm-clang-devel >= 8.0
# clangcodemodel hardcodes clang include paths: QTCREATORBUG-21972
%requires_eq    libclang%(rpm -q --qf '%''{version}' clang-devel | cut -d. -f1)
%endif
BuildRequires:  update-desktop-files
BuildRequires:  xz
Provides:       qt-creator = %{version}
Obsoletes:      qt-creator < %{version}
Recommends:     libqt5-qtbase-common-devel
Recommends:     libqt5-qtdoc-qch
Recommends:     libqt5-qtbase-devel
Recommends:     libqt5-qtdeclarative-devel
Recommends:     libqt5-qtquick1-devel
Recommends:     libqt5-qttranslations
Requires:       libqt5-qtquickcontrols
Suggests:       git-core

# Make sure to rebuild against latest Qt5 (using the last package in chain - libQt5Designer5)
# Explicitly require libQt5Script5 (needed by plugins). Qt Creator crashes with old versions on project load.
%requires_eq libQt5Designer5
%requires_eq libQt5DesignerComponents5
%requires_eq libQt5Script5

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
# We have a separate package for qbs
rm -r src/shared/qbs

%build
sed -i s,libexec/qtcreator,%{_lib}/qtcreator/libexec,g qtcreator.qbs
sed -i 's,libexec/qtcreator,$$IDE_LIBRARY_BASENAME/qtcreator/libexec,g' qtcreator.pri
# https://bugzilla.opensuse.org/962650
sed -i s,libexec/qtcreator,%{_lib}/qtcreator/libexec,g src/plugins/coreplugin/icore.cpp

export QBS_INSTALL_DIR=%{_bindir}

opts="IDE_LIBRARY_BASENAME=%{_lib}"
opts="$opts CONFIG+=use_system_botan"

%qmake5 $opts
make %{?_smp_mflags}
make qch_docs
make html_docs

%install
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}${LD_LIBRARY_PATH:+:}%{_libdir}"
# its qmake. of course it is broken
make INSTALL_ROOT=%{buildroot}/%{_prefix} install

# Source Code Pro is packaged independently
rm -r %{buildroot}%{_datadir}/qtcreator/fonts

mkdir -p %{buildroot}%{_datadir}/doc/packages/qt5
cp share/doc/qtcreator/qtcreator.qch %{buildroot}%{_datadir}/doc/packages/qt5/

mkdir -p %{buildroot}%{_datadir}/doc/packages/qt5/qtcreator
cp -a doc/qtcreator/* %{buildroot}%{_datadir}/doc/packages/qt5/qtcreator/

%suse_update_desktop_file -i org.qt-project.qtcreator Development Qt IDE

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
%{_bindir}/qtcreator
%{_libdir}/qtcreator/
%if %{build_clang_backend}
%{_libdir}/qtcreator/libexec/clangbackend
%endif
%{_datadir}/qtcreator/
%{_datadir}/icons/hicolor
%{_datadir}/applications/org.qt-project.qtcreator.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.qt-project.qtcreator.appdata.xml
%dir %{_datadir}/doc/packages/qt5
%{_datadir}/doc/packages/qt5/qtcreator/
%{_datadir}/doc/packages/qt5/qtcreator.qch

%files plugin-devel
%license *GPL*
%{_datadir}/qtcreator-devel/
%{_sysconfdir}/profile.d/qtcreator-devel.*

%changelog
