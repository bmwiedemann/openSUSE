#
# spec file for package python3-pyside2
#
# Copyright (c) 2023 SUSE LLC
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

# QML imports created and used by examples
%global __requires_exclude qmlimport\\((Charts|TextBalloonPlugin)

Name:           python3-pyside2
Version:        5.15.8
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
# PATCH-FIX-OPENSUSE
Patch0:         0001-Always-link-to-python-libraries.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Don-t-try-to-install-or-use-uic-rcc-designer-copies.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-cmake-Don-t-assume-qhelpgenerator-is-in-PATH.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Backport-Fix-GLES-builds.patch
# PATCH-FIX-UPSTREAM PYSIDE-1775
Patch4:         0001-Fix-build-with-Python-3.10.patch
# Provide the PyPI names
Provides:       python3-PySide2 = %{version}-%{release}
Provides:       python3-shiboken2 = %{version}-%{release}
Provides:       python3-shiboken2_generator = %{version}-%{release}
# SECTION common_dependencies
BuildRequires:  clang-devel >= 3.9
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  libxslt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-idna
BuildRequires:  python3-setuptools
BuildRequires:  python3-urllib3
BuildRequires:  python3-wheel
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
  -DPYTHON_EXECUTABLE:STRING=python3 \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON \
%if %{with tests}
  -DBUILD_TESTS:BOOL=ON
%endif

%cmake_build

%install
%cmake_install

sed -i 's#env python$#python%{python3_bin_suffix}#' \
  %{buildroot}%{_bindir}/pyside_tool.py

# Broken and conflicts with python3-pyside6
rm %{buildroot}%{_bindir}/shiboken_tool.py

# No use on linux
rm %{buildroot}%{_datadir}/PySide2/typesystems/*_{mac,win}.xml

# The cmake superproject forgets these
cp -r build/sources/pyside2/PySide2/*.pyi \
      build/sources/pyside2/PySide2/py.typed \
      build/sources/pyside2/PySide2/support \
    %{buildroot}%{python3_sitearch}/PySide2/
# this is not ideal, but at least we get some python dist metadata
python3 setup.py dist_info
for d in *.dist-info; do
  # the commands were copied verbatim, not wrapped by entry-points.
  rm -f $d/entry_points.txt
%if %{pkg_vcmp python3-setuptools < 63}
  cp -r $d %{buildroot}%{python3_sitearch}/${d/.dist-info/-%{version}.dist-info}
%else
  cp -r $d %{buildroot}%{python3_sitearch}/${d}
%endif
done

# Examples must be installed manually
cp -R examples %{buildroot}%{_datadir}/PySide2

%fdupes %{buildroot}%{_datadir}/PySide2/examples/
%fdupes %{buildroot}%{_libqt5_libdir}/cmake/
%fdupes %{buildroot}%{python3_sitearch}

%check
%if %{with tests}
# Set some environment variables
export PATH=%{_libqt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_libqt5_libdir}:$LD_LIBRARY_PATH
export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PWD/build/sources/pyside2/tests/pysidetest
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
%ifarch %{arm}
# bug_307 fails on armv7l only
ctest_exclude_regex="$ctest_exclude_regex|QtWidget_bug_307"
%endif
%ifarch ppc64le
# TODO: investigate/report test failure on PowerPC
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.*
%doc dist/changes*
%{_bindir}/pyside2-lupdate
%{_bindir}/pyside_tool.py
%{_bindir}/shiboken2
%{_libqt5_libdir}/libpyside2.%{py3_soflags}.so.*
%{_libqt5_libdir}/libshiboken2.%{py3_soflags}.so.*
%{python3_sitearch}/PySide2/
%{python3_sitearch}/PySide2-%{version}.dist-info
%{python3_sitearch}/shiboken2/
%{python3_sitearch}/shiboken2-%{version}.dist-info
%{python3_sitearch}/shiboken2_generator/
%{python3_sitearch}/shiboken2_generator-%{version}.dist-info

%files devel
%{_datadir}/PySide2/
%{_includedir}/PySide2/
%{_includedir}/shiboken2/
%{_libqt5_libdir}/libpyside2.%{py3_soflags}.so
%{_libqt5_libdir}/libshiboken2.%{py3_soflags}.so
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
