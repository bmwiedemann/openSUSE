#
# spec file for package python-pymarc
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
Name:           python-pymarc
Version:        5.2.3
Release:        0
Summary:        MARC bibliographic data manipulation module
License:        BSD-2-Clause
URL:            https://gitlab.com/pymarc/pymarc
Source:         https://files.pythonhosted.org/packages/source/p/pymarc/pymarc-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
pymarc is a Python library for working with bibliographic data
encoded in MARC21. It provides an API for reading, writing and
modifying MARC records. It was originally designed to be an emergency
eject seat for getting data assets out of MARC and into some kind of
saner representation.

%prep
%setup -q -n pymarc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pymarc
%{python_sitelib}/pymarc-%{version}.dist-info

%changelog
