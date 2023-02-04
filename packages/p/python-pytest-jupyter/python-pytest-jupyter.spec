#
# spec file for package python-pytest-jupyter
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-pytest-jupyter%{psuffix}
Version:        0.6.2
Release:        0
Summary:        A pytest plugin for testing Jupyter libraries and extensions
License:        MIT AND BSD-3-Clause
URL:            https://github.com/jupyter-server/pytest-jupyter
Source:         https://files.pythonhosted.org/packages/source/p/pytest_jupyter/pytest_jupyter-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jupyter_core
Requires:       python-pytest
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pytest-jupyter = %{version}}
BuildRequires:  %{python_module pytest-jupyter-client = %{version}}
BuildRequires:  %{python_module pytest-jupyter-server = %{version}}
BuildRequires:  %{python_module pytest-timeout}
%endif
%python_subpackages

%description
A pytest plugin for testing Jupyter libraries and extensions.

%package client
Summary:        A pytest plugin for testing Jupyter libraries and extensions [client] extra
Requires:       python-ipykernel
Requires:       python-jupyter_client >= 7.4
Requires:       python-pytest-jupyter = %{version}

%description client
A pytest plugin for testing Jupyter libraries and extensions.
This subpackage provides the [client] extra dependencies

%package server
Summary:        A pytest plugin for testing Jupyter libraries and extensions [server] extra
Requires:       python-jupyter-server >= 1.21
Requires:       python-nbformat >= 5.3
Requires:       python-pytest-jupyter = %{version}
Requires:       python-pytest-jupyter-client = %{version}

%description server
A pytest plugin for testing Jupyter libraries and extensions.
This subpackage provides the [server] extra dependencies

%prep
%setup -q -n pytest_jupyter-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_jupyter
%{python_sitelib}/pytest_jupyter-%{version}.dist-info

%files %{python_files client}
%license LICENSE

%files %{python_files server}
%license LICENSE
%endif

%changelog
