#
# spec file for package python-bqplot
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


%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
%define         pyver 0.12.25
%define         jupver 0.5.26
Name:           python-bqplot
Version:        %{pyver}
Release:        0
Summary:        Interactive plotting package for the Jupyter notebook
License:        Apache-2.0
URL:            https://github.com/bqplot/bqplot
# bundled js stuff from PyPI sdist
Source0:        https://files.pythonhosted.org/packages/source/b/bqplot/bqplot-%{pyver}.tar.gz
# tests from GitHub source
Source1:        https://github.com/bqplot/bqplot/archive/refs/tags/%{pyver}.tar.gz#/bqplot-%{pyver}-gh.tar.gz
BuildRequires:  %{python_module jupyter-packaging}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-bqplot-notebook = %{jupver}
Requires:       python-ipywidgets >= 7.5.0
Requires:       python-numpy >= 1.10.4
Requires:       python-pandas
Requires:       python-traitlets >= 4.3.0
Requires:       python-traittypes >= 0.0.6
Provides:       python-jupyter_bqplot = %{pyver}
Obsoletes:      python-jupyter_bqplot < %{pyver}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.5.0}
BuildRequires:  %{python_module nbval}
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

%package     -n jupyter-bqplot-notebook
Version:        %{jupver}
Summary:        Interactive plotting package for Jupyter Notebooke
Requires:       jupyter-notebook
Requires:       python3-bqplot = %{pyver}
Provides:       jupyter-bqplot =  %{pyver}-%{release}
# the jupyter-bqplot rpm package had the python package version until 0.12.13
Obsoletes:      jupyter-bqplot <  %{pyver}-%{release}

%description -n jupyter-bqplot-notebook
Plotting system for the Jupyter notebook based on the
interactive Jupyter widgets.

This package provides the jupyter notebook extension.

%package     -n jupyter-bqplot-jupyterlab
Version:        %{jupver}
Summary:        Interactive plotting package for Jupyterlab
Requires:       jupyter-bqplot-notebook
Requires:       jupyter-jupyterlab

%description -n jupyter-bqplot-jupyterlab
Plotting system for the Jupyter notebook based on the
interactive Jupyter widgets.

This package provides the jupyterlab extension.

%prep
%setup -q -n bqplot-%{pyver}
tar -x --strip-components=1 -f %{SOURCE1} bqplot-%{pyver}/{tests,ui-tests}
rm bqplot/install.py

%build
%python_build

%install
%python_install
cp -r etc/ %{buildroot}%{_sysconfdir}
cp -r share/ %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import bqplot"
%pytest tests/
%pytest --nbval ui-tests/tests/notebooks

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/bqplot/
%{python_sitelib}/bqplot-%{pyver}*-info

%files -n jupyter-bqplot-notebook
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/bqplot.json
%{_jupyter_nbextension_dir}/bqplot/

%files -n jupyter-bqplot-jupyterlab
%license LICENSE
%dir %{_jupyter_prefix}/labextensions
%{_jupyter_prefix}/labextensions/bqplot/

%changelog
