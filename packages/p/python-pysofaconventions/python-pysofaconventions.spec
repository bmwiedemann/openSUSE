#
# spec file for package python-pysofaconventions
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
Name:           python-pysofaconventions
Version:        0.1.5
Release:        0
Summary:        Python implementation of the SOFA Convention
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://andresperezlopez.github.io/pysofaconventions/
Source:         https://files.pythonhosted.org/packages/source/p/pysofaconventions/pysofaconventions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-netCDF4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
%python_subpackages

%description
pysofaconventions is a python implementation of the SOFA Specification.

%prep
%setup -q -n pysofaconventions-%{version}
sed -i -e '/^#!\//, 1d' pysofaconventions/__init__.py

%build
%python_build

%install
%python_install
%python_expand rm -rf  %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
