#
# spec file for package python-jupyterlab-widgets
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pyver 1.0.2
%define jupver 3.0.1
Name:           python-jupyterlab-widgets
Version:        %{pyver}
Release:        0
Summary:        A JupyterLab extension for Jupyter/IPython widgets
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/ipywidgets
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_widgets/jupyterlab_widgets-%{pyver}.tar.gz
# PATCH-FIX-UPSTREAM ipywidgets-pr3138-pr3194-packaging.patch -- gh#jupyter-widgets/ipywidgets#3138 gh#jupyter-widgets/ipywidgets#3194
Patch1:         ipywidgets-pr3138-pr3194-packaging.patch
Source99:       python-jupyterlab-widgets-rpmlintrc
BuildRequires:  %{python_module jupyter_packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab-widgets
BuildArch:      noarch
Provides:       python-jupyterlab_widgets = %{pyver}-%{release}
%python_subpackages

%description
A JupyterLab 3.0 extension for Jupyter/IPython widgets

%package -n jupyter-jupyterlab-widgets
Summary:        A JupyterLab extension for Jupyter/IPython widgets - Jupyter JS files
Version:        %{jupver}
Provides:       jupyter-jupyterlab_widgets = %{jupver}-%{release}
Requires:       jupyter-jupyterlab-filesystem

%description -n jupyter-jupyterlab-widgets
A JupyterLab 3.0 extension for Jupyter/IPython widgets - Jupyter JS files

%prep
%autosetup -p1 -n jupyterlab_widgets-%{pyver}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import jupyterlab_widgets'
}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyterlab_widgets
%{python_sitelib}/jupyterlab_widgets-%{pyver}*-info

%files -n jupyter-jupyterlab-widgets
%license LICENSE
%{_jupyter_labextensions_dir3}/@jupyter-widgets

%changelog
