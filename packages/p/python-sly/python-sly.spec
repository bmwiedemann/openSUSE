#
# spec file for package python-sly
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-sly
Version:        0.5
Release:        0
Summary:        Python implementation of the lex and yacc tools
License:        MIT
URL:            https://github.com/dabeaz/sly
Source:         https://files.pythonhosted.org/packages/source/s/sly/sly-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
SLY is a 100% Python implementation of the lex and yacc tools commonly used to write parsers and compilers. Parsing is based on the same LALR(1) algorithm used by many yacc tools. Here are a few notable features:
* SLY provides very extensive error reporting and diagnostic information to assist in parser construction. The original implementation was developed for instructional purposes. As a result, the system tries to identify the most common types of errors made by novice users.
* SLY provides full support for empty productions, error recovery, precedence specifiers, and moderately ambiguous grammars.
* SLY uses various Python metaprogramming features to specify lexers and parsers. There are no generated files or extra steps involved. You simply write Python code and run it.
* SLY can be used to build parsers for "real" programming languages. Although it is not ultra-fast due to its Python implementation, SLY can be used to parse grammars consisting of several hundred rules (as might be found for a language like C).

%prep
%setup -q -n sly-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sly*

%changelog
