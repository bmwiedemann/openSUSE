#
# spec file for package python-jupyterlab-widgets
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
Name:           python-jupyterlab-widgets
Version:        1.0.2
Release:        0
Summary:        A JupyterLab extension for Jupyter/IPython widgets
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/ipywidgets
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_widgets/jupyterlab_widgets-%{version}.tar.gz
Source99:       python-jupyterlab-widgets-rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module jupyter_packaging}
BuildRequires:  fdupes
BuildArch:      noarch
Provides:       python-jupyterlab_widgets = %{version}-%{release}
%python_subpackages

%description
A JupyterLab 3.0 extension for Jupyter/IPython widgets

%prep
%setup -q -n jupyterlab_widgets-%{version}

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
%{python_sitelib}/jupyterlab_widgets-%{version}*-info

%changelog
