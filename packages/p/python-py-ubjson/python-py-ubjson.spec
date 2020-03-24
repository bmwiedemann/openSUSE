#
# spec file for package python-py-ubjson
#
# Copyright (c) 2020 SUSE LLC
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
%define modname py-ubjson
Name:           python-py-ubjson
Version:        0.15.0
Release:        0
Summary:        Universal Binary JSON encoder/decoder
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Iotic-Labs/py-ubjson
Source:         https://files.pythonhosted.org/packages/source/p/py-ubjson/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a Python v3.2+ (and 2.7+) `Universal Binary JSON`
encoder/decoder based on the `draft-12` specification.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%check
touch test/__init__.py
%pytest test/test.py

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitearch}/*

%changelog
