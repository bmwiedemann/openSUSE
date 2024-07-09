#
# spec file for package python-ndtiff
#
# Copyright (c) 2024 SUSE LLC
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


%define commit e7e32f7d59d1a0ac7ce8727c6b166d1a0844e42c
Name:           python-ndtiff
Version:        1.12.0
Release:        0
Summary:        Python libraries for NDTiff datasets
License:        BSD-3-Clause
URL:            https://github.com/micro-manager/NDTiffStorage
# gh#micro-manager/NDTiffStorage#106
Source0:        https://github.com/micro-manager/NDTiffStorage/archive/%{commit}.tar.gz#/ndtiff-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dask-array >= 2022.2.0
Requires:       (python-numpy with python-numpy < 2)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dask-array >= 2022.2.0}
BuildRequires:  %{python_module numpy with %python-numpy < 2}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python libraries for NDTiff datasets

%prep
%setup -q -n NDTiffStorage-%{commit}/python

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license ../LICENSE
%doc ../README.md
%{python_sitelib}/ndtiff
%{python_sitelib}/ndtiff-%{version}.dist-info

%changelog
