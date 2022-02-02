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


%{?!python_module:%define python_module() python3-%{**}}
%bcond_without  test
# https://github.com/holoviz/holoviews/pull/5174
%define pversion 1.14.8a1
Name:           python-holoviews
Version:        1.14.8~a1
Release:        0
Summary:        Composable, declarative visualizations for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/holoviz/holoviews
Source0:        https://files.pythonhosted.org/packages/source/h/holoviews/holoviews-%{pversion}.tar.gz
BuildRequires:  %{python_module colorcet}
BuildRequires:  %{python_module numpy >= 1.0}
BuildRequires:  %{python_module pandas >= 0.20}
BuildRequires:  %{python_module panel >= 0.8.0}
BuildRequires:  %{python_module param >= 1.9.3}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 0.7.4}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorcet
Requires:       python-numpy >= 1.0
Requires:       python-pandas >= 0.20
Requires:       python-panel >= 0.8.0
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
%if "%python_flavor" != "python2"
Suggests:       python-pyarrow < 1.0
Suggests:       python-ibis-framework >= 1.3
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module bokeh >= 2.2}
BuildRequires:  %{python_module dash >= 1.16}
BuildRequires:  %{python_module dask if %python-base < 3.10}
BuildRequires:  %{python_module datashader >= 0.11.1 if %python-base < 3.10}
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
%setup -q -n holoviews-%{pversion}
%autopatch -p1
sed -i '/"nose"/ d' setup.py

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

