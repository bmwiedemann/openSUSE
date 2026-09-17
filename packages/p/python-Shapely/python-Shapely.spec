#
# spec file for package python-Shapely
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


%{?sle15_python_module_pythons}
Name:           python-Shapely
Version:        2.1.2
Release:        0
Summary:        Geospatial geometries, predicates, and operations
License:        BSD-3-Clause
URL:            https://github.com/shapely/shapely
Source:         https://files.pythonhosted.org/packages/source/s/shapely/shapely-%{version}.tar.gz
# PATCH-FIX-UPSTREAM TST_update_tests_for_GEOS_3_15.patch -- based on commit 639ff48319ac008841f02be597fd5fae3ddb4f23
Patch0:         TST_update_tests_for_GEOS_3_15.patch
# PATCH-FIX-UPSTREAM TST-fix-test_set_precision_collapse-with-normalized-.patch -- based on commit 703df27ec61bef4e2ebacfc791c0c01947ae47a8
Patch1:         TST-fix-test_set_precision_collapse-with-normalized-.patch
# PATCH-FIX-UPSTREAM TST-change-test_remove_repeated_points_invalid_resul.patch -- based on commit 9cca2e074cd9f695a99e3c884919eb18f99328d6
Patch2:         TST-change-test_remove_repeated_points_invalid_resul.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test
BuildRequires:  %{python_module pytest}
# Don't test with matplotlib until 15.x has python311-matplotlib.
# (It's currently in devel:languages:python:backports but not in the Leap :Update repositories)
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module matplotlib}
%endif
# /SECTION
BuildRequires:  fdupes
BuildRequires:  geos-devel >= 3.5
BuildRequires:  python-rpm-macros
# Shapely calls the GEOS libs libgeos and libgeos_c via ctypes in python scripts, undetected by rpm ld analyzer.
# (libgeos_c1 is detected due to some Cython optimized lib, but libgeos3 is not)
Requires:       %(rpm -q --requires geos-devel | sed -rne 's/^(libgeos3.* = .*)-.*/\1/p')
Requires:       (python-numpy >= 1.14 with python-numpy < 3)
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
%autosetup -p 1 -n shapely-%{version}

%build
CFLAGS="%{optflags} `geos-config --cflags` LDFLAGS=`geos-config --clibs`"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# make sure not to import the source dir without compiled shapely.vectorized during tests
mkdir testenv
cp -r shapely/tests setup.cfg testenv
pushd testenv
%pytest_arch -ra
popd

%files %{python_files}
%license LICENSE.txt
%doc CREDITS.txt README.rst docs/*
%{python_sitearch}/shapely
%{python_sitearch}/shapely-%{version}.dist-info

%changelog
