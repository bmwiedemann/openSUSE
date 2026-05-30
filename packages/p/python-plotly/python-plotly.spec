#
# spec file for package python-plotly
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without  libalternatives
%define distversion 6.7
Name:           python-plotly
Version:        6.7.0
Release:        0
Summary:        Interactive, browser-based graphing library for Python
License:        MIT
URL:            https://github.com/plotly/plotly.py
# Use the GitHub archive for the test suite
Source0:        https://github.com/plotly/plotly.py/archive/refs/tags/v%{version}.tar.gz#/plotly.py-%{version}-gh.tar.gz
# package-lock.json file generated with command in js/: `npm install` without the recommended flags. Apply Patch0 before.
Source10:       package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source11:       node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
# PATCH-FIX-OPENSUSE plotly-update-js-dependencies.patch code@bnavigator.de -- Update for local-npm-registry
Patch0:         plotly-update-js-dependencies.patch
# PATCH-FIX-OPENSUSE plotly-no-install.json.patch code@bnavigator.de -- Remove install.json from python package install
Patch1:         plotly-no-install.json.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module hatchling >= 1.26}
BuildRequires:  %{python_module jupyterlab >= 3}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-narwhals >= 1.15.1
Requires:       python-packaging
Recommends:     jupyter-plotly
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
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module narwhals >= 1.15.1}
BuildRequires:  %{python_module numpy >= 1.22}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pdfrw}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyshp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image if %python-base >= 3.12}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module statsmodels}
BuildRequires:  %{python_module xarray if %python-base >= 3.12}
# /SECTION
%python_subpackages

%description
An interactive, open-source, and browser-based graphing library for Python.

Built on top of plotly.js, plotly.py is a high-level, declarative charting library.
plotly.js ships with over 30 chart types, including scientific charts,
3D graphs, statistical charts, SVG maps, financial charts, and more.

Plotly graphs can be viewed in Jupyter notebooks, other Python notebook
software such as marimo, as standalone HTML files, or integrated into Dash applications.

%package     -n jupyter-plotly
Summary:        Jupyter integration for %{name}
Provides:       jupyterlab-plotly = %{version}-%{release}
Requires:       python3dist(plotly) = %{distversion}
Suggests:       python3-plotly

%description -n jupyter-plotly
An interactive, open-source, and browser-based graphing library for Python.

Built on top of plotly.js, plotly.py is a high-level, declarative charting library.
plotly.js ships with over 30 chart types, including scientific charts,
3D graphs, statistical charts, SVG maps, financial charts, and more.

Plotly graphs can be viewed in Jupyter notebooks, other Python notebook
software such as marimo, as standalone HTML files, or integrated into Dash applications.

This package provides the flavorless configuration for the
Jupyterlab integration and widgets.

%prep
%autosetup -p1 -n plotly.py-%{version}
pushd js
rm package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --include=peer
popd
# remove script interpreter line in non-executable script
sed -i '1{/env python/ d}' _plotly_utils/png.py
chmod -x _plotly_utils/png.py
# homogenize mtime of all __init__.py files for deduplicated compile cache consistency
find . -name __init__.py -exec touch -m -r plotly/__init__.py '{}' ';'

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
%python_clone -a %{buildroot}%{_bindir}/plotly_get_chrome

%check
# API parameter mismatch
donttest="test_described_subscript_error_on_type_error"
%pytest tests/test_core -k "not ($donttest)"
# not available
donttest="test_kaleido"
donttest="$donttest or test_px_input and (vaex or polars)"
# API parameter mismatches and precision errors
donttest="$donttest or test_matplotlylib"
# flaky timing error
donttest="$donttest or test_fast_track_finite_arrays"
# no scikit-image for python311 anymore
python311_donttest=" or TestTernarycontour"
# Optional dependencies not yet in openSUSE, requires python-polars
# --ignore doesn't work because the import is in the conftest.py
rm -rf tests/test_optional/test_px/
%pytest tests/test_optional -k "not ($donttest ${$python_donttest})"

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/_plotly_utils/
%{python_sitelib}/plotly/
%{python_sitelib}/plotly-%{version}.dist-info
%python_alternative %{_bindir}/plotly_get_chrome

%files -n jupyter-plotly
%license LICENSE.txt
%{_jupyter_labextensions_dir3}/jupyterlab-plotly/

%changelog
