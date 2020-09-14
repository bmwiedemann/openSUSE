#
# spec file for package python-funcparserlib
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
Name:           python-funcparserlib
Version:        0.3.6
Release:        0
Summary:        Recursive descent parsing library based on functional combinators
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vlasovskikh/funcparserlib
Source:         https://files.pythonhosted.org/packages/source/f/funcparserlib/funcparserlib-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-modernize
BuildArch:      noarch
%python_subpackages

%description
Parser combinators are just higher-order functions that take parsers as
their arguments and return them as result values. Parser combinators are:

First-class values. Extremely composable. Tend to make the code quite compact.
Resemble the readable notation of xBNF grammars.

Parsers made with funcparserlib are pure-Python LL(*) parsers. It means that
it's very easy to write them without thinking about look-aheads and all that
hardcore parsing stuff. But the recursive descent parsing is a rather slow
method compared to LL(k) or LR(k) algorithms.

So the primary domain for funcparserlib is parsing little languages or external
DSLs (domain specific languages).

The library itself is very small. Its source code is only 0.5 KLOC, with lots
of comments included. It features the longest parsed prefix error reporting,
as well as a tiny lexer generator for token position tracking.

%prep
%setup -q -n funcparserlib-%{version}
python-modernize -nw funcparserlib/
sed -i "s/ur'/r'/" funcparserlib/tests/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README CHANGES
%{python_sitelib}/funcparserlib/
%{python_sitelib}/funcparserlib*egg-info

%changelog
