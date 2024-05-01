#
# spec file for package python-jplephem
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


Name:           python-jplephem
Version:        2.22
Release:        0
Summary:        Planet position predictor using a JPL ephemeris
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/brandon-rhodes/python-jplephem/
Source:         https://github.com/brandon-rhodes/python-jplephem/archive/%{version}.tar.gz#/jplephem-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd ci
%pyunittest -v test
popd

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jplephem
%{python_sitelib}/jplephem-%{version}.dist-info

%changelog
