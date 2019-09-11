#
# spec file for package python-jplephem
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-jplephem
Version:        2.9
Release:        0
Summary:        Planet position predictor using a JPL ephemeris
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/brandon-rhodes/python-jplephem/
Source:         https://files.pythonhosted.org/packages/source/j/jplephem/jplephem-%{version}.tar.gz
# Test files
Source10:       http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de405.bsp
Source11:       http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de421.bsp
Source12:       http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp
Source13:       ftp://ssd.jpl.nasa.gov/pub/eph/planets/test-data/430/testpo.430
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
%setup -q -n jplephem-%{version}
cp %{SOURCE10} .
cp %{SOURCE11} .
cp %{SOURCE12} .
cp %{SOURCE13} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m jplephem.jpltest

%files %{python_files}
%{python_sitelib}/*

%changelog
