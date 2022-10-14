#
# spec file for package python-geopandas
#
# Copyright (c) 2022 SUSE LLC.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-geopandas
Version:        0.11.1
Release:        0
License:        BSD-3-Clause
Summary:        Geographic pandas extensions
Url:            http://geopandas.org
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/g/geopandas/geopandas-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module Fiona}
BuildRequires:  %{python_module folium}
# mapclassify not yet available
#BuildRequires: %%{python_module mapclassify}
BuildRequires:  %{python_module pandas >= 0.23.0}
BuildRequires:  %{python_module pygeos}
BuildRequires:  %{python_module pyproj}
BuildRequires:  %{python_module shapely}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module geopy}
BuildRequires:  %{python_module Rtree}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module scipy}
BuildRequires:  libgdal-devel
BuildRequires:  proj
BuildRequires:  proj-devel
# /SECTION
BuildRequires:  fdupes
Requires:       python-Fiona
Requires:       python-pandas >= 0.23.0
Requires:       python-pyproj
Requires:       python-shapely
Recommends:     python-geopy
Recommends:     python-matplotlib
BuildArch:      noarch

%python_subpackages

%description
Geopandas combines the capabilities of pandas and shapely, providing geospatial
operations in pandas and a high-level interface to multiple geometries to shapely.
GeoPandas enables you to easily do operations in python that would otherwise
require a spatial database such as PostGIS.

%prep
%setup -q -n geopandas-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs -k 'not test_overlay'

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/geopandas*/

%changelog
