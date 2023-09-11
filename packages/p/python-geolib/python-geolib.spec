#
# spec file for package python-geolib
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-geolib
Version:        1.0.7
Release:        0
Summary:        A library for geohash encoding, decoding and associated functions
License:        MIT
URL:            https://geolib.readthedocs.io/en/latest/
Source:         https://github.com/joyanujoy/geolib/archive/%{version}.tar.gz#/geolib-%{version}.tar.gz
Patch0:         fix-setup.py.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
# SECTION docs requirements
BuildRequires:  python3-Sphinx
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A Python library for geohash encoding, decoding and finding neighbour cells.
This is a Python port of Chris Veness's Javascript implementation,
https://www.movable-type.co.uk/scripts/geohash.html .

%prep
%autosetup -p1 -n geolib-%{version}

%build
%pyproject_wheel
pushd docs
make html
rm _build/html/.buildinfo
rm _build/html/.nojekyll
popd

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md docs/_build/html/
%license LICENSE
%{python_sitelib}/geolib
%{python_sitelib}/geolib-%{version}.dist-info

%changelog
