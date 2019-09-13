#
# spec file for package python-geolinks
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-geolinks
Version:        0.2.0
Release:        0
License:        MIT
Summary:        Utilities to deal with geospatial links
Url:            https://github.com/geopython/geolinks
Group:          Development/Languages/Python
# pypi source lack license and tests
Source:         https://github.com/geopython/geolinks/archive/%{version}.tar.gz#/geolinks-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Python implementation of Cat-Interop utilities for geospatial links.

%prep
%setup -q -n geolinks-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B run_tests.py
}
popd

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
