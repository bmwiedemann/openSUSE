#
# spec file for package python-pytest-mypy
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
Name:           python-pytest-mypy
Version:        1.0.1
Release:        0
Summary:        Mypy static type checker plugin for Pytest
License:        MIT
URL:            https://github.com/realpython/pytest-mypy
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mypy/pytest_mypy-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 3.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.0
Requires:       python-filelock >= 3.0
Requires:       python-mypy >= 1.0
Requires:       python-pytest >= 7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.0}
BuildRequires:  %{python_module filelock >= 3.0}
BuildRequires:  %{python_module mypy >= 1.0}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-xdist}

# /SECTION
%python_subpackages

%description
Mypy static type checker plugin for Pytest.

%prep
%autosetup -p1 -n pytest_mypy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# encoding_warnings: 3 unexpected extra warnings
# test_looponfail: timeout error
%pytest -k 'not (test_mypy_encoding_warnings or test_looponfail)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_mypy
%{python_sitelib}/pytest[-_]mypy-%{version}.dist-info

%changelog
