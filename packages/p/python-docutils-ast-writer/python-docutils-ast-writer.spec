#
# spec file for package python-docutils-ast-writer
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-docutils-ast-writer
Version:        0.1.2
Release:        0
License:        MIT
Summary:        AST Writer for docutils
Url:            https://github.com/jimo1001/docutils-ast-writer
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/docutils-ast-writer/docutils-ast-writer-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jimo1001/docutils-ast-writer/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module docutils >= 0.12}
Requires:       python-docutils >= 0.12
BuildArch:      noarch

%python_subpackages

%description
Docutils-ast-writer is an AST writer of Docutils.

%prep
%setup -q -n docutils-ast-writer-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check has no tests https://github.com/jimo1001/docutils-ast-writer/issues/2

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/rst2ast
%{python_sitelib}/*

%changelog
