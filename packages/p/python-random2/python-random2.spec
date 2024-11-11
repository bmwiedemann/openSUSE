#
# spec file for package python-random2
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-random2
Version:        1.0.2
Release:        0
Summary:        A Session and Caching library with WSGI Middleware
License:        Python-2.0
URL:            https://pypi.python.org/pypi/random2
Source:         https://files.pythonhosted.org/packages/source/r/random2/random2-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package provides a Python 3 ported version of Python 2.7's random module.
It has also been back-ported to work in Python 2.6.

In Python 3, the implementation of randrange() was changed, so that even with
the same seed you get different sequences in Python 2 and 3. Note that several
high-level functions such as randint() and choice() use randrange().

In my testing code I heavily rely on stable random generator results and it
makes porting code to Python 3 a lot harder, if all those tests have to be
adjusted. This package fixes that.

%prep
%autosetup -p1 -n random2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# see tests.test_suite
classes='WichmannHill_TestBasicOps or MersenneTwister_TestBasicOps or TestDistributions or TestModule'
%pytest -k "$classes" src/tests.py

%files %{python_files}
%doc CHANGES.rst README.rst
%{python_sitelib}/random2.py
%pycache_only %{python_sitelib}/__pycache__/random2*
%{python_sitelib}/random2-%{version}.dist-info

%changelog
