#
# spec file for package python-jupyter-collaboration-ui
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


%define distversion 1
Name:           python-jupyter-collaboration-ui
Version:        1.0.0
Release:        0
Summary:        Jupyter extension providing collaboration
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter-collaboration
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_collaboration_ui/jupyter_collaboration_ui-%{version}.tar.gz
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.5}
BuildRequires:  %{python_module hatchling >= 1.4.0}
BuildRequires:  %{python_module jupyterlab >= 4.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-collaboration-ui = %{version}
Provides:       python-jupyter_collaboration_ui = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
JupyterLab/Jupyter Notebook 7+ extension providing user interface integration
for real time collaboration.

%package -n jupyter-collaboration-ui
Summary:        Jupyter extension providing collaboration
Requires:       python3dist(jupyter-collaboration-ui) = %{distversion}
Suggests:       python3-jupyter-collaboration-ui = %{version}

%description -n jupyter-collaboration-ui
JupyterLab/Jupyter Notebook 7+ extension providing user interface integration
for real time collaboration.

This package provides the jupyter components.

%prep
%autosetup -p1 -n jupyter_collaboration_ui-%{version}
rm jupyter_collaboration_ui/labextension/schemas/@jupyter/collaboration-extension/package.json.orig

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# tests are in the python-jupyter-collaboration metapackage

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/jupyter_collaboration_ui
%{python_sitelib}/jupyter_collaboration_ui-%{version}.dist-info

%files -n jupyter-collaboration-ui
%license LICENSE
%doc README.md
%dir %{_jupyter_labextensions_dir3}/@jupyter
%{_jupyter_labextensions_dir3}/@jupyter/collaboration-extension

%changelog
