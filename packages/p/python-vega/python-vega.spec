#
# spec file for package python-vega
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-vega
Version:        2.6.0
Release:        0
Summary:        An IPython/Jupyter widget for Vega 3 and Vega-Lite 2
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/vega/ipyvega/
Source:         https://files.pythonhosted.org/packages/source/v/vega/vega-%{version}.tar.gz
BuildRequires:  %{python_module jupyter-client >= 4.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-vega = %{version}
Requires:       python-ipython
Requires:       python-jupyter-client >= 4.2
Provides:       python-jupyter_vega = %{version}
Obsoletes:      python-jupyter_vega < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
IPython/Jupyter notebook module for Vega and Vega-Lite,
Polestar, and Voyager. Notebooks with embedded visualizations
can be viewed on github and nbviewer.

This package provides the python interface.

%package     -n jupyter-vega
Summary:        An IPython/Jupyter widget for Vega 3 and Vega-Lite 2
Requires:       jupyter-notebook
Requires:       python3-vega = %{version}
Conflicts:      python3-jupyter_vega < 2.1.0

%description -n jupyter-vega
IPython/Jupyter notebook module for Vega and Vega-Lite,
Polestar, and Voyager. Notebooks with embedded visualizations
can be viewed on github and nbviewer.

This package provides the jupyter notebook extension.

%prep
%setup -q -n vega-%{version}
rm -rf vega/.ipynb_checkpoints

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{jupyter_move_config}

%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%check
%pytest vega

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/vega/
%{python_sitelib}/vega-%{version}-py*.egg-info

%files -n jupyter-vega
%license LICENSE
%{_jupyter_nbextension_dir}/jupyter-vega/
%config %{_jupyter_nb_notebook_confdir}/vega.json

%changelog
}