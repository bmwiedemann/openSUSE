#
# spec file for package python-mkdocstrings
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
Name:           python-mkdocstrings
Version:        1.0.3
Release:        0
Summary:        Automatic documentation from sources, for MkDocs
License:        ISC
URL:            https://github.com/mkdocstrings/mkdocstrings 
Source:         https://files.pythonhosted.org/packages/source/m/mkdocstrings/mkdocstrings-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.11.1}
BuildRequires:  %{python_module Markdown >= 3.3}
BuildRequires:  %{python_module MarkupSafe >= 1.1}
BuildRequires:  %{python_module mkdocs >= 1.2}
BuildRequires:  %{python_module mkdocs-autorefs >= 0.3.1}
BuildRequires:  %{python_module pymdown-extensions >= 6.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Jinja2 >= 2.11.1
Requires:       python-Markdown >= 3.3
Requires:       python-MarkupSafe >= 1.1
Requires:       python-mkdocs >= 1.2
Requires:       python-mkdocs-autorefs >= 0.3.1
Requires:       python-pymdown-extensions >= 6.3
Suggests:       python-mkdocstrings-crystal >= 0.3.4
Suggests:       python-mkdocstrings-python-legacy >= 0.2.1
Suggests:       python-mkdocstrings-python >= 0.5.2
BuildArch:      noarch
%python_subpackages

%description
Automatic documentation from sources, for [MkDocs](https://mkdocs.org/).

%prep
%autosetup -p1 -n mkdocstrings-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/mkdocstrings
%{python_sitelib}/mkdocstrings-%{version}.dist-info

%changelog
