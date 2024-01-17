#
# spec file for package python-funcparserlib
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-funcparserlib
Version:        1.0.1
Release:        0
Summary:        Recursive descent parsing library based on functional combinators
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vlasovskikh/funcparserlib
Source:         https://github.com/vlasovskikh/funcparserlib/archive/refs/tags/%{version}.tar.gz#/funcparserlib-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The primary focus of funcparserlib is parsing little languages or external
DSLs (domain specific languages).

Parsers made with funcparserlib are pure-Python LL(*) parsers. It means that
it's very easy to write parsers without thinking about lookaheads and other
hardcore parsing stuff. However, recursive descent parsing is a rather
low method compared to LL(k) or LR(k) algorithms. Still, parsing with
funcparserlib is at least twice faster than PyParsing, a very popular library
for Python.

%prep
%setup -q -n funcparserlib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/funcparserlib
%{python_sitelib}/funcparserlib-%{version}*-info

%changelog
