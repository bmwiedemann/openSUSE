#
# spec file for package python-pytest-examples
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-pytest-examples
Version:        0.0.10
Release:        0
Summary:        Pytest plugin for testing examples in docstrings and markdown files
License:        MIT
URL:            https://github.com/pydantic/pytest-examples 
# sdist without tests
Source:         https://github.com/pydantic/pytest-examples/archive/refs/tags/v%{version}.tar.gz#/pytest-examples-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruff}
BuildRequires:  %{python_module black}
BuildRequires:  fdupes
Requires:       python-pytest
Requires:       python-ruff
Requires:       python-black
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
%autosetup -p1 -n pytest-examples-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/pytest_examples
%{python_sitelib}/pytest_examples-%{version}.dist-info

%check
%pytest

%changelog
