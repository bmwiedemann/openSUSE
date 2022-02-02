#
# spec file
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
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
%define         skip_python2 1
# dask is not compatible with Python 3.10 yet
%define         skip_python310 1
Name:           python-datashader%{psuffix}
Version:        0.13.0
Release:        0
Summary:        Data visualization toolchain based on aggregating into a grid
License:        BSD-3-Clause
URL:            https://datashader.org
Source0:        https://files.pythonhosted.org/packages/source/d/datashader/datashader-%{version}.tar.gz
Patch0:         datashader-pr1022-RaggedTests.patch
Patch1:         datashader-pr1025-testfixes.patch
Source100:      python-datashader-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module param >= 1.6.1}
BuildRequires:  %{python_module pyct >= 0.4.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-DataShape >= 0.5.1
Requires:       python-Pillow >= 3.1.1
Requires:       python-PyYAML
Requires:       python-bokeh
Requires:       python-colorcet >= 0.9.0
Requires:       python-dask-all >= 0.18.0
Requires:       python-numba >= 0.51
Requires:       python-numpy >= 1.7
Requires:       python-pandas >= 0.24.1
Requires:       python-param >= 1.6.1
Requires:       python-pyct >= 0.4.5
Requires:       python-scikit-image
Requires:       python-scipy
Requires:       python-xarray >= 0.9.6
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if %{with test}
BuildRequires:  %{python_module DataShape >= 0.5.1}
BuildRequires:  %{python_module Pillow >= 3.1.1}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module colorcet >= 0.9.0}
BuildRequires:  %{python_module dask-all >= 0.18.0}
BuildRequires:  %{python_module fastparquet >= 0.1.6}
BuildRequires:  %{python_module holoviews >= 1.10.0}
BuildRequires:  %{python_module nbsmoke >= 0.5.0}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module numba >= 0.51}
BuildRequires:  %{python_module numpy >= 1.7}
BuildRequires:  %{python_module pandas >= 0.24.1}
BuildRequires:  %{python_module pytest >= 3.9.3}
BuildRequires:  %{python_module pytest-benchmark >= 3.0.0}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module xarray >= 0.9.6}
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

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/datashader
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
chmod a-x %{buildroot}%{$python_sitelib}/datashader/examples/filetimes.py
}
%endif

%if %{with test}
%check
export PYTHONPATH=examples
# https://github.com/holoviz/datashader/issues/1043
donttest="(TestRaggedGetitem and test_getitem_invalid)"
donttest+=" or (TestRaggedInterface and test_tolist)"
donttest+=" or (TestRaggedMethods and test_where_series)"
%pytest datashader/tests --doctest-modules --doctest-ignore-import-errors -k "not ($donttest)"
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
%{python_sitelib}/datashader-%{version}*-info
%endif

%changelog
