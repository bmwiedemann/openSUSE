#
# spec file for package python-geolib
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
Name:           python-geolib
Version:        1.0.7
Release:        0
Summary:        A library for geohash encoding, decoding and associated functions
License:        MIT
Group:          Development/Languages/Python
URL:            https://geolib.readthedocs.io/en/latest/
# does not include license, docs, tests: https://github.com/joyanujoy/geolib/issues/1
#Source:         https://files.pythonhosted.org/packages/source/g/geolib/geolib-%{version}.tar.gz
Source:         https://github.com/joyanujoy/geolib/archive/%{version}.tar.gz#/geolib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
# /SECTION
# SECTION docs requirements
BuildRequires:  python3-Sphinx
# /SECTION
BuildRequires:  fdupes
Requires:       python-future
BuildArch:      noarch

%python_subpackages

%description
A Python library for geohash encoding, decoding and finding neighbour cells.
This is a Python port of Chris Veness's Javascript implementation,
https://www.movable-type.co.uk/scripts/geohash.html .

%prep
%setup -q -n geolib-%{version}

%build
%python_build
pushd docs
make html
rm _build/html/.buildinfo
rm _build/html/.nojekyll
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}a

%check
%pytest

%files %{python_files}
%doc README.md docs/_build/html/
%license LICENSE
%{python_sitelib}/*

%changelog
