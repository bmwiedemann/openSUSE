#
# spec file for package libqt5-qtxmlpatterns
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
%define libname libQt5XmlPatterns5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtxmlpatterns-everywhere-src-5.15.1
Name:           libqt5-qtxmlpatterns
Version:        5.15.1
Release:        0
Summary:        Qt 5 XmlPatterns Library
# Legal:
# the tools are GPL-3.0 WITH Qt-exception-1.0
# The rest is LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
License:        (LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
The Qt XML Patterns module provides support for XPath, XQuery, XSLT,
and XML Schema validation.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 XmlPatterns Library
Group:          System/Libraries
%requires_ge    libQt5Core5
%requires_ge    libQt5Network5

%description -n %{libname}
The Qt XML Patterns module provides support for XPath, XQuery, XSLT,
and XML Schema validation.

%package imports
Summary:        QML imports for the XmlPatterns module
Group:          System/Libraries
Requires:       %{libname} = %{version}
# It was previously part of that package
Supplements:    libQtQuick5

%description imports
This package provides the QtQuick.XmlListModel QML import.

%package devel
Summary:        Development files for the Qt5 XML Patterns library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       libQt5XmlPatterns-devel = %{version}
Obsoletes:      libQt5XmlPatterns-devel < %{version}

%description devel
You need this package if you want to compile programs with QtXmlPatterns.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 XML Patterns library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
Provides:       libQt5XmlPatterns-private-headers-devel = %{version}
Obsoletes:      libQt5XmlPatterns-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtxmlpatterns that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 xmlpatterns examples
Group:          Development/Libraries/X11
Recommends:     %{name}-devel
License:        BSD-3-Clause

%description examples
Examples for the libqt5-qtxmlpatterns module.

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
  case "${i}" in
    xmlpatterns|xmlpatternsvalidator)
      mv $i ../../../bin/${i}-qt5
      ln -s ../../../bin/${i}-qt5 .
      ln -s ../../../bin/${i}-qt5 $i
      ;;
   *)
      mv $i ../../../bin/
      ln -s ../../../bin/$i .
      ;;
  esac
done
popd

%files -n %{libname}
%license LICENSE.*
%{_bindir}/*-qt5
%{_libqt5_bindir}/*
%{_libqt5_libdir}/libQt5XmlPatterns.so.*

%files imports
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick/XmlListModel

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtXmlPatterns/%{so_version}

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtXmlPatterns/%{so_version}
%{_libqt5_includedir}/QtXmlPatterns
%{_libqt5_libdir}/cmake/Qt5XmlPatterns
%{_libqt5_libdir}/libQt5XmlPatterns.prl
%{_libqt5_libdir}/libQt5XmlPatterns.so
%{_libqt5_libdir}/pkgconfig/Qt5XmlPatterns.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
