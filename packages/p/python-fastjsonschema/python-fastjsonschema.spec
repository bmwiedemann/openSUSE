#
# spec file for package python-fastjsonschema
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-fastjsonschema
Version:        2.16.3
Release:        0
Summary:        Fastest Python implementation of JSON schema
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/horejsek/python-fastjsonschema
Source:         https://files.pythonhosted.org/packages/source/f/fastjsonschema/fastjsonschema-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-colorama
Suggests:       python-json-spec
Suggests:       python-jsonschema
Suggests:       python-pylint
Suggests:       python-pytest
Suggests:       python-pytest-benchmark
Suggests:       python-pytest-cache
Suggests:       python-validictory
BuildArch:      noarch
%python_subpackages

%description
Fastest Python implementation of JSON schema

%prep
%autosetup -p1 -n fastjsonschema-%{version}

chmod -x fastjsonschema.egg-info/*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/fastjsonschema
%{python_sitelib}/fastjsonschema-%{version}*-info

%changelog
