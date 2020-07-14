#
# spec file for package python-skyfield
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
%define skip_python2 1
%ifarch %{ix86}
%define skyfield_atol export SKYFIELD_TEST_DEFAULT_ATOL=2e-16
%endif
Name:           python-skyfield
Version:        1.23
Release:        0
Summary:        Elegant astronomy for Python
License:        MIT
URL:            https://github.com/skyfielders/python-skyfield/
Source0:        https://files.pythonhosted.org/packages/source/s/skyfield/skyfield-%{version}.tar.gz
# Test data that is needed by the unit tests and would be downloaded on networking hosts
Source1:        https://naif.jpl.nasa.gov/pub/naif/generic_kernels/fk/satellites/moon_080317.tf
Source2:        https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/moon_pa_de421_1900-2050.bpc
Source3:        https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/a_old_versions/pck00008.tpc
Source4:        ftp://ssd.jpl.nasa.gov/pub/eph/planets/bsp/de405.bsp
Source5:        ftp://ssd.jpl.nasa.gov/pub/eph/planets/bsp/de421.bsp
Source6:        ftp://cddis.nasa.gov/products/iers/deltat.data
Source7:        ftp://cddis.nasa.gov/products/iers/deltat.preds
Source8:        https://hpiers.obspm.fr/iers/bul/bulc/Leap_Second.dat
Source9:        http://cdsarc.u-strasbg.fr/ftp/cats/I/239/hip_main.dat.gz
Source99:       python-skyfield-rpmlintrc
# PR404 Refine some float comparisons in the unit tests for flaky platforms
Patch0:         https://github.com/skyfielders/python-skyfield/pull/404.patch#/skyfield-pr404-comparefloat.patch
# PR405 Replace upstreams custom testrunner 'assay' with standard pytest (first commit the rest is git repository specific)
# https://github.com/skyfielders/python-skyfield/pull/405
Patch1:         https://github.com/skyfielders/python-skyfield/pull/405/commits/cc229382ea8f301a1d911f228482feb043fc4db1.patch#/skyfield-pr405-replace-assay-by-pytest.patch
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module jplephem >= 2.13}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sgp4 >= 2.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy
Requires:       python-beautifulsoup4
Requires:       python-certifi
Requires:       python-html5lib
Requires:       python-jplephem >= 2.13
Requires:       python-lxml
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-sgp4 >= 2.2
BuildArch:      noarch
%python_subpackages

%description
A Python astronomy package that makes it easy to generate high precision
research-grade positions for planets and Earth satellites.

%prep
%setup -q -n skyfield-%{version}
%autopatch -p1
# copy all test data files into the rootdir
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} ./

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/skyfielders/python-skyfield/pull/404
%{?skyfield_atol}
%pytest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/skyfield
%{python_sitelib}/skyfield-%{version}-py*.egg-info

%changelog
