#
# spec file for package python-jupyter-docprovider
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
Name:           python-jupyter-docprovider
Version:        1.0.0
Release:        0
Summary:        Jupyter extension integrating collaborative shared models
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter-collaboration
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_docprovider/jupyter_docprovider-%{version}.tar.gz
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.5}
BuildRequires:  %{python_module hatchling >= 1.4.0}
BuildRequires:  %{python_module jupyterlab >= 4.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-docprovider = %{version}
Provides:       python-jupyter_docprovider = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
JupyterLab/Jupyter Notebook 7+ extension integrating collaborative shared models.

The collaborative shared models are used for both:
- real time collaboration, and
- server-side execution of notebooks

%package -n jupyter-docprovider
Summary:        Jupyter extension providing collaboration
Requires:       python3dist(jupyter-docprovider) = %{distversion}
Suggests:       python3-docprovider = %{version}

%description -n jupyter-docprovider
JupyterLab/Jupyter Notebook 7+ extension integrating collaborative shared models.

The collaborative shared models are used for both:
- real time collaboration, and
- server-side execution of notebooks

This package provides the jupyter components.

%prep
%autosetup -p1 -n jupyter_docprovider-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# tests are in the python-jupyter-collaboration metapackage


%files %{python_files}
%{python_sitelib}/jupyter_docprovider
%{python_sitelib}/jupyter_docprovider-%{version}.dist-info

%files -n jupyter-docprovider
%license LICENSE
%doc README.md
%dir %{_jupyter_labextensions_dir3}/@jupyter
%{_jupyter_labextensions_dir3}/@jupyter/docprovider-extension

%changelog
