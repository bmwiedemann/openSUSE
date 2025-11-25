#
# spec file for package python3-pyside6
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%define tar_version 6.10.1

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
Version:        6.10.1
Release:        0
Summary:        Python bindings for Qt 6
License:        (GPL-2.0-only AND (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-3.0-only WITH Qt-GPL-exception-1.0) OR LGPL-3.0-only
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-%{version}-src/%{tar_name}-%{tar_version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Always-link-to-python-libraries.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Revert-Modify-headers-installation-for-CMake-builds.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-installation.patch
# SECTION common_dependencies
BuildRequires:  clang-devel
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{mypython}-devel >= 3.10
BuildRequires:  %{mypython}-numpy-devel
BuildRequires:  %{mypython}-setuptools
BuildRequires:  fdupes
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core) >= %{version}
BuildRequires:  cmake(Qt6CorePrivate) >= %{version}
BuildRequires:  cmake(Qt6Test) >= %{version}
BuildRequires:  cmake(Qt6TestPrivate) >= %{version}
BuildRequires:  cmake(Qt6Xml) >= %{version}
BuildRequires:  cmake(Qt6XmlPrivate) >= %{version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
# /SECTION
%if "%{pyside_flavor}" == "pyside6"
# For the registry_existence test
BuildRequires:  %{mypython}-distro
BuildRequires:  %{mypython}-shiboken6-devel = %{version}
# SECTION test_dependencies
BuildRequires:  Mesa-dri
BuildRequires:  qt6-location
BuildRequires:  qt6-sql-sqlite
BuildRequires:  xvfb-run
# /SECTION
# SECTION essential_modules
BuildRequires:  cmake(Qt6Concurrent) >= %{version}
BuildRequires:  cmake(Qt6ExampleIconsPrivate) >= %{version}
BuildRequires:  cmake(Qt6Gui) >= %{version}
BuildRequires:  cmake(Qt6GuiPrivate) >= %{version}
BuildRequires:  cmake(Qt6Network) >= %{version}
BuildRequires:  cmake(Qt6NetworkPrivate) >= %{version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{version}
BuildRequires:  cmake(Qt6PrintSupportPrivate) >= %{version}
BuildRequires:  cmake(Qt6Sql) >= %{version}
BuildRequires:  cmake(Qt6SqlPrivate) >= %{version}
BuildRequires:  cmake(Qt6Widgets) >= %{version}
BuildRequires:  cmake(Qt6WidgetsPrivate) >= %{version}
# /SECTION
# SECTION optional_modules
BuildRequires:  cmake(Qt63DAnimation) >= %{version}
BuildRequires:  cmake(Qt63DAnimationPrivate) >= %{version}
BuildRequires:  cmake(Qt63DCore) >= %{version}
BuildRequires:  cmake(Qt63DCorePrivate) >= %{version}
BuildRequires:  cmake(Qt63DExtras) >= %{version}
BuildRequires:  cmake(Qt63DExtrasPrivate) >= %{version}
BuildRequires:  cmake(Qt63DInput) >= %{version}
BuildRequires:  cmake(Qt63DInputPrivate) >= %{version}
BuildRequires:  cmake(Qt63DLogic) >= %{version}
BuildRequires:  cmake(Qt63DLogicPrivate) >= %{version}
BuildRequires:  cmake(Qt63DRender) >= %{version}
BuildRequires:  cmake(Qt63DRenderPrivate) >= %{version}
BuildRequires:  cmake(Qt6Bluetooth) >= %{version}
BuildRequires:  cmake(Qt6BluetoothPrivate) >= %{version}
BuildRequires:  cmake(Qt6Charts) >= %{version}
BuildRequires:  cmake(Qt6ChartsPrivate) >= %{version}
BuildRequires:  cmake(Qt6DBus) >= %{version}
BuildRequires:  cmake(Qt6DBusPrivate) >= %{version}
BuildRequires:  cmake(Qt6DataVisualization) >= %{version}
BuildRequires:  cmake(Qt6DataVisualizationPrivate) >= %{version}
BuildRequires:  cmake(Qt6Designer) >= %{version}
BuildRequires:  cmake(Qt6DesignerPrivate) >= %{version}
BuildRequires:  cmake(Qt6Graphs) >= %{version}
BuildRequires:  cmake(Qt6GraphsPrivate) >= %{version}
BuildRequires:  cmake(Qt6GraphsWidgets) >= %{version}
BuildRequires:  cmake(Qt6GraphsWidgetsPrivate) >= %{version}
BuildRequires:  cmake(Qt6Help) >= %{version}
BuildRequires:  cmake(Qt6HelpPrivate) >= %{version}
BuildRequires:  cmake(Qt6HttpServer) >= %{version}
BuildRequires:  cmake(Qt6HttpServerPrivate) >= %{version}
BuildRequires:  cmake(Qt6Location) >= %{version}
BuildRequires:  cmake(Qt6LocationPrivate) >= %{version}
BuildRequires:  cmake(Qt6Multimedia) >= %{version}
BuildRequires:  cmake(Qt6MultimediaPrivate) >= %{version}
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{version}
BuildRequires:  cmake(Qt6MultimediaWidgetsPrivate) >= %{version}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{version}
BuildRequires:  cmake(Qt6NetworkAuthPrivate) >= %{version}
BuildRequires:  cmake(Qt6Nfc) >= %{version}
BuildRequires:  cmake(Qt6NfcPrivate) >= %{version}
BuildRequires:  cmake(Qt6OpenGL) >= %{version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{version}
BuildRequires:  cmake(Qt6Positioning) >= %{version}
BuildRequires:  cmake(Qt6PositioningPrivate) >= %{version}
BuildRequires:  cmake(Qt6Qml) >= %{version}
BuildRequires:  cmake(Qt6QmlPrivate) >= %{version}
BuildRequires:  cmake(Qt6Quick) >= %{version}
BuildRequires:  cmake(Qt6Quick3D) >= %{version}
BuildRequires:  cmake(Qt6Quick3DPrivate) >= %{version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{version}
BuildRequires:  cmake(Qt6QuickControls2Private) >= %{version}
BuildRequires:  cmake(Qt6QuickPrivate) >= %{version}
BuildRequires:  cmake(Qt6QuickTest) >= %{version}
BuildRequires:  cmake(Qt6QuickTestPrivate) >= %{version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{version}
BuildRequires:  cmake(Qt6QuickWidgetsPrivate) >= %{version}
BuildRequires:  cmake(Qt6RemoteObjects) >= %{version}
BuildRequires:  cmake(Qt6RemoteObjectsPrivate) >= %{version}
BuildRequires:  cmake(Qt6RepParser) >= %{version}
BuildRequires:  cmake(Qt6Scxml) >= %{version}
BuildRequires:  cmake(Qt6ScxmlPrivate) >= %{version}
BuildRequires:  cmake(Qt6Sensors) >= %{version}
BuildRequires:  cmake(Qt6SensorsPrivate) >= %{version}
BuildRequires:  cmake(Qt6SerialBus) >= %{version}
BuildRequires:  cmake(Qt6SerialBusPrivate) >= %{version}
BuildRequires:  cmake(Qt6SerialPort) >= %{version}
BuildRequires:  cmake(Qt6SerialPortPrivate) >= %{version}
BuildRequires:  cmake(Qt6SpatialAudio) >= %{version}
BuildRequires:  cmake(Qt6SpatialAudioPrivate) >= %{version}
BuildRequires:  cmake(Qt6StateMachine) >= %{version}
BuildRequires:  cmake(Qt6StateMachinePrivate) >= %{version}
BuildRequires:  cmake(Qt6Svg) >= %{version}
BuildRequires:  cmake(Qt6SvgPrivate) >= %{version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{version}
BuildRequires:  cmake(Qt6TextToSpeechPrivate) >= %{version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{version}
BuildRequires:  cmake(Qt6UiTools) >= %{version}
BuildRequires:  cmake(Qt6UiToolsPrivate) >= %{version}
BuildRequires:  cmake(Qt6WebChannel) >= %{version}
BuildRequires:  cmake(Qt6WebChannelPrivate) >= %{version}
%ifarch x86_64 %{x86_64} aarch64 riscv64
BuildRequires:  cmake(Qt6Pdf) >= %{version}
BuildRequires:  cmake(Qt6PdfPrivate) >= %{version}
BuildRequires:  cmake(Qt6PdfWidgets) >= %{version}
BuildRequires:  cmake(Qt6PdfWidgetsPrivate) >= %{version}
BuildRequires:  cmake(Qt6WebEngineCore) >= %{version}
BuildRequires:  cmake(Qt6WebEngineCorePrivate) >= %{version}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{version}
BuildRequires:  cmake(Qt6WebEngineQuickPrivate) >= %{version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{version}
BuildRequires:  cmake(Qt6WebEngineWidgetsPrivate) >= %{version}
BuildRequires:  cmake(Qt6WebView) >= %{version}
BuildRequires:  cmake(Qt6WebViewPrivate) >= %{version}
BuildRequires:  cmake(Qt6WebViewQuick) >= %{version}
BuildRequires:  cmake(Qt6WebViewQuickPrivate) >= %{version}
%endif
BuildRequires:  cmake(Qt6WebSockets) >= %{version}
BuildRequires:  cmake(Qt6WebSocketsPrivate) >= %{version}
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
%if "%{pyside_flavor}" == "shiboken6"
# Shiboken runs llvm-config to find Clang's built-in include directory
Requires:       llvm%{_llvm_sonum}-devel
%endif
%if 0%{?suse_version} > 1500
Provides:       python3-%{pyside_flavor}-devel = %{version}-%{release}
Obsoletes:      python3-%{pyside_flavor}-devel < %{version}-%{release}
%endif

%description devel
Python bindings for the Qt cross-platform application and UI framework

%prep
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

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

# numpy changed the include path on 2.0
numpyinc=$(%{__mypython} -c 'import numpy; print(numpy.get_include())')

# NOTE:The compiler and linker flags shall not be defined
%cmake_qt6 \
  -DBUILD_TESTS:BOOL=ON \
  -DLIB_SUFFIX:STRING="${_libsuffix}" \
  -DCMAKE_C_FLAGS:STRING="" \
  -DCMAKE_CXX_FLAGS:STRING="" \
  -DCMAKE_EXE_LINKER_FLAGS:STRING="" \
  -DPython_EXECUTABLE:STRING=%{__mypython} \
  -DNUMPY_INCLUDE_DIR:STRING=${numpyinc} \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON \
%if "%{pyside_flavor}" == "shiboken6"
  -DCMAKE_SKIP_RPATH:BOOL=ON \
%endif
  -DQFP_NO_STRIP:BOOL=ON \
  -DCTEST_TESTING_TIMEOUT=120 \
  %{nil}

%{qt6_build}

popd

%install
pushd sources/%{pyside_flavor}
%{qt6_install}
popd

%if "%{pyside_flavor}" == "shiboken6"
sed -i 's@^#.*env python.*$@#!%{__mypython}@' %{buildroot}%{_bindir}/shiboken_tool.py

# Delete weird copies
rm -r %{buildroot}%{_prefix}/shiboken6

# and fix broken library location
sed -i 's#/shiboken6/libshiboken6#/%{_lib}/libshiboken6#' %{buildroot}%{_qt6_cmakedir}/Shiboken6/Shiboken6Targets-*.cmake

%else
rm %{buildroot}%{_datadir}/PySide6/typesystems/*_{mac,win}.xml

# Also fix pyside manually
mv %{buildroot}%{_prefix}/PySide6/* %{buildroot}%{_libdir}
%define rel_sitearch %(printf %{mypython_sitearch} | sed 's#%{_prefix}/##')
sed -i 's#PYSIDE_PYTHONPATH "\${PACKAGE_PREFIX_DIR}/#PYSIDE_PYTHONPATH "\${PACKAGE_PREFIX_DIR}/%{rel_sitearch}/PySide6/#' %{buildroot}%{_qt6_cmakedir}/PySide6/PySide6Config*.cmake
sed -i 's#/PySide6/libpyside6#/%{_lib}/libpyside6#' %{buildroot}%{_qt6_cmakedir}/*/*.cmake
sed -i 's#/typesystems#/share/PySide6/typesystems#' %{buildroot}%{_qt6_cmakedir}/PySide6/*.cmake
sed -i 's#/glue#/share/PySide6/glue#' %{buildroot}%{_qt6_cmakedir}/PySide6/*.cmake

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
# 2025-03-18 Fails on armv7l and ppc64le
%ifarch armv7l armv7hl ppc64le
%define excluded_tests 1
ctest_exclude_regex="smart_smart_pointer"
%endif
%endif

%if "%{pyside_flavor}" == "pyside6"
%define xvfb_command xvfb-run -s "-screen 0 1600x1200x16 -ac +extension GLX +render -noreset" \\

%define excluded_tests 1
# Excluded tests (last update: 2025-05-07)
# QtWebEngineWidgets_pyside-474-qtwebengineview fails with 'ContextResult::kTransientFailure: Failed to send GpuControl.CreateCommandBuffer'
# QtGui_qpen_test times out
# QtMultimediaWidgets_qmultimediawidgets aborts
# Qt3DExtras_qt3dextras_test fails on s390x (timeout) and randomly everywhere else (exception)
# QtPositioning_positioning fails
# QtWidgets_qwidget_test fails randomly
# pyside6-android-deploy_test_pyside6_android_deploy
# QtCore_qoperatingsystemversion_test fails after https://code.qt.io/cgit/qt/qtbase.git/commit/?id=1214edc
# cpp_interop_cpp_interop_test is flaky
ctest_exclude_regex="QtWebEngineWidgets_pyside-474-qtwebengineview|QtGui_qpen_test|QtMultimediaWidgets_qmultimediawidgets|Qt3DExtras_qt3dextras_test|QtPositioning_positioning|pyside6-deploy_test_pyside6_deploy|QtWidgets_qwidget_test|pyside6-android-deploy_test_pyside6_android_deploy|qoperatingsystemversion|cpp_interop_cpp_interop_test"

# QtWebEngineCore_web_engine_custom_scheme asserts
# QtWebEngineCore_qwebenginecookiestore_test, pysidetest_new_inherited_functions_test fail with a mesa error ('MESA: error: ZINK: vkCreateInstance failed (VK_ERROR_INCOMPATIBLE_DRIVER)')
# QtWidgets_bug_668, QtWidgets_bug_728 segfault
%ifarch aarch64
ctest_exclude_regex="$ctest_exclude_regex|QtWebEngineCore_web_engine_custom_scheme|QtWebEngineCore_qwebenginecookiestore_test|pysidetest_new_inherited_functions_test|QtWidgets_bug_668|QtWidgets_bug_728"
%endif
# QtWebEngineCore_web_engine_custom_scheme is flaky
# QtQml_qquickitem_grabToImage fails for unknown reasons
%ifarch riscv64
ctest_exclude_regex+="|QtWebEngineCore_web_engine_custom_scheme|QtQml_qquickitem_grabToImage"
%endif
%ifarch ppc64le
# Tests started segfaulting after an unknown change that happened ~ april 10
ctest_exclude_regex+="|QtQml_bug_825_old|QtQml_bug_825|QtQml_bug_847|QtQml_qqmlnetwork_test|QtQml_registertype|QtQml_registersingletontype|QtQml_qqmlincubator_incubateWhile|QtQml_qquickitem_grabToImage|quicktestmainwithsetup_tst_quicktestmainwithsetup|QtDataVisualization_datavisualization_test"
%endif
%ifarch x86_64 riscv64
# QtWebengine failures caused by fixes for AMD graphics (cf. sr#1274939)
ctest_exclude_regex+="|QtWebEngineCore_web_engine_custom_scheme|QtWebEngineCore_qwebenginecookiestore_test"
%endif

# qemu linux-user emulation is always multi-threaded, sandbox refuses to start
%if 0%{?qemu_user_space_build}
ctest_exclude_regex+="|QtWebEngineCore_web_engine_custom_scheme|QtWebEngineCore_qwebenginecookiestore_test|QtWebEngineWidgets_pyside-474-qtwebengineview"
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
# This library is used to interpret .rep files from Python
# it is intentionally static (also see https://bugreports.qt.io/browse/PYSIDE-862)
%{_libdir}/libpyside6remoteobjects.a
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
%endif
%{_libdir}/lib%{pyside_flavor}.abi3.so
%{_libdir}/pkgconfig/%{pyside_flavor}.pc

%changelog
