#
# spec file for package qbs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define qt5_version 5.9.0
Name:           qbs
Version:        1.13.1
Release:        0
Summary:        Modern build tool for software projects
License:        (LGPL-2.1-with-Qt-Company-Qt-exception-1.1 OR LGPL-3.0-only) AND GPL-3.0-with-Qt-Company-Qt-exception-1.1
Group:          Development/Tools/Building
URL:            https://wiki.qt.io/Qbs
Source:         https://download.qt.io/official_releases/%{name}/%{version}/%{name}-src-%{version}.tar.gz
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
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
%if 0%{?sle_version} <= 120200
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc7-c++
%endif
%endif

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
%setup -q -n %{name}-src-%{version}

%build
makeopts=""
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
%if 0%{?sle_version} <= 120200
makeopts="$makeopts CC=gcc-6 CXX=g++-6"
%else
makeopts="$makeopts CC=gcc-7 CXX=g++-7"
%endif
%endif

# QBS_LIBEXEC_DESTDIR, QBS_RELATIVE_LIBEXEC_PATH need to be
# set because the defaults are hardcoded to 'libexec'
#
# qbs_enable_project_file_updates allow to build Qt Creator
# against the installed qbs.
%qmake5 %{name}.pro -r QBS_INSTALL_PREFIX=%{_prefix} \
    QBS_LIBRARY_DIRNAME=%{_lib} \
    QBS_LIBEXEC_DESTDIR=../../../lib/%{name} \
    QBS_LIBEXEC_INSTALL_DIR=%{_libexecdir}/%{name} \
    QBS_RELATIVE_LIBEXEC_PATH=../lib/%{name} \
    QBS_LIB_INSTALL_DIR=%{_libdir} \
    QBS_PLUGINS_INSTALL_DIR=%{_libdir} \
    CONFIG+=qbs_enable_project_file_updates

make %{?_smp_mflags} $makeopts

%install
%qmake5_install

# Cleanup
rm -f %{buildroot}%{_datadir}/%{name}/python/biplist/qt_attribution.json
rm -f %{buildroot}%{_datadir}/%{name}/python/dmgbuild/qt_attribution.json
rm -f %{buildroot}%{_datadir}/%{name}/python/ds_store/qt_attribution.json
rm -f %{buildroot}%{_datadir}/%{name}/python/mac_alias/qt_attribution.json

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
%doc README
%license LGPL_EXCEPTION.txt LICENSE.LGPLv21 LICENSE.LGPLv3
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
%{_datadir}/%{name}/python/
%{_datadir}/%{name}/qml-type-descriptions/
%{_libdir}/%{name}/plugins/lib%{name}_cpp_scanner.so
%{_libdir}/%{name}/plugins/lib%{name}_qt_scanner.so
%{_libdir}/%{name}/plugins/libclangcompilationdbgenerator.so
%{_libdir}/%{name}/plugins/libmakefilegenerator.so
%{_libdir}/%{name}/plugins/libvisualstudiogenerator.so
%{_libdir}/lib%{name}*.so.*
%{_libexecdir}/%{name}/%{name}_processlauncher
%{_libexecdir}/%{name}/dmgbuild
%{_mandir}/man1/qbs*%{ext_man}

%files devel
%license LGPL_EXCEPTION.txt LICENSE.LGPLv21 LICENSE.LGPLv3
%doc %{_datadir}/%{name}/examples/
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*.prl
%{_libdir}/lib%{name}*.so

%changelog
