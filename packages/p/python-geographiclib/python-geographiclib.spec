#
# spec file for package python-geographiclib
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
Name:           python-geographiclib
Version:        1.50
Release:        0
Summary:        Python geodesic routines
License:        MIT
Group:          Development/Languages/Python
URL:            https://geographiclib.sourceforge.io/
Source:         https://files.pythonhosted.org/packages/source/g/geographiclib/geographiclib-%{version}.tar.gz
Source1:        https://sourceforge.net/p/geographiclib/code/ci/master/tree/LICENSE.txt?format=raw#/LICENSE.txt
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a Python implementation of the geodesic routines from GeographicLib.

This contains implementations of the classes Math, Accumulator, Geodesic,
GeodesicLine and PolygonArea.

%prep
%setup -q -n geographiclib-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/geographiclib/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v geographiclib/test

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
