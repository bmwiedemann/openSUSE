#
# spec file for package python-notebook-shim
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


Name:           python-notebook-shim
Version:        0.2.2
Release:        0
Summary:        A shim layer for notebook traits and config
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/notebook_shim
Source:         https://files.pythonhosted.org/packages/source/n/notebook_shim/notebook_shim-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-notebook-shim = %{version}
Requires:       (python-jupyter_server >= 1.8 with python-jupyter_server < 3)
Provides:       python-notebook_shim = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  %{python_module jupyter_server >= 1.8 with %python-jupyter_server < 3}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-jupyter}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
This project provides a way for JupyterLab and other frontends to switch to
Jupyter Server for their Python Web application backend.

%package -n jupyter-notebook-shim
Summary:        The configuration file for python-notebook-shim
Provides:       juypter-notebook_shim = %{version}-%{release}
# Any flavor is okay
Requires: (%(echo "%{python_module notebook-shim = %{version}@or@}" | sed "s/@or@/ or /g" | sed 's/ or\s*$//'))

%description -n jupyter-notebook-shim
This project provides a way for JupyterLab and other frontends to switch to
Jupyter Server for their Python Web application backend. Common configuration
file

%prep
%setup -q -n notebook_shim-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest notebook_shim

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/notebook_shim
%{python_sitelib}/notebook_shim-%{version}*-info

%files -n jupyter-notebook-shim
%_jupyter_config %{_jupyter_server_confdir}/notebook_shim.json

%changelog
