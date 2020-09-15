#
# spec file for package libqt5-qtscxml
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


%define qt5_snapshot 0
%define libname libQt5Scxml5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtscxml-everywhere-src-5.15.1
Name:           libqt5-qtscxml
Version:        5.15.1
Release:        0
Summary:        Qt 5 State Chart XML Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          System/Libraries
URL:            https://qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  xz
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt is a set of libraries for developing applications.

The Qt SCXML module provides functionality to create state machines from SCXML files.
It also contains functionality to support data models and executable content.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 State Chart XML Library
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n %{libname}
Qt is a set of libraries for developing applications.

The Qt SCXML module provides functionality to create state machines
from SCXML files. This includes both dynamically creating state
machines (loading the SCXML file and instantiating states and
transitions) and generating a C++ file that has a class implementing
the state machine. It also contains functionality to support data
models and executable content.

%package -n %{libname}-imports
Summary:        Qt 5 Scxml Addon - QML imports
Group:          Development/Libraries/X11
%requires_ge    libQtQuick5
Supplements:    (%{libname} and libQtQuick5)

%description -n %{libname}-imports
The Qt SCXML module provides functionality to create state machines
from SCXML files.

The Qt SCXML module provides functionality to create state machines from SCXML files.
It also contains functionality to support data models and executable content.

%package tools
Summary:        Qt 5 State Chart XML tools
Group:          Development/Tools/Debuggers
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0

%description tools
Qt is a set of libraries for developing applications.

This package contains tools for handling Qt SCXML files.

%package devel
Summary:        Development files for Qt5's State Chart XML library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-tools = %{version}

%description devel
You need this package if you want to compile programs with QtScxml.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for Qt5's State Chart XML library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtscxml that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 State Chart XML examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtscxml module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

# put all the binaries to %%_bindir, add -qt5 suffix, and symlink them back to %%_qt5_bindir
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
  mv $i ../../../bin/
  ln -s ../../../bin/$i .
done
popd

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5Scxml.so.*

%files -n %{libname}-imports
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtScxml

%files tools
%defattr(-,root,root,755)
%license LICENSE.*
%{_bindir}/qscxmlc
%{_libqt5_bindir}/qscxmlc

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtScxml/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtScxml/%{so_version}
%{_libqt5_includedir}/QtScxml/
%{_libqt5_libdir}/cmake/Qt5Scxml/
%{_libqt5_libdir}/libQt5Scxml.prl
%{_libqt5_libdir}/libQt5Scxml.so
%{_libqt5_libdir}/pkgconfig/Qt5Scxml.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri
%{_libqt5_archdatadir}/mkspecs/features/*.prf

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
