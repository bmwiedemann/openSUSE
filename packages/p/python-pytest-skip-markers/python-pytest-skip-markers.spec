#
# spec file for package python-pytest-skip-markers
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
Name:           python-pytest-skip-markers
Version:        1.5.2
Release:        0
Summary:        Pytest plugin for conditionally skipping tests
License:        Apache-2.0
URL:            https://github.com/saltstack/pytest-skip-markers
Source:         https://files.pythonhosted.org/packages/source/p/pytest-skip-markers/pytest_skip_markers-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 50.3.2}
BuildRequires:  %{python_module setuptools-declarative-requirements}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest >= 6.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 19.2.0
Requires:       python-distro
Requires:       python-pytest >= 6.0.0
BuildArch:      noarch
%python_subpackages

%description
It’s a collection of of useful skip markers created to simplify and reduce code
required to skip tests in some common scenarios, for example, platform specific
tests.

%prep
%setup -q -n pytest_skip_markers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytestskipmarkers
%{python_sitelib}/pytest_skip_markers-%{version}*-info

%changelog
