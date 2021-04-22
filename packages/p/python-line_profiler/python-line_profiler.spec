#
# spec file for package python-line_profiler
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
Name:           python-line_profiler
Version:        3.1.0
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
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
Requires:       python-jupyter_ipython
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/line_profiler/*.py
sed -i "s|#!%{_bindir}/env python|#!%__$python|" %{buildroot}%{$python_sitelib}/line_profiler/*.py
$python -m compileall -d %{$python_sitelib}/line_profiler %{buildroot}%{$python_sitelib}/line_profiler
$python -O -m compileall -d %{$python_sitelib}/line_profiler %{buildroot}%{$python_sitelib}/line_profiler
rm -rf %{buildroot}%{$python_sitelib}/line_profiler/__pycache__
%fdupes %{buildroot}%{$python_sitelib}
}

%post
%python_install_alternative kernprof

%postun
%python_uninstall_alternative kernprof

%check
# test_cli needs ubelt, which we don't have and which is needed just for tests
%pytest -k "not test_cli" tests

%files %{python_files}
%doc README.rst
%license LICENSE.txt LICENSE_Python.txt
%python_alternative %{_bindir}/kernprof
%dir %{python_sitelib}/line_profiler
%{python_sitelib}/line_profiler-%{version}-py*.egg-info
%{python_sitelib}/kernprof.py*
%{python_sitelib}/line_profiler/*.py*
%{python_sitelib}/line_profiler/_line_profiler*.so

%changelog
