#
# spec file for package python-pytest-dependency
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-pytest-dependency
Version:        0.6.0
Release:        0
Summary:        Manage dependencies of tests
License:        Apache-2.0
URL:            https://github.com/RKrahl/pytest-dependency
Source:         https://files.pythonhosted.org/packages/source/p/pytest-dependency/pytest-dependency-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.6.0
BuildArch:      noarch
%python_subpackages

%description
This pytest plugin manages dependencies of tests.  It allows to mark
some tests as dependent from other tests.  These tests will then be
skipped if any of the dependencies did fail or has been skipped.

%prep
%setup -q -n pytest-dependency-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/pytest_dependency.py
%pycache_only %{python_sitelib}/__pycache__/pytest_dependency*.pyc
%{python_sitelib}/pytest_dependency-%{version}.dist-info

%changelog
