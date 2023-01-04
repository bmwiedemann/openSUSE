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


%define skip_python2 1
# Not compatible with Python 3.11 yet. If this changes, and the python311
# flavor is active, make sure to expand the multibuild test flavors
# https://github.com/numba/numba/issues/8304
%define skip_python311 1
%define plainpython python
# upper bound is exclusive: min-numpy_ver <= numpy < max_numpy_ver
%define min_numpy_ver 1.18
%define max_numpy_ver 1.25

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%bcond_without test
%endif

Name:           python-numba%{?psuffix}
Version:        0.56.4
Release:        0
Summary:        NumPy-aware optimizing compiler for Python using LLVM
License:        BSD-2-Clause
URL:            https://numba.pydata.org/
# SourceRepository: https://github.com/numba/numba
Source:         https://files.pythonhosted.org/packages/source/n/numba/numba-%{version}.tar.gz
# PATCH-FIX-UPSTREAM numba-pr8620-np1.24.patch gh#numba/numba#8620 + raising upper bound in setup.py and numba/__init__.py
Patch1:         numba-pr8620-np1.24.patch
# PATCH-FIX-OPENSUSE skip tests failing due to OBS specifics
Patch3:         skip-failing-tests.patch
# PATCH-FIX-OPENSUSE update-tbb-backend-calls-2021.6.patch, based on gh#numba/numba#7608
Patch4:         update-tbb-backend-calls-2021.6.patch
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= %{min_numpy_ver} with %python-numpy-devel < %{max_numpy_ver}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  (tbb-devel >= 2021)
Requires:       (python-llvmlite >= 0.39 with python-llvmlite < 0.40)
Requires:       (python-numpy >= %{min_numpy_ver} with python-numpy < %{max_numpy_ver})
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-Jinja2
Recommends:     python-Pygments
Recommends:     python-cffi
Recommends:     python-scipy > 1.0
Recommends:     python-tbb
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module numba = %{version}}
BuildRequires:  %{python_module numba-devel = %{version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.0}
BuildRequires:  %{python_module tbb}
%endif
# Tests fail on ppc64 big endian, not resolvable on s390x
# Supported Platforms: https://numba.pydata.org/numba-doc/dev/user/installing.html#compatibility
ExclusiveArch:  x86_64 %ix86 ppc64le %arm aarch64
%python_subpackages

%description
Numba is a NumPy-aware optimizing compiler for Python. It uses the
LLVM compiler infrastructure to compile Python syntax to
machine code.

It is aware of NumPy arrays as typed memory regions and so can speed-up
code using NumPy arrays.  Other, less well-typed code will be translated
to Python C-API calls, effectively removing the "interpreter", but not removing
the dynamic indirection.

Numba is also not a tracing JIT.  It *compiles* your code before it gets
run, either using run-time type information or type information you provide
in the decorator.

Numba is a mechanism for producing machine code from Python syntax and typed
data structures such as those that exist in NumPy.

%package        devel
Summary:        Development files for numba applications
Requires:       %{name} = %{version}
Requires:       python-devel
Requires:       %{plainpython}(abi) = %{python_version}
Requires:       (python-numpy-devel >= %{min_numpy_ver} with python-numpy-devel < %{max_numpy_ver})

%description    devel
This package contains files for developing applications using numba.

%prep
%autosetup -p1 -n numba-%{version}
sed -i -e '1{/env python/ d}' numba/misc/appdirs.py

# random timeouts in OBS
rm numba/tests/test_typedlist.py
# if we reduced the amount of tests too much:
# sed -i -e '/check_testsuite_size/ s/5000/3000/' numba/tests/test_runtests.py

%build
%if !%{with test}
export CFLAGS="%{optflags} -fPIC"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%{python_expand #
%fdupes %{buildroot}%{$python_sitearch}
find %{buildroot}%{$python_sitearch} -name '*.[ch]' > devel-files0-%{$python_bin_suffix}.files
sed 's|^%{buildroot}||' devel-files0-%{$python_bin_suffix}.files > devel-files-%{$python_bin_suffix}.files
sed 's|^%{buildroot}|%%exclude |' devel-files0-%{$python_bin_suffix}.files > devel-files-exclude-%{$python_bin_suffix}.files
}
%python_clone -a %{buildroot}%{_bindir}/numba
%python_clone -a %{buildroot}%{_bindir}/pycc
%endif

%check
%if %{with test}
# test the installed package, not the source without compiled modules
mkdir emptytestdir
pushd emptytestdir
%{python_expand # numbatests: check specific tests with `osc build -M test --define="numbatests <testnames>"`
%{_bindir}/numba-%%{$python_bin_suffix} -s
$python -m numba.runtests -v -b --exclude-tags='long_running' -m %{_smp_build_ncpus} -- %{?!numbatests:numba.tests}%{?numbatests}
}
popd
%endif

%if !%{with test}
%post
%python_install_alternative numba pycc

%postun
%python_uninstall_alternative numba

%files %{python_files} -f devel-files-exclude-%{python_bin_suffix}.files
%license LICENSE
%doc CHANGE_LOG README.rst
%python_alternative %{_bindir}/numba
%python_alternative %{_bindir}/pycc
%{python_sitearch}/numba/
%{python_sitearch}/numba-%{version}.dist-info

%files %{python_files devel} -f devel-files-%{python_bin_suffix}.files
%license LICENSE
%endif

%changelog
