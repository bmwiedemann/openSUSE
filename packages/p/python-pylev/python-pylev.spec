#
# spec file for package python-pylev
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pylev
Version:        1.3.0
Release:        0
License:        BSD-3-Clause
Summary:        A pure Python Levenshtein implementation
Url:            http://github.com/toastdriven/pylev
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pylev/pylev-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/toastdriven/pylev/master/LICENSE
Source2:        https://raw.githubusercontent.com/toastdriven/pylev/master/tests.py
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A pure Python Levenshtein implementation.

%prep
%setup -q -n pylev-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
