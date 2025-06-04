#
# spec file for package python-bowler
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


%bcond_without libalternatives
Name:           python-bowler
Version:        0.9.0
Release:        0
Summary:        Safe code refactoring for modern Python projects
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/facebookincubator/bowler
Source:         https://files.pythonhosted.org/packages/source/b/bowler/bowler-%{version}.tar.gz
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module fissix}
BuildRequires:  %{python_module moreorless}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  %{python_module volatile}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-attrs
Requires:       python-click
Requires:       python-fissix
Requires:       python-moreorless
Requires:       python-volatile
BuildArch:      noarch
%python_subpackages

%description
Bowler is a refactoring tool for manipulating Python at the syntax tree level. It enables
safe, large scale code modifications while guaranteeing that the resulting code compiles
and runs. It provides both a simple command line interface and a fluent API in Python for
generating complex code modifications in code.

Bowler uses a "fluent" `Query` API to build refactoring scripts through a series
of selectors, filters, and modifiers.  Many simple modifications are already possible
using the existing API, but you can also provide custom selectors, filters, and
modifiers as needed to build more complex or custom refactorings.  See the
[Query Reference](https://pybowler.io/docs/api-query) for more details.

%prep
%autosetup -p1 -n bowler-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bowler
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m bowler.tests

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative bowler

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/bowler
%{python_sitelib}/bowler-%{version}*-info
%python_alternative %{_bindir}/bowler

%changelog
