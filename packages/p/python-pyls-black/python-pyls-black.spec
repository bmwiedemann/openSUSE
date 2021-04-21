#
# spec file for package python-pyls-black
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
Name:           python-pyls-black
Version:        0.4.6
Release:        0
Summary:        Black plugin for the Python Language Server
License:        MIT
URL:            https://github.com/rupert/pyls-black
# GitHub archive instead of PyPI sdist because of test files and LICENSE
Source:         %{url}/archive/v%{version}.tar.gz#/pyls-black-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module black >= 19.3b0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-language-server}
BuildRequires:  %{python_module toml}
# /SECTION
BuildRequires:  fdupes
Requires:       python-black >= 19.3b0
Requires:       python-python-language-server
Requires:       python-toml
BuildArch:      noarch
%python_subpackages

%description
A Black plugin for the Python Language Server

To avoid unexpected results you should make sure yapf and autopep8 are not installed.

- pyls-black can either format an entire file or just the selected text.
- The code will only be formatted if it is syntactically valid Python.
- Text selections are treated as if they were a separate Python file.
  Unfortunately this means you can't format an indented block of code.
- pyls-black will use your project's pyproject.toml if it has one.

%prep
%setup -q -n pyls-black-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyls_black
%{python_sitelib}/pyls_black-%{version}*-info

%changelog
