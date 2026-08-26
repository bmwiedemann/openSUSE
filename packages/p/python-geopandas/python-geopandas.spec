#
# spec file for package python-geopandas
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-geopandas%{psuffix}
Version:        1.1.4
Release:        0
Summary:        Geographic pandas extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://geopandas.org
# SourceRepository: https://github.com/geopandas/geopandas
# Use Repository for test data
Source0:        https://github.com/geopandas/geopandas/archive/refs/tags/v{%version}.tar.gz#/geopandas-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       proj
Requires:       python-numpy >= 2
Requires:       python-packaging
Requires:       python-pandas >= 2.2.0
Requires:       python-pyogrio >= 0.8
Requires:       python-pyproj >= 3.7
Requires:       python-shapely >= 2.1
Recommends:     python-geopy
Recommends:     python-matplotlib >= 3.9
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Fiona}
BuildRequires:  %{python_module Rtree}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module fsspec}
BuildRequires:  %{python_module geopandas = %{version}}
BuildRequires:  %{python_module geopy}
BuildRequires:  %{python_module matplotlib >= 3.9}
BuildRequires:  %{python_module psycopg >= 3.2}
BuildRequires:  %{python_module pyarrow >= 15}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sqlalchemy >= 2}
# mapclassify not yet available
#BuildRequires: %%{python_module mapclassify}
%endif
%python_subpackages

%description
Geopandas combines the capabilities of pandas and shapely, providing geospatial
operations in pandas and a high-level interface to multiple geometries to shapely.
GeoPandas enables you to easily do operations in python that would otherwise
require a spatial database such as PostGIS.

%prep
%autosetup -p1 -n geopandas-%{version}

%build
%if ! %{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
donttest="dummydonttest"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest="$donttest or test_explode or test_get_coordinates_parts"
fi
%pytest -n auto -rsfE -m "not web" -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/geopandas
%{python_sitelib}/geopandas-%{version}.dist-info
%endif

%changelog
