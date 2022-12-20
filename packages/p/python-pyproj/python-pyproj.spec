#
# spec file for package python-pyproj
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


%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python3-%{**}}
Name:           python-pyproj
Version:        3.4.1
Release:        0
Summary:        Python interface to PROJ library
License:        SUSE-Public-Domain AND X11
Group:          Development/Languages/Python
URL:            https://github.com/pyproj4/pyproj
Source:         https://files.pythonhosted.org/packages/source/p/pyproj/pyproj-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.28.4}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  proj
BuildRequires:  proj-devel >= 8
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires(post): update-alternatives
Requires(postun):update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xarray}
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

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyproj
%python_expand rm -rf  %{buildroot}%{$python_sitearch}/test
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pyproj pyproj_temp
export PROJ_DIR=$(pkg-config --variable=libdir proj)
%{python_expand # Multiline
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c "import pyproj; pyproj.Proj(init='epsg:4269')"
}
# Reset to remove wrong flavor path from loop above
export PYTHONPATH=""
%pytest_arch -rs -k "not (network or test_transformer_group__get_transform_crs)"
mv pyproj_temp pyproj

%post
%python_install_alternative pyproj

%postun
%python_uninstall_alternative pyproj

%files %{python_files}
%python_alternative %{_bindir}/pyproj
%license LICENSE
%doc README.md
%{python_sitearch}/pyproj
%{python_sitearch}/pyproj-%{version}*-info

%changelog
