#
# spec file for package python-pysofaconventions
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


%define skip_python36 1
Name:           python-pysofaconventions
Version:        0.1.5
Release:        0
Summary:        Python implementation of the SOFA Convention
License:        BSD-3-Clause
URL:            https://github.com/andresperezEUT/pysofaconventions
Source0:        https://files.pythonhosted.org/packages/source/p/pysofaconventions/pysofaconventions-%{version}.tar.gz
# LICENSE not shipped in sdist
Source1:        https://raw.githubusercontent.com/andresperezEUT/pysofaconventions/refs/heads/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-netCDF4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
pysofaconventions is a python implementation of the SOFA Specification.

%prep
%setup -q -n pysofaconventions-%{version}
sed -i -e '/^#!\//, 1d' pysofaconventions/__init__.py
sed -i -e 's/--cov-report term-missing --cov pysofaconventions//' setup.cfg
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -rf  %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pysofaconventions
%{python_sitelib}/pysofaconventions-%{version}.dist-info

%changelog
