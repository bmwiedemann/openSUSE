#
# spec file
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

# https://github.com/Nuitka/Nuitka/issues/1856
%define skip_python311 1

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%bcond_with     test_clang
%bcond_with     test_gcc
%define psuffix %{nil}
%else
%define psuffix -%{flavor}
%endif

# QT is not available on several arch
%ifarch %{arm} aarch64 x86_64 %{ix86} ppc64le
%bcond_without  test_qt6
%else
%bcond_with     test_qt6
%endif

# Can't test for substrings server-side, so spell everything out.
# Keep this in sync with the multi-python build set!
%if 0%{suse_version} < 1550

%if "%{flavor}" == "clang-test-py2"
%bcond_without  test_clang
%bcond_with     test_gcc
%define pythons python2
%endif
%if "%{flavor}" == "clang-test-py36"
%bcond_without  test_clang
%bcond_with     test_gcc
%define pythons python3
%endif
%if "%{flavor}" == "clang-test-py38"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "clang-test-py39"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "clang-test-py310"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gcc-test-py2"
%bcond_with     test_clang
%bcond_without  test_gcc
%define pythons python2
%endif
%if "%{flavor}" == "gcc-test-py36"
%bcond_with     test_clang
%bcond_without  test_gcc
%define pythons python3
%endif
%if "%{flavor}" == "gcc-test-py38"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gcc-test-py39"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gcc-test-py310"
ExclusiveArch:  do-not-build
%endif

%else

%if "%{flavor}" == "clang-test-py2"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "clang-test-py36"
ExclusiveArch:  do-not-build
%bcond_without  test_clang
%bcond_with     test_gcc
%define pythons python36
%endif
%if "%{flavor}" == "clang-test-py38"
%bcond_without  test_clang
%bcond_with     test_gcc
%define pythons python38
%endif
%if "%{flavor}" == "clang-test-py39"
%bcond_without  test_clang
%bcond_with     test_gcc
%define pythons python39
%endif
%if "%{flavor}" == "clang-test-py310"
%bcond_without  test_clang
%bcond_with     test_gcc
%define pythons python310
%endif
%if "%{flavor}" == "gcc-test-py2"
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gcc-test-py36"
ExclusiveArch:  do-not-build
%bcond_with     test_clang
%bcond_without  test_gcc
%define pythons python36
%endif
%if "%{flavor}" == "gcc-test-py38"
%bcond_with     test_clang
%bcond_without  test_gcc
%define pythons python38
%endif
%if "%{flavor}" == "gcc-test-py39"
%bcond_with     test_clang
%bcond_without  test_gcc
%define pythons python39
%endif
%if "%{flavor}" == "gcc-test-py310"
%bcond_with     test_clang
%bcond_without  test_gcc
%define pythons python310
%endif

%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Nuitka%{?psuffix}
Version:        1.3.5
Release:        0
Summary:        Python compiler with full language support and CPython compatibility
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://nuitka.net
Source:         https://files.pythonhosted.org/packages/source/N/Nuitka/Nuitka-%{version}.tar.gz
Source1:        nuitka-rpmlintrc
# PATCH-FIX-UPSTREAM no-binary-distribution.patch gh#Nuitka/Nuitka#1702 mcepl@suse.com
# Do not pretend this is binary distribution
Patch0:         no-binary-distribution.patch
BuildRequires:  %{python_module boltons}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  scons
Requires:       gcc-c++
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-atomicwrites
Requires:       python-boltons
Requires:       python-devel
Requires:       scons
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     ccache
Recommends:     chrpath
Recommends:     clang
Recommends:     patchelf
Recommends:     python-tqdm
Recommends:     strace
Suggests:       execstack
Suggests:       gdb
Suggests:       libfuse2
Suggests:       python-glob2
Suggests:       python-zstd
BuildArch:      noarch
# SECTION Testing requirements
%if %{with test_clang}
BuildRequires:  clang
%endif
%if %{with test_gcc} || %{with test_clang}
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module boltons}
BuildRequires:  %{python_module glfw}
BuildRequires:  %{python_module glob2}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module opengl-accelerate}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module pendulum}
BuildRequires:  %{python_module pmw}
BuildRequires:  %{python_module pycairo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module sip4}
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module xml}
BuildRequires:  %{python_module zstd}
BuildRequires:  ccache
BuildRequires:  chrpath
BuildRequires:  distribution-release
BuildRequires:  gdb
BuildRequires:  patchelf
BuildRequires:  strace
BuildRequires:  tk
BuildRequires:  %{python_module gtk if (%python-base with python-base)}
BuildRequires:  %{python_module matplotlib if (%python-base without python36-base)}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module pandas if (%python-base without python36-base)}
%if %{with test_qt6}
%if 0%{?suse_version} > 1500
# Leap doesnt have PySide6, and it has old naming on Tumbleweed
BuildRequires:  python3-pyside6
%endif
%endif
# AppImageKit not available in Factory yet
# https://github.com/Nuitka/Nuitka/issues/992
#BuildRequires:  appimagetool
#BuildRequires:  pkgconfig(fuse)
BuildRequires:  libfuse2
%endif
# /SECTION Testing requirements
%python_subpackages

