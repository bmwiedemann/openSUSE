#
# spec file for package python-jupyterlab-widgets
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


%define pyver 3.0.7
%define jupver 5.0.7
Name:           python-jupyterlab-widgets
Version:        %{pyver}
Release:        0
Summary:        A JupyterLab extension for Jupyter/IPython widgets
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/ipywidgets
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_widgets/jupyterlab_widgets-%{pyver}.tar.gz
Source99:       python-jupyterlab-widgets-rpmlintrc
BuildRequires:  %{python_module jupyter_packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab-widgets
Provides:       python-jupyterlab_widgets = %{pyver}-%{release}
BuildArch:      noarch
%python_subpackages

%description
A JupyterLab 3.0 extension for Jupyter/IPython widgets

%package -n jupyter-jupyterlab-widgets
Version:        %{pyver}
Summary:        A JupyterLab extension for Jupyter/IPython widgets - Jupyter JS files
Requires:       jupyter-jupyterlab-filesystem
Provides:       jupyter-jupyter-widgets-jupyterlab-manager = %{jupver}-%{release}
Provides:       jupyter-jupyterlab_widgets = %{pyver}-%{release}

%description -n jupyter-jupyterlab-widgets
A JupyterLab 3.0 extension for Jupyter/IPython widgets - Jupyterlab-manager JS files

%prep
%autosetup -p1 -n jupyterlab_widgets-%{pyver}

%build
%pyproject_wheel

%install
%pyproject_install
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
%dir %{_jupyter_labextensions_dir3}/@jupyter-widgets
%{_jupyter_labextensions_dir3}/@jupyter-widgets/jupyterlab-manager

%changelog
