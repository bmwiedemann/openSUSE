#
# spec file for package python-pytest-mypy-plugins
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
Name:           python-pytest-mypy-plugins
Version:        3.2.0
Release:        0
Summary:        pytest plugin for mypy plugins
License:        MIT
URL:            https://github.com/TypedDjango/pytest-mypy-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mypy-plugins/pytest_mypy_plugins-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mypy >= 1.3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module tomlkit >= 0.11}
# /SECTION
BuildRequires:  fdupes
Requires:       python-decorator
Requires:       python-Jinja2
Requires:       python-jsonschema
Requires:       python-mypy >= 1.3
Requires:       python-packaging
Requires:       python-pytest >= 7.0.0
Requires:       python-PyYAML
Requires:       python-regex
Requires:       python-tomlkit >= 0.11
BuildArch:      noarch
%python_subpackages

%description
pytest plugin for writing tests for mypy plugins

%prep
%autosetup -p1 -n pytest_mypy_plugins-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=%{buildroot}:$PYTHONPATH
%pytest

%files %{python_files}
%{python_sitelib}/pytest_mypy_plugins
%{python_sitelib}/pytest_mypy_plugins-%{version}.dist-info

%changelog
