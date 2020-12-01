#
# spec file for package python-python-multipart
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-multipart
Version:        0.0.5
Release:        0
License:        Apache-2.0
Summary:        Python streaming multipart parser
Url:            http://github.com/andrew-d/python-multipart
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/python-multipart/python-multipart-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module six >= 1.4.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module PyYAML}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six >= 1.4.0
BuildArch:      noarch

%python_subpackages

%description
A streaming multipart parser for Python.

%prep
%setup -q -n python-multipart-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
