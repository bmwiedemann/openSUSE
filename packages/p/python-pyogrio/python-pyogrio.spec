#
# spec file for package python-pyogrio
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pyogrio%{psuffix}
Version:        0.11.1
Release:        0
Summary:        Vectorized spatial vector file format I/O using GDAL/OGR
License:        MIT
URL:            https://github.com/geopandas/pyogrio
Source:         https://files.pythonhosted.org/packages/source/p/pyogrio/pyogrio-%{version}.tar.gz
Source99:       python-pyogrio.rpmlintrc
BuildRequires:  %{python_module Cython >= 0.29}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gdal-devel
BuildRequires:  python-rpm-macros
Requires:       gdal
Requires:       python-certifi
Requires:       python-numpy
Requires:       python-packaging
Requires:       python-sqlite3
Suggests:       python-Shapely >= 2
Suggests:       python-geopandas >= 0.12
Suggests:       python-pyarrow
%if %{with test}
BuildRequires:  %{python_module Shapely >= 2}
BuildRequires:  %{python_module geopandas >= 0.12}
BuildRequires:  %{python_module pyarrow}
BuildRequires:  %{python_module pyogrio = %{version}}
BuildRequires:  %{python_module pyproj}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Pyogrio provides a GeoPandas-oriented API to OGR vector
data sources, such as ESRI Shapefile, GeoPackage, and GeoJSON. Vector data sources
have geometries, such as points, lines, or polygons, and associated records
with potentially many columns worth of data.

Pyogrio uses a vectorized approach for reading and writing GeoDataFrames to and
from OGR vector data sources in order to give you faster interoperability. It
uses pre-compiled bindings for GDAL/OGR so that the performance is primarily
limited by the underlying I/O speed of data source drivers in GDAL/OGR rather
than multiple steps of converting to and from Python data types within Python.

%prep
%autosetup -p1 -n pyogrio-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%{python_expand #
sed -i /arrow_bridge\.h/d %{buildroot}%{$python_sitearch}/pyogrio-%{version}.dist-info/RECORD
sed -i /_io\.pxd/d %{buildroot}%{$python_sitearch}/pyogrio-%{version}.dist-info/RECORD
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
# missing network mark
donttest="test_url_dataframe"
mv pyogrio pyogrio.src
%pytest_arch --pyargs pyogrio.tests -m "not network" -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/pyogrio
%{python_sitearch}/pyogrio-%{version}.dist-info
%endif

%changelog