# wrong MPL api parameter expectations
# gh#holoviz/holoviews#4621
donttest+=" or (MPLRendererTest and test_get_size_column_plot)"
donttest+=" or (MPLRendererTest and test_get_size_row_plot)"
donttest+=" or (TestBokehUtils and test_py2js_funcformatter_arg_and_kwarg)"
donttest+=" or (TestBokehUtils and test_py2js_funcformatter_single_arg)"
donttest+=" or (TestBokehUtils and test_py2js_funcformatter_two_args)"
donttest+=" or (TestColorbarPlot and test_colormapper_clims)"
donttest+=" or (TestContoursPlot and test_contours_line_width_op_update)"
donttest+=" or (TestContoursPlot and test_contours_line_width_op)"
donttest+=" or (TestCrossBackendOptionPickling and test_builder_backend_switch_signature)"
donttest+=" or (TestCrossBackendOptionPickling and test_builder_cross_backend_validation)"
donttest+=" or (TestCrossBackendOptions and test_builder_backend_switch_signature)"
donttest+=" or (TestCrossBackendOptions and test_builder_cross_backend_validation)"
donttest+=" or (TestCurvePlot and test_curve_linewidth_op)"
donttest+=" or (TestCurvePlot and test_curve_style_mapping_constant_value_dimensions)"
donttest+=" or (TestCurvePlot and test_curve_style_mapping_ndoverlay_dimensions)"
donttest+=" or (TestElementPlot and test_element_zformatter_function)"
donttest+=" or (TestElementPlot and test_element_zformatter_instance)"
donttest+=" or (TestElementPlot and test_element_zformatter_string)"
donttest+=" or (TestErrorBarPlot and test_errorbars_line_color_op)"
donttest+=" or (TestErrorBarPlot and test_errorbars_line_width_op_update)"
donttest+=" or (TestErrorBarPlot and test_errorbars_line_width_op)"
donttest+=" or (TestHistogramPlot and test_histogram_line_color_op)"
donttest+=" or (TestHistogramPlot and test_histogram_line_width_op)"
donttest+=" or (TestHistogramPlot and test_op_ndoverlay_value)"
donttest+=" or (TestLabelsPlot and test_label_alpha_op_update)"
donttest+=" or (TestLabelsPlot and test_label_alpha_op)"
donttest+=" or (TestLabelsPlot and test_label_categorical_color_op)"
donttest+=" or (TestLabelsPlot and test_label_color_op_update)"
donttest+=" or (TestLabelsPlot and test_label_color_op)"
donttest+=" or (TestLabelsPlot and test_label_linear_color_op)"
donttest+=" or (TestLabelsPlot and test_label_rotation_op_update)"
donttest+=" or (TestLabelsPlot and test_label_rotation_op)"
donttest+=" or (TestLabelsPlot and test_label_size_op_update)"
donttest+=" or (TestLabelsPlot and test_label_size_op)"
donttest+=" or (TestLookupOptions and test_lookup_options_honors_backend)"
donttest+=" or (TestMplChordPlot and test_chord_nodes_categorically_colormapped)"
donttest+=" or (TestMplGraphPlot and test_graph_op_edge_line_width_update)"
donttest+=" or (TestMplGraphPlot and test_graph_op_edge_linewidth)"
donttest+=" or (TestMplGraphPlot and test_graph_op_node_linewidth_update)"
donttest+=" or (TestMplGraphPlot and test_graph_op_node_linewidth)"
donttest+=" or (TestMplGraphPlot and test_plot_graph_categorical_colored_nodes)"
donttest+=" or (TestMplGraphPlot and test_plot_graph_numerically_colored_nodes)"
donttest+=" or (TestMplTriMeshPlot and test_trimesh_op_edge_line_width)"
donttest+=" or (TestMplTriMeshPlot and test_trimesh_op_node_line_width)"
donttest+=" or (TestOptionsMethod and test_plot_options_keywords)"
donttest+=" or (TestOptionsMethod and test_plot_options_object_list)"
donttest+=" or (TestOptionsMethod and test_plot_options_one_object)"
donttest+=" or (TestOptionsMethod and test_plot_options_two_object)"
donttest+=" or (TestOptsMagic and test_cell_opts_style_dynamic)"
donttest+=" or (TestOptsMethod and test_opts_method_with_utility)"
donttest+=" or (TestOptsMethod and test_simple_clone_disabled)"
donttest+=" or (TestOptsMethod and test_simple_opts_clone_enabled)"
donttest+=" or (TestPathPlot and test_path_continuously_varying_line_width_op_update)"
donttest+=" or (TestPathPlot and test_path_continuously_varying_line_width_op)"
donttest+=" or (TestPlotDefinitions and test_matplotlib_plot_definitions)"
donttest+=" or (TestPointPlot and test_curve_padding_square_per_axis)"
donttest+=" or (TestPointPlot and test_point_fill_color_op)"
donttest+=" or (TestPointPlot and test_point_line_color_op_update)"
donttest+=" or (TestPointPlot and test_point_line_color_op)"
donttest+=" or (TestPointPlot and test_point_line_width_op_update)"
donttest+=" or (TestPointPlot and test_point_line_width_op)"
donttest+=" or (TestPointPlot and test_point_size_index_size_clash)"
donttest+=" or (TestPointPlot and test_point_size_op_update)"
donttest+=" or (TestPointPlot and test_point_size_op)"
donttest+=" or (TestPointPlot and test_points_padding_datetime_nonsquare)"
donttest+=" or (TestPointPlot and test_points_padding_datetime_square)"
donttest+=" or (TestPointPlot and test_points_sizes_scalar_update)"
donttest+=" or (TestPointPlot and test_scatter3d_colorbar_label)"
donttest+=" or (TestPointPlot and test_scatter3d_padding_hard_zrange)"
donttest+=" or (TestPointPlot and test_scatter3d_padding_logz)"
donttest+=" or (TestPointPlot and test_scatter3d_padding_nonsquare)"
donttest+=" or (TestPointPlot and test_scatter3d_padding_soft_zrange)"
donttest+=" or (TestPointPlot and test_scatter3d_padding_square)"
donttest+=" or (TestPointPlot and test_scatter3d_padding_unequal)"
donttest+=" or (TestPolygonPlot and test_polygons_line_width_op)"
donttest+=" or (TestSankeyPlot and test_sankey_label_index)"
donttest+=" or (TestSankeyPlot and test_sankey_simple)"
donttest+=" or (TestSpikesPlot and test_spikes_line_width_op_update)"
donttest+=" or (TestSpikesPlot and test_spikes_line_width_op)"
donttest+=" or (TestSpikesPlot and test_spikes_padding_datetime_nonsquare)"
donttest+=" or (TestSpikesPlot and test_spikes_padding_datetime_square_heights)"
donttest+=" or (TestSpikesPlot and test_spikes_padding_datetime_square)"
donttest+=" or (TestVectorFieldPlot and test_vectorfield_line_width_op_update)"
donttest+=" or (TestVectorFieldPlot and test_vectorfield_line_width_op)"

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

%pytest -o python_files='test*.py base.py' holoviews/tests -k "not (${donttest:4})"
%endif

%post
%python_install_alternative holoviews

%postun
%python_uninstall_alternative holoviews

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/holoviews
%{python_sitelib}/holoviews-%{pversion}*-info
%{python_sitelib}/holoviews/

%changelog
