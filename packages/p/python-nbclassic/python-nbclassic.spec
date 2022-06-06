#
# spec file for package python-nbclassic
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-nbclassic
Version:        0.3.7
Release:        0
Summary:        Jupyter Notebook as a Jupyter Server Extension
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/nbclassic
# The github archive has the tests
Source:         https://github.com/jupyterlab/nbclassic/archive/v%{version}.tar.gz#/nbclassic-%{version}-gh.tar.gz
BuildRequires:  %{python_module jupyter_server >= 1.8}
BuildRequires:  %{python_module notebook < 7}
BuildRequires:  %{python_module notebook_shim >= 0.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros >= 20210929
Requires:       jupyter-nbclassic = %{version}
Requires:       python-jupyter_server >= 1.8
Requires:       python-notebook < 7
Requires:       python-notebook_shim >= 0.1.0
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
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
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbclassic
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%jupyter_move_config

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-nbclassic

%post
%python_install_alternative jupyter-nbclassic

%postun
%python_uninstall_alternative jupyter-nbclassic

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-nbclassic
%{python_sitelib}/nbclassic
%{python_sitelib}/nbclassic-%{version}*-info

%files -n jupyter-nbclassic
%license LICENSE
%_jupyter_config %{_jupyter_server_confdir}/nbclassic.json

%changelog
