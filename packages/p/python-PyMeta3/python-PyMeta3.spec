#
# spec file for package python-PyMeta3
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
Name:           python-PyMeta3
Version:        0.5.1
Release:        0
Summary:        Pattern-matching language based on OMeta for Python 3 and 2
License:        MIT
URL:            https://github.com/wbond/pymeta3
Source:         https://files.pythonhosted.org/packages/source/P/PyMeta3/PyMeta3-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PyMeta is an implementation of OMeta, an object-oriented pattern-matching
language developed by Alessandro Warth
(http://www.cs.ucla.edu/~awarth/ometa/). PyMeta provides a compact syntax based
on Parsing Expression Grammars (PEGs) for common lexing, parsing and
tree-transforming activities in a way that's easy to reason about for Python
programmers.

It is a fork of PyMeta 0.5.0 that supports Python 2 and 3.

%prep
%setup -q -n PyMeta3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -D -m0755 bin/generate_parser %{buildroot}%{_bindir}/generate_parser
sed -i  -e 's/env python$/python3/' %{buildroot}%{_bindir}/generate_parser
%python_clone -a %{buildroot}%{_bindir}/generate_parser

%post
%python_install_alternative generate_parser

%postun
%python_uninstall_alternative generate_parser

%files %{python_files}
%license LICENSE
%doc NEWS README
%{python_sitelib}/*
%python_alternative %{_bindir}/generate_parser

%changelog
