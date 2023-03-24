#
# spec file for package python-jupyterlab-rtc
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
%define python3distversion 0.8
Name:           python-jupyter-collaboration%{psuffix}
# Don't update until jupyterlab requires a larger version
Version:        0.8.0
Release:        0
Summary:        Jupyter Server Extension Providing Y Documents
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter_collaboration
# the packagename is jupyter-server-ydoc until 0.8, future releases will change to jupyter-collaboration (or change the name again, we are at rename #4)
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_server_ydoc/jupyter_server_ydoc-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 0.25}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       (python-jupyter_server_fileid >= 0.6.0 with python-jupyter_server_fileid < 1)
Requires:       (python-jupyter_ydoc >= 0.2.0 with python-jupyter_ydoc < 0.4)
Requires:       (python-ypy-websocket >= 0.8.2 with python-ypy-websocket < 0.9)
Requires:       jupyter-jupyterlab-rtc = %{version}
# SECTION remove me on a release > 0.8
Provides:       python-jupyter-server-ydoc = %{version}-%{release}
Provides:       python-jupyter_server_ydoc = %{version}-%{release}
# /SECTION
Obsoletes:      python-jupyter-server-ydoc < %{version}-%{release}
Obsoletes:      python-jupyter_server_ydoc < %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyter-collaboration = %{version}}
BuildRequires:  %{python_module jupyter-server-test >= 2}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-tornasync}
%endif
%python_subpackages

%description
A Jupyter Server Extension Providing Y Documents.

%package -n jupyter-jupyterlab-rtc
Summary: A Jupyter Server Extension Providing Y Documents. -- Jupyter configuration
# CHANGE me on release > 0.8
Requires: %{plainpython3dist}(jupyter-server-ydoc) = %{python3distversion}
Provides: jupyter-server-ydoc = %{version}-%{release}

%description -n jupyter-jupyterlab-rtc
A Jupyter Server Extension Providing Y Documents.

This subpackage provides the jupyter configuration

%prep
%setup -q -n jupyter_server_ydoc-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
# CHANGE me on release > 0.7
%{python_sitelib}/jupyter_server_ydoc
%{python_sitelib}/jupyter_server_ydoc-%{version}.dist-info

%files -n jupyter-jupyterlab-rtc
%license LICENSE
%_jupyter_config %{_jupyter_servextension_confdir}/jupyter_server_ydoc.json
%_jupyter_config %{_jupyter_server_confdir}/jupyter_server_ydoc.json
%endif

%changelog
