#
# spec file for package python-awpa
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
%define skip_python2 1
Name:           python-awpa
Version:        0.19.1.0
Release:        0
License:        Python-2.0 and MIT
Summary:        A Working Python AST
Url:            https://github.com/pyga/awpa
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/awpa/awpa-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A Working Python AST.

%prep
%setup -q -n awpa-%{version}
# https://github.com/pyga/awpa/issues/13
sed -i "s/'pattern'//" awpa/pygram_test.py

%build
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitelib}/awpa/pygram_test.py
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.rst
%{python_sitelib}/*

%changelog
