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

%define plainpython3dist python3dist
%define python3distversion 1
Name:           python-jupyter-collaboration%{psuffix}
Version:        1.0.0
Release:        0
Summary:        Jupyter Server Extension Providing Y Documents
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter_collaboration
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_collaboration/jupyter_collaboration-%{version}.tar.gz
Source99:       python-jupyter-collaboration.rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.5}
BuildRequires:  %{python_module hatch-nodejs-version}
BuildRequires:  %{python_module hatchling >= 1.4}
BuildRequires:  %{python_module jupyterlab >= 4}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-collaboration = %{version}
Requires:       python-jupyter_events
Requires:       (python-jupyter_server >= 2.0.0 with python-jupyter_server < 3.0.0)
Requires:       (python-jupyter_server_fileid >= 0.6.0 with python-jupyter_server_fileid < 1)
Requires:       (python-jupyter_ydoc >= 1.0.1 with  python-jupyter_ydoc < 2.0.0)
Requires:       (python-ypy-websocket >= 0.8.3 with python-ypy-websocket < 0.9.0)
Provides:       python-jupyter_collaboration = %{version}-%{release}
Obsoletes:      python-jupyter-server-ydoc < 1
Obsoletes:      python-jupyter_server_ydoc < 1
Obsoletes:      python-jupyterlab-rtc < 1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyter-server-test >= 2}
BuildRequires:  %{python_module jupyter_collaboration = %{version}}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-asyncio}
%endif
%python_subpackages

%description
A Jupyter Server Extension Providing Y Documents.

%package -n jupyter-collaboration
Summary:        A Jupyter Server Extension Providing Y Documents. -- Jupyter configuration
Requires:       %{plainpython3dist}(jupyter-collaboration) = %{python3distversion}
Provides:       jupyter_collaboration = %{version}-%{release}
Obsoletes:      jupyter-server-ydoc < 1
Obsoletes:      jupyterlab-rtc < 1

%description -n jupyter-collaboration
A Jupyter Server Extension Providing Y Documents.

This subpackage provides the jupyter configuration

%prep
%setup -q -n jupyter_collaboration-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
rm %{buildroot}%{_jupyter_labextensions_dir3}/@jupyter/collaboration-extension/schemas/@jupyter/collaboration-extension/package.json.orig
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/jupyter_collaboration
%{python_sitelib}/jupyter_collaboration-%{version}.dist-info

%files -n jupyter-collaboration
%license LICENSE
%_jupyter_config %{_jupyter_server_confdir}/jupyter_collaboration.json
%_jupyter_config %dir %{_jupyter_labextensions_dir3}/@jupyter
%_jupyter_config %{_jupyter_labextensions_dir3}/@jupyter/collaboration-extension
%endif

%changelog
