#
# spec file for package python-geolinks
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-geolinks
Version:        0.2.0
Release:        0
License:        MIT
Summary:        Utilities to deal with geospatial links
URL:            https://github.com/geopython/geolinks
Group:          Development/Languages/Python
# pypi source lack license and tests
Source:         https://github.com/geopython/geolinks/archive/%{version}.tar.gz#/geolinks-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Python implementation of Cat-Interop utilities for geospatial links.

%prep
%setup -q -n geolinks-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/geolinks
%{python_sitelib}/geolinks-%{version}.dist-info

%changelog
