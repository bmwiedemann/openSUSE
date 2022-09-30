#
# spec file for package python-nested-lookup
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-nested-lookup
Version:        0.2.25
Release:        0
Summary:        Python functions for working with deeply nested documents (lists and dicts)
License:        SUSE-Public-Domain
Group:          Development/Languages/Python
URL:            https://github.com/russellballestrini/nested-lookup
Source:         https://files.pythonhosted.org/packages/source/n/nested-lookup/nested-lookup-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/russellballestrini/nested-lookup/307983caa591bfd08a1f414109f640671a4dea51/test_lookup_api.py
Source2:        https://raw.githubusercontent.com/russellballestrini/nested-lookup/master/test_nested_lookup.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python functions for working with deeply nested documents (lists and dicts)

%prep
%setup -q -n nested-lookup-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%{python_sitelib}/nested_lookup*

%changelog
