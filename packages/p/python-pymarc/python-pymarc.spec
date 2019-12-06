#
# spec file for package python-pymarc
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-pymarc
Version:        3.1.13
Release:        0
Summary:        MARC bibliographic data manipulation module
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/edsu/pymarc
Source:         https://files.pythonhosted.org/packages/source/p/pymarc/pymarc-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/edsu/pymarc/master/LICENSE
Patch0:         python38.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module six >= 1.9.0}
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
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
