#
# spec file for package python-greenlet
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2010 B1 Systems GmbH, Vohburg, Germany.
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


# Requires python-furo
%bcond_with docs

%{?sle15_python_module_pythons}
Name:           python-greenlet
Version:        3.3.2
Release:        0
Summary:        Lightweight in-process concurrent programming
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/python-greenlet/greenlet
Source0:        https://files.pythonhosted.org/packages/source/g/greenlet/greenlet-%{version}.tar.gz
Source9:        python-greenlet-rpmlintrc
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module setuptools >= 77.0.3}
BuildRequires:  %{python_module wheel}
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with docs}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-furo
%endif
%python_subpackages

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

%package devel
Summary:        C development headers for python-greenlet
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
This package contains header files required for C modules development.

%prep
%autosetup -p1 -n greenlet-%{version}
sed -i '1{/env python/d}' src/greenlet/tests/test_version.py

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
export CFLAGS="%{optflags} -fno-tree-dominator-opts -fno-strict-aliasing"
%pyproject_wheel

%if %{with docs}
export PYTHONPATH=$PWD/src
cd docs && make html && rm _build/html/.buildinfo
%endif

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CFLAGS="%{optflags} -fno-tree-dominator-opts -fno-strict-aliasing"
# ignore some Flaky tests
export GREENLET_MANYLINUX=1
%pyunittest_arch discover -v greenlet.tests

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%if %{with docs}
%doc docs/_build/html/
%endif
%license LICENSE*
%{python_sitearch}/greenlet
%{python_sitearch}/greenlet-%{version}.dist-info

%files %{python_files devel}
%doc AUTHORS
%license LICENSE*
%{_includedir}/python%{python_version}*/greenlet/

%changelog
