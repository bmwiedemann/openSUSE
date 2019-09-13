#
# spec file for package python-line_profiler
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
Name:           python-line_profiler
Version:        2.1.2
Release:        0
Summary:        Line-by-line profiler
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rkern/line_profiler
Source:         https://files.pythonhosted.org/packages/source/l/line_profiler/line_profiler-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel >= 3.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
%ifpython3
Requires:       python3-base >= 3.5
%endif
%python_subpackages

%description
line_profiler will profile the time individual lines of code take to execute.
The profiler is implemented in C via Cython in order to reduce the overhead of
profiling.

Also included is the script kernprof.py which can be used to conveniently
profile Python applications and scripts either with line_profiler or with the
function-level profiling tools in the Python standard library.

%prep
%setup -q -n line_profiler-%{version}

%build
# fix wrongly generated cyx files
find . -name '*.pyx' -exec cython {} \;
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/kernprof
%{python_expand chmod a+x %{buildroot}%{$python_sitearch}/*.py
sed -i "s|#!%{_bindir}/env python|#!%__$python|" %{buildroot}%{$python_sitearch}/*.py
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}
%fdupes %{buildroot}%{$python_sitearch}
}

%post
%python_install_alternative kernprof

%postun
%python_uninstall_alternative kernprof

%check
# https://github.com/rkern/line_profiler/issues/128
# %%{python_expand export PYTHONPATH="%%{buildroot}%%{$python_sitearch}"
# py.test-%%{$python_bin_suffix} tests
# }

%files %{python_files}
%doc README.rst
%license LICENSE.txt LICENSE_Python.txt
%python_alternative %{_bindir}/kernprof
%{python_sitearch}/line_profiler-%{version}-py*.egg-info
%{python_sitearch}/kernprof.py*
%{python_sitearch}/line_profiler*.py*
%{python_sitearch}/_line_profiler*.so
%python3_only %{python_sitearch}/line_profiler_py35.py*
%pycache_only %{python_sitearch}/__pycache__/kernprof*.py*
%pycache_only %{python_sitearch}/__pycache__/line_profiler*.py*

%changelog
