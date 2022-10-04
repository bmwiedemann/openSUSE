#
# spec file for package python-Shapely
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


%{?!python_module:%define python_module() python3-%{**}}
%bcond_without test
%define skip_python2 1
Name:           python-Shapely
Version:        1.8.4
Release:        0
Summary:        Geospatial geometries, predicates, and operations
License:        BSD-3-Clause
URL:            https://github.com/shapely/shapely
Source:         https://files.pythonhosted.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  geos-devel >= 3.5
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} > 1320
BuildRequires:  %{python_module matplotlib}
%endif
# Shapely calls the GEOS libs libgeos and libgeos_c via ctypes in python scripts, undetected by rpm ld analyzer.
# (libgeos_c1 is detected due to some Cython optimized lib, but libgeos3 is not)
# use requires_eq in order to be detectable by the python_subpackages rewriter
%requires_eq    %(rpm -q --requires geos-devel | grep libgeos)
Recommends:     python-numpy
Provides:       python-shapely = %{version}-%{release}
Obsoletes:      python-shapely < %{version}-%{release}
%python_subpackages

%description
Shapely is a Python package for manipulation and analysis of
planar geometric objects. It is based on the GEOS (the
engine of PostGIS) and JTS (from which GEOS is ported) libraries.
Shapely is not concerned with data formats or coordinate systems,
but can be readily integrated with packages that are like WorldMill
and pyproj.

%prep
%autosetup -p1 -n Shapely-%{version}

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
%python_expand rm %{buildroot}%{$python_sitearch}/shapely/*/*.c

%check
# make sure not to import the source dir without compiled shapely.vectorized during tests
mkdir testenv
cp -r tests setup.cfg testenv
pushd testenv
%pytest_arch -ra
popd

%files %{python_files}
%license LICENSE.txt
%doc CREDITS.txt README.rst docs/*
%{python_sitearch}/shapely
%{python_sitearch}/Shapely-%{version}*-info

%changelog
