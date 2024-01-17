#
# spec file for package python-spark_parser
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
Name:           python-spark_parser
Version:        1.8.9
Release:        0
Summary:        An Earley-Algorithm Context-free grammar Parser Toolkit
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rocky/python-spark/
Source:         https://files.pythonhosted.org/packages/source/s/spark_parser/spark_parser-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
SPARK stands for Scanning, Parsing, and Rewriting Kit. It uses Jay
Earley's algorithm for parsing context-free grammars, and comes with
some generic Abstract Syntax Tree routines. There is also a prototype
scanner which does its job by combining Python regular expressions.

Please Note: Earley algorithm parsers are almost linear when given an LR
grammar. These are grammars which are left-recursive.

%prep
%setup -q -n spark_parser-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/spark-parser-coverage
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test

%post
%python_install_alternative spark-parser-coverage

%postun
%python_uninstall_alternative spark-parser-coverage

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/spark-parser-coverage
%{python_sitelib}/*

%changelog
