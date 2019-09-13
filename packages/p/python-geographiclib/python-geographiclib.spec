#
# spec file for package python-geographiclib
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-geographiclib
Version:        1.49
Release:        0
License:        MIT
Summary:        Python geodesic routines
Url:            https://geographiclib.sourceforge.io/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/g/geographiclib/geographiclib-%{version}.tar.gz
Source1:        https://sourceforge.net/p/geographiclib/code/ci/master/tree/LICENSE.txt?format=raw#/LICENSE.txt
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
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
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
