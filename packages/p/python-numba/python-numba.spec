#
# spec file for package python-numba
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-numba%{psuffix}
Version:        0.51.2
Release:        0
Summary:        NumPy-aware optimizing compiler for Python using LLVM
License:        BSD-2-Clause
URL:            https://github.com/numba/numba
Source:         https://files.pythonhosted.org/packages/source/n/numba/numba-%{version}.tar.gz
Patch0:         skip-failing-tests.patch
# PATCH-FIX-UPSTREAM fix-max-name-size.patch -- fix for gh#numba/numba#3876 -- from gh#numba/numba#4373
Patch1:         fix-max-name-size.patch
Patch2:         unpin-llvmlite.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.15}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  tbb-devel
Requires:       python-llvmlite >= 0.33
Requires:       python-numpy >= 1.15
Requires:       python-scipy >= 0.16
Requires(post): update-alternatives
Requires(preun): update-alternatives
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
BuildRequires:  %{python_module llvmlite >= 0.33}
BuildRequires:  %{python_module numba >= %{version}}
BuildRequires:  %{python_module numba-devel >= %{version}}
BuildRequires:  %{python_module pip}
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

%description    devel
This package contains files for developing applications using numba.

%prep
%setup -q -n numba-%{version}
%autopatch -p1

# due to new numpy version tests now fail
# Remove this with version update! (>0.48.0)
# https://github.com/numba/numba/issues/5251
rm numba/tests/test_np_functions.py
rm numba/tests/test_ufuncs.py
rm numba/tests/test_array_manipulation.py
rm numba/tests/test_array_reductions.py
# https://github.com/numba/numba/issues/5179
rm numba/tests/test_hashing.py
# timeouts randomly in OBS
rm numba/tests/test_typedlist.py
# as we reduced the amount of tests:
sed -i -e 's:5000:3000:' numba/tests/test_runtests.py

%build
export CFLAGS="%{optflags} -fPIC"
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/numba
%python_clone -a %{buildroot}%{_bindir}/pycc
%endif

%check
%if %{with test}
mv numba numba_temp
export NUMBA_PARALLEL_DIAGNOSTICS=1
%{python_expand export PYTHONPATH=%{$python_sitearch}
%{_bindir}/numba-%{$python_bin_suffix} -s
$python -m numba.runtests -v -b --exclude-tags='long_running' -m %{_smp_build_ncpus} -- numba.tests
}
mv numba_temp numba
%endif

%if !%{with test}
%post
%{python_install_alternative numba pycc}

%preun
%python_uninstall_alternative numba

%files %{python_files}
%license LICENSE
%doc CHANGE_LOG README.rst
%python_alternative %{_bindir}/numba
%python_alternative %{_bindir}/pycc
%{python_sitearch}/numba/
%{python_sitearch}/numba-%{version}-py*.egg-info
%exclude %{python_sitearch}/numba/*.c
%exclude %{python_sitearch}/numba/*.h
%exclude %{python_sitearch}/numba/*/*.c
%exclude %{python_sitearch}/numba/*/*.h

%files %{python_files devel}
%{python_sitearch}/numba/*.c
%{python_sitearch}/numba/*.h
%{python_sitearch}/numba/*/*.c
%{python_sitearch}/numba/*/*.h
%endif

%changelog
