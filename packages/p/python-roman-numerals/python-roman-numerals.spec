#
# spec file for package python-roman-numerals
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-roman-numerals
Version:        4.1.0
Release:        0
Summary:        Manipulate well-formed Roman numerals
License:        0BSD
URL:            https://github.com/AA-Turner/roman-numerals/
Source:         https://files.pythonhosted.org/packages/source/r/roman-numerals/roman_numerals-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.12}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8}
# /SECTION
%python_subpackages

%description
A library for manipulating well-formed Roman numerals.

%prep
%autosetup -p1 -n roman_numerals-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENCE.rst
%{python_sitelib}/roman_numerals
%{python_sitelib}/roman_numerals-%{version}.dist-info

%changelog
