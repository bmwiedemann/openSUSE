#
# spec file for package libqt5-qtdeclarative
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


%define qt5_snapshot 1
%define libname libQtQuick5
%define base_name libqt5
%define real_version 5.15.7
%define so_version 5.15.7
%define tar_version qtdeclarative-everywhere-src-%{version}
Name:           libqt5-qtdeclarative
Version:        5.15.7+kde25
Release:        0
Summary:        Qt 5 Declarative Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE sse2_nojit.patch -- enable JIT and sse2 only on sse2 case
Patch100:       sse2_nojit.patch
Patch103:       qtdeclarative-5.15.0-FixMaxXMaxYExtent.patch
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{real_version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{real_version}
BuildRequires:  libQt5Test-private-headers-devel >= %{real_version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{real_version}
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Gui) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Network) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Sql) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Widgets) >= %{real_version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

# NOTE recheck this once/if this package gets further splitted
%requires_ge    libQt5Core5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Network5
%requires_ge    libQt5Sql5
%requires_ge    libQt5Test5
%requires_ge    libQt5Widgets5

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%prep
%autosetup -p1 -n qtdeclarative-everywhere-src-%{version}

%package -n %{libname}
Summary:        Qt 5 Declarative Library
Group:          Development/Libraries/X11
# Used by QtQuick.LocalStorage
Requires:       libQt5Sql5-sqlite
Requires:       (qml-autoreqprov if rpm-build)

%description -n %{libname}
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Requires:       %{name}-tools = %{version}
Provides:       libQt5Quick-devel = %{version}
Obsoletes:      libQt5Quick-devel < %{version}

%description devel
You need this package, if you want to compile programs with qtdeclarative.

%package tools
Summary:        Qt 5 Declarative Tools
Group:          Development/Tools/Debuggers
License:        GPL-3.0-only

%description tools
Qt is a set of libraries for developing applications.

This package contains aditional tools for inspecting, testing, viewing, etc, QML imports and files.

%package private-headers-devel
Summary:        Non-ABI stable experimental API
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{real_version}
Requires:       libQt5Gui-private-headers-devel >= %{real_version}
Requires:       libQt5Test-private-headers-devel >= %{real_version}
Requires:       libQt5Widgets-private-headers-devel >= %{real_version}
Provides:       libQt5Quick-private-headers-devel = %{version}
Obsoletes:      libQt5Quick-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtdeclarative that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 quick/qml examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel
Recommends:     %{name}-tools

%description examples
Examples for libqt5-qtdeclarative (quick/qml) modules.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif

mkdir -p %{_target_platform}
pushd %{_target_platform}
# Force-enable the JIT for 32-bit x86
%ifarch %{ix86}
qmake-qt5 .. -- -qml-jit
%else
qmake-qt5 ..
%endif
popd

make %{?_smp_mflags} VERBOSE=1 -C %{_target_platform}

%ifarch %{ix86}
%if 0%{?sle_version:%sle_version} < 150000
# build libQt5Qml with no_sse2
mkdir -p %{_target_platform}-no_sse2
pushd %{_target_platform}-no_sse2
%qmake5 -config no_sse2 .. -- -no-qml-jit

make %{?_smp_mflags} VERBOSE=1 sub-src-qmake_all
# src/qml/Makefile has to be generated after qmltyperegistrar was built,
# so we have to run qmake again after that. There is no explicit
# dependency, it relies on CONFIG+=ordered...
make %{?_smp_mflags} VERBOSE=1 -C src/qmltyperegistrar
make %{?_smp_mflags} VERBOSE=1 sub-src-qmake_all
make %{?_smp_mflags} VERBOSE=1 -C src/qml
popd
%endif
%endif

%install
pushd %{_target_platform}
%qmake5_install
popd

%ifarch %{ix86}
%if 0%{?sle_version:%sle_version} < 150000
mkdir -p %{buildroot}%{_libqt5_libdir}//sse2
mv %{buildroot}%{_libqt5_libdir}/libQt5Qml.so.5* %{buildroot}%{_libqt5_libdir}/sse2/
pushd %{_target_platform}-no_sse2/src/qml
%qmake5_install
popd
%endif
%endif

find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
find %{buildroot}/%{_libdir}/pkgconfig -type f -name '*pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

# Link all the binaries with -qt5 suffix to %{_bindir}
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
  case "${i}" in
    qmlplugindump|qmlprofiler)
      ln -s %{_libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}-qt5
      ;;
   *)
      # No conflict with Qt4, so keep the original name for compatibility
      ln -s %{_libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}
      ln -s %{_libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}-qt5
      ;;
  esac
done
popd

%fdupes -s %{buildroot}%{_libqt5_includedir}
%fdupes -s %{buildroot}%{_libqt5_examplesdir}

%files -n %{libname}
%license LICENSE.*
%{_libqt5_libdir}/libQt5Q*.so.*
%ifarch %{ix86}
%if 0%{?sle_version:%sle_version} < 150000
%{_libqt5_libdir}/sse2/libQt5Q*.so.*
%endif
%endif
%dir %{_libqt5_archdatadir}/qml
%dir %{_libqt5_archdatadir}/qml/Qt
%{_libqt5_archdatadir}/qml/QtQuick
%{_libqt5_archdatadir}/qml/QtQuick.2
%{_libqt5_archdatadir}/qml/QtQml
%{_libqt5_archdatadir}/qml/builtins.qmltypes
%dir %{_libqt5_archdatadir}/qml/Qt/labs
%{_libqt5_archdatadir}/qml/Qt/labs/animation/
%{_libqt5_archdatadir}/qml/Qt/labs/folderlistmodel/
%{_libqt5_archdatadir}/qml/Qt/labs/settings/
%{_libqt5_archdatadir}/qml/Qt/labs/sharedimage/
%{_libqt5_archdatadir}/qml/Qt/labs/qmlmodels/
%{_libqt5_archdatadir}/qml/Qt/labs/wavefrontmesh/
%dir %{_libqt5_archdatadir}/qml/Qt/test
%{_libqt5_archdatadir}/qml/Qt/test/qtestroot/
%{_libqt5_plugindir}/qmltooling

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files tools
%license LICENSE.*
%{_bindir}/*
%{_libqt5_bindir}/*

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5*.prl
%{_libqt5_libdir}/libQt5Q*.so
%{_libqt5_libdir}/libQt5*.a
%{_libqt5_libdir}/pkgconfig/Qt5Q*.pc
%{_libqt5_libdir}/metatypes/qt5quick*_metatypes.json
%{_libqt5_libdir}/metatypes/qt5qml*_metatypes.json
%{_libqt5_archdatadir}/mkspecs/modules/*.pri
%{_libqt5_archdatadir}/mkspecs/features/qmlcache.prf
%{_libqt5_archdatadir}/mkspecs/features/qmltypes.prf
%{_libqt5_archdatadir}/mkspecs/features/qtquickcompiler.prf
%{_libqt5_archdatadir}/qml/QtTest

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
