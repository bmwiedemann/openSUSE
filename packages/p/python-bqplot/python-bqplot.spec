#
# spec file for package python-bqplot
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
Name:           python-bqplot
Version:        0.12.12
Release:        0
Summary:        Interactive plotting package for the Jupyter notebook
License:        Apache-2.0
URL:            https://github.com/bloomberg/bqplot
Source:         https://files.pythonhosted.org/packages/source/b/bqplot/bqplot-%{version}.tar.gz
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-bqplot = %{version}
Requires:       python-ipywidgets >= 7.5.0
Requires:       python-numpy >= 1.10.4
Requires:       python-pandas
Requires:       python-traitlets >= 4.3.0
Requires:       python-traittypes >= 0.0.6
Provides:       python-jupyter_bqplot = %{version}
Obsoletes:      python-jupyter_bqplot < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.5.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy >= 1.10.4}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module traitlets >= 4.3.0}
BuildRequires:  %{python_module traittypes >= 0.0.6}
# /SECTION
%python_subpackages

%description
Plotting system for the Jupyter notebook based on the
interactive Jupyter widgets.

This package provides the python interface.

%package     -n jupyter-bqplot
Summary:        Interactive plotting package for the Jupyter notebook
Requires:       jupyter-notebook
Requires:       python3-bqplot = %{version}

%description -n jupyter-bqplot
Plotting system for the Jupyter notebook based on the
interactive Jupyter widgets.

This package provides the jupyter notebook extension.

%prep
%setup -q -n bqplot-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_nb_notebook_confdir}
%fdupes %{buildroot}%{_jupyter_nbextension_dir}

%{python_expand sed -i -e "s|^#!%{_bindir}/env python|#!%{__$python}|" %{buildroot}%{$python_sitelib}/bqplot/install.py
chmod a+x %{buildroot}%{$python_sitelib}/bqplot/install.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/bqplot/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/bqplot/
%python_expand %fdupes %{buildroot}%{$python_sitelib}
}

%jupyter_move_config

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c "import bqplot"
}
%pytest tests/

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/bqplot/
%{python_sitelib}/bqplot-%{version}-py*.egg-info

%files -n jupyter-bqplot
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/bqplot.json
%{_jupyter_nbextension_dir}/bqplot/

%changelog
