#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-jupyterlab-server%{psuffix}
Version:        2.18.0
Release:        0
Summary:        Server components for JupyterLab and JupyterLab-like applications
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyterlab_server
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_server/jupyterlab_server-%{version}.tar.gz
Source100:      python-jupyterlab-server-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 2.10
Requires:       python-Jinja2 >= 3.0.3
Requires:       python-json5 >= 0.9.0
Requires:       python-jsonschema >= 4.17.3
Requires:       python-packaging >= 21.3
Requires:       python-requests >= 2.28
Requires:       (python-jupyter-server >= 1.21 with python-jupyter-server < 3)
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 4.8.3
%endif
Provides:       python-jupyterlab_server = %{version}-%{release}
Obsoletes:      python-jupyterlab_server < %{version}-%{release}
Provides:       python-jupyter-jupyterlab-server = %{version}-%{release}
Obsoletes:      python-jupyter-jupyterlab-server < %{version}-%{release}
Provides:       python-jupyter_jupyterlab_server = %{version}-%{release}
Obsoletes:      python-jupyter_jupyterlab_server < %{version}-%{release}
Provides:       python-jupyter_jupyterlab_launcher = %{version}-%{release}
Obsoletes:      python-jupyter_jupyterlab_launcher < %{version}-%{release}
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-jupyterlab-launcher = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab-launcher < %{version}-%{release}
Provides:       jupyter-jupyterlab_launcher = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab_launcher < %{version}-%{release}
Provides:       jupyter-jupyterlab-server = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab-server < %{version}-%{release}
Provides:       jupyter-jupyterlab_server = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab_server < %{version}-%{release}
%endif
%if %{with test}
BuildRequires:  %{python_module jupyterlab-server-test = %{version}}
%endif
%python_subpackages

%description
JupyterLab Server sits between JupyterLab and Jupyter Server,
and provides a set of REST API handlers and utilities that are
used by JupyterLab. It is a separate project in order to
accommodate creating JupyterLab-like applications from a more
limited scope.

%package test
Summary:        The jupyterlab_server[test] requirements
Requires:       python-Werkzeug
Requires:       python-ipykernel
Requires:       python-jupyterlab-server-openapi = %{version}
Requires:       python-openapi-spec-validator >= 0.5.1
Requires:       python-pytest >= 7
Requires:       python-pytest-console-scripts
Requires:       python-pytest-jupyter-server >= 0.6.2
Requires:       python-pytest-timeout
Requires:       python-requests-mock
#Requires:       python-sphinxcontrib-spelling
Requires:       python-strict-rfc3339

%description test
Metapackage for the jupyterlab_server[test] requirement specifier
without code coverage.

%package openapi
Summary:        The jupyterlab_server[openapi]] extra
Requires:       python-jupyterlab-server = %{version}
Requires:       python-openapi-core >= 0.16.1
Requires:       python-ruamel.yaml

%description openapi
Metapackage for the jupyterlab_server[openapi] extra

%prep
%autosetup -p1 -n jupyterlab_server-%{version}
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
%{python_sitelib}/jupyterlab_server
%{python_sitelib}/jupyterlab_server-%{version}.dist-info

%files %{python_files test}
%license LICENSE

%files %{python_files openapi}
%license LICENSE
%endif

%changelog
