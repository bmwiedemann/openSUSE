#
# spec file for package python-python-stdnum
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


%global modname python-stdnum
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        1.20
Release:        0
Summary:        Python module to handle standardized numbers and codes
License:        LGPL-2.1-or-later
URL:            https://arthurdejong.org/python-stdnum/
Source:         https://files.pythonhosted.org/packages/source/p/python-stdnum/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-PySimpleSOAP
Suggests:       python-suds
BuildArch:      noarch
%python_subpackages

%description
This library offers functions for parsing, validating and reformatting
standard numbers and codes in various formats.

Apart from the validate() function, modules generally provide extra
parsing, validation, formatting or conversion functions.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license COPYING
%doc NEWS ChangeLog README.md
%{python_sitelib}/stdnum
%{python_sitelib}/python_stdnum-%{version}.dist-info

%changelog
