#
# spec file for package python-memory_profiler
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-memory_profiler
Version:        0.61.0
Release:        0
Summary:        A module for monitoring memory usage of a python program
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pythonprofilers/memory_profiler
Source:         https://files.pythonhosted.org/packages/source/m/memory_profiler/memory_profiler-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-psutil
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module psutil}
# /SECTION
%python_subpackages

%description
This is a python module for monitoring memory consumption of a process
as well as line-by-line analysis of memory consumption for python
programs. It is a pure python module and has the psutil
module as optional (but highly recommended) dependencies.

%prep
%autosetup -p1 -n memory_profiler-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mprof
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%python_exec -m memory_profiler test/test_func.py
%python_exec -m memory_profiler test/test_loop.py
%python_exec -m memory_profiler test/test_as.py
%python_exec -m memory_profiler test/test_global.py
%python_exec -m memory_profiler test/test_precision_command_line.py
%python_exec -m memory_profiler test/test_gen.py
%python_exec -m memory_profiler test/test_unicode.py
%python_exec -m memory_profiler test/test_tracemalloc.py
%python_exec -m memory_profiler test/test_import.py
%python_exec -m memory_profiler test/test_memory_usage.py
%python_exec -m memory_profiler test/test_precision_import.py

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative mprof

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/mprof
%{python_sitelib}/memory_profiler.py
%{python_sitelib}/mprof.py
%{python_sitelib}/memory_profiler-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/memory_profiler*
%pycache_only %{python_sitelib}/__pycache__/mprof*

%changelog
