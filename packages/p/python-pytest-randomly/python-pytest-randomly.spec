#
# spec file for package python-pytest-randomly
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


%{?!python_module:%define python_module() python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-pytest-randomly
Version:        3.7.0
Release:        0
Summary:        Pytest plugin to randomly order tests and control random.seed
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source:         https://github.com/pytest-dev/pytest-randomly/archive/%{version}.tar.gz#/pytest-randomly-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata >= 3.6.0
Requires:       python-pytest
Recommends:     python-Faker >= 4.1.0
Suggests:       python-numpy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Faker >= 4.1.0}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module importlib-metadata >= 3.6.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
# /SECTION
%python_subpackages

%description
Pytest plugin to randomly order tests and control random.seed.

Features:
   * Randomly shuffles the order of test items. This is done first at
     the level of modules, then at the level of test classes (if you
     have them), then at the order of functions. This also works with
     things like doctests.
   * Resets random.seed() at the start of every test case and test to
     fixed number - this defaults to time.time() from the start of
     your test run, but you can pass in --randomly-seed to repeat a
     randomness-induced failure.
   * If factory boy is installed, its random state is reset at the
     start of every test. This allows for repeatable use of its random
     'fuzzy' features.
   * If faker is installed, its random state is reset at the start of
     every test. This is also for repeatable fuzzy data in tests.
   * If numpy is installed, its random state is reset at the start of
     every test.

%prep
%setup -q -n pytest-randomly-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_entrypoint_injection needs installed module for pytest to use
donttest="test_entrypoint_injection"
# no python36-numpy
python36_donttest="or test_numpy"
%pytest -k "not ($donttest ${$python_donttest})"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_randomly.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_randomly*.pyc
%{python_sitelib}/pytest_randomly-%{version}*-info

%changelog
