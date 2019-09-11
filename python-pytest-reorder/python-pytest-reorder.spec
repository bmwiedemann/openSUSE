#
# spec file for package python-pytest-reorder
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
Name:           python-pytest-reorder
Version:        0.1.1
Release:        0
Summary:        Pytest plugin for reordering tests depending on their paths and names
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/not-raspberry/pytest_reorder
Source:         https://github.com/not-raspberry/pytest_reorder/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.8.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module pylama >= 7.0.6}
BuildRequires:  %{python_module pytest >= 2.8.5}
# /SECTION
%python_subpackages

%description
Reorder tests depending on their nodeids (strings of test file path plus test name plus
parametrization, like:
``test/test_prefix_reordering.py::test_reordering_default[test_names5-expected_test_order5]``).

Normally tests are sorted alphabetically. That makes integration tests run before unit tests.

With **pytest_reorder** you can install a hook that will change the order of tests in the suite.
By default **pytest_reorder** will seek for *unit*, *integration* and *ui* tests and put them in
the following order:

  * *unit*
  * all tests with names not indicating unit, integration, nor UI tests
  * *integration*
  * *ui*

The default regular expressions can find unit, integration and UI tests both laid flat and **deeply
nested**. You can also specify your custom order.

%prep
%setup -q -n pytest_reorder-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
