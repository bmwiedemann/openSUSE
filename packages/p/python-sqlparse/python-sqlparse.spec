#
# spec file for package python-sqlparse
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sqlparse
Version:        0.3.0
Release:        0
Summary:        Non-validating SQL parser
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/andialbrecht/sqlparse
Source:         https://files.pythonhosted.org/packages/source/s/sqlparse/sqlparse-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
sqlparse is a non-validating SQL parser module.  It provides support for
parsing, splitting and formatting SQL statements.

%prep
%setup -q -n sqlparse-%{version}
sed -i -e '1{\,^#!%{_bindir}/env python,d}' sqlparse/__main__.py sqlparse/cli.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sqlformat
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative sqlformat

%postun
%python_uninstall_alternative sqlformat

%check
%pytest

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%python_alternative %{_bindir}/sqlformat
%{python_sitelib}/*

%changelog
