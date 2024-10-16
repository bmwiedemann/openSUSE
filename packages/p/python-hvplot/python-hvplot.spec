#
# spec file for package python-hvplot
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_modules_python}
Name:           python-hvplot%{psuffix}
Version:        0.11.0
Release:        0
Summary:        High-level plotting API for the PyData ecosystem built on HoloViews
License:        BSD-3-Clause
URL:            https://github.com/pyviz/hvplot
Source0:        https://files.pythonhosted.org/packages/source/h/hvplot/hvplot-%{version}.tar.gz
# Test data. Bump the commit whenever you bump this version
Source1:        https://github.com/pydata/xarray-data/archive/7d8290e0be9d2a8f4b4381641f20a97db6eaea3d.tar.gz#/xarray-data.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bokeh >= 3.1
Requires:       python-colorcet >= 2
Requires:       python-holoviews >= 1.19.0
Requires:       python-numpy >= 1.21
Requires:       python-packaging
Requires:       python-pandas >= 1.3
Requires:       python-panel >= 1.0
Requires:       (python-param >= 1.12 with python-param < 3)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Pillow
Recommends:     python-dask
Recommends:     python-datashader >= 0.6.5
Recommends:     python-geopandas
Recommends:     python-intake
Recommends:     python-intake-parquet
Recommends:     python-intake-xarray
Recommends:     python-nbsite >= 0.5.1
Recommends:     python-networkx
Recommends:     python-notebook >= 5.4
Recommends:     python-phantomjs
Recommends:     python-python-snappy
Recommends:     python-rasterio
Recommends:     python-s3fs
Recommends:     python-scikit-mage
Recommends:     python-scipy
Recommends:     python-selenium
Recommends:     python-spatialpandas
Recommends:     python-streamz >= 0.3.0
Recommends:     python-xarray
Suggests:       python-duckdb
Suggests:       python-pyproj
Suggests:       python-cartopy
Suggests:       python-geoviews
BuildArch:      noarch
%if %{with test}
##
BuildRequires:  %{python_module hvplot = %{version}}
##
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module bokeh_sampledata}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module datashader}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pooch}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module streamz >= 0.3.0}
BuildRequires:  %{python_module xarray}
# Only pyproj of the triple available
#BuildRequires:  %%{python_module pyproj}
#BuildRequires:  %%{python_module cartopy}
#BuildRequires:  %%{python_module geoviews}
%endif
%python_subpackages

%description
hvPlot provides a high-level plotting API built on HoloViews that
provides a general and consistent API for plotting data in various
formats from the PyData ecosystem. hvPlot can integrate neatly with
individual PyData libraries if an extension mechanism for the native
plot APIs is offered, or it can be used as a standalone component.

%prep
%autosetup -p1 -n hvplot-%{version}
mkdir -p cache/xarray_tutorial_data
pushd cache/xarray_tutorial_data
tar -x -f %{SOURCE1} --strip-components=1
popd

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# set pooch cache dir
export XDG_CACHE_HOME=$(pwd)/cache
# no network
donttest="test_urls"
# not all packages for geographic projection support
donttest="$donttest or test_check_crs or test_explorer_geo_revise_kind"
# These tests cannot cast to 32-bit datatypes gh#holoviz/hvplot#560
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest+=" or test_aspect_and_frame_height_with_datashade"
  donttest+=" or test_aspect_with_datashade"
  donttest+=" or test_when_datashade_is_true"
  donttest+=" or test_when_datashade_is_true"
  donttest+=" or test_xlim_affects_x_range"
  donttest+=" or test_plot_resolution_with_rasterize"
fi
%pytest hvplot/tests/test* -n auto -ra -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/hvplot
%exclude %{python_sitelib}/hvplot/tests
%{python_sitelib}/hvplot-%{version}.dist-info
%endif

%changelog
