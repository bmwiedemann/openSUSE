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


%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
Name:           python-plotly
Version:        5.5.0
Release:        0
Summary:        Library for collaborative, interactive, publication-quality graphs
License:        MIT
URL:            https://github.com/plotly/plotly.py
# Get the PyPI archive for the bundles JS files
Source:         https://files.pythonhosted.org/packages/source/p/plotly/plotly-%{version}.tar.gz
# Additionally use the GitHub archive for the test suite
Source1:        https://github.com/plotly/plotly.py/archive/refs/tags/v%{version}.tar.gz#/plotly.py-%{version}-gh.tar.gz
Source100:      python-plotly-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.15.0}
BuildRequires:  %{python_module tenacity >= 6.2.0}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.15.0
Requires:       python-tenacity >= 6.2.0
Recommends:     python-ipython
Recommends:     python-matplotlib >= 2.2.2
Recommends:     python-numpy
Recommends:     python-pandas
Recommends:     python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
# Currently not building in TW
#BuildRequires:  %%{python_module Shapely}
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
Requires:       (python-jupyterlab or python-notebook)
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
# remove script interpreter line in non-executable script
sed -i '1{/env python/ d}' _plotly_utils/png.py
# homogenize mtime of all __init__.py files for deduplicated compile cache consistency
find . -name __init__.py -exec touch -m -r plotly/__init__.py '{}' ';'

%build
%python_build

%install
%python_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
# No test suite in the PyPI package, which is required for the bundled JS files, go to the GitHub repo tree now.
cd ../plotly.py-%{version}/packages/python/plotly
%{pytest plotly/tests/test_core
# cleanup between flavor runs
rm plotly/tests/test_core/test_offline/plotly.min.js
}
# most of the optional packages are not available on python36: skip entire test suite
python36_skip="-V"
# not available
donttest="test_kaleido"
# API parameter mismatches and precision errors
donttest+=" or test_matplotlylib"
%pytest ${$python_skip} plotly/tests/test_optional -k "not ($donttest)"

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/_plotly_future_/
%{python_sitelib}/_plotly_utils/
%{python_sitelib}/plotly/
%{python_sitelib}/plotly-%{version}-py*.egg-info

%files %{python_files jupyter}
%license LICENSE.txt
%{python_sitelib}/jupyterlab_plotly

%files -n jupyter-plotly
%license LICENSE.txt
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyterlab-plotly.json

%changelog
