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
%define assaycommit 23c18c2457c035996057144e1fe74cd6e19b44eb
%define assayver    256.23c18c2
%define skip_python2 1
Name:           python-skyfield
Version:        1.27
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
# use generate-hipparcos.sh to download and truncate the test data
Source6:        hip_main.dat.gz
Source97:       generate-hipparcos.sh
# upstreams custom test runner assay: gh#skyfielders/python-skyfield#405
Source98:       https://github.com/brandon-rhodes/assay/archive/%{assaycommit}.tar.gz#/assay-master-%{assayver}.tar.gz
Source99:       python-skyfield-rpmlintrc
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module jplephem >= 2.13}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
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
%setup -q -n skyfield-%{version} -b 98
# copy all test data files into the rootdir from where the tests are run
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} ./

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH="../assay-%{assaycommit}"
%python_exec -m assay --batch skyfield.tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/skyfield
%{python_sitelib}/skyfield-%{version}-py*.egg-info

%changelog
