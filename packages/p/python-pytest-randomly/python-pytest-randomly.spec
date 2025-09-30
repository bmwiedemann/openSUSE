#
# spec file for package python-pytest-randomly
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pytest-randomly
Version:        4.0.1
Release:        0
Summary:        Pytest plugin to randomly order tests and control random.seed
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source:         https://github.com/pytest-dev/pytest-randomly/archive/%{version}.tar.gz#/pytest-randomly-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata >= 3.6.0
Requires:       python-pytest
Recommends:     python-Faker >= 13.11.0
Suggests:       python-numpy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Faker >= 13.11.0}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module importlib-metadata >= 3.6.0}
# Django package not available on SLFO:Main
%if 0%{suse_version} > 1600
BuildRequires:  %{python_module model-bakery >= 1.13.0}
%endif
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
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
%autosetup -p1 -n pytest-randomly-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_entrypoint_injection needs installed module for pytest to use
skiptest="test_entrypoint_injection or test_it_runs_before_stepwise"

# Django package not available on SLFO:Main
%if 0%{suse_version} <= 1600
skiptest+=" or test_model_bakery"
%endif

%pytest -k "not ($skiptest)"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_randomly
%{python_sitelib}/pytest_randomly-%{version}*-info

%changelog
