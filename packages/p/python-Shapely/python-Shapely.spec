#
# spec file for package python-Shapely
#
# Copyright (c) 2020 SUSE LLC
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
%define oldpython python
%bcond_without test
Name:           python-Shapely
Version:        1.7.1
Release:        0
Summary:        Geospatial geometries, predicates, and operations
License:        BSD-3-Clause
URL:            https://github.com/Toblerity/Shapely
Source:         https://files.pythonhosted.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.19}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  geos-devel >= 3.3
BuildRequires:  python-rpm-macros
Requires:       geos >= 3.3
# SECTION test requirements
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} > 1320
BuildRequires:  %{python_module matplotlib}
%endif
# /SECTION
%ifpython2
Obsoletes:      %{oldpython}-shapely < %{version}
Provides:       %{oldpython}-shapely = %{version}
%endif
%ifpython3
Obsoletes:      python3-shapely < %{version}
Provides:       python3-shapely = %{version}
%endif
%python_subpackages

%description
Shapely is a Python package for manipulation and analysis of
planar geometric objects. It is based on the GEOS (the
engine of PostGIS) and JTS (from which GEOS is ported) libraries.
Shapely is not concerned with data formats or coordinate systems,
but can be readily integrated with packages that are like WorldMill
and pyproj.

%prep
%setup -q -n Shapely-%{version}

%build
CFLAGS="%{optflags} `geos-config --cflags` LDFLAGS=`geos-config --clibs`"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Those are just needed to build cython extension
# Not for distribute
rm -fv %{buildroot}%{_prefix}/shapely/_geos.pxi
rm -frv %{buildroot}%{_prefix}/shapely

%check
mv shapely shapely_temp
%pytest_arch
mv shapely_temp shapely

%files %{python_files}
%license LICENSE.txt
%doc CREDITS.txt README.rst docs/*
%{python_sitearch}/*

%changelog
