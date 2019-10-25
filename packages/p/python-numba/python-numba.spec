#
# spec file for package python-numba
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-numba
Version:        0.46.0
Release:        0
Summary:        NumPy-aware optimizing compiler for Python using LLVM
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/numba/numba
Source:         https://files.pythonhosted.org/packages/source/n/numba/numba-%{version}.tar.gz
Patch0:         skip-failing-tests.patch
# PATCH-FIX-UPSTREAM fix-max-name-size.patch -- fix for gh#numba/numba#3876 -- from gh#numba/numba#4373
Patch1:         fix-max-name-size.patch
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module llvmlite >= 0.29}
BuildRequires:  %{python_module numpy-devel >= 1.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.16}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-funcsigs
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
BuildRequires:  python2-funcsigs
BuildRequires:  python2-singledispatch
BuildRequires:  python3-tbb
BuildRequires:  tbb-devel
Requires:       python-llvmlite >= 0.29
Requires:       python-numpy >= 1.10
Requires:       python-scipy >= 0.16
Recommends:     python-Jinja2
Recommends:     python-Pygments
Recommends:     python-cffi
Recommends:     python-tbb
Requires(post): update-alternatives
Requires(preun): update-alternatives
%ifpython2
Requires:       python2-enum34
Requires:       python2-funcsigs
Requires:       python2-singledispatch
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
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python-devel
Requires:       python-numpy-devel >= 1.7

%description    devel
This package contains files for developing applications using numba.

%prep
%setup -q -n numba-%{version}
%autopatch -p1
sed -i '1{\@^#!%{_bindir}/env python@d}' numba/appdirs.py

%build
export CFLAGS="%{optflags} -fPIC"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/numba
%python_clone -a %{buildroot}%{_bindir}/pycc

%check
mv numba numba_temp
export NUMBA_PARALLEL_DIAGNOSTICS=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
%{buildroot}%{_bindir}/numba-%{$python_bin_suffix} -s
$python -m numba.runtests -v -b --exclude-tags='long_running' -m %{_smp_build_ncpus} -- numba.tests
}
mv numba_temp numba

%post
%{python_install_alternative numba pycc}

%preun
%python_uninstall_alternative numba

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGE_LOG README.rst
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

%changelog
