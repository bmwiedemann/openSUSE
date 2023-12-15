#
# spec file for package python-ply
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
Name:           python-ply
Version:        3.11
Release:        0
Summary:        Python Lex & Yacc
License:        BSD-3-Clause
URL:            http://www.dabeaz.com/ply/
Source:         https://files.pythonhosted.org/packages/source/p/ply/ply-%{version}.tar.gz
Patch0:         python-ply-shebangs.patch
Patch1:         fix-assert-methods.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PLY is yet another implementation of lex and yacc for Python. Some notable
features include the fact that its implemented entirely in Python and it
uses LALR(1) parsing which is efficient and well suited for larger grammars.

PLY provides most of the standard lex/yacc features including support for empty
productions, precedence rules, error recovery, and support for ambiguous grammars.

PLY provides extensive error checking.
It is compatible with both Python 2 and Python 3.

%if 0%{?suse_version} > 1500
%package -n %{name}-doc
Summary:        Python Lex & Yacc
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python

%description -n %{name}-doc
PLY is yet another implementation of lex and yacc for Python. Some notable
features include the fact that its implemented entirely in Python and it
uses LALR(1) parsing which is efficient and well suited for larger grammars.

PLY provides most of the standard lex/yacc features including support for empty
productions, precedence rules, error recovery, and support for ambiguous grammars.

PLY provides extensive error checking.
It is compatible with both Python 2 and Python 3.
%endif

%prep
%autosetup -p1 -n ply-%{version}
# remove unneeded executable bit
chmod -x test/testlex.py

# Fix wrong-script-interpreter
find example -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python||" {} +

%fdupes doc
%fdupes example

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd test
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B testlex.py
$python -B testyacc.py
}
popd

%files %{python_files}
# yay for upstream that puts the license to readme
%license README.md
%doc ANNOUNCE CHANGES README.md TODO
%{python_sitelib}/ply
%{python_sitelib}/ply-%{version}.dist-info

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc doc/
%doc example/

%changelog
