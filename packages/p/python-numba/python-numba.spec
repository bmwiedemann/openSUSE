#
# spec file for package python-numba
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


%define plainpython python
# upper bound is exclusive: min-numpy_ver <= numpy < max_numpy_ver
%define min_numpy_ver 1.22
%define max_numpy_ver 2.1

%{?sle15_python_module_pythons}

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
# Supported Platforms: https://numba.pydata.org/numba-doc/dev/user/installing.html#compatibility
ExclusiveArch:  x86_64 %ix86 ppc64le %arm aarch64
%else
%bcond_without test
%define psuffix -%{flavor}
%if "%{flavor}" != "test-py39"
%define skip_python39 1
%endif
%if "%{flavor}" != "test-py310"
%define skip_python310 1
%endif
%if "%{flavor}" != "test-py311"
%define skip_python311 1
%endif
%if "%{flavor}" != "test-py312"
%define skip_python312 1
%endif
# The obs server-side interpreter cannot use lua or rpm shrink
%if "%pythons" == "" || "%pythons" == " " || "%pythons" == "  " || "%pythons" == "   " || "%pythons" == "    " || ( "%pythons" == "python311" && 0%{?skip_python311} )
ExclusiveArch:  donotbuild
%define python_module() %flavor-not-enabled-in-buildset-for-suse-%{?suse_version}
%else
# Tests fail on ppc64 big endian, not resolvable on s390x, wrong types on 32-bit. See also above compatibility list for building
ExcludeArch:    s390x ppc64 %ix86 %arm
%endif
%endif

Name:           python-numba%{?psuffix}
Version:        0.60.0
Release:        0
Summary:        NumPy-aware optimizing compiler for Python using LLVM
License:        BSD-2-Clause
URL:            https://numba.pydata.org/
# SourceRepository: https://github.com/numba/numba
Source:         https://files.pythonhosted.org/packages/source/n/numba/numba-%{version}.tar.gz
# PATCH-FIX-OPENSUSE skip tests failing due to OBS specifics
Patch3:         skip-failing-tests.patch
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module numpy-devel >= %{min_numpy_ver} with %python-numpy-devel < %{max_numpy_ver}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  (tbb-devel >= 2021)
Requires:       (python-llvmlite >= 0.43 with python-llvmlite < 0.44)
Requires:       (python-numpy >= %{min_numpy_ver} with python-numpy < %{max_numpy_ver})
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
Requires:       python-numpy-devel >= %{min_numpy_ver}
Requires:       %{plainpython}(abi) = %{python_version}

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
%python_install_alternative numba

%postun
%python_uninstall_alternative numba

%files %{python_files} -f devel-files-exclude-%{python_bin_suffix}.files
%license LICENSE
%doc CHANGE_LOG README.rst
%python_alternative %{_bindir}/numba
%{python_sitearch}/numba/
%{python_sitearch}/numba-%{version}.dist-info

%files %{python_files devel} -f devel-files-%{python_bin_suffix}.files
%license LICENSE
%endif

%changelog
