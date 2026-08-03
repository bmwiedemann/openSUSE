#
# spec file for package python-pytest-test-groups
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-pytest-test-groups
Version:        1.2.1
Release:        0
Summary:        Pytest plugin to split your tests into equally sized groups
License:        MIT
URL:            https://github.com/mark-adams/pytest-test-groups
Source:         https://files.pythonhosted.org/packages/source/p/pytest-test-groups/pytest_test_groups-1.2.1.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 75}
BuildRequires:  %{python_module setuptools_scm >= 8}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 7.0.0
BuildArch:      noarch
%python_subpackages

%description
A Pytest plugin for running a subset of your tests by splitting them in to equally sized groups.

%prep
%autosetup -p1 -n pytest_test_groups-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_test_groups
%{python_sitelib}/pytest_test_groups-%{version}.dist-info

%changelog
