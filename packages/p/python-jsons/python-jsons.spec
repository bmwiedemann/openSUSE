#
# spec file for package python-jsons
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


Name:           python-jsons
Version:        1.6.3
Release:        0
Summary:        Serialize Python objects to JSON and back
License:        MIT
URL:            https://github.com/ramonhagenaars/jsons
Source:         https://github.com/ramonhagenaars/jsons/archive/refs/tags/v%{version}.tar.gz#/jsons-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh187-test_dump_load_parameterized_collections-fails.patch gh#ramonhagenaars/jsons#187 mcepl@suse.com
# skip failing test test_dump_load_parameterized_collections
Patch0:         gh187-test_dump_load_parameterized_collections-fails.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typish >= 1.9.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module typish >= 1.9.2}
BuildRequires:  %{python_module tzdata}
# /SECTION
%python_subpackages

%description
Python module for serializing Python objects to JSON (dicts) and back.

%prep
%autosetup -p1 -n jsons-%{version}
# Fix line endings
sed -i 's/\r$//' README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%doc README.md
%{python_sitelib}/jsons
%{python_sitelib}/jsons-%{version}.dist-info

%changelog
