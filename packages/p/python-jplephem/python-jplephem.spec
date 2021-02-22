#
# spec file for package python-jplephem
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
Name:           python-jplephem
Version:        2.15
Release:        0
Summary:        Planet position predictor using a JPL ephemeris
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/brandon-rhodes/python-jplephem/
Source:         https://github.com/brandon-rhodes/python-jplephem/archive/v%{version}.tar.gz#/python-jplephem-%{version}.tar.gz
# Test files
Source10:       http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp
Source11:       ftp://ssd.jpl.nasa.gov/pub/eph/planets/test-data/430/testpo.430
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
BuildArch:      noarch

%python_subpackages

%description
This package can load and use a Jet Propulsion Laboratory (JPL)
ephemeris for predicting the position and velocity of a planet or other
Solar System body.  It only needs NumPy <http://www.numpy.org/>`.

%prep
%setup -q -n python-jplephem-%{version}
cp %{SOURCE10} ci
cp %{SOURCE11} ci

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd ci
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m jplephem.jpltest
}
popd

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jplephem
%{python_sitelib}/jplephem-%{version}-py*.egg-info

%changelog
