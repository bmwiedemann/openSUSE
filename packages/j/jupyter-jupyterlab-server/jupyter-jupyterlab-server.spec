#
# spec file for package jupyter-jupyterlab-server
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


%define oldpython python
Name:           jupyter-jupyterlab-server
Version:        2.15.1
Release:        0
Summary:        Server components for JupyterLab and JupyterLab-like applications
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyterlab_server
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_server/jupyterlab_server-%{version}.tar.gz
Source100:      jupyter-jupyterlab-server-rpmlintrc
# PATCH-FIX-OPENSUSE jupyterlab-server-fix-testing.patch code@bnavigator.de -- remove color, failing deprecation warnings, and used nbconvert vendored mistune
Patch0:         jupyterlab-server-fix-testing.patch
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Jinja2 >= 3.0.3}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 0.25}
BuildRequires:  %{python_module importlib-metadata >= 3.6 if %python-base < 3.10}
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module jsonschema >= 3.0.1}
BuildRequires:  %{python_module jupyter_server >= 1.4}
BuildRequires:  %{python_module packaging > 0.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel
Requires:       python-Jinja2 >= 3.0.3
Requires:       python-json5
Requires:       python-jsonschema >= 3.0.1
Requires:       python-packaging
Requires:       python-requests
Requires:       (python-jupyter-server >= 1.8 with python-jupyter-server < 2)
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 3.6
%endif
Provides:       python-jupyterlab-server = %{version}-%{release}
Obsoletes:      python-jupyterlab-server < %{version}-%{release}
Provides:       python-jupyterlab_server = %{version}-%{release}
Obsoletes:      python-jupyterlab_server < %{version}-%{release}
Provides:       python-jupyter_jupyterlab_server = %{version}-%{release}
Obsoletes:      python-jupyter_jupyterlab_server < %{version}-%{release}
Provides:       python-jupyter_jupyterlab_launcher = %{version}-%{release}
Obsoletes:      python-jupyter_jupyterlab_launcher < %{version}-%{release}
Provides:       %{oldpython}-jupyter_jupyterlab_server = %{version}-%{release}
Obsoletes:      %{oldpython}-jupyter_jupyterlab_server < %{version}-%{release}
Provides:       %{oldpython}-jupyter_jupyterlab_launcher = %{version}-%{release}
Obsoletes:      %{oldpython}-jupyter_jupyterlab_launcher < %{version}-%{release}
Provides:       %{oldpython}-jupyterlab-server = %{version}-%{release}
Obsoletes:      %{oldpython}-jupyterlab-server < %{version}-%{release}
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
# SECTION test requirements
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-server-test}
BuildRequires:  %{python_module openapi-core >= 0.14.2}
BuildRequires:  %{python_module pytest >= 5.3.2}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module strict-rfc3339}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
JupyterLab Server sits between JupyterLab and Jupyter Server,
and provides a set of REST API handlers and utilities that are
used by JupyterLab. It is a separate project in order to
accommodate creating JupyterLab-like applications from a more
limited scope.

%package test
Summary:        The jupyterlab_server[test] requirements
Provides:       python-jupyterlab-server-test = %{version}-%{release}
Obsoletes:      python-jupyterlab-server-test < %{version}-%{release}
Requires:       python-ipykernel
Requires:       python-jupyter-server-test
Requires:       python-jupyterlab-server = %{version}
Requires:       python-openapi-core >= 0.14.2
Requires:       python-pytest >= 5.3.2
Requires:       python-pytest-console-scripts
Requires:       python-ruamel.yaml
Requires:       python-strict-rfc3339

%description test
Metapackage for the jupyterlab_server[test] requirement specifier

%package openapi
Summary:        The jupyterlab_server[openapi]] extra
Provides:       python-jupyterlab-server-openapi = %{version}-%{release}
Obsoletes:      python-jupyterlab-server-openapi < %{version}-%{release}
Requires:       python-jupyterlab-server = %{version}
Requires:       python-openapi-core >= 0.14.2

%description openapi
Metapackage for the jupyterlab_server[openapi] extra

%prep
%autosetup -p1 -n jupyterlab_server-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# pytest error when trying to import tornasync plugin pulled in by jupyter-server-test (?)
%pytest -p no:tornasync

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/jupyterlab_server
%{python_sitelib}/jupyterlab_server-%{version}*-info

%files %{python_files test}
%license LICENSE

%files %{python_files openapi}
%license LICENSE

%changelog
