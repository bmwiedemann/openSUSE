#
# spec file for package python-vega
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
Name:           python-vega
Version:        3.4.0
Release:        0
Summary:        An IPython/Jupyter widget for Vega 3 and Vega-Lite 2
License:        BSD-3-Clause
URL:            https://github.com/vega/ipyvega/
Source:         https://files.pythonhosted.org/packages/py3/v/vega/vega-%{version}-py3-none-any.whl
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module jupyter-client >= 4.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-vega = %{version}
Requires:       python-altair
Requires:       python-ipython
Requires:       python-jupyter-client >= 4.2
Provides:       python-jupyter_vega = %{version}
Obsoletes:      python-jupyter_vega < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module altair}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas >= 1.0.0}
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
%setup -q -c -T

%build
# Not Needed

%install
cp -a %{SOURCE0} .
%pyproject_install

# Don't package files with generic names
rm %{buildroot}%{_bindir}/test

# %%jupyter_move_config
cp %{buildroot}%{python3_sitelib}/vega-%{version}.dist-info/LICENSE .
%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest %{buildroot}%{$python_sitelib}/vega/

%files %{python_files}
%{python_sitelib}/vega/
%{python_sitelib}/vega-%{version}.dist-info/
%license %{python_sitelib}/vega-%{version}.dist-info/LICENSE

%files -n jupyter-vega
%license LICENSE
# %%{_jupyter_nbextension_dir}/jupyter-vega/
# %%config %%{_jupyter_nb_notebook_confdir}/vega.json

%changelog
