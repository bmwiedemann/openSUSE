#
# spec file for package python-schema
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-schema
Version:        0.7.5
Release:        0
Summary:        Data validation library
License:        MIT
URL:            https://github.com/keleshev/schema
Source:         https://files.pythonhosted.org/packages/source/s/schema/schema-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#keleshev/schema#273
Patch0:         remove-old-python-support.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python data-types.

%prep
%autosetup -p1 -n schema-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test_schema.py

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE-MIT
%{python_sitelib}/*

%changelog
