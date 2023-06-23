#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-geopandas%{psuffix}
Version:        0.13.2
Release:        0
Summary:        Geographic pandas extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://geopandas.org
Source:         https://files.pythonhosted.org/packages/source/g/geopandas/geopandas-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       proj
Requires:       python-Fiona >= 1.8.19
Requires:       python-packaging
Requires:       python-pandas >= 1.1.0
Requires:       python-pyproj >= 3.0.1
Requires:       python-shapely >= 1.7.1
Recommends:     python-geopy
Recommends:     python-matplotlib
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Rtree}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module fsspec}
BuildRequires:  %{python_module geopandas = %{version}}
BuildRequires:  %{python_module geopy}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pyarrow}
BuildRequires:  %{python_module pygeos >= 0.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sqlalchemy}
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
# online resource
donttest="test_read_file_url"
# test files missing in sdist
donttest="$donttest or test_overlay"
donttest="$donttest or (test_arrow and (test_read_versioned_file or test_read_gdal_file))"
# wrong shapely type
donttest="$donttest or (test_geom_methods and test_sample_points_array)"
donttest="$donttest or (test_random and test_uniform and geom)"
%pytest -rsfE -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/geopandas
%{python_sitelib}/geopandas-%{version}.dist-info
%endif

%changelog
