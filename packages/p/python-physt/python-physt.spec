#
# spec file for package python-physt
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-physt
Version:        0.8.5
Release:        0
Summary:        Python histogram library
License:        MIT
URL:            https://github.com/janpipek/physt
Source:         https://github.com/janpipek/physt/archive/v%{version}.tar.gz#/physt-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 65}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hypothesis >= 6.96.1
Requires:       python-numpy >= 1.25
Requires:       python-packaging
Requires:       python-typing-extensions
Recommends:     python-astropy >= 6
Recommends:     python-dask-array >= 2023.0
Recommends:     python-folium
Recommends:     python-matplotlib
Recommends:     python-pandas
Recommends:     python-xarray
Suggests:       python-plotly
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module dask-array >= 2023.0}
BuildRequires:  %{python_module hypothesis >= 6.96.1}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy >= 1.25}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
%python_subpackages

%description
P(i/y)thon h(i/y)stograms. Inspired (and based on) numpy.histogram.

The unifies different concepts of histograms as occurring in numpy,
pandas, matplotlib, ROOT, etc. and to create one representation that
can be manipulated with from the data point of view and at the same
time provides integration into IPython notebook and various plotting
options.

%prep
%autosetup -p1 -n physt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no polars
ignore="--ignore tests/compat/test_polars.py"
# gh#janpipek/physt#121
python313_donttest=("-k" "not test_zero_statistics")
%pytest $ignore "${$python_donttest[@]}"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/physt
%{python_sitelib}/physt-%{version}.dist-info

%changelog
