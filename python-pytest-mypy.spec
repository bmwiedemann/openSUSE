#
# spec file for package python-pytest-mypy
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
%define         skip_python2 1
Name:           python-pytest-mypy
Version:        0.8.0
Release:        0
Summary:        Mypy static type checker plugin for Pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dbader/pytest-mypy
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mypy/pytest-mypy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 3.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-filelock
Requires:       python-mypy >= 0.500
Requires:       python-pytest >= 2.8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module mypy >= 0.500}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
%python_subpackages

%description
Mypy static type checker plugin for Pytest.

%prep
%setup -q -n pytest-mypy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -s

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
