#
# spec file for package python-pytest-lazy-fixture
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-pytest-lazy-fixture
Version:        0.6.3
Release:        0
Summary:        Helper to use fixtures in pytest.markparametrize
License:        MIT
URL:            https://github.com/tvorog/pytest-lazy-fixture
Source:         https://files.pythonhosted.org/packages/source/p/pytest-lazy-fixture/pytest-lazy-fixture-%{version}.tar.gz
# PATCH-FIX-UPSTREAM (ish) Sourced from gh#TvoroG/pytest-lazy-fixture/issues/65
Patch0:         support-pytest-8.patch
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 8.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 8.0
BuildArch:      noarch
%python_subpackages

%description
Helper to use fixtures in pytest.mark.parametrize.

%prep
%autosetup -p1 -n pytest-lazy-fixture-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_lazyfixture.py
%pycache_only %{python_sitelib}/__pycache__/pytest_lazyfixture*.pyc
%{python_sitelib}/pytest_lazy_fixture-%{version}.dist-info

%changelog
