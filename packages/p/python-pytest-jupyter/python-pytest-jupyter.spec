#
# spec file for package python-pytest-jupyter
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

# defined at Ring1-MinimalX lettered staging prjconf
# We do not want jupyter-server in ring1
%bcond_with ringdisabled
%define skip_python39 1
Name:           python-pytest-jupyter%{psuffix}
Version:        0.10.1
Release:        0
Summary:        A pytest plugin for testing Jupyter libraries and extensions
License:        BSD-3-Clause AND MIT
URL:            https://github.com/jupyter-server/pytest-jupyter
Source:         https://files.pythonhosted.org/packages/source/p/pytest_jupyter/pytest_jupyter-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jupyter_core >= 5.7
Requires:       python-pytest >= 7.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest-jupyter = %{version}}
BuildRequires:  %{python_module pytest-jupyter-client = %{version}}
%if !%{with ringdisabled}
BuildRequires:  %{python_module pytest-jupyter-server = %{version}}
%endif
BuildRequires:  %{python_module pytest-timeout}
%endif
%python_subpackages

%description
A pytest plugin for testing Jupyter libraries and extensions.

%package client
Summary:        A pytest plugin for testing Jupyter libraries and extensions [client] extra
Requires:       python-ipykernel >= 6.14
Requires:       python-jupyter-client >= 7.4
Requires:       python-nbformat >= 5.3
Requires:       python-pytest-jupyter = %{version}

%description client
A pytest plugin for testing Jupyter libraries and extensions.
This subpackage provides the [client] extra dependencies

%package server
Summary:        A pytest plugin for testing Jupyter libraries and extensions [server] extra
Requires:       python-ipykernel >= 6.14
Requires:       python-jupyter-client >= 7.4
Requires:       python-jupyter-server >= 1.21
Requires:       python-nbformat >= 5.3
Requires:       python-pytest-jupyter = %{version}

%description server
A pytest plugin for testing Jupyter libraries and extensions.
This subpackage provides the [server] extra dependencies

%prep
%setup -q -n pytest_jupyter-%{version}
sed -e 's/ "--color=yes",//' -i pyproject.toml
%if %{with ringdisabled}
sed -e "/jupyter_server/d" -i tests/conftest.py
%endif

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
mv pytest_jupyter pytest_jupyter.moved
%pytest %{?_with_ringdisabled:--ignore tests/test_jupyter_server.py}
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_jupyter
%{python_sitelib}/pytest_jupyter-%{version}.dist-info

%files %{python_files client}
%license LICENSE

%if !%{with ringdisabled}
%files %{python_files server}
%license LICENSE
%endif
%endif

%changelog
