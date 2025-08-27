#
# spec file for package python-pytest-examples
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
Name:           python-pytest-examples
Version:        0.0.18
Release:        0
Summary:        Pytest plugin for testing examples in docstrings and markdown files
License:        MIT
URL:            https://github.com/pydantic/pytest-examples
Source:         https://files.pythonhosted.org/packages/source/p/pytest-examples/pytest_examples-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pydantic/pytest-examples/pull/65 Bump Ruff to 0.12.9, update regexes for new output rendering
Patch0:         ruff.patch
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruff}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-black
Requires:       python-pytest
Requires:       python-ruff
BuildArch:      noarch
%python_subpackages

%description
Pytest plugin for testing Python code examples in docstrings and markdown files.

`pytest-examples` can:
* lint code examples using `ruff` and `black`
* run code examples
* run code examples and check print statements are inlined correctly in the code

It can also update code examples in place to format them and insert or update print statements.

%prep
%autosetup -p1 -n pytest_examples-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_run_example_ok_fail'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_examples
%{python_sitelib}/pytest_examples-%{version}.dist-info

%changelog
