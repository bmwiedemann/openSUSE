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
Version:        0.11.1
Release:        0
Summary:        Geographic pandas extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://geopandas.org
Source:         https://files.pythonhosted.org/packages/source/g/geopandas/geopandas-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Fiona
Requires:       python-pandas >= 0.23.0
Requires:       python-pyproj
Requires:       python-shapely
Recommends:     python-geopy
Recommends:     python-matplotlib
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Fiona}
BuildRequires:  %{python_module Rtree}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module geopy}
BuildRequires:  %{python_module matplotlib}
# mapclassify not yet available
#BuildRequires: %%{python_module mapclassify}
BuildRequires:  %{python_module pandas >= 0.23.0}
BuildRequires:  %{python_module pygeos}
BuildRequires:  %{python_module pyproj}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module shapely}
BuildRequires:  libgdal-devel
BuildRequires:  proj
BuildRequires:  proj-devel
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
%if ! %{with wheel}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest -rs -k 'not test_overlay'
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/geopandas*/
%endif

%changelog
