#
# spec file for package python-pycparser
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pycparser
Version:        2.23
Release:        0
Summary:        C parser in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/eliben/pycparser
Source0:        https://files.pythonhosted.org/packages/source/p/pycparser/pycparser-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
# fix end of line
sed -i 's/\r//' LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
%pytest

%files %{python_files}
%doc README.rst
%doc examples/
%license LICENSE
%{python_sitelib}/pycparser
%{python_sitelib}/pycparser-%{version}*-info

%changelog
