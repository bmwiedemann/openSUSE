#
# spec file for package qbs
#
# Copyright (c) 2022 SUSE LLC
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


%define qt5_version 5.14.0
Name:           qbs
Version:        1.23.2
Release:        0
Summary:        Modern build tool for software projects
# Legal:
# scripts/ is LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
# share/ is LGPL-2.1-only OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1.
# src/ is a mix of both licenses combo...except transformerchangetracking.{cpp,h}
# which is GPL-3.0-only WITH Qt-GPL-exception-1.0
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND (LGPL-2.1-only OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group:          Development/Tools/Building
URL:            https://wiki.qt.io/Qbs
Source:         https://download.qt.io/official_releases/%{name}/%{version}/%{name}-src-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch1:         0001-Use-qmake-qt5-for-openSUSE.patch
BuildRequires:  fdupes
BuildRequires:  libQt5Concurrent-devel >= %{qt5_version}
BuildRequires:  libQt5Core-devel >= %{qt5_version}
BuildRequires:  libQt5Core-private-headers-devel >= %{qt5_version}
BuildRequires:  libQt5Gui-devel >= %{qt5_version}
BuildRequires:  libQt5Network-devel >= %{qt5_version}
BuildRequires:  libQt5Script-devel >= %{qt5_version}
BuildRequires:  libQt5Test-devel >= %{qt5_version}
BuildRequires:  libQt5Widgets-devel >= %{qt5_version}
BuildRequires:  libQt5Xml-devel >= %{qt5_version}
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
Summary:        Development files for %{name}
Group:          Development/Tools/Building
Requires:       %{name} = %{version}-%{release}

%description devel
This package is required to develop applications using %{name} as a library

%prep
%autosetup -p1 -n %{name}-src-%{version}

%build
makeopts=""

# QBS_LIBEXEC_DESTDIR, QBS_RELATIVE_LIBEXEC_PATH need to be
# set for Leap 15 because the defaults are hardcoded to 'libexec'
#
# qbs_enable_project_file_updates allow to build Qt Creator
# against the installed qbs.
%qmake5 %{name}.pro -r QBS_INSTALL_PREFIX=%{_prefix} \
    QBS_LIBRARY_DIRNAME=%{_lib} \
    QBS_LIBEXEC_INSTALL_DIR=%{_libexecdir}/%{name} \
    QBS_LIB_INSTALL_DIR=%{_libdir} \
    QBS_PLUGINS_INSTALL_DIR=%{_libdir} \
    CONFIG+=qbs_enable_project_file_updates \
%if 0%{?suse_version} <= 1500
    QBS_RELATIVE_LIBEXEC_PATH=../lib/%{name} \
    QBS_LIBEXEC_DESTDIR=../../../lib/%{name}
%endif

%make_build $makeopts

%install
%qmake5_install

# Cleanup, until the code is ported to python3
rm %{buildroot}%{_libexecdir}/%{name}/dmgbuild
rm -r %{buildroot}%{_datadir}/%{name}/python

# E: version-control-internal-file
rm %{buildroot}%{_datadir}/qbs/modules/typescript/qbs-tsc-scan/.gitignore

ln -f -s qbs.1.gz %{buildroot}/%{_mandir}/man1/qbs-config.1.gz
ln -f -s qbs.1.gz %{buildroot}/%{_mandir}/man1/qbs-config-ui.1.gz
ln -f -s qbs.1.gz %{buildroot}/%{_mandir}/man1/qbs-create-project.1.gz
ln -f -s qbs.1.gz %{buildroot}/%{_mandir}/man1/qbs-setup-android.1.gz
ln -f -s qbs.1.gz %{buildroot}/%{_mandir}/man1/qbs-setup-qt.1.gz
ln -f -s qbs.1.gz %{buildroot}/%{_mandir}/man1/qbs-setup-toolchains.1.gz

%fdupes %{buildroot}%{_datadir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LGPL_EXCEPTION.txt LICENSE.LGPLv21 LICENSE.LGPLv3 LICENSE.GPL3-EXCEPT
%doc README.md
%doc changelogs/changes-%{version}.md
%dir %{_datadir}/%{name}/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/
%dir %{_libexecdir}/%{name}/
%{_bindir}/%{name}-config
%{_bindir}/%{name}-config-ui
%{_bindir}/%{name}-create-project
%{_bindir}/%{name}-setup-android
%{_bindir}/%{name}-setup-qt
%{_bindir}/%{name}-setup-toolchains
%{_bindir}/qbs
%{_datadir}/%{name}/imports/
%{_datadir}/%{name}/module-providers/
%{_datadir}/%{name}/modules/
%{_datadir}/%{name}/qml-type-descriptions/
%{_libdir}/%{name}/plugins/lib%{name}_cpp_scanner.so
%{_libdir}/%{name}/plugins/lib%{name}_qt_scanner.so
%{_libdir}/%{name}/plugins/libclangcompilationdbgenerator.so
%{_libdir}/%{name}/plugins/libiarewgenerator.so
%{_libdir}/%{name}/plugins/libkeiluvgenerator.so
%{_libdir}/%{name}/plugins/libmakefilegenerator.so
%{_libdir}/%{name}/plugins/libvisualstudiogenerator.so
%{_libdir}/lib%{name}*.so.*
%{_libexecdir}/%{name}/%{name}_processlauncher
%{_mandir}/man1/qbs*%{ext_man}

%files devel
%doc %{_datadir}/%{name}/examples/
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*.prl
%{_libdir}/lib%{name}*.so

%changelog
