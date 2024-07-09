#
# spec file for package python-holoviews
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


%bcond_without  test
%define skip_python39 1
Name:           python-holoviews
Version:        1.19.1
Release:        0
Summary:        Composable, declarative visualizations for Python
License:        BSD-3-Clause
URL:            https://github.com/holoviz/holoviews
Source0:        https://files.pythonhosted.org/packages/source/h/holoviews/holoviews-%{version}.tar.gz
Patch0:         ignore-pandas-warning.patch
BuildRequires:  %{python_module colorcet}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module numpy >= 1.21 with %python-numpy < 2}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 1.3}
BuildRequires:  %{python_module panel >= 1.0}
BuildRequires:  %{python_module param >= 1.12 with %python-param < 3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 2.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bokeh >= 3.1
Requires:       python-colorcet
Requires:       python-packaging
Requires:       python-pandas >= 1.3
Requires:       python-panel >= 1.0
Requires:       python-pyviz-comms >= 2.1
Requires:       (python-numpy >= 1.21 with python-numpy < 2)
Requires:       (python-param >= 1.12 with python-param < 3)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-ipython >= 5.4.0
Recommends:     python-matplotlib >= 3
Recommends:     python-notebook
Recommends:     python-pscript >= 0.7.1
Suggests:       python-networkx
Suggests:       python-Pillow
Suggests:       python-xarray >= 0.10.4
Suggests:       python-plotly >= 4.0
Suggests:       python-dash >= 1.16
Suggests:       python-streamz >= 0.5.0
Suggests:       python-datashader >= 0.11.1
Suggests:       python-ffmpeg-python
Suggests:       python-netCDF4
Suggests:       python-dask
Suggests:       python-scipy
Suggests:       python-shapely
Suggests:       python-scikit-image
Suggests:       python-pyarrow < 1.0
Suggests:       python-ibis-framework >= 1.3
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module contourpy}
BuildRequires:  %{python_module dash >= 1.16}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module datashader >= 0.11.1}
BuildRequires:  %{python_module deepdiff}
BuildRequires:  %{python_module ffmpeg-python}
BuildRequires:  %{python_module ipython >= 5.4.0}
BuildRequires:  %{python_module keyring}
BuildRequires:  %{python_module matplotlib >= 3}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbsmoke}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module plotly >= 4.0}
BuildRequires:  %{python_module pscript >= 0.7.1}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rfc3986}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module shapely}
BuildRequires:  %{python_module streamz >= 0.5.0}
BuildRequires:  %{python_module xarray >= 0.10.4}
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
%autosetup -p1 -n holoviews-%{version}
sed -i 's/, "--color=yes"//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/holoviews
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/holoviews/util/command.py
sed -i "s|^#!.*%{_bindir}/env python$|#!%__$python|" %{buildroot}%{$python_sitelib}/holoviews/util/command.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/holoviews/util/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/holoviews/util/
%fdupes %{buildroot}%{$python_sitelib}
}

%if %{with test}
%check
# Flaky
donttest="test_cell_opts_plot_float_division or test_cell_opts_style"
# These fail on 32-bit -- gh#holoviz/holoviews#4778
if [[ $(getconf LONG_BIT) -eq 32 ]]; then
    donttest+=" or (DatashaderAggregateTests and test_rasterize_regrid_and_spikes_overlay)"
    donttest+=" or (DatashaderAggregateTests and test_rgb_regrid_packed)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_image_string_aggregator)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_image)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_quadmesh_string_aggregator)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_quadmesh)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh_ds_aggregator)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh_node_explicit_vdim)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh_node_vdim_precedence)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh_string_aggregator)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh_vertex_vdims)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh_zero_range)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_trimesh)"
    donttest+=" or (DatashaderRegridTests and test_regrid_max)"
    donttest+=" or (DatashaderRegridTests and test_regrid_mean_xarray_transposed)"
    donttest+=" or (DatashaderRegridTests and test_regrid_mean)"
    donttest+=" or (DatashaderRegridTests and test_regrid_rgb_mean)"
    donttest+=" or (DatashaderRegridTests and test_regrid_upsampling)"
    donttest+=" or (DatashaderTestCase and test_datashade_curve)"
    donttest+=" or (TestDecollation and test_decollate_datashade_kdims_layout)"
    donttest+=" or (TestDecollation and test_decollate_datashade_kdims)"
    donttest+=" or (TestDecollation and test_decollate_spread)"
    donttest+=" or (TestDimTransforms and test_digitize)"
    donttest+=" or (TestLinkSelectionsBokeh and test_datashade_in_overlay_selection)"
    donttest+=" or (TestLinkSelectionsBokeh and test_datashade_selection)"
    donttest+=" or (TestLinkSelectionsPlotly and test_datashade_in_overlay_selection)"
    donttest+=" or (TestLinkSelectionsPlotly and test_datashade_selection)"
    donttest+=" or (TestPointerCallbacks and test_tap_datetime_out_of_bounds)"
    donttest+=" or (TestPointerCallbacks and test_pointer_x_datetime_out_of_bounds)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_dask_trimesh)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_dask_trimesh_implicit_nodes)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_dask_trimesh_with_node_vdims)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_pandas_trimesh_implicit_nodes)"
fi

%pytest -W ignore::UserWarning -n auto holoviews -k "not ($donttest)"
%endif

%post
%python_install_alternative holoviews

%postun
%python_uninstall_alternative holoviews

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/holoviews
%{python_sitelib}/holoviews-%{version}.dist-info
%{python_sitelib}/holoviews/

%changelog
