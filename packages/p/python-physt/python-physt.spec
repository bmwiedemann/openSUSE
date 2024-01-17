#
# spec file for package python-physt
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.5.3
Release:        0
Summary:        Python histogram library
License:        MIT
URL:            https://github.com/janpipek/physt
Source:         https://github.com/janpipek/physt/archive/v%{version}.tar.gz#/physt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-pandas
Recommends:     python-dask
Recommends:     python-folium
Recommends:     python-matplotlib
Recommends:     python-protobuf
Recommends:     python-uproot
Recommends:     python-vega3
Recommends:     python-xarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest}
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
%setup -q -n physt-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
