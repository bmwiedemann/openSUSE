#
# spec file for package python-pytest-helpers-namespace
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
Name:           python-pytest-helpers-namespace
Version:        2021.12.29
Release:        0
Summary:        PyTest Helpers Namespace
License:        Apache-2.0
URL:            https://github.com/saltstack/pytest-helpers-namespace
Source:         https://files.pythonhosted.org/packages/source/p/pytest-helpers-namespace/pytest-helpers-namespace-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-declarative-requirements}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyTest Helpers Namespace.

%prep
%setup -q -n pytest-helpers-namespace-%{version}
# Remove versions which cause pypi.org network access
sed -i '/setuptools/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -ra --forked

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/pytest_helpers_namespace
%{python_sitelib}/pytest_helpers_namespace-%{version}.dist-info

%changelog
