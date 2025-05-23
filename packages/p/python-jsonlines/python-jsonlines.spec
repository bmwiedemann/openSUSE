#
# spec file for package python-jsonlines
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


%{?sle15_python_module_pythons}
Name:           python-jsonlines
Version:        4.0.0
Release:        0
Summary:        Library with helpers for the jsonlines file format
License:        BSD-3-Clause
URL:            https://github.com/wbolster/jsonlines
Source:         https://github.com/wbolster/jsonlines/archive/%{version}.tar.gz
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ujson}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-attrs >= 19.2.0
Recommends:     python-ujson
%python_subpackages

%description
Python library to simplify working with jsonlines_ and ndjson_ data.

%prep
%setup -q -n jsonlines-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/jsonlines
%{python_sitelib}/jsonlines-%{version}.dist-info

%changelog
