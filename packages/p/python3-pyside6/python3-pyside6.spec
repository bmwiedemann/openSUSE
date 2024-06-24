#
# spec file for package python3-pyside6
#
# Copyright (c) 2024 SUSE LLC
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


%define tar_name pyside-setup-everywhere-src
%define short_version 6.7

%global flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == ""
# factory-auto requires the main build_flavor to match the specfile name
%define mypython python3
%global pyside_flavor pyside6
# stop-gap for local builds
BuildRequires:  no-build-without-multibuild-flavor
ExclusiveArch:  donotbuild
%else
%global pyside_flavor %flavor
%if 0%{suse_version} > 1500
# This builds only for the primary python flavor, it provides the python3 flavor
%define pythons %{primary_python}
%else
# This only works with the SLE15 python module for a more modern python than 3.6.
# The build will stay unresolvable for regular python3 = 3.6
%{?sle15_python_module_pythons}
%endif
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}
%define mypython_sitearch %{expand:%%%{mypython}_sitearch}
%endif

Name:           %{mypython}-%{pyside_flavor}
Version:        6.7.2
Release:        0
Summary:        Python bindings for Qt 6
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-2.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-%{version}-src/%{tar_name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Always-link-to-python-libraries.patch
# PATCH-FIX-UPSTREAM https://codereview.qt-project.org/c/pyside/pyside-setup/+/567559
Patch1:         fix-pytest-qt.patch
# SECTION common_dependencies
BuildRequires:  clang-devel
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{mypython}-devel >= 3.7
BuildRequires:  %{mypython}-numpy-devel
BuildRequires:  %{mypython}-setuptools
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
# /SECTION
%if "%{pyside_flavor}" == "pyside6"
# For the registry_existence test
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150500
# Not available in 15.5
BuildRequires:  %{mypython}-distro
%endif
BuildRequires:  %{mypython}-shiboken6-devel = %{version}
# SECTION test_dependencies
BuildRequires:  Mesa-dri
BuildRequires:  qt6-location
BuildRequires:  qt6-sql-sqlite
BuildRequires:  xvfb-run
# /SECTION
# SECTION essential_modules
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6ExampleIconsPrivate)
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
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6HttpServer)
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6Scxml)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6SerialBus)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6SpatialAudio)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WebChannel)
%ifarch x86_64 %x86_64 aarch64 riscv64
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PdfWidgets)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6WebEngineWidgets)
%endif
BuildRequires:  cmake(Qt6WebSockets)
# /SECTION
Requires:       %{mypython}-shiboken6
%endif
%if 0%{?suse_version} > 1500
Provides:       python3-%{pyside_flavor} = %{version}-%{release}
Obsoletes:      python3-%{pyside_flavor} < %{version}-%{release}
%endif

%description
Python bindings for the Qt cross-platform application and UI framework.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
%if 0%{?suse_version} > 1500
Provides:       python3-%{pyside_flavor}-devel = %{version}-%{release}
Obsoletes:      python3-%{pyside_flavor}-devel < %{version}-%{release}
%endif

%description devel
Python bindings for the Qt cross-platform application and UI framework

%prep
%autosetup -p1 -n %{tar_name}-%{version}

# Restore 6.6.1 RPATH value. rpmlint will complain otherwise
sed -i 's#${base}/../shiboken6/##' sources/pyside6/CMakeLists.txt

%build
_libsuffix=$(echo %{_lib} | cut -b4-)

# The python script used to set paths before running tests
# doesn't handle build dirs called 'build'
%global __qt6_builddir %{pyside_flavor}

# Fix installation dir
sed -i 's#purelib#platlib#' sources/shiboken6/cmake/ShibokenHelpers.cmake

pushd sources/%{pyside_flavor}

# NOTE:The compiler and linker flags shall not be defined
%cmake_qt6 \
  -DBUILD_TESTS:BOOL=ON \
  -DLIB_SUFFIX:STRING="${_libsuffix}" \
  -DCMAKE_C_FLAGS:STRING="" \
  -DCMAKE_CXX_FLAGS:STRING="" \
  -DCMAKE_EXE_LINKER_FLAGS:STRING="" \
  -DPython_EXECUTABLE:STRING=%{__mypython} \
  -DNUMPY_INCLUDE_DIR:STRING=%{mypython_sitearch}/numpy/core/include \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON \
%if "%{pyside_flavor}" == "shiboken6"
  -DCMAKE_SKIP_RPATH:BOOL=ON \
%endif
  -DQFP_NO_STRIP:BOOL=ON

%{qt6_build}

popd

%install
pushd sources/%{pyside_flavor}
%{qt6_install}
popd