%description
Python compiler with full language support and CPython compatibility.

This Python compiler achieves full language compatibility and compiles Python
code into compiled objects that are not second class at all. Instead they can be
used in the same way as pure Python objects.

%prep
%autosetup -p1 -n Nuitka-%{version}

# De-vendor
rm -r nuitka/build/inline_copy/appdirs/
rm -r nuitka/build/inline_copy/atomicwrites/
rm -r nuitka/build/inline_copy/jinja2/
rm -r nuitka/build/inline_copy/jinja2_35/
rm -r nuitka/build/inline_copy/markupsafe/  # dep of Jinja2
rm -r nuitka/build/inline_copy/yaml
rm -r nuitka/build/inline_copy/yaml_27/
rm -r nuitka/build/inline_copy/yaml_35/

# SCons has copies here that are automatically excluded, but remove them to be sure
rm -r nuitka/build/inline_copy/lib/scons*/
rm nuitka/build/inline_copy/bin/scons.py

# De-vendor optional dependencies
rm -r nuitka/build/inline_copy/tqdm/
rm -r nuitka/build/inline_copy/zstd/  # 'Onefile' feature

rm -r nuitka/build/inline_copy/glob2/  # Only needed for Python <3.5

# Ensure there are no other inline copies
rm -r nuitka/build/inline_copy/clcache/  # Only needed for Windows
rm -r nuitka/build/inline_copy/colorama/  # Only needed for Windows
rm -r nuitka/build/inline_copy/pkg_resources/  # For ancient Pythons

rmdir nuitka/build/inline_copy/bin/
rmdir nuitka/build/inline_copy/lib/

rmdir nuitka/build/inline_copy/ || (ls nuitka/build/inline_copy/ && exit 1)

# De-vendor backwards compatibility https://github.com/Nuitka/Nuitka/issues/967
# Not working; causes AttributeError: 'str' object has no attribute 'get'
# echo 'from collections import OrderedDict' > nuitka/containers/OrderedDicts.py
# echo 'from boltons.setutils import IndexedSet as OrderedSet' > nuitka/containers/OrderedSetsFallback.py

sed -i '1{/^#!/d}' nuitka/tools/testing/*/__main__.py nuitka/tools/general/dll_report/__main__.py

# Allow these tests to run
# https://github.com/Nuitka/Nuitka/issues/965
sed -Ei 's/(NumpyUsing)/IgnoreThisConditional/' tests/standalone/run_all.py

# https://github.com/Nuitka/Nuitka/issues/1340
rm tests/standalone/PandasUsing.py

# adjust mtime so that deduplicating the cache files after install does not make them inconsistent
find nuitka -name __init__.py -exec touch -m -r nuitka/__init__.py {} ';'

%build
%pyproject_wheel

%if ! %{with test_gcc} && ! %{with test_clang}
%install
%pyproject_install --ignore-installed
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -mnuitka --version
%fdupes %{buildroot}%{$python_sitelib}
}

if [ -f %{buildroot}%{_bindir}/nuitka3 ]; then
  mv %{buildroot}%{_bindir}/nuitka3 %{buildroot}%{_bindir}/nuitka
  mv %{buildroot}%{_bindir}/nuitka3-run %{buildroot}%{_bindir}/nuitka-run
fi

rm -f %{buildroot}%{_bindir}/nuitka2
rm -f %{buildroot}%{_bindir}/nuitka2-run

%python_clone -a %{buildroot}%{_bindir}/nuitka
%python_clone -a %{buildroot}%{_bindir}/nuitka-run

%fdupes %{buildroot}%{_bindir}

# Allow building from source repo tarball
if [ -f doc/nuitka3.1 ]; then
  mkdir -p %{buildroot}%{_mandir}/man1
  gzip -c doc/nuitka3.1 > %{buildroot}%{_mandir}/man1/nuitka.1.gz
  gzip -c doc/nuitka3-run.1 > %{buildroot}%{_mandir}/man1/nuitka-run.1.gz

  %python_clone -a %{buildroot}%{_mandir}/man1/nuitka.1.gz
  %python_clone -a %{buildroot}%{_mandir}/man1/nuitka-run.1.gz
fi
%endif

%check
export CCACHE_DIR=~/.ccache/

export TCL_LIBRARY=%{_libdir}/tcl/tcl8.6
export TK_LIBRARY=%{_libdir}/tcl/tk8.6

# scons is primary python3 only, but used in the tests it needs to find the modules in its "own" flavor. Luckily it is pure...
mkdir my-scons
%if 0%{?sle_version} == 150100
# Leap 15.1 placed scons here
cp -rp %{_libexecdir}/scons-*/ my-scons/
%else
cp -r %{python3_sitelib}/SCons my-scons/
%endif

