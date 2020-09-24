#
# spec file for package python-pyproj
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyproj
Version:        2.6.1.post1
Release:        0
Summary:        Python interface to PROJ library
License:        SUSE-Public-Domain AND X11
Group:          Development/Languages/Python
URL:            https://github.com/pyproj4/pyproj
Source:         https://files.pythonhosted.org/packages/source/p/pyproj/pyproj-%{version}.tar.gz
Patch0:         pyproj-3.0.0-TST-Update-tests-with-scope-remarks-649.patch
BuildRequires:  %{python_module Cython} >= 0.23.5
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  proj
BuildRequires:  proj-devel >= 6.2.0
BuildRequires:  python-rpm-macros
Requires:       python-aenum
Requires:       python-numpy
# SECTION test requirements
BuildRequires:  %{python_module cov-core}
BuildRequires:  %{python_module coverage} >= 4.0
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
# /SECTION
%python_subpackages

%description
Performs cartographic transformations and geodetic computations.

The Proj class can convert from geographic (longitude,latitude) to native map
projection (x,y) coordinates and vice versa, or from one map projection
coordinate system directly to another.

The Geod class can perform forward and inverse geodetic, or Great Circle,
computations. The forward computation involves determining latitude, longitude
and back azimuth of a terminus point given the latitude and longitude of an
initial point, plus azimuth and distance. The inverse computation involves
determining the forward and back azimuths and distance given the latitudes and
longitudes of an initial and terminus point.

Input coordinates can be given as python arrays, lists/tuples, scalars or
numpy/Numeric/numarray arrays. Optimized for objects that support the Python
buffer protocol (regular python and numpy array objects).

This project has a git repository https://github.com/pyproj4/pyproj
where you may access the most up-to-date source.

%prep
%setup -q -n pyproj-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pyproj pyproj_temp
export PROJ_DIR=$(pkg-config --variable=libdir proj)
%{python_expand # Multiline
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c "import pyproj; pyproj.Proj(init='epsg:4269')"
py.test-%{$python_bin_suffix} --ignore=_build.python2 --ignore=_build.python3 --ignore=_build.pypy3 -v
}
mv pyproj_temp pyproj

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/*

%changelog
