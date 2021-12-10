#
# spec file for package python3-pyside6
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


%define tar_name pyside-setup-opensource-src
#
%if "@BUILD_FLAVOR@%{nil}" == "shiboken6"
%global pyside_flavor shiboken6
%else
%global pyside_flavor pyside6
%endif
#
# llvm/clang are too old in Leap 15.2
%if %{?suse_version} == 1500 && 0%{?sle_version} == 150200
ExclusiveArch:  do_not_build
%endif
#
Name:           python3-%{pyside_flavor}
Version:        6.2.2
Release:        0
Summary:        Python bindings for Qt 6
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-2.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-%{version}-src/%{tar_name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Don-t-install-CMake-files-into-versioned-directories.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Always-link-to-python-libraries.patch
# SECTION common_dependencies
BuildRequires:  clang-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
# /SECTION
%if "%{pyside_flavor}" == "pyside6"
BuildRequires:  cmake(Shiboken6)
# SECTION test_dependencies
BuildRequires:  Mesa-dri
BuildRequires:  qt6-location
BuildRequires:  qt6-sql-sqlite
BuildRequires:  xvfb-run
# /SECTION
# SECTION essential_modules
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
# /SECTION
# SECTION optional_modules
BuildRequires:  qt6-qml-private-devel
BuildRequires:  cmake(Qt63DAnimation)
BuildRequires:  cmake(Qt63DCore)
BuildRequires:  cmake(Qt63DExtras)
BuildRequires:  cmake(Qt63DInput)
BuildRequires:  cmake(Qt63DLogic)
BuildRequires:  cmake(Qt63DRender)
BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6DataVisualization)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6Scxml)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WebChannel)
%ifnarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6WebEngineWidgets)
%endif
BuildRequires:  cmake(Qt6WebSockets)
# /SECTION
%endif

%description
Python bindings for the Qt cross-platform application and UI framework.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
Python bindings for the Qt cross-platform application and UI framework

%prep
%autosetup -p1 -n %{tar_name}-%{version}

%build
_libsuffix=$(echo %{_lib} | cut -b4-)

# The python script used to set paths before running tests
# doesn't handle build dirs called 'build'
%global __qt6_builddir %{pyside_flavor}

# Fix installation dir
sed -i 's#purelib#platlib#' sources/{pyside6/cmake/PySideSetup.cmake,shiboken6/cmake/ShibokenHelpers.cmake}

pushd sources/%{pyside_flavor}

# NOTE:The compiler and linker flags shall not be defined
%cmake_qt6 \
  -DBUILD_TESTS:BOOL=ON \
  -DLIB_SUFFIX:STRING="${_libsuffix}" \
  -DCMAKE_C_FLAGS:STRING="" \
  -DCMAKE_CXX_FLAGS:STRING="" \
  -DCMAKE_EXE_LINKER_FLAGS:STRING="" \
  -DPYTHON_EXECUTABLE:STRING=python3 \
  -DNUMPY_INCLUDE_DIR:STRING=%{python_sitearch}/numpy/core/include \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON

%{qt6_build}

popd

%install
pushd sources/%{pyside_flavor}
%{qt6_install}
popd

%if "%{pyside_flavor}" == "shiboken6"

%fdupes -s %{buildroot}%{python_sitearch}

sed -i 's#env python#python3#' %{buildroot}%{_bindir}/shiboken_tool.py

%else

rm %{buildroot}%{_datadir}/PySide6/typesystems/*_{mac,win}.xml

%fdupes -s %{buildroot}%{python_sitearch}/PySide6

mkdir -p %{buildroot}%{_qt6_pluginsdir}/designer
mv %{buildroot}%{_prefix}/plugins/designer/libPySidePlugin.so %{buildroot}%{_qt6_pluginsdir}/designer

%endif

%fdupes -s %{buildroot}%{_libdir}/cmake

%check
# the pyside tests need to know the path to the 'qmake' executable
export PATH=%{_qt6_bindir}:$PATH

# Needed by the shiboken tests
export LD_LIBRARY_PATH=%{buildroot}%{_qt6_libdir}:$LD_LIBRARY_PATH

%if "%{pyside_flavor}" == "pyside6"
%define xvfb_command xvfb-run -s "-screen 0 1600x1200x16 -ac +extension GLX +render -noreset" \\

# Excluded tests (last update: 2021-10-12)
# registry_existence_test can only be run if pyside and shiboken are built together
# QtWidgets_bug_635 fails
# QtWebEngineWidgets_pyside-474-qtwebengineview & QtWebEngineCore_web_engine_custom_scheme
# pass locally but not on the build service
%define ctest_exclude_regex '(registry_existence_test|QtWidgets_bug_635|QtWebEngineWidgets_pyside-474-qtwebengineview|QtWebEngineCore_web_engine_custom_scheme)'
%endif

pushd sources/%{pyside_flavor}
%{?xvfb_command}
ctest \
  --output-on-failure \
  --force-new-ctest-process \
  --test-dir %{__qt6_builddir} \
  --parallel %{_smp_build_ncpus} \
  %{?ctest_exclude_regex:--exclude-regex %{ctest_exclude_regex}}
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license sources/%{pyside_flavor}/COPYING*
%{_libdir}/lib%{pyside_flavor}.%{py3_soflags}.so.*
%if "%{pyside_flavor}" == "shiboken6"
%{_bindir}/shiboken6
%{_bindir}/shiboken_tool.py
%{python_sitearch}/shiboken6/
%{python_sitearch}/shiboken6_generator/
%else
%{python_sitearch}/PySide6/
%dir %{_qt6_pluginsdir}/designer
%{_qt6_pluginsdir}/designer/libPySidePlugin.so
%endif

%files devel
%if "%{pyside_flavor}" == "shiboken6"
%{_includedir}/shiboken6/
%{_qt6_cmakedir}/Shiboken6/
%else
%{_datadir}/PySide6/
%{_includedir}/PySide6/
%{_qt6_cmakedir}/PySide6/
%endif
%{_libdir}/lib%{pyside_flavor}.%{py3_soflags}.so
%{_libdir}/pkgconfig/%{pyside_flavor}.pc

%changelog
