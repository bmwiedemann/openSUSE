#
# spec file for package python-holoviews
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


%bcond_without  test
Name:           python-holoviews
Version:        1.15.2
Release:        0
Summary:        Composable, declarative visualizations for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/holoviz/holoviews
Source0:        https://files.pythonhosted.org/packages/source/h/holoviews/holoviews-%{version}.tar.gz
Source99:       python-holoviews-rpmlintrc
BuildRequires:  %{python_module colorcet}
BuildRequires:  %{python_module numpy >= 1.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 0.20}
BuildRequires:  %{python_module panel >= 0.13.1}
BuildRequires:  %{python_module param >= 1.9.3}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 0.7.4}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorcet
Requires:       python-numpy >= 1.0
Requires:       python-packaging
Requires:       python-pandas >= 0.20
Requires:       python-panel >= 0.13.1
Requires:       python-param >= 1.9.3
Requires:       python-pyviz-comms >= 0.7.4
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-bokeh >= 2.2
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
# Upstream doesn't specify the upper pin and relies on panel,
# see https://github.com/holoviz/holoviews/pull/5507,
# but we need to pin it here in order to avoid obs resolver conflicts
BuildRequires:  %{python_module bokeh >= 2.4.3 with %python-bokeh < 2.5}
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
%setup -q -n holoviews-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
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
#different size in MPL >= 3.3
donttest="(MPLRendererTest and test_get_size)"
# gh#holoviz/holoviews#5517
donttest+=" or test_py2js_funcformatter"
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
    donttest+=" or (TestPointerCallbacks and test_pointer_x_datetime_out_of_bounds)"
    donttest+=" or (TestPointerCallbacks and test_tap_datetime_out_of_bounds)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_dask_trimesh)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_dask_trimesh_implicit_nodes)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_dask_trimesh_with_node_vdims)"
    donttest+=" or (DatashaderRasterizeTests and test_rasterize_pandas_trimesh_implicit_nodes)"
fi
%pytest holoviews -k "not ($donttest)"
%endif

%post
%python_install_alternative holoviews

%postun
%python_uninstall_alternative holoviews

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/holoviews
%{python_sitelib}/holoviews-%{version}*-info
%{python_sitelib}/holoviews/

%changelog
