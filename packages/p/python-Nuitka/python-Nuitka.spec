#
# spec file for package python-Nuitka
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test_clang
%bcond_without  test_gcc
Name:           python-Nuitka
Version:        0.6.14.4
Release:        0
Summary:        Python compiler with full language support and CPython compatibility
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://nuitka.net
Source:         https://files.pythonhosted.org/packages/source/N/Nuitka/Nuitka-%{version}.tar.gz
Source1:        nuitka-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  scons
Requires:       gcc-c++
Requires:       python-appdirs
Requires:       python-atomicwrites
Requires:       python-boltons
Requires:       python-devel
Requires:       scons
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     ccache
Recommends:     chrpath
Recommends:     clang
Recommends:     python-tqdm
Recommends:     strace
Suggests:       execstack
Suggests:       gdb
Suggests:       libfuse2
BuildArch:      noarch
# SECTION Testing requirements
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module boltons}
BuildRequires:  %{python_module glfw}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module opengl-accelerate}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module passlib}
#BuildRequires: %%{python_module pendulum}
BuildRequires:  %{python_module pycairo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pmw}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module sip4}
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module xml}
BuildRequires:  ccache
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  gdb
BuildRequires:  strace
BuildRequires:  tk
BuildRequires:  (python2-gtk if python2-base)
BuildRequires:  (python2-numpy if python2-base)
BuildRequires:  (python2-pandas if python2-base)
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
# pyside2 has working tests, however it exists on few arch
#BuildRequires:  python3-pyside2
# AppImageKit not available in Factory yet
# https://github.com/Nuitka/Nuitka/issues/992
#BuildRequires:  appimagetool
#BuildRequires:  pkgconfig(fuse)
BuildRequires:  libfuse2
# /SECTION Testing requirements
%python_subpackages

%description
Python compiler with full language support and CPython compatibility.

This Python compiler achieves full language compatibility and compiles Python
code into compiled objects that are not second class at all. Instead they can be
used in the same way as pure Python objects.

%prep
%setup -q -n Nuitka-%{version}
# De-vendor
rm -r nuitka/build/inline_copy/appdirs/
rm -r nuitka/build/inline_copy/atomicwrites/
rm -r nuitka/build/inline_copy/tqdm/
# SCons has copies here that are automatically excluded, but remove them to be sure
rm -r nuitka/build/inline_copy/lib/scons*/
rm nuitka/build/inline_copy/bin/scons.py

# Ensure there are no other inline copies
rm -r nuitka/build/inline_copy/clcache/  # Only needed for Windows
rm -r nuitka/build/inline_copy/colorama/  # Only needed for Windows

rmdir nuitka/build/inline_copy/bin/
rmdir nuitka/build/inline_copy/lib/
rmdir nuitka/build/inline_copy/ || (ls nuitka/build/inline_copy/ && exit 1)

# De-vendor https://github.com/Nuitka/Nuitka/issues/967
echo 'from collections import OrderedDict' > nuitka/containers/odict.py
echo 'from boltons.setutils import IndexedSet as OrderedSet' > nuitka/containers/oset.py

