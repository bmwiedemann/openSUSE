#
# spec file for package python-nbclassic
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-nbclassic
Version:        0.2.6
Release:        0
Summary:        Jupyter Notebook as a Jupyter Server Extension
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/nbclassic
# The github archive has the tests
Source:         https://github.com/jupyterlab/nbclassic/archive/%{version}.tar.gz#/nbclassic-%{version}-gh.tar.gz
BuildRequires:  %{python_module jupyter_server >= 1.1}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-nbclassic = %{version}
Requires:       python-jupyter_server >= 1.1
Requires:       python-notebook
# SECTION test requirements
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
# /SECION
BuildArch:      noarch
%python_subpackages

%description
NBClassic runs the Jupyter Notebook frontend on the Jupyter Server backend.

This project prepares for a future where JupyterLab and other frontends switch
to Jupyter Server for their Python Web application backend. Using this package,
users can launch Jupyter Notebook, JupyterLab and other frontends side-by-side
on top of the new Python server backend.

%package -n jupyter-nbclassic
Summary:        Jupyter Notebook as a Jupyter Server Extension

%description -n jupyter-nbclassic
NBClassic runs the Jupyter Notebook frontend on the Jupyter Server backend.

This project prepares for a future where JupyterLab and other frontends switch
to Jupyter Server for their Python Web application backend. Using this package,
users can launch Jupyter Notebook, JupyterLab and other frontends side-by-side
on top of the new Python server backend.

This package contains the jupyterlab server configuration file

%prep
%setup -q -n nbclassic-%{version}

%build
%python_build

%install
%python_install
install -m 644 -D -t %{buildroot}%{_jupyter_server_confdir} jupyter_server_config.d/*
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbclassic
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative jupyter-nbclassic

%postun
%python_uninstall_alternative jupyter-nbclassic

%check
# suppress color output
rm setup.cfg
%pytest -s

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-nbclassic
%{python_sitelib}/

%files -n jupyter-nbclassic
%license LICENSE
%config %{_jupyter_server_confdir}/nbclassic.json

%changelog
