#
# spec file for package python-pygments-pytest
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
Name:           python-pygments-pytest
Version:        2.4.0
Release:        0
Summary:        A pygments lexer for pytest output
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source:         https://github.com/asottile/pygments-pytest/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygments-ansi-color >= 0.0.3}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest >= 4.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygments
Requires:       python-pytest >= 4.0.1
BuildArch:      noarch
%python_subpackages

%description
This library provides a pygments lexer called "pytest".

%prep
%setup -q -n pygments-pytest-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/pytest-dev/pygments-pytest/issues/135
%pytest -k 'not test_warnings'

%files %{python_files}
%doc README.md
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/pygments_pytest.py
%{python_sitelib}/pygments_pytest-%{version}.dist-info

%changelog