sed -i '1{/^#!/d}' nuitka/tools/testing/*/__main__.py nuitka/tools/general/dll_report/__main__.py

# Allow these tests to run
# https://github.com/Nuitka/Nuitka/issues/965
sed -Ei 's/(Boto3Using|NumpyUsing|PySideUsing)/IgnoreThisConditional/' tests/standalone/run_all.py

# - Boto3Using needs BR boto3, and moto which
#   is not available on many arch, and test fails with
# ModuleNotFoundError: No module named 'moto.s3'
rm tests/standalone/Boto3Using.py

# - NumpyUsing fails
rm tests/standalone/NumpyUsing.py

# Pendulum fails with OOM in pyparsing on most arch, except for s390x,
# with clang, and a new error in 0.6.13:
# https://github.com/Nuitka/Nuitka/issues/1037
rm tests/standalone/PendulumUsing.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mv %{buildroot}%{_bindir}/nuitka3 %{buildroot}%{_bindir}/nuitka
mv %{buildroot}%{_bindir}/nuitka3-run %{buildroot}%{_bindir}/nuitka-run

%python_clone -a %{buildroot}%{_bindir}/nuitka
%python_clone -a %{buildroot}%{_bindir}/nuitka-run

%fdupes %{buildroot}%{_bindir}

# Allow building from source repo tarball
if [ -f doc/nuitka.1 ]; then
  mkdir -p %{buildroot}%{_mandir}/man1
  gzip -c doc/nuitka.1 > %{buildroot}%{_mandir}/man1/nuitka.1.gz
  gzip -c doc/nuitka-run.1 > %{buildroot}%{_mandir}/man1/nuitka-run.1.gz

  %python_clone -a %{buildroot}%{_mandir}/man1/nuitka.1.gz
  %python_clone -a %{buildroot}%{_mandir}/man1/nuitka-run.1.gz
fi

%check
export CCACHE_DIR=~/.ccache/

export TCL_LIBRARY=%{_libdir}/tcl/tcl8.6
export TK_LIBRARY=%{_libdir}/tcl/tk8.6

# Use `export CC=clang` to force using clang
# which has known failures
# https://github.com/Nuitka/Nuitka/issues/960

# Reflection tests are very time consuming and not helpful for smoke tests

%{python_expand #

%if %{with test_clang}

# FlaskUsing OOM in LLVM on Python 3.6 and 3.8 with clang
# https://github.com/Nuitka/Nuitka/issues/960
# Also numpy causes the opengl tests to OOM
mv tests/standalone/FlaskUsing.py /tmp
mv tests/standalone/OpenGLUsing.py /tmp
mv tests/standalone/PandasUsing.py /tmp

# https://github.com/Nuitka/Nuitka/issues/1057
if [[ "$python" == "python3.8" || "$python" == "python3.9" ]]; then
  mv tests/standalone/RsaUsing.py /tmp
fi

# clang with debug

export NUITKA_EXTRA_OPTIONS="--debug"

CC=clang $python ./tests/run-tests --skip-basic-tests --skip-syntax-tests --skip-program-tests --skip-package-tests --skip-plugins-tests --skip-reflection-test --no-other-python

mv /tmp/*Using.py tests/standalone/ ||:
ccache -d ~/.ccache/ --show-stats
ccache -d ~/.ccache/ --clear

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

export NUITKA_EXTRA_OPTIONS=""

CC=clang $python ./tests/run-tests --skip-basic-tests --skip-syntax-tests --skip-program-tests --skip-package-tests --skip-plugins-tests --skip-reflection-test --no-other-python

mv /tmp/*Using.py tests/standalone/ ||:
ccache -d ~/.ccache/ --show-stats
ccache -d ~/.ccache/ --clear

find tests -name '*.log' -print -delete
rm -r /tmp/* ||:

%endif
%if %{with test_gcc}
# gcc with debug

# PandasUsing on ppc64 regularly fails in various modules like
# `scons: *** [module.pandas.io.formats.style.o] Error 1`
mv tests/standalone/PandasUsing.py /tmp

export NUITKA_EXTRA_OPTIONS="--debug"

CC=gcc $python ./tests/run-tests --skip-reflection-test --no-other-python

mv /tmp/*Using.py tests/standalone/ ||:
ccache -d ~/.ccache/ --show-stats
ccache -d ~/.ccache/ --clear

find tests -name '*.log' -print -delete
rm -r /tmp/* ||:

%endif
}

%post
%python_install_alternative nuitka nuitka-run nuitka.1 nuitka-run.1

%postun
%python_uninstall_alternative nuitka

%files %{python_files}
%doc Changelog.rst README.rst Developer_Manual.rst
%license LICENSE.txt
%{python_sitelib}/*
%python_alternative %{_bindir}/nuitka-run
%python_alternative %{_bindir}/nuitka
%python_alternative %{_mandir}/man1/nuitka.1
%python_alternative %{_mandir}/man1/nuitka-run.1

%changelog
