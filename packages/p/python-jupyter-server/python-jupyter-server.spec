#
# spec file for package python-jupyter-server
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
%define         skip_python2 1
Name:           python-jupyter-server
Version:        0.2.1
Release:        0
Summary:        The Jupyter Server
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_server
Source:         https://github.com/jupyter/jupyter_server/archive/%{version}.tar.gz#/jupyter_server-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Send2Trash}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter-client >= 5.2.0}
BuildRequires:  %{python_module jupyter-core >= 4.4.0}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module prometheus_client}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module terminado >= 0.8.1}
BuildRequires:  %{python_module tornado >= 4}
BuildRequires:  %{python_module traitlets >= 4.2.1}
BuildRequires:  pandoc
# /SECTION
Requires:       jupyter-jupyter-server = %{version}
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-ipykernel
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 5.2.0
Requires:       python-jupyter-core >= 4.4.0
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-prometheus_client
Requires:       python-pyzmq >= 17
Requires:       python-terminado >= 0.8.1
Requires:       python-tornado >= 4
Requires:       python-traitlets >= 4.2.1
%ifpython2
Requires:       python-ipaddress
%endif
BuildArch:      noarch

%python_subpackages

%description
The Jupyter Server is a web application that allows you to create and
share documents that contain live code, equations, visualizations, and
explanatory text. The Notebook has support for multiple programming
languages, sharing, and interactive widgets.

This package provides the python interface.

%package     -n jupyter-jupyter-server
Summary:        The Jupyter Server
Group:          Development/Languages/Python
Requires:       jupyter-ipykernel
Requires:       jupyter-jupyter-client >= 5.2.0
Requires:       jupyter-jupyter-core >= 4.4.0
Requires:       jupyter-nbconvert
Requires:       jupyter-nbformat
Requires:       python3-jupyter-server = %{version}

%description -n jupyter-jupyter-server
The Jupyter Server is a web application that allows you to create and
share documents that contain live code, equations, visualizations, and
explanatory text. The Notebook has support for multiple programming
languages, sharing, and interactive widgets.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_server-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Avoid conflict with jupyter-notebook
mv %{buildroot}%{_bindir}/jupyter-bundlerextension %{buildroot}%{_bindir}/jupyter-server-bundlerextension

%check
export LANG=en_US.UTF-8
export PATH=$PATH:%{buildroot}%{_bindir}
%pytest tests

%files %{python_files}
%doc README.md
%license COPYING.md
%{python_sitelib}/*

%files -n jupyter-jupyter-server
%license COPYING.md
%{_bindir}/jupyter-server
%{_bindir}/jupyter-server-bundlerextension

%changelog
