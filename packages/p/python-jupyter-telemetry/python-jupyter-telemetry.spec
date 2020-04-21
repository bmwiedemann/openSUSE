#
# spec file for package python-jupyter-telemetry
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-jupyter-telemetry
Version:        0.1.0
Release:        0
Summary:        Jupyter telemetry library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://jupyter.org
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_telemetry/jupyter_telemetry-%{version}.tar.gz
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-json-logger}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traitlets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonschema
Requires:       python-python-json-logger
Requires:       python-ruamel.yaml
Requires:       python-traitlets
BuildArch:      noarch
%python_subpackages

%description
*Telemetry for Jupyter Applications and extensions.*

> Telemetry (t&#601;&#712;lem&#601;tr&#275;): the process of recording and transmitting the readings of an instrument. [Oxford Dictionaries]

Jupyter Telemetry enables Jupyter Applications (e.g. Jupyter Server, Jupyter Notebook, JupyterLab, JupyterHub, etc.) to record **events**&#8212;i.e. actions by application users&#8212;and transmit them to remote (or local) destinations as **structured** data. It works with Python's standard `logging` library to handle the transmission of events allowing users to send events to local files, over the web, etc.

%prep
%setup -q -n jupyter_telemetry-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
