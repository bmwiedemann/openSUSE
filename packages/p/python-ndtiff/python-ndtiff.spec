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


%define commit 6f4a5eed38ca466c529fca210fb37494bbd3890f
Name:           python-ndtiff
Version:        3.1.0
Release:        0
Summary:        Python libraries for NDTiff datasets
License:        BSD-3-Clause
URL:            https://github.com/micro-manager/NDStorage
# gh#micro-manager/NDTiffStorage#106
Source0:        https://github.com/micro-manager/NDStorage/archive/%{commit}.tar.gz#/ndtiff-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dask-array >= 2022.2.0
Requires:       python-numpy
Requires:       python-sortedcontainers
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dask-array >= 2022.2.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sortedcontainers}
# /SECTION
%python_subpackages

%description
Python libraries for NDTiff datasets

%prep
%autosetup -p1 -n NDStorage-%{commit}/python

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
