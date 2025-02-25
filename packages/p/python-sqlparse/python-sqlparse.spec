#
# spec file for package python-sqlparse
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


%{?sle15_python_module_pythons}
Name:           python-sqlparse
Version:        0.5.3
Release:        0
Summary:        Non-validating SQL parser
License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
Source:         https://files.pythonhosted.org/packages/source/s/sqlparse/sqlparse-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
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
chmod -x sqlparse/cli.py

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/sqlparse
%{python_sitelib}/sqlparse-%{version}.dist-info

%changelog
