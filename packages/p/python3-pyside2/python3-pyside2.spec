#
# spec file for package python3-pyside2
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


%bcond_with tests

%define mypython python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Name:           python3-pyside2
Version:        5.15.1
Release:        0
Summary:        Python bindings for Qt
# Legal:
# Most files are LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
# pyside2-tools is GPL-2.0-only
# shiboken2 contains files under GPL-3.0-only WITH Qt-GPL-exception-1.0
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-2.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group:          Development/Languages/Python
URL:            http://wiki.qt.io/Qt_for_Python
Source0:        https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-opensource-src-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         lib64.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Don-t-try-to-install-or-use-uic-rcc-designer-copies.patch
# PATCH-FIX-OPENSUSE
Patch2:         0002-Fix-the-openSUSE-executable-names.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-cmake-Don-t-assume-qhelpgenerator-is-in-PATH.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++

BuildRequires:  libqt5-qtdeclarative-private-headers-devel

##### essential modules
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)

##### optional modules
BuildRequires:  libQt53DQuickScene2D5
BuildRequires:  cmake(Qt53DAnimation)
BuildRequires:  cmake(Qt53DCore)
BuildRequires:  cmake(Qt53DExtras)
BuildRequires:  cmake(Qt53DInput)
BuildRequires:  cmake(Qt53DLogic)
BuildRequires:  cmake(Qt53DRender)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5DataVisualization)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5MultimediaWidgets)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5RemoteObjects)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5ScriptTools)
BuildRequires:  cmake(Qt5Scxml)
BuildRequires:  cmake(Qt5Sensors)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
# FreeCAD 0.18 still uses Qt5Webkit
BuildRequires:  cmake(Qt5WebKit)

BuildRequires:  clang-devel >= 3.9
BuildRequires:  libxslt-devel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-idna
BuildRequires:  python3-urllib3
BuildRequires:  python3-wheel

%description
The PySide2 project provides Python bindings for the Qt
application and UI framework.

%package devel
Summary:        Header Files for PySide2
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-2.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description devel
Files needed for development with the PySide2 bindings
for Qt.

%package examples
Summary:        Examples for using PySide2
License:        BSD-3-Clause
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description examples
Examples and Tutorials for the PySide2 bindings for Qt.

%prep
%setup -q -n pyside-setup-opensource-src-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if "%{_lib}" == "lib64"
%patch0 -p1
%endif

%build
export LLVM_INSTALL_DIR=%{_prefix}
# Workaround for PYSIDE-880
export LC_ALL=C.utf8
%{mypython} setup.py build --reuse-build --ignore-git %{?jobs:--parallel=%{jobs}} \
%if %{with tests}
  --build-tests
%endif

%install
export LC_ALL=C.utf8
%{mypython} setup.py install --reuse-build --ignore-git --prefix=%{_prefix} --root=%{buildroot} \
%if %{with tests}
  --build-tests
%endif

# and hack re-installation, since setup is doing it wrong
rm -rf %{buildroot}/*
mkdir -p %{buildroot}/%{_libdir}
cp -a ./pyside?_install/py*-release/* %{buildroot}%{_prefix}/

cp -a ./pyside3_build/py*-release/pyside2/PySide2/*.pyi %{buildroot}%{python_sitearch}/PySide2/

cp -a ./examples %{buildroot}%{_datadir}/PySide2/

sed -i 's,=.*/pyside._install/[^\/]*,=/usr,' %{buildroot}/%{_libdir}/pkgconfig/*.pc
sed -i 's,^libdir=.*,libdir=%{_libdir},' %{buildroot}/%{_libdir}/pkgconfig/*.pc

sed -i 's,"[^"]*/include/shiboken2","%{_includedir}/shiboken2",' %{buildroot}/%{_libdir}/cmake/Shiboken*/*.cmake
sed -i 's,"[^"]*/%{_lib}/libshiboken2.\(.*\)","%{_libdir}/libshiboken2.\1",' %{buildroot}/%{_libdir}/cmake/Shiboken*/*.cmake
sed -i 's,"[^"]*/bin/shiboken2","%{_bindir}/shiboken2",' %{buildroot}/%{_libdir}/cmake/Shiboken*/*.cmake
sed -i 's,^include("[^"]*-release/%{_lib}/,include("%{_libdir}/,' %{buildroot}/%{_libdir}/cmake/Shiboken*/*.cmake

sed -i 's,"[^"]*/include/PySide2","%{_includedir}/PySide2",' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake
sed -i 's,"[^"]*/%{_lib}/cmake/\(.*\)","%{_libdir}/cmake/\1",' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake
sed -i 's,"[^"]*/%{_lib}/libpyside2\.\(.*\)","%{_libdir}/libpyside2.\1",' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake
sed -i 's,"[^"]*/\(python.*/site-packages\)","%{_libdir}/\1",' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake
sed -i 's,"[^"]*/share/PySide2/typesystems","%{_datadir}/PySide2/typesystems",' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake
sed -i 's,"[^"]*/share/PySide2/glue","%{_datadir}/PySide2/glue",' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake
sed -i 's,^include("[^"]*-release/%{_lib}/,include("%{_libdir}/,' %{buildroot}/%{_libdir}/cmake/PySide2*/*.cmake

rm %{buildroot}%{_bindir}/*_tool.py
rm -Rf %{buildroot}%{_datadir}/PySide2/typesystems/typesystem_*_win.xml

%fdupes %{buildroot}%{_datadir}/PySide2/examples/

%check
%if %{with tests}
%{mypython} testrunner.py test
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.*
%doc dist/changes*
%{_bindir}/*
%{_libdir}/*.so.*
%{python_sitearch}/*

%files devel
%{_datadir}/PySide2/
%exclude %{_datadir}/PySide2/examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake
%{_libdir}/pkgconfig
%{_mandir}/man*/*

%files examples
%dir %{_datadir}/PySide2
%{_datadir}/PySide2/examples

%changelog
