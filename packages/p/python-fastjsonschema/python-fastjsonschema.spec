#
# spec file for package python-fastjsonschema
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


%{?sle15_python_module_pythons}
Name:           python-fastjsonschema
Version:        2.20.0
Release:        0
Summary:        Fastest Python implementation of JSON schema
License:        BSD-3-Clause
URL:            https://github.com/horejsek/python-fastjsonschema
Source:         https://files.pythonhosted.org/packages/source/f/fastjsonschema/fastjsonschema-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-json-spec
Suggests:       python-jsonschema
Suggests:       python-validictory
BuildArch:      noarch
%python_subpackages

%description
Fastest Python implementation of JSON schema

%prep
%autosetup -p1 -n fastjsonschema-%{version}

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/fastjsonschema
%{python_sitelib}/fastjsonschema-%{version}.dist-info

%changelog