%if "%{pyside_flavor}" == "shiboken6"
sed -i 's@^#.*env python.*$@#!%{__mypython}@' %{buildroot}%{_bindir}/shiboken_tool.py
%else
rm %{buildroot}%{_datadir}/PySide6/typesystems/*_{mac,win}.xml
%endif
# Install egg-info
# qtpaths is needed
export PATH="%{_qt6_bindir}:$PATH"
%__mypython setup.py egg_info --build-type=%{pyside_flavor}
# fdupes macro does not expand this (!?)
sitearch=%{buildroot}%{mypython_sitearch}
cp -r *.egg-info $sitearch
%fdupes $sitearch

%fdupes -s %{buildroot}%{_libdir}/cmake

%check
# the pyside tests need to know the path to the 'qmake' executable
export PATH=%{_qt6_bindir}:$PATH

# Needed by the shiboken tests
export LD_LIBRARY_PATH=%{buildroot}%{_qt6_libdir}:$LD_LIBRARY_PATH

%if "%{pyside_flavor}" == "shiboken6"
# Since we need CMAKE_SKIP_RPATH to avoid having bogus RUNPATH in the shiboken libraries,
# It needs to know the path to a couple tests folders
for dir in libminimal libother libsample libsmart; do
  export LD_LIBRARY_PATH=$PWD/sources/shiboken6/shiboken6/tests/$dir:$LD_LIBRARY_PATH
done
# 2023-05-30 Only fails on armv7l
%ifarch armv7l armv7hl
%define excluded_tests 1
ctest_exclude_regex="smart_smart_pointer"
%endif
%endif

%if "%{pyside_flavor}" == "pyside6"
%define xvfb_command xvfb-run -s "-screen 0 1600x1200x16 -ac +extension GLX +render -noreset" \\

%define excluded_tests 1
# Excluded tests (last update: 2024-05-27)
# QtWebEngineWidgets_pyside-474-qtwebengineview fails with 'ContextResult::kTransientFailure: Failed to send GpuControl.CreateCommandBuffer'
# QtGui_qpen_test times out
# QtMultimediaWidgets_qmultimediawidgets aborts
# Qt3DExtras_qt3dextras_test fails on s390x (timeout) and randomly everywhere else (exception)
# QtPositioning_positioning fails
# QtWidgets_qwidget_test fails randomly
# pyside6-android-deploy_test_pyside6_android_deploy
# QtCore_qoperatingsystemversion_test fails after https://code.qt.io/cgit/qt/qtbase.git/commit/?id=1214edc
ctest_exclude_regex="QtWebEngineWidgets_pyside-474-qtwebengineview|QtGui_qpen_test|QtMultimediaWidgets_qmultimediawidgets|Qt3DExtras_qt3dextras_test|QtPositioning_positioning|pyside6-deploy_test_pyside6_deploy|QtWidgets_qwidget_test|pyside6-android-deploy_test_pyside6_android_deploy|qoperatingsystemversion"

# registry_existence_test randomly times out and QtWebEngineCore_web_engine_custom_scheme asserts
# QtWebEngineCore_qwebenginecookiestore_test fails with a mesa error ('MESA: error: ZINK: vkCreateInstance failed (VK_ERROR_INCOMPATIBLE_DRIVER)')
%ifarch aarch64
ctest_exclude_regex="$ctest_exclude_regex|registry_existence_test|QtWebEngineCore_web_engine_custom_scheme|QtWebEngineCore_qwebenginecookiestore_test"
%endif
# python311-distro is unavailable in 15.5, skip registry_existence_test
%if 0%{?sle_version} == 150500
ctest_exclude_regex="$ctest_exclude_regex|registry_existence_test"
%endif
%endif

pushd sources/%{pyside_flavor}
%{?xvfb_command}
ctest \
  --output-on-failure \
  --force-new-ctest-process \
  --test-dir %{__qt6_builddir} \
  --parallel %{_smp_build_ncpus} \
  %{?excluded_tests:--exclude-regex "($ctest_exclude_regex)"}
popd

%ldconfig_scriptlets

%files
%license sources/%{pyside_flavor}/COPYING*
%doc doc/changelogs/changes-*
%{_libdir}/lib%{pyside_flavor}.abi3.so.*
%if "%{pyside_flavor}" == "shiboken6"
%{_bindir}/shiboken6
%{_bindir}/shiboken_tool.py
%{mypython_sitearch}/shiboken6/
%{mypython_sitearch}/shiboken6_generator/
%endif
%if "%{pyside_flavor}" == "pyside6"
%{_libdir}/libpyside6qml.abi3.so.*
%dir %{_qt6_pluginsdir}/designer
%{_qt6_pluginsdir}/designer/libPySidePlugin.so
%{mypython_sitearch}/PySide6/
%endif
%{mypython_sitearch}/*.egg-info

%files devel
%if "%{pyside_flavor}" == "shiboken6"
%{_includedir}/shiboken6/
%{_qt6_cmakedir}/Shiboken6/
%{_qt6_cmakedir}/Shiboken6Tools/
%endif
%if "%{pyside_flavor}" == "pyside6"
%{_datadir}/PySide6/
%{_includedir}/PySide6/
%{_libdir}/libpyside6qml.abi3.so
%{_qt6_cmakedir}/PySide6/
%{_qt6_cmakedir}/PySide6Qml/
%endif
%{_libdir}/lib%{pyside_flavor}.abi3.so
%{_libdir}/pkgconfig/%{pyside_flavor}.pc

%changelog
