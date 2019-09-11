#
# spec file for package python-pytools
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
Name:           python-pytools
Version:        2019.1.1
Release:        0
Summary:        A collection of tools for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/pytools
Source0:        https://files.pythonhosted.org/packages/source/p/pytools/pytools-%{version}.tar.gz
BuildRequires:  %{python_module appdirs} >= 1.4.0
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module decorator} >= 3.2.0
BuildRequires:  %{python_module numpy} >= 1.6.0
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six} >= 1.8.0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pytools is a big bag of things that are "missing" from the Python standard library.
This is mainly a dependency of other software packages (pycuda, pyopencl, etc ),
and is probably of little interest to you unless you use those. If you're curious
nonetheless, here's what's on offer:
* A ton of small tool functions such as len_iterable, argmin, tuple generation,
  permutation generation, ASCII table pretty printing, GvR's mokeypatch_xxx() hack,
  the elusive flatten, and much more.
* Michele Simionato's decorator module
* A time-series logging module, pytools.log.
* Batch job submission, pytools.batchjob.
* A lexer, pytools.lex.

%prep
%setup -q -n pytools-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{python_sitelib}

%check
# The tests are successful when run only with python2.
# When run with python3, the tests require mpi4py and all the
# necessary libraries and configuration that comes with MPI.
python2 setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
