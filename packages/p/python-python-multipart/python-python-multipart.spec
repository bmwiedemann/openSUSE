#
# spec file for package python-python-multipart
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
Name:           python-python-multipart
Version:        0.0.17
Release:        0
License:        Apache-2.0
Summary:        Python streaming multipart parser
URL:            http://github.com/andrew-d/python-multipart
Source:         https://files.pythonhosted.org/packages/source/p/python-multipart/python_multipart-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A streaming multipart parser for Python.

%prep
%autosetup -p1 -n python_multipart-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/multipart
%{python_sitelib}/python_multipart
%{python_sitelib}/python_multipart-%{version}.dist-info

%changelog
