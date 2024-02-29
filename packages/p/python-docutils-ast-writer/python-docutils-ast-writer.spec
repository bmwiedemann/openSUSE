#
# spec file for package python-docutils-ast-writer
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-docutils-ast-writer
Version:        0.1.2
Release:        0
Summary:        AST Writer for docutils
License:        MIT
URL:            https://github.com/jimo1001/docutils-ast-writer
Source:         https://files.pythonhosted.org/packages/source/d/docutils-ast-writer/docutils-ast-writer-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jimo1001/docutils-ast-writer/master/LICENSE
# PATCH-FIX-UPSTREAM Based on gh#jimo1001/docutils-ast-writer#5
Patch0:         pr_5.patch
BuildRequires:  %{python_module docutils >= 0.12}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils >= 0.12
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Docutils-ast-writer is an AST writer of Docutils.

%prep
%autosetup -p1 -n docutils-ast-writer-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rst2ast
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check has no tests https://github.com/jimo1001/docutils-ast-writer/issues/2

%post
%python_install_alternative rst2ast

%postun
%python_uninstall_alternative rst2ast

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/rst2ast
%{python_sitelib}/rst2ast
%{python_sitelib}/docutils_ast_writer-%{version}.dist-info

%changelog
