#
# spec file for package python-holoviews
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
%bcond_without  test
Name:           python-holoviews
Version:        1.13.3
Release:        0
Summary:        Composable, declarative visualizations for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ioam/holoviews
Source0:        https://files.pythonhosted.org/packages/source/h/holoviews/holoviews-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove-cyordereddict.patch gh#holoviz/holoviews#4620 mcepl@suse.com
# Package cyordereddict has been declared obsolete even by its own upstream
Patch0:         remove-cyordereddict.patch
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#holoviz/holoviews#4621 mcepl@suse.com
# Remove last residues of using nose
Patch1:         remove_nose.patch
BuildRequires:  %{python_module numpy >= 1.0}
BuildRequires:  %{python_module panel}
BuildRequires:  %{python_module param < 2.0}
BuildRequires:  %{python_module param >= 1.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyct}
BuildRequires:  %{python_module pyviz-comms >= 0.7.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.0
Requires:       python-param < 2.0
Requires:       python-param >= 1.8.0
Requires:       python-pyviz-comms >= 0.7.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     ImageMagick
Recommends:     ffmpeg
Recommends:     python-Jinja2
Recommends:     python-Pygments
Recommends:     python-bokeh >= 0.12.14
Recommends:     python-colorcet
Recommends:     python-dask
Recommends:     python-dask-array
Recommends:     python-dask-dataframe
Recommends:     python-datashader
Recommends:     python-flexx
Recommends:     python-jsonschema
Recommends:     python-jupyter_ipykernel
Recommends:     python-jupyter_ipython
Recommends:     python-jupyter_ipywidgets
Recommends:     python-jupyter_nbconvert
Recommends:     python-jupyter_nbformat
Recommends:     python-jupyter_notebook
Recommends:     python-jupyter_widgetsnbextension
Recommends:     python-matplotlib
Recommends:     python-netCDF4
Recommends:     python-networkx
Recommends:     python-pandas
Recommends:     python-panel
Recommends:     python-plotly
Recommends:     python-pyparsing
Recommends:     python-pyzmq
Recommends:     python-scipy
Recommends:     python-scitools-iris
Recommends:     python-seaborn
Recommends:     python-selenium
Recommends:     python-streamz
Recommends:     python-tornado
Recommends:     python-xarray
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module bokeh >= 0.12.14}
BuildRequires:  %{python_module colorcet}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module datashader}
BuildRequires:  %{python_module flexx}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module jupyter_ipykernel}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module jupyter_ipywidgets}
BuildRequires:  %{python_module jupyter_nbconvert}
BuildRequires:  %{python_module jupyter_nbformat}
BuildRequires:  %{python_module jupyter_notebook}
BuildRequires:  %{python_module jupyter_widgetsnbextension}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module seaborn}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module xarray}
BuildRequires:  ImageMagick
%endif
%python_subpackages

%description
HoloViews is a Python library for automated plotting of annotated
data.

Instead of building a plot using direct calls to a plotting library,
the developer instead first describes the data with semantic
information and then additional metadata to determine more detailed
aspects of the visualization. This approach provides automatic
visualization that can be requested at any time as the data evolves,
rendered automatically by one of the supported plotting libraries
(such as Bokeh or Matplotlib).

%prep
%setup -q -n holoviews-%{version}
%autopatch -p1

# remove tests that install additional files using npm/etc
# "conda install -c bokeh flexx" or "pip install flexx"
rm -f holoviews/tests/plotting/testplotutils.py
rm -rf holoviews/tests/ipython
# "conda install phantomjs"
rm -rf holoviews/tests/plotting/bokeh holoviews/tests/test_annotators.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/holoviews
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/holoviews/util/command.py
sed -i "s|^#! %{_bindir}/env python$|#!%__$python|" %{buildroot}%{$python_sitelib}/holoviews/util/command.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/holoviews/util/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/holoviews/util/
%fdupes %{buildroot}%{$python_sitelib}
}

%post
%python_install_alternative holoviews

%postun
%python_uninstall_alternative holoviews

%if %{with test}
%check
export HOLOVIEWSRC=`pwd`'/holoviews.rc'
echo 'import holoviews as hv;hv.config(style_17=True);hv.config.warn_options_call=True' > holoviews.rc
%pytest
%endif

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/holoviews
%{python_sitelib}/holoviews-%{version}-py*.egg-info
%{python_sitelib}/holoviews/

%changelog
