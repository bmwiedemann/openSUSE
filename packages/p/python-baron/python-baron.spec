#
# spec file for package python-baron
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-baron
Version:        0.10.1
Release:        0
Summary:        Full Syntax Tree for Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/baron
Source0:        https://files.pythonhosted.org/packages/source/b/baron/baron-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rply
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rply}
# /SECTION
%python_subpackages

%description
Baron is a Full Syntax Tree (FST) library for Python. In contrast
to an AST which drops some syntax information in the process of its
creation (like empty lines, comments, formatting), a FST keeps
everything and guarantees the operation
fst_to_code(code_to_fst(source_code)) == source_code.

%prep
%setup -q -n baron-%{version}
# remove cache files accidentaly put in sdist
rm -f tests/*.pyc
rm -r tests/__pycache__

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/baron
%{python_sitelib}/baron-%{version}*-info

%changelog
