#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
%define skip_python310 1
%define plainpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-numba%{psuffix}
Version:        0.54.1
Release:        0
Summary:        NumPy-aware optimizing compiler for Python using LLVM
License:        BSD-2-Clause
URL:            https://numba.pydata.org/
Source:         https://files.pythonhosted.org/packages/source/n/numba/numba-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-max-name-size.patch -- fix for gh#numba/numba#3876 -- from gh#numba/numba#4373
Patch0:         fix-max-name-size.patch
# PATCH-FIX-UPSTREAM support numpy 1.21 -- gh#numba/numba#7176, gh#numba/numba#7483, gh#numpy/numpy#20376
Patch1:         numba-pr7483-numpy1_21.patch
# PATCH-FIX-OPENSUSE skip tests failing due to OBS specifics
Patch3:         skip-failing-tests.patch
BuildRequires:  %{python_module devel >= 3.7 with %python-devel < 3.10}
BuildRequires:  %{python_module numpy-devel >= 1.18 with %python-numpy-devel < 1.22}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  tbb-devel >= 2021
Requires:       python-llvmlite < 0.38
Requires:       python-llvmlite >= 0.37
Requires:       python-scipy >= 0.16
Requires:       (python-numpy >= 1.18 with python-numpy < 1.22)
Requires(post): update-alternatives
Requires(preun):update-alternatives
Recommends:     python-Jinja2
Recommends:     python-Pygments
Recommends:     python-cffi
Recommends:     python-tbb
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module numba >= %{version}}
BuildRequires:  %{python_module numba-devel >= %{version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.16}
BuildRequires:  %{python_module tbb}
%endif
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
Requires:       python-numpy-devel >= 1.11
Requires:       %{plainpython}(abi) = %{python_version}

%description    devel
This package contains files for developing applications using numba.

%prep
%setup -q -n numba-%{version}
%autopatch -p1

# timeouts randomly in OBS
rm numba/tests/test_typedlist.py
# if we reduced the amount of tests too much:
# sed -i -e '/check_testsuite_size/ s/5000/3000/' numba/tests/test_runtests.py
# our setup imports distutils. Not sure why, but should not be a problem.
sed -i -e "/def test_laziness/,/def/ {/'distutils',/ d}" numba/tests/test_import.py

sed -i -e '1{/env python/ d}' numba/misc/appdirs.py

%build
%if !%{with test}
export CFLAGS="%{optflags} -fPIC"
%python_build
%endif

%install
%if !%{with test}
%python_install
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
mv numba numba_temp
export NUMBA_PARALLEL_DIAGNOSTICS=1
%{python_expand # test the installed package
%{_bindir}/numba-%{$python_bin_suffix} -s
$python -m numba.runtests -v -b --exclude-tags='long_running' -m %{_smp_build_ncpus} -- numba.tests
}
mv numba_temp numba
%endif

%if !%{with test}
%post
%{python_install_alternative numba pycc}

%postun
%python_uninstall_alternative numba

%files %{python_files} -f devel-files-exclude-%{python_bin_suffix}.files
%license LICENSE
%doc CHANGE_LOG README.rst
%python_alternative %{_bindir}/numba
%python_alternative %{_bindir}/pycc
%{python_sitearch}/numba/
%{python_sitearch}/numba-%{version}-py*.egg-info

%files %{python_files devel}  -f devel-files-%{python_bin_suffix}.files
%license LICENSE
%endif

%changelog
