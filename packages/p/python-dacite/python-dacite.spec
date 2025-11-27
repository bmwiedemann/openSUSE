#
# spec file for package python-dacite
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-dacite
Version:        1.9.2
Release:        0
Summary:        Simple creation of data classes from dictionaries
License:        MIT
URL:            https://github.com/konradhalas/dacite
Source:         https://github.com/konradhalas/dacite/archive/refs/tags/v%{version}.tar.gz#/dacite-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-benchmark}
# /SECTION
BuildRequires:  unzip
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Simplifies creating type-hinted data transfer objects (DTOs) from dictionaries, useful for data from HTTP requests or databases. It complements Python's dataclasses and isn't a validation library. For validation, combine it with other libraries.

%prep
%autosetup -p1 -n dacite-%{version}
sed -ri 's/--benchmark-[^ "]+//g' pyproject.toml
# fix wrong version in setup.py, see gh#konradhalas/dacite#daad7e4
sed -i 's/1.9.1/1.9.2/g' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%{python_sitelib}/dacite
%{python_sitelib}/dacite-%{version}.dist-info

%changelog
