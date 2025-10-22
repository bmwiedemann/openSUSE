#
# spec file for package qbs
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2018 The Qt Company.
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


%if %{?suse_version} > 1500
# No python-beautifulsou4 is 15.6
%bcond_without qch_doc
%endif
Name:           qbs
Version:        3.1.0
Release:        0
Summary:        Build tool for software projects
# Legal:
# scripts/ is LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
# share/ is LGPL-2.1-only OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1.
# src/ is a mix of both licenses combo...except transformerchangetracking.{cpp,h}
# which is GPL-3.0-only WITH Qt-GPL-exception-1.0
License:        LGPL-3.0-only
URL:            https://wiki.qt.io/Qbs
Source:         https://download.qt.io/official_releases/qbs/%{version}/qbs-src-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-with-Qt-6.10.patch
BuildRequires:  fdupes
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
%if %{with qch_doc}
BuildRequires:  python3
BuildRequires:  python3-bs4
BuildRequires:  python3-lxml
BuildRequires:  cmake(Qt6Tools)
%endif
# Qt Creator used to package qbs too
Conflicts:      libqt5-creator <= 4.5.0

%description
Qbs is a tool that helps simplify the build process for developing projects
across multiple platforms. Qbs can be used for any software project, whether
it is written with Qt or not.

Qbs is an all-in one tool that generates a build graph from a high-level
project description (like qmake or CMake) and additionally undertakes the tasks
of executing the commands in the low-level build graph (like make).

This package contains the command line interface. The Qt Creator IDE does
directly support working qbs projects.

%package devel
Summary:        Development files for qbs
Requires:       %{name} = %{version}-%{release}

%description devel
This package is required to develop applications using qbs as a library

%package examples
Summary:        Examples for qbs
Requires:       %{name}
# Split from the -devel package
Conflicts:      qbs-devel < 2.0.2

%description examples
This package contains examples to show different qbs usages.

%prep
%autosetup -p1 -n %{name}-src-%{version}

%build
%cmake_qt6 \
  -DQBS_ENABLE_RPATH:BOOL=FALSE \
  -DQBS_INSTALL_MAN_PAGE:BOOL=TRUE \
%if %{with qch_doc}
  -DQBS_INSTALL_QCH_DOCS:BOOL=TRUE \
%endif
%if 0%{?suse_version} == 1500
  -DQBS_LIBEXEC_INSTALL_DIR:STRING=lib/qbs \
%endif
  -DQBS_LIB_INSTALL_DIR:STRING=%{_lib} \
  -DQBS_PLUGINS_INSTALL_BASE:STRING=%{_lib} \
  -DWITH_TESTS:BOOL=FALSE

%qt6_build

%install
%qt6_install

# Cleanup
rm -r %{buildroot}%{_qt6_sharedir}/qbs/python

%fdupes %{buildroot}%{_qt6_sharedir}/qbs

%ldconfig_scriptlets

%files
%license LGPL_EXCEPTION.txt LICENSE.LGPLv21 LICENSE.LGPLv3 LICENSE.GPL3-EXCEPT
%doc README.md changelogs/changes-%{version}.md
%if %{with qch_doc}
%dir %{_qt6_sharedir}/doc/qbs
%doc %{_qt6_sharedir}/doc/qbs/qbs.qch
%endif
%{_bindir}/qbs
%{_bindir}/qbs-config
%{_bindir}/qbs-config-ui
%{_bindir}/qbs-create-project
%{_bindir}/qbs-setup-android
%{_bindir}/qbs-setup-qt
%{_bindir}/qbs-setup-toolchains
%dir %{_libexecdir}/qbs/
%{_libexecdir}/qbs/qbs_processlauncher
%{_mandir}/man1/qbs.1%{ext_man}
%dir %{_qt6_libdir}/qbs
%dir %{_qt6_libdir}/qbs/plugins
%{_qt6_libdir}/libqbscore.so.*
%{_qt6_libdir}/qbs/plugins/libclangcompilationdbgenerator.so
%{_qt6_libdir}/qbs/plugins/libgraphvizgenerator.so
%{_qt6_libdir}/qbs/plugins/libiarewgenerator.so
%{_qt6_libdir}/qbs/plugins/libkeiluvgenerator.so
%{_qt6_libdir}/qbs/plugins/libmakefilegenerator.so
%{_qt6_libdir}/qbs/plugins/libqbs_cpp_scanner.so
%{_qt6_libdir}/qbs/plugins/libqbs_qt_scanner.so
%{_qt6_libdir}/qbs/plugins/libvisualstudiogenerator.so
%dir %{_qt6_sharedir}/qbs
%{_qt6_sharedir}/qbs/imports/
%{_qt6_sharedir}/qbs/module-providers/
%{_qt6_sharedir}/qbs/modules/
%{_qt6_sharedir}/qbs/qml-type-descriptions/

%files devel
%{_includedir}/qbs/
%{_qt6_libdir}/libqbscore.so

%files examples
%dir %{_qt6_sharedir}/qbs
%{_qt6_sharedir}/qbs/examples/

%changelog
