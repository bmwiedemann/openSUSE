#
# spec file for package python-pytest-random-order
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-pytest-random-order
Version:        1.0.4
Release:        0
Summary:        Pytest plugin to randomize the order of pytests
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jbasko/pytest-random-order
Source:         https://files.pythonhosted.org/packages/source/p/pytest-random-order/pytest-random-order-%{version}.tar.gz
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-py
Requires:       python-pytest >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.0.0}
# /SECTION
%python_subpackages

%description
pytest-random-order is a plugin for `pytest <http://pytest.org>`_ that randomises the order in which
tests are run to reveal unwanted coupling between tests. The plugin allows user to control the level
of randomness they want to introduce and to disable reordering on subsets of tests.
Tests can be rerun in a specific order by passing a seed value reported in a previous test run.

%prep
%setup -q -n pytest-random-order-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/random_order
%{python_sitelib}/pytest_random_order-%{version}*-info

%changelog
