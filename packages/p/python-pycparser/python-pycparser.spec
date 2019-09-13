#
# spec file for package python-pycparser
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pycparser
Version:        2.19
Release:        0
Summary:        C parser in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/eliben/pycparser
Source0:        https://files.pythonhosted.org/packages/source/p/pycparser/pycparser-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
Patch1:         fix-lexer-build.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
pycparser is a complete parser of the C language, written in pure Python using
the PLY parsing library. It parses C code into an AST and can serve as a
front-end for C compilers or analysis tools.

%prep
%setup -q -n pycparser-%{version}
%patch1 -p1
# fix end of line
sed -i 's/\r//' LICENSE

%build
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
%python_exec tests/all_tests.py

%files %{python_files}
%doc README.rst
%doc examples/
%license LICENSE
%{python_sitelib}/*

%changelog