export PYTHONPATH=$PYTHONPATH:$PWD/my-scons/

mkdir build/testbin
cp -r %{_bindir}/scons* build/testbin/

export SCONS_LIB_DIR=$PWD/my-scons
export PATH=$PWD/build/testbin:$PATH

# Seems run-tests is broken, because it explictly adds numpy plugin, which results in
# +Nuitka-Plugins:WARNING: numpy: This plugin has been deprecated, do not enable it anymore.
sed -i '/if filename == "GlfwUsing.py"/d' tests/standalone/run_all.py
sed -i '/plugin_enable:numpy/d' tests/standalone/run_all.py

# https://github.com/Nuitka/Nuitka/issues/1972
rm tests/standalone/PyQt5*.py

%{python_expand #

%if %{with test_clang}

# clang with debug

# Use `export CC=clang` to force using clang
# which has known failures

# FlaskUsing et al OOM in LLVM on Python 3 with clang
# https://github.com/Nuitka/Nuitka/issues/960
# Also numpy causes the opengl tests to OOM
if [[ "$python" != "python2" ]]; then
  mv tests/standalone/FlaskUsing.py /tmp
  mv tests/standalone/MatplotlibUsing.py /tmp
  mv tests/standalone/OpenGLUsing.py /tmp
  mv tests/standalone/PandasUsing.py /tmp || true
  mv tests/standalone/PendulumUsing.py /tmp
  # NumpyUsing.py can OOM on ppc64 & ppc64le
  mv tests/standalone/NumpyUsing.py /tmp
fi

# OOM (last checked 02-01-2023)
mv tests/standalone/PkgResourcesRequiresUsing.py /tmp

export NUITKA_EXTRA_OPTIONS="--debug"

CC=clang $python ./tests/run-tests --skip-basic-tests --skip-syntax-tests --skip-program-tests --skip-package-tests --skip-plugins-tests --skip-reflection-test --no-other-python

mv /tmp/*Using.py tests/standalone/ ||:
%if 0%{?suse_version} >= 1550
ccache -d ~/.ccache/ --show-stats
ccache -d ~/.ccache/ --clear
%else
ccache --show-stats
ccache --clear
%endif

# VM disk is being exceeded by PandasUsing.
# Trying to find where, if any, disk space is being consumed by each test run
# https://github.com/Nuitka/Nuitka/issues/1053
find tests -name '*.log' -print -delete
rm -r /tmp/* ||:

# clang without debug

# On Leap python2.7 and python3, OpenGL tests fail OOM
if [[ "$python" == "python2" || "$python" == "python3" ]]; then
  mv tests/standalone/OpenGLUsing.py /tmp
fi

# OOM (last checked 02-01-2023)
mv tests/standalone/PkgResourcesRequiresUsing.py /tmp

export NUITKA_EXTRA_OPTIONS=""

CC=clang $python ./tests/run-tests --skip-basic-tests --skip-syntax-tests --skip-program-tests --skip-package-tests --skip-plugins-tests --skip-reflection-test --no-other-python

mv /tmp/*Using.py tests/standalone/ ||:
%if 0%{?suse_version} >= 1550
ccache -d ~/.ccache/ --show-stats
ccache -d ~/.ccache/ --clear
%else
ccache --show-stats
ccache --clear
%endif

find tests -name '*.log' -print -delete
rm -r /tmp/* ||:

%endif
%if %{with test_gcc}
# gcc without debug
# Please add/remove --debug periodically as many bugs
# have been found with/without this flag.

# https://github.com/Nuitka/Nuitka/issues/1338 is a current failure with ``
export NUITKA_EXTRA_OPTIONS="--debug"

# OOM
mv tests/standalone/MatplotlibUsing.py /tmp

CC=gcc $python ./tests/run-tests --no-other-python --skip-reflection-test

mv /tmp/*Using.py tests/standalone/ ||:
%if 0%{?suse_version} >= 1550
ccache -d ~/.ccache/ --show-stats
ccache -d ~/.ccache/ --clear
%else
ccache --show-stats
ccache --clear
%endif

find tests -name '*.log' -print -delete
rm -r /tmp/* ||:

%endif
}

%if ! %{with test_gcc} && ! %{with test_clang}
%post
%python_install_alternative nuitka nuitka-run nuitka.1 nuitka-run.1

%postun
%python_uninstall_alternative nuitka

%files %{python_files}
%doc Changelog.rst README.rst Developer_Manual.rst
%license LICENSE.txt
%{python_sitelib}/nuitka
%{python_sitelib}/Nuitka-%{version}*-info
%python_alternative %{_bindir}/nuitka-run
%python_alternative %{_bindir}/nuitka
%python_alternative %{_mandir}/man1/nuitka.1
%python_alternative %{_mandir}/man1/nuitka-run.1
%endif

%changelog
