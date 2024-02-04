#
# spec file for package python-skyfield
#
# Copyright (c) 2024 SUSE LLC
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


%define assaycommit bb62d1f7d51d798b05a88045fff3a2ff92c299c3
%define assayver    264.bb62d1f
Name:           python-skyfield
Version:        1.47
Release:        0
Summary:        Elegant astronomy for Python
License:        MIT
URL:            https://github.com/skyfielders/python-skyfield/
Source0:        https://files.pythonhosted.org/packages/source/s/skyfield/skyfield-%{version}.tar.gz
# Test data that is needed by the unit tests and would be downloaded on networking hosts
Source1:        https://naif.jpl.nasa.gov/pub/naif/generic_kernels/fk/satellites/moon_080317.tf
Source2:        https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/moon_pa_de421_1900-2050.bpc
Source3:        https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/a_old_versions/pck00008.tpc
Source4:        https://ssd.jpl.nasa.gov/ftp/eph/planets/bsp/de405.bsp
Source5:        https://ssd.jpl.nasa.gov/ftp/eph/planets/bsp/de421.bsp
# use generate-hipparcos.sh to download and truncate the test data
Source6:        hip_main.dat.gz
Source7:        https://datacenter.iers.org/data/9/finals2000A.all
# Original with invalid https certificate or http url: http://astro.ukho.gov.uk/nao/lvm/Table-S15.2020.txt
Source8:        https://github.com/skyfielders/python-skyfield/raw/%{version}/Table-S15.2020.txt
Source9:        https://github.com/skyfielders/python-skyfield/raw/%{version}/ci/tyc_main_head.dat
Source97:       generate-hipparcos.sh
# upstreams custom test runner assay: gh#skyfielders/python-skyfield#405
Source98:       https://github.com/brandon-rhodes/assay/archive/%{assaycommit}.tar.gz#/assay-master-%{assayver}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test
BuildRequires:  %{python_module certifi  >= 2017.4.17}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module jplephem >= 2.13}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module sgp4 >= 2.2}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi >= 2017.4.17
Requires:       python-jplephem >= 2.13
Requires:       python-numpy
Requires:       python-sgp4 >= 2.2
Recommends:     python-astropy
Recommends:     python-matplotlib
Recommends:     python-pandas
BuildArch:      noarch
%python_subpackages

%description
A Python astronomy package that makes it easy to generate high precision
research-grade positions for planets and Earth satellites.

%prep
%setup -q -n skyfield-%{version} -b 98
# copy all test data files into the rootdir from where the tests are run
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} ./

# allow some float error for all platforms -- gh#skyfielders/python-skyfield#582
sed -i 's/if IS_32_BIT/if True/' skyfield/tests/test_planetarylib.py
sed -i 's/assert abs(distance.au - 1) < 1e-16/assert abs(distance.au - 1) < 1e-15/' skyfield/tests/test_positions.py

%build
export SKYFIELD_USE_SETUPTOOLS=1
%pyproject_wheel

%install
export SKYFIELD_USE_SETUPTOOLS=1
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH="../assay-%{assaycommit}"
%{python_expand #
if [ %{$python_version_nodots} -lt 311 ]; then
  $python -m assay --batch skyfield.tests
else
  # assay not compatible, at least test that we import. gh#brandon-rhodes/assay#15
  $python -c 'import skyfield'
fi
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/skyfield
%{python_sitelib}/skyfield-%{version}.dist-info

%changelog
