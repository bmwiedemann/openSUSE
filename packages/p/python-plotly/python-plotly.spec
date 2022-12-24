#
# spec file for package python-plotly
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


%define         skip_python2 1
Name:           python-plotly
Version:        5.11.0
Release:        0
Summary:        Library for collaborative, interactive, publication-quality graphs
License:        MIT
URL:            https://github.com/plotly/plotly.py
# Get the PyPI archive for the bundles JS files
Source:         https://files.pythonhosted.org/packages/source/p/plotly/plotly-%{version}.tar.gz
# Additionally use the GitHub archive for the test suite
Source1:        https://github.com/plotly/plotly.py/archive/refs/tags/v%{version}.tar.gz#/plotly.py-%{version}-gh.tar.gz
Source100:      python-plotly-rpmlintrc
# PATCH-FIX-UPSTREAM plotly-fix-tests-np1.24.patch and plotly-fix-sources-np1.24.patch gh#plotly/plotly.py#3997
Patch1:         plotly-fix-sources-np1.24.patch
Patch2:         plotly-fix-tests-np1.24.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module jupyterlab >= 3}
BuildRequires:  %{python_module notebook >= 5.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tenacity >= 6.2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-tenacity >= 6.2.0
Recommends:     python-ipython
Recommends:     python-matplotlib >= 2.2.2
Recommends:     python-numpy
Recommends:     python-pandas
Recommends:     python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyshp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module statsmodels}
BuildRequires:  %{python_module xarray}
# /SECTION
%python_subpackages

%description
Use this package to make collaborative, interactive,
publication-quality graphs from Python on https://plot.ly.

Plotly is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

%package        jupyter
Summary:        Jupyter notebook integration for %{name}
Requires:       %{name} = %{version}
Requires:       jupyter-plotly = %{version}
Requires:       python-ipywidgets >= 7.6
Requires:       (python-jupyterlab >= 3 or python-notebook >= 5.3)
Provides:       python-jupyterlab-plotly = %{version}-%{release}

%description    jupyter
Use this package to make collaborative, interactive,
publication-quality graphs from Python on https://plot.ly.

Plotly is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

This package provides Jupyterlab and Notebook integration and widgets.

%package     -n jupyter-plotly
Summary:        Jupyter notebook integration for %{name}
Requires:       python3-plotly-jupyter = %{version}
Provides:       jupyterlab-plotly = %{version}-%{release}

%description -n jupyter-plotly
Use this package to make collaborative, interactive,
publication-quality graphs from Python on https://plot.ly.

Plotly is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

This package provides the flavorless configuration for the
Jupyterlab and Notebook integration and widgets.

%prep
%setup -q -n plotly-%{version} -b 1
%patch1 -p4
# remove script interpreter line in non-executable script
sed -i '1{/env python/ d}' _plotly_utils/png.py
# homogenize mtime of all __init__.py files for deduplicated compile cache consistency
find . -name __init__.py -exec touch -m -r plotly/__init__.py '{}' ';'
# patch the sources and tests in the github archive too
pushd ../plotly.py-%{version}
%patch1 -p1
%patch2 -p1
popd

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
# No test suite in the PyPI package, which is required for the bundled JS files, we are using the GitHub repo tree now.
# Important: make sure you patched the sources the same as the github repo
pushd ../plotly.py-%{version}/packages/python/plotly
%pytest plotly/tests/test_core
# not available
donttest="test_kaleido"
# API parameter mismatches and precision errors
donttest+=" or test_matplotlylib"
# flaky timing error
donttest+=" or test_fast_track_finite_arrays"
%pytest plotly/tests/test_optional -k "not ($donttest)"
popd

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/_plotly_future_/
%{python_sitelib}/_plotly_utils/
%{python_sitelib}/plotly/
%{python_sitelib}/plotly-%{version}.dist-info

%files %{python_files jupyter}
%license LICENSE.txt
%{python_sitelib}/jupyterlab_plotly

%files -n jupyter-plotly
%license LICENSE.txt
%{_jupyter_nbextension_dir}/jupyterlab-plotly/
%{_jupyter_labextensions_dir3}/jupyterlab-plotly/
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/jupyterlab-plotly.json

%changelog
