#
# spec file for package python-datashader
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
ExclusiveArch:  x86_64
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
BuildArch:      noarch
%endif

%{?sle15_python_module_pythons}
Name:           python-datashader%{psuffix}
Version:        0.16.3
Release:        0
Summary:        Data visualization toolchain based on aggregating into a grid
License:        BSD-3-Clause
URL:            https://datashader.org
# SourceRepository: https://github.com/holoviz/datashader
Source0:        https://files.pythonhosted.org/packages/source/d/datashader/datashader-%{version}.tar.gz
Source100:      python-datashader-rpmlintrc
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module multipledispatch}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module param}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyct}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-colorcet
Requires:       python-dask-dataframe
Requires:       python-multipledispatch
Requires:       python-numba
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-param
Requires:       python-pyct
Requires:       python-requests
Requires:       python-scipy
Requires:       python-toolz
Requires:       python-xarray
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if %{with test}
BuildRequires:  %{python_module bokeh >= 3.1}
BuildRequires:  %{python_module datashader = %{version}}
BuildRequires:  %{python_module fastparquet}
BuildRequires:  %{python_module matplotlib >= 3.3}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module nbsmoke >= 0.5.0}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module pyarrow}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-image}
%endif
%python_subpackages

%description
Traditional visualization systems treat plotting as a unitary process
transforming incoming data into an onscreen or printed image, with
parameters that can be specified beforehand that affect the final
result.  While this approach works for small collections of data that
can be viewed in their entirety, the visualization for large datasets
is often the only way to understand what the data consists of, and
there is no objective way to set the parameters to reveal this data.

The datashader library breaks up the rendering pipeline into a series
of stages where user-defined computations can be performed, allowing
the visualization to adapt to and reveal the underlying properties of
the dataset, i.e. the datashader pipeline allows computation *on
the visualization*, not just on the dataset, allowing it to do
automatic ranging and scaling that takes the current visualization
constraints into account.  For instance, where a traditional system
would use a transparency/opacity parameter to show the density of
overlapping points in a scatterplot, datashader can automatically
calculate how many datapoints are mapped to each pixel, scaling the
representation to accurately convey the data at every location, with no
saturation, overplotting, or underplotting issues.

%prep
%autosetup -p1 -n datashader-%{version}
sed -i -e '/^#!\//, 1d' examples/*.py
chmod -x examples/getting_started/2_Pipeline.ipynb

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/datashader
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
chmod a-x %{buildroot}%{$python_sitelib}/datashader/examples/filetimes.py
}
%endif

%if %{with test}
%check
export PYTHONPATH=examples
# skip known failing test with latest dask gh#holoviz/datashader#1032
donttest="test_raster_quadmesh_autorange_reversed[dask.array]"
%pytest datashader/tests --doctest-modules --doctest-ignore-import-errors -n auto -rsfE -k "not $donttest"
%endif

%if ! %{with test}
%post
%python_install_alternative datashader

%postun
%python_uninstall_alternative datashader

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/datashader
%{python_sitelib}/datashader
%{python_sitelib}/datashader-%{version}.dist-info
%endif

%changelog
