#
# spec file for package python-geojson
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
Name:           python-geojson
Version:        2.5.0
Release:        0
Summary:        Python bindings and utilities for GeoJSON
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/python-geojson
Source:         https://files.pythonhosted.org/packages/source/g/geojson/geojson-%{version}.tar.gz
# PATCH-FIX-UPSTREAM geojson-py39-jsonload.patch -- gh#jazzband/python-geojson#151
Patch0:         https://github.com/jazzband/geojson/pull/151.patch#/geojson-py39-jsonload.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library contains functions for encoding and decoding GeoJSON formatted
data, classes for all GeoJSON Objects and an implementation of the Python
geo interface specification.

%prep
%autosetup -p1 -n geojson-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pyunittest -v

%files %{python_files}
%license LICENSE.rst
%doc README.rst CHANGELOG.rst
%{python_sitelib}/geojson
%{python_sitelib}/geojson-%{version}*-info

%changelog
