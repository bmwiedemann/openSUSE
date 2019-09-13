#
# spec file for package python-python-stdnum
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define modname python-stdnum
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        1.11
Release:        0
Summary:        Python module to handle standardized numbers and codes
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://arthurdejong.org/python-stdnum/
Source:         https://files.pythonhosted.org/packages/source/p/python-stdnum/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -m nose

%files %{python_files}
%license COPYING
%doc NEWS ChangeLog README
%{python_sitelib}/*

%changelog
