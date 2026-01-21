#
# spec file for package python-pytest-sugar
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
Name:           python-pytest-sugar
Version:        1.1.1
Release:        0
Summary:        Pretty printer for pytest progress
License:        BSD-3-Clause
URL:            https://github.com/Frozenball/pytest-sugar
Source:         https://files.pythonhosted.org/packages/source/p/pytest-sugar/pytest-sugar-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: drop-pytest6-support.patch gh#Teemu/pytest-sugar@05a1e912fd9f
Patch0:         drop-pytest6-support.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module termcolor}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-termcolor
BuildArch:      noarch
%python_subpackages

%description
pytest-sugar is a plugin for py.test that shows failures and errors instantly and shows a progress bar.

%prep
%autosetup -p1 -n pytest-sugar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/pytest_sugar.py
%{python_sitelib}/pytest_sugar-%{version}.dist-info

%changelog
