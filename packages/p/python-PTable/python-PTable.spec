#
# spec file for package python-PTable
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-PTable
Version:        0.9.2
Release:        0
Summary:        Python library for displaying data as tabular ASCII
License:        BSD-3-Clause
URL:            https://github.com/kxxoling/PTable
Source0:        https://files.pythonhosted.org/packages/source/P/PTable/PTable-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-PrettyTable
BuildArch:      noarch
%python_subpackages

%description
Python library for displaying tabular data in an ASCII table format.

%prep
%setup -q -n PTable-%{version}
sed -i '1{/^#!/d}' prettytable/prettytable.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No tests available in package, github has no tags

%files %{python_files}
%doc CHANGELOG README.rst
%license COPYING
%dir %{python_sitelib}/prettytable/
%dir %{python_sitelib}/prettytable/__pycache__/
%python3_only %{_bindir}/ptable
%{python_sitelib}/PTable-%{version}-py%{python_version}.egg-info/
%{python_sitelib}/prettytable/*.py
%pycache_only %{python_sitelib}/prettytable/__pycache__/*.pyc

%changelog
