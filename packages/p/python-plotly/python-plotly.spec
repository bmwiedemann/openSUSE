#
# spec file for package python-plotly
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


Name:           python-plotly
Version:        5.22.0
Release:        0
Summary:        Library for collaborative, interactive, publication-quality graphs
License:        MIT
URL:            https://github.com/plotly/plotly.py
# Use the GitHub archive for the test suite
Source0:        https://github.com/plotly/plotly.py/archive/refs/tags/v%{version}.tar.gz#/plotly.py-%{version}-gh.tar.gz
# package-lock.json file generated with command in packages/javascript/jupyterlab-plotly:
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source10:       package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source11:       node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
Source100:      python-plotly-rpmlintrc
# PATCH-FIX-UPSTREAM plotly-pr4622-np2.patch gh#plotly/plotly.py#4622
Patch0:         plotly-pr4622-np2.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module jupyterlab >= 3}
BuildRequires:  %{python_module notebook >= 5.3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tenacity >= 6.2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
Requires:       python-packaging
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
# So that any of the flavor satisifies the jupyter package
Provides:       jupyterpython(plotly-jupyter) = %{version}
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
Requires:       jupyterpython(plotly-jupyter) = %{version}
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
%autosetup -p4 -n plotly.py-%{version}/packages/python/plotly
pushd ../../javascript/jupyterlab-plotly/
rm package-lock.json
# allow builder v4
sed -i '/jupyterlab.builder/ s/\^3/>=3/' package.json
local-npm-registry %{_sourcedir} install --include=dev --include=peer
popd
# remove script interpreter line in non-executable script
sed -i '1{/env python/ d}' _plotly_utils/png.py
# homogenize mtime of all __init__.py files for deduplicated compile cache consistency
find . -name __init__.py -exec touch -m -r plotly/__init__.py '{}' ';'

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
# API parameter mismatch
donttest="test_described_subscript_error_on_type_error"
%pytest plotly/tests/test_core -k "not ($donttest)"
# not available
donttest="test_kaleido"
donttest="$donttest or test_px_input and (vaex or polars)"
# API parameter mismatches and precision errors
donttest="$donttest or test_matplotlylib"
# fails to plot with numpy 2 but cannot reproduce failure interactively
donttest="$donttest or test_masked_constants_example"
# flaky timing error
donttest="$donttest or test_fast_track_finite_arrays"
%pytest plotly/tests/test_optional -k "not ($donttest)"

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
