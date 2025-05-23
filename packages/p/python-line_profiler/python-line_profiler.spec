#
# spec file for package python-line_profiler
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


%{?sle15_python_module_pythons}
Name:           python-line_profiler
Version:        4.2.0
Release:        0
Summary:        Line-by-line profiler
License:        BSD-3-Clause
URL:            https://github.com/pyutils/line_profiler
Source:         https://files.pythonhosted.org/packages/source/l/line_profiler/line_profiler-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ubelt}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
Requires:       python-ipython
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
line_profiler will profile the time individual lines of code take to execute.
The profiler is implemented in C via Cython in order to reduce the overhead of
profiling.

Also included is the script kernprof.py which can be used to conveniently
profile Python applications and scripts either with line_profiler or with the
function-level profiling tools in the Python standard library.

%prep
%autosetup -p1 -n line_profiler-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
# remove shebangs
sed -i '1{/env python/d}' line_profiler/line_profiler.py kernprof.py
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/kernprof
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative kernprof

%postun
%python_uninstall_alternative kernprof

%check
# test_cli needs ubelt, which we don't have and which is needed just for tests
# test_assumed_noop removed upstream, stop skipping it with 4.2.0.
%pytest_arch -k "not (test_cli or test_assumed_noop)" tests

%files %{python_files}
%doc README.rst
%license LICENSE.txt LICENSE_Python.txt
%python_alternative %{_bindir}/kernprof
%{python_sitearch}/line_profiler
%{python_sitearch}/line_profiler-%{version}.dist-info
%{python_sitearch}/kernprof.py
%pycache_only %{python_sitearch}/__pycache__/kernprof.*.pyc

%changelog
