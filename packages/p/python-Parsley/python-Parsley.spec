#
# spec file for package python-Parsley
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
%define modname  Parsley
%define oldpython python
Name:           python-Parsley
Version:        1.3
Release:        0
Summary:        PEG algorithm based parser generator
License:        MIT
URL:            https://github.com/pyga/parsley
Source:         https://files.pythonhosted.org/packages/source/P/%{modname}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pyga/parsley#82
Patch0:         support-python312.patch
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-parsley
Obsoletes:      %{oldpython}-Parsley-doc
Obsoletes:      python-Parsley-doc
BuildArch:      noarch
%python_subpackages

%description
Parsley is a parsing library. Most parser generators like ANTLR and
Bison are based on LL or LR parsing algorithms that compile to big
state machine tables, whereas Parsley, like pyparsing and
ZestyParser, uses the PEG algorithm, so each expression in the
grammar rules works like a Python expression. In particular,
alternatives are evaluated in order, unlike table-driven parsers such
as yacc, bison or PLY.

The binaries are prefixed with parsley-.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Remove with bump, missing fixtures
rm -f ometa/test/test_vm_builder.py

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
mkdir %{buildroot}/%{_bindir}
# rename binaries in order to avoid name clashes with other system packages
for f in {generate_parser,stage}; do
    sed -i \
	-e "s|^#!%{_bindir}/env python$|#!%{_bindir}/python3|" \
	bin/$f
    cp -v bin/$f %{buildroot}/%{_bindir}/parsley-$f
    %python_clone -a %{buildroot}%{_bindir}/parsley-$f
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest ometa/test
%pytest terml/test

%post
%python_install_alternative parsley-stage
%python_install_alternative parsley-generate_parser

%postun
%python_uninstall_alternative parsley-stage
%python_uninstall_alternative parsley-generate_parser

%files %{python_files}
%license LICENSE
%doc NEWS PKG-INFO README
%python_alternative %{_bindir}/parsley-stage
%python_alternative %{_bindir}/parsley-generate_parser
%{python_sitelib}/parsley.py
%pycache_only %{python_sitelib}/__pycache__/parsley.*.py*
%{python_sitelib}/terml
%{python_sitelib}/ometa
%{python_sitelib}/Parsley-%{version}.dist-info

%changelog
