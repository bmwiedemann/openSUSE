#
# spec file for package python3-pyside2
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without tests

%global flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == "sle15_python_module"
%{?sle15_python_module_pythons}
%{!?sle15_python_module_pythons:ExclusiveArch: donotbuild}
%{!?sle15_python_module_pythons:BuildRequires: no-build-without-sle15_python_module}
%else
# SLE15: python3.6, Tumbleweed: primary python
%define pythons python3
%endif
%global mypython %pythons
%global __mypython %{expand:%%__%{mypython}}
%global mypython_sitearch %{expand:%%%{mypython}_sitearch}
%global mypython_version_nodots %{expand:%%%{mypython}_version_nodots}
%global mypython_soflags %(%__mypython -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")

# QML imports created and used by examples
%global __requires_exclude qmlimport\\((Charts|TextBalloonPlugin)

Name:           %{mypython}-pyside2
Version:        5.15.12
Release:        0
Summary:        Python bindings for Qt
# Legal:
# Most files are LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
# pyside2-tools is GPL-2.0-only
# shiboken2 contains files under GPL-3.0-only WITH Qt-GPL-exception-1.0
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-2.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://wiki.qt.io/Qt_for_Python
Source0:        https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-opensource-src-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Always-link-to-python-libraries.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Don-t-try-to-install-or-use-uic-rcc-designer-copies.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-cmake-Don-t-assume-qhelpgenerator-is-in-PATH.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Fix-tests-sample_privatector-sample_privatedtor-fail.patch
# PATCH-FIX-UPSTREAM
Patch4:         AsLong.patch
# PATCH-FIX-UPSTREAM, adapted to older codebase
Patch5:         python312.patch
# Provide the PyPI names
Provides:       %{mypython}-PySide2 = %{version}-%{release}
Provides:       %{mypython}-shiboken2 = %{version}-%{release}
Provides:       %{mypython}-shiboken2_generator = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION common_dependencies
%if 0%{?suse_version} > 1500
# boo#1210176 - PYSIDE-2268
BuildRequires:  clang15-devel
BuildRequires:  llvm15-libclang13
#!BuildIgnore:  clang16
#!BuildIgnore:  clang17
%else
%if 0%{?sle_version} >= 150600
# boo#1210176 - PYSIDE-2268, PY-2288
BuildRequires:  clang14-devel
BuildRequires:  llvm14-libclang13
#!BuildIgnore:  clang16
#!BuildIgnore:  clang17
%else
BuildRequires:  clang-devel >= 3.9
%endif
%endif
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-idna
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-urllib3
BuildRequires:  %{mypython}-wheel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  libxslt-devel
BuildRequires:  python-rpm-macros
%if %{with tests}
BuildRequires:  Mesa-dri
BuildRequires:  xvfb-run
%endif
# /SECTION
# SECTION essential_modules
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
# /SECTION
# SECTION optional_modules
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
%ifnarch ppc64 ppc64le s390x
BuildRequires:  cmake(Qt5WebEngineWidgets)
%endif
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
# /SECTION

%description
The PySide2 project provides Python bindings for the Qt
application and UI framework.

%package devel
Summary:        Header Files for PySide2
License:        (GPL-2.0-only AND (GPL-2.0-only OR GPL-3.0-or-later) AND GPL-3.0-only WITH Qt-GPL-exception-1.0) OR LGPL-3.0-only
Requires:       %{name} = %{version}
# can be used to disambiguate multiple providers of cmake(PySide2) and cmake(Shiboken2)
Provides:       pyside2_python_abi(%{mypython_soflags}) = %{version}
%if "%{mypython}" != "python3"
# Can only build for one flavor at a time
Conflicts:      python3-pyside2-devel
%endif

%description devel
Files needed for development with the PySide2 bindings
for Qt.

%package examples
Summary:        Examples for using PySide2
License:        BSD-3-Clause
Requires:       %{name} = %{version}
%if "%{mypython}" != "python3"
Conflicts:      python3-pyside2-examples
%endif
BuildArch:      noarch

%description examples
Examples and Tutorials for the PySide2 bindings for Qt.

%prep
%autosetup -p1 -n pyside-setup-opensource-src-%{version}

%build
_libsuffix=$(echo %{_lib} | cut -b4-)

# NOTE:The compiler and linker flags shall not be defined
%cmake \
  -DLIB_SUFFIX:STRING="${_libsuffix}" \
  -DCMAKE_C_FLAGS:STRING="" \
  -DCMAKE_CXX_FLAGS:STRING="" \
  -DCMAKE_EXE_LINKER_FLAGS:STRING="" \
  -DPYTHON_EXECUTABLE:STRING=%{__mypython} \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON \
%if %{with tests}
  -DBUILD_TESTS:BOOL=ON
%endif

%cmake_build

%install
%cmake_install

%python_clone -a %{buildroot}%{_bindir}/pyside2-lupdate
%python_clone -a %{buildroot}%{_bindir}/pyside_tool.py
%python_clone -a %{buildroot}%{_bindir}/shiboken2

# Broken and conflicts with python3X-pyside6
rm %{buildroot}%{_bindir}/shiboken_tool.py

# No use on linux
rm %{buildroot}%{_datadir}/PySide2/typesystems/*_{mac,win}.xml

# The cmake superproject forgets these
cp -r build/sources/pyside2/PySide2/*.pyi \
      build/sources/pyside2/PySide2/py.typed \
      build/sources/pyside2/PySide2/support \
    %{buildroot}%{mypython_sitearch}/PySide2/
# this is not ideal, but at least we get some python dist metadata
%{__mypython} setup.py dist_info
for d in *.dist-info; do
  # the commands were copied verbatim, not wrapped by entry-points.
  rm -f $d/entry_points.txt
%if %{pkg_vcmp %{mypython}-setuptools < 63}
  cp -r $d %{buildroot}%{mypython_sitearch}/${d/.dist-info/-%{version}.dist-info}
%else
  cp -r $d %{buildroot}%{mypython_sitearch}/${d}
%endif
done

# Examples must be installed manually
cp -R examples %{buildroot}%{_datadir}/PySide2

%fdupes %{buildroot}%{_datadir}/PySide2/examples/
%fdupes %{buildroot}%{_libqt5_libdir}/cmake/
%fdupes %{buildroot}%{mypython_sitearch}

%check
%if %{with tests}
# Set some environment variables
export PATH=%{_libqt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_libqt5_libdir}:$LD_LIBRARY_PATH
export PYTHONPATH=%{buildroot}%{mypython_sitearch}:$PWD/build/sources/pyside2/tests/pysidetest
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
# Leap 15.3: ctest searches the libs before shiboken_paths.py can set the search path (!?)
for binding in $PWD/build/sources/shiboken2/tests/lib*; do
  export LD_LIBRARY_PATH=$binding:$LD_LIBRARY_PATH
done
export LD_LIBRARY_PATH=$PWD/build/sources/pyside2/tests/pysidetest:$LD_LIBRARY_PATH
%endif

%define xvfb_command xvfb-run -s "-screen 0 1600x1200x16 -ac +extension GLX +render -noreset"

# Tests known to fail (listed in build_history/blacklist.txt)
ctest_exclude_regex="QtMultimedia_audio_test"
ctest_exclude_regex="$ctest_exclude_regex|QtQml_javascript_exceptions"
ctest_exclude_regex="$ctest_exclude_regex|QtScriptTools_debugger_test"
ctest_exclude_regex="$ctest_exclude_regex|registry_existence_test"
ctest_exclude_regex="$ctest_exclude_regex|QtWebEngineWidgets_pyside-474-qtwebengineview"
ctest_exclude_regex="$ctest_exclude_regex|QtWebEngineCore_web_engine_custom_scheme"

%if %{mypython_version_nodots} >= 311
# Blacklist broken test with python 3.11
ctest_exclude_regex="$ctest_exclude_regex|signal_enum_test|QtCore_qenum_test"
%endif

%ifarch %{arm}
# bug_307 fails on armv7l only
ctest_exclude_regex="$ctest_exclude_regex|QtWidget_bug_307"
%endif
%ifarch ppc64le s390x
# TODO: investigate/report test failure on PowerPC and s390x
ctest_exclude_regex="$ctest_exclude_regex|QtQml_signal_arguments"
%endif

# Tests are executed from subdirectories. %%ctest can't be used.
%define ctest_command %{shrink:ctest
  --output-on-failure
  --force-new-ctest-process
  --parallel %{_smp_build_ncpus}
  --exclude-regex "($ctest_exclude_regex)"}

pushd build/sources/shiboken2
%{xvfb_command} %{ctest_command}
popd
pushd build/sources/pyside2
%{xvfb_command} %{ctest_command}
popd
%endif

%post
%{?ldconfig}
%python_install_alternative pyside2-lupdate
%python_install_alternative pyside_tool.py
%python_install_alternative shiboken2

%postun
%{?ldconfig}
%python_uninstall_alternative pyside2-lupdate
%python_uninstall_alternative pyside_tool.py
%python_uninstall_alternative shiboken2

%files
%license LICENSE.*
%doc dist/changes*
%python_alternative %{_bindir}/pyside2-lupdate
%python_alternative %{_bindir}/pyside_tool.py
%python_alternative %{_bindir}/shiboken2
%{_libqt5_libdir}/libpyside2.%{mypython_soflags}.so.*
%{_libqt5_libdir}/libshiboken2.%{mypython_soflags}.so.*
%{mypython_sitearch}/PySide2/
%{mypython_sitearch}/PySide2-%{version}.dist-info
%{mypython_sitearch}/shiboken2/
%{mypython_sitearch}/shiboken2-%{version}.dist-info
%{mypython_sitearch}/shiboken2_generator/
%{mypython_sitearch}/shiboken2_generator-%{version}.dist-info

%files devel
%{_datadir}/PySide2/
%{_includedir}/PySide2/
%{_includedir}/shiboken2/
%{_libqt5_libdir}/libpyside2.%{mypython_soflags}.so
%{_libqt5_libdir}/libshiboken2.%{mypython_soflags}.so
%{_libqt5_libdir}/cmake/PySide2-%{version}
%{_libqt5_libdir}/cmake/Shiboken2-%{version}
%{_libqt5_libdir}/pkgconfig/pyside2.pc
%{_libqt5_libdir}/pkgconfig/shiboken2.pc
%{_mandir}/man1/pyside2-lupdate.1%{?ext_man}
%exclude %{_datadir}/PySide2/examples

%files examples
%dir %{_datadir}/PySide2
%{_datadir}/PySide2/examples

%changelog
