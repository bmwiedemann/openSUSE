#
# spec file for package python-memory_profiler
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
Name:           python-memory_profiler
Version:        0.57.0
Release:        0
Summary:        A module for monitoring memory usage of a python program
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pythonprofilers/memory_profiler
Source:         https://files.pythonhosted.org/packages/source/m/memory_profiler/memory_profiler-%{version}.tar.gz
# PATCH-FIX-UPSTREAM revert-5fe38da92673.patch gh#pythonprofilers/memory_profiler#226 mcepl@suse.com
# Revert broken patch, leading to the failure of spyder-memory-profiler
Patch0:         revert-5fe38da92673.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%setup -q -n memory_profiler-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mprof
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod -x %{buildroot}%{$python_sitelib}/memory_profiler-%{version}-py%{$python_bin_suffix}.egg-info/*

%check
export LANG="en_US.UTF8"
%python_exec -m memory_profiler test/test_func.py
%python_exec -m memory_profiler test/test_loop.py
%python_exec -m memory_profiler test/test_as.py
%python_exec -m memory_profiler test/test_global.py
%python_exec -m memory_profiler test/test_precision_command_line.py
%python_exec -m memory_profiler test/test_gen.py
# unicode handling only proper in python3
python3 -m memory_profiler test/test_unicode.py
%python_exec -m memory_profiler test/test_tracemalloc.py
%python_exec -m memory_profiler test/test_import.py
%python_exec -m memory_profiler test/test_memory_usage.py
%python_exec -m memory_profiler test/test_precision_import.py

%post
%python_install_alternative mprof

%postun
%python_uninstall_alternative mprof

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/mprof
%{python_sitelib}/*

%changelog
