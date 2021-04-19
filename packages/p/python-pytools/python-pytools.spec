#
# spec file for package python-pytools
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
%define skip_python2 1
%define skip_python36 1
Name:           python-pytools
Version:        2021.2.3
Release:        0
Summary:        A collection of tools for Python
License:        MIT
URL:            https://pypi.python.org/pypi/pytools
Source0:        https://files.pythonhosted.org/packages/source/p/pytools/pytools-%{version}.tar.gz
BuildRequires:  %{python_module appdirs >= 1.4.0}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module numpy >= 1.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  ( python3-dataclasses >= 0.7 if python3-base <= 3.6 )
BuildRequires:  ( python36-dataclasses >= 0.7 if python36-base )
Requires:       python-appdirs >= 1.4.0
Requires:       python-numpy >= 1.6.0
%if %{python_version_nodots} <= 36
Requires:       python-dataclasses >= 0.7
%endif
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
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
