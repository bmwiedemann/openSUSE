#
# spec file for package python-geojson
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
Name:           python-geojson
Version:        2.4.1
Release:        0
Summary:        Python bindings and utilities for GeoJSON
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/frewsxcv/python-geojson
Source:         https://github.com/frewsxcv/python-geojson/archive/%{version}.tar.gz
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
%setup -q -n python-geojson-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%license LICENSE.rst
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*

%changelog
